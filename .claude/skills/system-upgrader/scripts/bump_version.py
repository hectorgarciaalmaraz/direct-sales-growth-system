#!/usr/bin/env python3
"""bump_version.py — Semantic version bump + changelog entry (stdlib only).

Deterministic helper for the `system-upgrader` skill. Finds the current semantic version in
ops/changelog.md (pattern vMAJOR.MINOR.PATCH), computes the next version, and prepends a dated
entry. Cross-platform via pathlib. No third-party dependencies.

Examples:
    python bump_version.py --part patch --message "Mejor description de script-writer" \\
        --file ../../../ops/changelog.md
    python bump_version.py --part minor --message "Nueva skill hook-writer" \\
        --reason "Necesidad recurrente de hooks" --impact "Más hooks por plataforma" \\
        --file ../../../ops/changelog.md --dry-run
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

# Windows consoles default to cp1252; force UTF-8 so es-MX text never crashes output.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001 - non-fatal; falls back to default stream
    pass

VERSION_RE = re.compile(r"v(\d+)\.(\d+)\.(\d+)")


def find_current(text: str) -> tuple[int, int, int]:
    """Return the highest ``vX.Y.Z`` found in the changelog text (``(0, 1, 0)`` if none)."""
    versions = [tuple(map(int, m.groups())) for m in VERSION_RE.finditer(text)]
    if not versions:
        return (0, 1, 0)
    return max(versions)


def bump(ver: tuple[int, int, int], part: str) -> tuple[int, int, int]:
    """Increment the ``major``, ``minor`` or ``patch`` part of a version tuple."""
    major, minor, patch = ver
    if part == "major":
        return (major + 1, 0, 0)
    if part == "minor":
        return (major, minor + 1, 0)
    return (major, minor, patch + 1)


def entry(new: str, args: argparse.Namespace) -> str:
    """Format a dated changelog entry from ``--message``, ``--reason`` and ``--impact``."""
    lines = [f"## v{new} — {date.today().isoformat()}", f"- **Cambio:** {args.message}"]
    if args.reason:
        lines.append(f"- **Razón:** {args.reason}")
    if args.impact:
        lines.append(f"- **Impacto:** {args.impact}")
    return "\n".join(lines) + "\n\n"


def main(argv: list[str] | None = None) -> int:
    """CLI entry point: bump the version and insert a changelog entry below the title.

    Also rewrites the ``**Current version:**`` pointer; ``--dry-run`` only prints the result.
    """
    p = argparse.ArgumentParser(description="Bump semantic version + add changelog entry.")
    p.add_argument("--file", default="ops/changelog.md", help="path to changelog.md")
    p.add_argument("--part", choices=["major", "minor", "patch"], default="patch")
    p.add_argument("--message", required=True, help="what changed")
    p.add_argument("--reason", help="why")
    p.add_argument("--impact", help="expected impact")
    p.add_argument("--dry-run", action="store_true", help="print, do not write")
    args = p.parse_args(argv)

    path = Path(args.file)
    # utf-8-sig tolerates a BOM if the changelog was edited in an editor that adds one.
    text = path.read_text(encoding="utf-8-sig") if path.exists() else ""
    cur = find_current(text)
    new = bump(cur, args.part)
    cur_s, new_s = ".".join(map(str, cur)), ".".join(map(str, new))
    new_entry = entry(new_s, args)

    print(f"Versión: v{cur_s} → v{new_s}")
    print("Entrada de changelog:")
    print(new_entry.rstrip())

    if args.dry_run:
        print("(dry-run: no se escribió nada)")
        return 0

    # Insert the new entry after the first heading line if present, else at the top.
    if text:
        parts = text.split("\n", 1)
        if parts[0].startswith("#"):
            head = parts[0] + "\n\n"
            rest = parts[1] if len(parts) > 1 else ""
            # drop a leading blank line in rest to keep spacing clean
            rest = rest.lstrip("\n")
            updated = head + new_entry + rest
        else:
            updated = new_entry + text
    else:
        updated = (
            f"# changelog.md — System version & changes\n\n"
            f"**Current version:** v{new_s}\n\n" + new_entry
        )

    # keep a single "Current version" pointer in sync if present
    updated = re.sub(
        r"\*\*Current version:\*\*\s*v\d+\.\d+\.\d+", f"**Current version:** v{new_s}", updated
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(updated, encoding="utf-8")
    print(f"Actualizado {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
