#!/usr/bin/env python3
"""compute_metrics.py — Summarize ops/metrics.csv (stdlib only).

Deterministic helper for the `metrics-analyst` skill. Reads the metrics log and prints totals
overall and per platform, optionally filtered to a date range (a week). Cross-platform via
pathlib. No third-party dependencies.

metrics.csv headers:
    date, platform, posts, reach, saves, comments, dms, leads, sales, recruits, notes

Examples:
    python compute_metrics.py --file ../../../ops/metrics.csv
    python compute_metrics.py --file ../../../ops/metrics.csv --since 2026-06-22 --until 2026-06-28
"""

import argparse
import csv
import sys
from pathlib import Path

# Windows consoles default to cp1252; force UTF-8 so es-MX text never crashes output.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001 - non-fatal; falls back to default stream
    pass

NUMERIC = ["posts", "reach", "saves", "comments", "dms", "leads", "sales", "recruits"]


def _to_int(v: str) -> int:
    """Convert a CSV cell to int (``"12"``, ``"12.0"`` → 12); blanks and bad values count as 0."""
    v = (v or "").strip()
    try:
        return int(float(v)) if v else 0
    except ValueError:
        return 0


def load(path: Path, since: str | None, until: str | None) -> list[dict]:
    """Read ``metrics.csv`` rows whose ``date`` falls inside ``[since, until]`` (inclusive).

    Raises:
        SystemExit: If the file does not exist.
    """
    if not path.exists():
        raise SystemExit(f"ERROR: no existe {path}")
    # utf-8-sig tolerates a BOM (Excel often saves CSV with one) without breaking headers.
    with path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        d = (r.get("date") or "").strip()
        if since and d and d < since:
            continue
        if until and d and d > until:
            continue
        out.append(r)
    return out


def totals(rows: list[dict]) -> dict:
    """Sum every numeric column (posts, reach, saves, comments, dms, leads, sales, recruits)."""
    t = {k: 0 for k in NUMERIC}
    for r in rows:
        for k in NUMERIC:
            t[k] += _to_int(r.get(k, "0"))
    return t


def main(argv: list[str] | None = None) -> int:
    """CLI entry point: print totals overall and per platform for the selected range; returns the exit code."""
    p = argparse.ArgumentParser(description="Summarize ops/metrics.csv (stdlib only).")
    p.add_argument("--file", default="ops/metrics.csv", help="path to metrics.csv")
    p.add_argument("--since", help="start date YYYY-MM-DD (inclusive)")
    p.add_argument("--until", help="end date YYYY-MM-DD (inclusive)")
    args = p.parse_args(argv)

    rows = load(Path(args.file), args.since, args.until)
    if not rows:
        print("(sin datos en el rango)")
        return 0

    rng = ""
    if args.since or args.until:
        rng = f" [{args.since or '...'} a {args.until or '...'}]"
    print(f"RESUMEN MÉTRICAS{rng} — {len(rows)} registros")

    t = totals(rows)
    print("Totales: " + " ".join(f"{k}={t[k]}" for k in NUMERIC))

    # per platform
    plats: dict[str, list[dict]] = {}
    for r in rows:
        plats.setdefault((r.get("platform") or "?").strip() or "?", []).append(r)
    print("Por plataforma:")
    for plat in sorted(plats):
        pt = totals(plats[plat])
        print(f"  {plat:<12} " + " ".join(f"{k}={pt[k]}" for k in NUMERIC))

    # floor signals
    days = len({(r.get("date") or "").strip() for r in rows if r.get("date")})
    print(f"Días con registro: {days} · sales={t['sales']} · recruits={t['recruits']}")
    if days:
        print(
            f"Promedio ventas/día (sobre días con registro): {t['sales']/days:.2f} "
            f"(floor ≥ 1.0)"
        )
    print(f"Reclutas en rango: {t['recruits']} (floor ≥ 1/semana)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
