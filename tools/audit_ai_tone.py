#!/usr/bin/env python3
"""Scan Chinese Dachuang drafts for generic AI-style wording.

This is a lightweight heuristic checker. It reports phrases and lines that may
need more concrete project details, but it does not decide whether a draft is
acceptable by itself.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PHRASES = [
    "具有重要意义",
    "具有重要的现实意义",
    "具有广阔的应用前景",
    "广阔应用前景",
    "极大提升",
    "显著提升",
    "有效解决",
    "充分体现",
    "进一步推动",
    "赋能",
    "助力",
    "打造",
    "痛点",
    "落地",
    "高质量发展",
    "智能化转型",
    "数字化转型",
    "社会效益和经济效益",
    "理论意义和实践价值",
    "国内外研究现状表明",
    "随着人工智能技术的不断发展",
]

WEAK_PATTERNS = [
    (re.compile(r"(提高|提升|优化|改善|增强).{0,8}(效率|效果|体验|水平)"), "提升类表述建议补充指标、对象或验证方式"),
    (re.compile(r"(创新性|先进性|实用性).{0,12}(较强|明显|突出)"), "创新性表述建议改成可验证差异点"),
    (re.compile(r"(拟|将)?(广泛|全面|深入).{0,10}(应用|推广|研究)"), "范围可能偏大，建议缩到具体场景"),
]


def line_score(line: str) -> list[str]:
    hits: list[str] = []
    for phrase in PHRASES:
        if phrase in line:
            hits.append(f"模板短语：{phrase}")
    for pattern, message in WEAK_PATTERNS:
        if pattern.search(line):
            hits.append(message)
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit AI-style wording in Dachuang Markdown drafts.")
    parser.add_argument("file", type=Path, help="Markdown/text file to scan")
    parser.add_argument("--context", type=int, default=90, help="max characters shown per flagged line")
    args = parser.parse_args()

    text = args.file.read_text(encoding="utf-8")
    findings: list[tuple[int, str, list[str]]] = []

    for number, line in enumerate(text.splitlines(), start=1):
        clean = line.strip()
        if not clean or clean.startswith("|---"):
            continue
        hits = line_score(clean)
        if hits:
            snippet = clean[: args.context]
            findings.append((number, snippet, hits))

    print(f"AI-tone audit: {args.file}")
    print(f"Flagged lines: {len(findings)}")
    if not findings:
        print("No obvious generic AI-style wording found.")
        return 0

    for number, snippet, hits in findings:
        print(f"\nL{number}: {snippet}")
        for hit in hits:
            print(f"  - {hit}")

    print("\nRewrite hints:")
    print("- Replace broad claims with scene, module, metric, data source, or deliverable.")
    print("- Keep simulated data and placeholder achievements visibly labeled.")
    print("- Do not add fake field visits, dates, teacher comments, or results just to sound natural.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
