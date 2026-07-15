from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


def parse_log_file(file_path: Path) -> dict[str, Any]:
    raw = file_path.read_text(encoding="utf-8")
    lines = raw.splitlines()

    headers: dict[str, str] = {}
    message_index = -1

    for index, line in enumerate(lines):
        stripped = line.strip().lstrip("\ufeff")
        if stripped.lower().startswith("message:"):
            message_index = index
            break

        if ":" not in stripped:
            continue

        key, value = stripped.split(":", 1)
        key = key.strip().lower()
        value = value.strip()
        if not key:
            continue
        headers[key] = value

    subject = headers.get("subject") or file_path.stem.replace("_", " ")
    modified_date = datetime.fromtimestamp(file_path.stat().st_mtime, tz=UTC).strftime("%Y-%m-%d")
    date = headers.get("date") or modified_date
    subtitle = headers.get("subtitle") or ""
    repo_link = headers.get("repo link") or ""
    category = headers.get("category") or "Architecture Log"

    entry_id = file_path.stem.lower().replace(" ", "-")

    return {
        "id": entry_id,
        "file": file_path.name,
        "category": category,
        "title": subject,
        "date": date,
        "subtitle": subtitle,
        "repoLink": repo_link,
    }


def build_manifest(logs_dir: Path) -> list[dict[str, Any]]:
    entries = [
        parse_log_file(path)
        for path in sorted(logs_dir.glob("*.txt"))
        if not path.name.startswith("_") and path.name.lower() != "index.json"
    ]

    entries.sort(
        key=lambda item: (
            item.get("date", "1970-01-01"),
            item.get("file", ""),
        ),
        reverse=True,
    )

    return entries


def main() -> int:
    parser = argparse.ArgumentParser(description="Build architecture log index manifest.")
    parser.add_argument(
        "--logs-dir",
        default="PresentationHub/architecture_logs",
        help="Directory that contains architecture log .txt files.",
    )
    parser.add_argument(
        "--output",
        default="PresentationHub/architecture_logs/index.json",
        help="Output manifest JSON path.",
    )
    args = parser.parse_args()

    logs_dir = Path(args.logs_dir).resolve()
    output_path = Path(args.output).resolve()

    if not logs_dir.exists():
        raise FileNotFoundError(f"Logs directory not found: {logs_dir}")

    manifest = build_manifest(logs_dir)
    output_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {len(manifest)} entries to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
