#!/usr/bin/env python3
"""Fast, dependency-free repository and deployment checks for SignalWall."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("index.html", "app.js", "style.css", "LICENSE", "SECURITY.md", "docs/STANDALONE_OPERATION.md")


def main() -> int:
    errors = []
    for name in REQUIRED:
        path = ROOT / name
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing or empty: {name}")

    html = (ROOT / "index.html").read_text(encoding="utf-8")
    javascript = (ROOT / "app.js").read_text(encoding="utf-8")
    for element_id in ("wall", "linkInput", "cardTemplate", "importInput"):
        if f'id="{element_id}"' not in html:
            errors.append(f"index.html missing #{element_id}")
    for capability in ("detectSource", "renderFeed", "exportBtn", "importInput"):
        if capability not in javascript:
            errors.append(f"app.js missing {capability}")
    if "parsed.protocol==='http:'||parsed.protocol==='https:'" not in javascript:
        errors.append("app.js does not restrict embedded URLs to HTTP(S)")
    if "detectSource(saved.source?.url||saved.url||'')" not in javascript:
        errors.append("session imports can bypass source URL validation")

    if "GROUNDSTATE_ADMIN" in javascript or "admin_center" in javascript.lower():
        errors.append("app.js contains a required company identity integration")

    if errors:
        print("SignalWall doctor failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("SignalWall doctor passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
