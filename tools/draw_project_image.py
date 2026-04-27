#!/usr/bin/env python3
"""Generate optional Dachuang project visuals with user-provided APIs.

This tool is intentionally opt-in. It reads API keys from the environment or a
local .env file and should only be used for conceptual visuals, PPT covers,
posters, and placeholders. Do not use generated images as real evidence.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


OPENAI_IMAGE_URL = "https://api.openai.com/v1/images/generations"


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def read_prompt(path_or_text: str) -> str:
    path = Path(path_or_text)
    if path.exists():
        return path.read_text(encoding="utf-8").strip()
    return path_or_text.strip()


def post_json(url: str, headers: dict[str, str], payload: dict[str, Any]) -> dict[str, Any]:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {exc.code} from image provider:\n{detail}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"Could not reach image provider: {exc}") from exc


def extract_image_bytes(data: dict[str, Any]) -> bytes:
    candidates: list[Any] = []
    if isinstance(data.get("data"), list):
        candidates.extend(data["data"])
    if isinstance(data.get("images"), list):
        candidates.extend(data["images"])
    if data.get("b64_json") or data.get("image_base64") or data.get("base64"):
        candidates.append(data)

    for item in candidates:
        if not isinstance(item, dict):
            continue
        encoded = item.get("b64_json") or item.get("image_base64") or item.get("base64")
        if encoded:
            return base64.b64decode(encoded)
        url = item.get("url") or item.get("image_url")
        if url:
            with urllib.request.urlopen(url, timeout=180) as response:
                return response.read()

    raise SystemExit("Provider response did not contain b64_json, image_base64, base64, or url.")


def generate_openai(prompt: str, size: str, quality: str, output_format: str) -> bytes:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("Missing OPENAI_API_KEY. Fill .env or export it before running.")

    model = os.environ.get("DACHUANG_OPENAI_IMAGE_MODEL", "gpt-image-1.5")
    payload: dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "size": size,
        "quality": quality,
        "n": 1,
    }
    if output_format:
        payload["output_format"] = output_format

    data = post_json(
        OPENAI_IMAGE_URL,
        {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        payload,
    )
    return extract_image_bytes(data)


def generate_nano_banana2(prompt: str, size: str, quality: str) -> bytes:
    url = os.environ.get("DACHUANG_NANO_BANANA2_API_URL")
    api_key = os.environ.get("DACHUANG_NANO_BANANA2_API_KEY")
    model = os.environ.get("DACHUANG_NANO_BANANA2_MODEL", "nano-banana-2")
    if not url:
        raise SystemExit("Missing DACHUANG_NANO_BANANA2_API_URL. Fill .env or export it before running.")
    if not api_key:
        raise SystemExit("Missing DACHUANG_NANO_BANANA2_API_KEY. Fill .env or export it before running.")

    data = post_json(
        url,
        {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        {
            "model": model,
            "prompt": prompt,
            "size": size,
            "quality": quality,
            "n": 1,
        },
    )
    return extract_image_bytes(data)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate optional conceptual visuals for Dachuang materials.")
    parser.add_argument("--provider", choices=["openai", "nano-banana2"], required=True)
    parser.add_argument("--prompt", required=True, help="Prompt text or path to a prompt file")
    parser.add_argument("--out", type=Path, required=True, help="Output image path")
    parser.add_argument("--env", type=Path, default=Path(".env"), help="Local env file path")
    parser.add_argument("--size", default="1024x1024", help="Image size, provider dependent")
    parser.add_argument("--quality", default="auto", help="Image quality, provider dependent")
    parser.add_argument("--format", default="png", choices=["png", "jpeg", "webp"], help="Output format hint")
    args = parser.parse_args()

    load_dotenv(args.env)
    prompt = read_prompt(args.prompt)
    if not prompt:
        raise SystemExit("Prompt is empty.")

    warning = (
        "Note: generated images are conceptual visuals/placeholders only. "
        "Do not present them as real experiments, screenshots, certificates, receipts, or prototypes."
    )
    print(warning, file=sys.stderr)

    if args.provider == "openai":
        image = generate_openai(prompt, args.size, args.quality, args.format)
    else:
        image = generate_nano_banana2(prompt, args.size, args.quality)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(image)
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
