#!/usr/bin/env python3
"""Check basic consistency across Dachuang material drafts.

The script extracts common fields with conservative regexes and reports possible
conflicts. It is meant for Markdown or text drafts, not locked school forms.
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path


FIELD_PATTERNS = {
    "项目题目": [
        re.compile(r"(?:项目名称|项目题目|题目)[:：]\s*([^\n|]+)"),
    ],
    "指导老师": [
        re.compile(r"(?:指导教师|指导老师)[:：]\s*([^\n|]+)"),
    ],
    "项目级别": [
        re.compile(r"(?:项目级别|立项级别)[:：]\s*([^\n|]+)"),
    ],
    "经费总额": [
        re.compile(r"(?:经费总额|总经费|申请经费|预算总额)[:：]?\s*([0-9]+(?:\.[0-9]+)?\s*(?:元|万元)?)"),
    ],
    "项目周期": [
        re.compile(r"(?:项目周期|实施周期|研究周期)[:：]\s*([^\n|]+)"),
    ],
}

PLACEHOLDER_RE = re.compile(r"(示例数据|占位数据|参考示例|占位示例|拟申请|申请中|已授权|获奖|专利|软著)")


def normalize(value: str) -> str:
    value = re.sub(r"\s+", "", value)
    return value.strip("；;。,.， ")


def extract_fields(path: Path) -> dict[str, set[str]]:
    text = path.read_text(encoding="utf-8")
    result: dict[str, set[str]] = defaultdict(set)
    for field, patterns in FIELD_PATTERNS.items():
        for pattern in patterns:
            for match in pattern.finditer(text):
                value = normalize(match.group(1))
                if value:
                    result[field].add(value)
    return result


def scan_placeholder_labels(path: Path) -> list[tuple[int, str]]:
    findings: list[tuple[int, str]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if PLACEHOLDER_RE.search(line):
            if "示例" not in line and "占位" not in line and "参考" not in line and "拟" not in line and "计划" not in line and "真实" not in line:
                findings.append((number, line.strip()[:120]))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Check consistency across Dachuang drafts.")
    parser.add_argument("files", type=Path, nargs="+", help="Markdown/text files to check")
    args = parser.parse_args()

    by_field: dict[str, dict[str, set[str]]] = defaultdict(dict)
    for path in args.files:
        fields = extract_fields(path)
        for field, values in fields.items():
            by_field[field][str(path)] = values

    conflicts = 0
    print("Dachuang consistency check")
    print(f"Files: {len(args.files)}")

    for field, file_values in by_field.items():
        all_values = set().union(*file_values.values())
        if len(all_values) <= 1:
            continue
        conflicts += 1
        print(f"\nPossible conflict: {field}")
        for file_name, values in file_values.items():
            print(f"  - {file_name}: {', '.join(sorted(values))}")

    label_warnings = 0
    for path in args.files:
        findings = scan_placeholder_labels(path)
        if findings:
            label_warnings += len(findings)
            print(f"\nPotential unlabeled achievement/data wording: {path}")
            for number, line in findings:
                print(f"  - L{number}: {line}")

    if conflicts == 0 and label_warnings == 0:
        print("No obvious conflicts or unlabeled achievement/data wording found.")
        return 0

    print("\nReview hints:")
    print("- Keep title, teacher, members, budget, and project cycle identical across materials.")
    print("- If scope changed between proposal and final report, explain the change explicitly.")
    print("- Mark simulated data and unverified achievements as 示例/占位/拟申请/计划.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
