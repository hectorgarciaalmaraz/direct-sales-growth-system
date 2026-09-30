#!/usr/bin/env python3
"""build_calendar.py — Generate a content-calendar CSV skeleton (stdlib only).

Deterministic helper for the `content-planner` skill. Produces N dated rows with the
weekly-plan columns so the planner can fill ideas without hand-counting dates. Cross-platform
(uses pathlib). No third-party dependencies.

Usage:
    python build_calendar.py --start 2026-06-25 --days 30 --out ../../../strategy/calendar-30d.csv
    python build_calendar.py --start 2026-06-25 --days 7   # prints to stdout
"""

import argparse
import csv
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

# Windows consoles default to cp1252; force UTF-8 so es-MX text/symbols never crash output.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001 - non-fatal; falls back to default stream
    pass

COLUMNS = [
    "date",
    "weekday",
    "master_idea",
    "pillar",
    "layer",
    "hook_es_mx",
    "primary_platform",
    "repurpose_to",
    "cta_goal",
    "best_time",
    "status",
]

# Default rotation matches strategy/content-system.md weekly cadence.
PRIMARY_ROTATION = ["TikTok", "Instagram", "TikTok", "Instagram", "TikTok", "YouTube", "Instagram"]
WEEKDAYS_ES = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


def parse_date(s: str) -> date:
    """Parse ``YYYY-MM-DD`` or exit with a clear error message."""
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        raise SystemExit(f"ERROR: --start must be YYYY-MM-DD, got: {s!r}") from None


def build_rows(start: date, days: int) -> list[dict]:
    """Return ``days`` calendar rows starting at ``start``.

    Each row has the date, the Spanish weekday, the primary platform from ``PRIMARY_ROTATION``,
    the platforms to repurpose to and ``status="planned"``; idea, pillar, layer, hook, CTA and
    time are left empty for ``content-planner`` to fill.
    """
    rows = []
    for i in range(days):
        d = start + timedelta(days=i)
        wd = d.weekday()  # 0=Mon
        primary = PRIMARY_ROTATION[wd]
        rows.append(
            {
                "date": d.isoformat(),
                "weekday": WEEKDAYS_ES[wd],
                "master_idea": "",
                "pillar": "",
                "layer": "",
                "hook_es_mx": "",
                "primary_platform": primary,
                "repurpose_to": "IG/FB/YT" if primary == "TikTok" else "TikTok/FB/YT",
                "cta_goal": "",
                "best_time": "",
                "status": "planned",
            }
        )
    return rows


def main(argv: list[str] | None = None) -> int:
    """CLI entry point: build the calendar and write it to ``--out`` or stdout; returns the exit code."""
    p = argparse.ArgumentParser(description="Build a content-calendar CSV skeleton.")
    p.add_argument("--start", required=True, help="start date YYYY-MM-DD")
    p.add_argument("--days", type=int, default=7, help="number of days (default 7)")
    p.add_argument("--out", help="output CSV path (default: stdout)")
    args = p.parse_args(argv)

    if args.days < 1:
        raise SystemExit("ERROR: --days must be >= 1")

    rows = build_rows(parse_date(args.start), args.days)

    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            w.writeheader()
            w.writerows(rows)
        print(f"Wrote {len(rows)} rows to {out}")
    else:
        w = csv.DictWriter(sys.stdout, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
