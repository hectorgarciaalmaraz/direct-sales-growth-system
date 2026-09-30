#!/usr/bin/env python3
"""update_crm.py — Deterministic CRM helper for the `crm-tracker` skill (stdlib only).

Manages crm/leads.csv and crm/team.csv: add / list / update rows and find due follow-ups.
Creates files with the correct headers if missing. Cross-platform via pathlib. Privacy by
design: use an alias, never store unnecessary sensitive data.

Examples:
    python update_crm.py add-lead --alias "Ana_IG" --platform instagram --interest sale \\
        --next-step "enviar rutina" --next-date 2026-06-26 --crm-dir ../../../crm
    python update_crm.py list-leads --crm-dir ../../../crm
    python update_crm.py update-lead --id 1 --stage en_conversacion --crm-dir ../../../crm
    python update_crm.py due --crm-dir ../../../crm
    python update_crm.py add-member --alias "Luis" --role consultor --crm-dir ../../../crm
"""

import argparse
import csv
import sys
from datetime import date
from pathlib import Path

# Windows consoles default to cp1252; force UTF-8 so es-MX text never crashes output.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001 - non-fatal; falls back to default stream
    pass

LEADS_HEADERS = [
    "id",
    "alias",
    "platform",
    "first_contact_date",
    "interest",
    "stage",
    "last_contact",
    "next_step",
    "notes",
]
TEAM_HEADERS = [
    "id",
    "alias",
    "role",
    "initiation_date",
    "status",
    "last_contact",
    "next_step",
    "notes",
]

# crm/leads.csv carries an explicit 'next_date' for scheduling; keep it last so the
# spec headers stay intact while still supporting `due`.
LEADS_FULL = LEADS_HEADERS + ["next_date"]
TEAM_FULL = TEAM_HEADERS + ["next_date"]


def _today() -> str:
    """Return today's date in ISO format."""
    return date.today().isoformat()


def _read(path: Path, headers: list[str]) -> list[dict]:
    """Read a CRM CSV (missing file → empty list), filling any absent column with ``""``."""
    if not path.exists():
        return []
    # utf-8-sig tolerates a BOM (Excel often saves CSV with one) without breaking headers.
    with path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    # tolerate files that only have the spec headers (no next_date yet)
    for r in rows:
        for h in headers:
            r.setdefault(h, "")
    return rows


def _write(path: Path, headers: list[str], rows: list[dict]) -> None:
    """Rewrite a CRM CSV with ``headers`` as columns, creating the folder if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader()
        for r in rows:
            w.writerow({h: r.get(h, "") for h in headers})


def _next_id(rows: list[dict]) -> int:
    """Return the next numeric id (max existing id + 1, or 1)."""
    ids = [int(r["id"]) for r in rows if str(r.get("id", "")).isdigit()]
    return (max(ids) + 1) if ids else 1


def cmd_add_lead(args: argparse.Namespace, crm: Path) -> int:
    """Append a lead to ``leads.csv`` (defaults: interest ``sale``, stage ``nuevo``, today's dates)."""
    path = crm / "leads.csv"
    rows = _read(path, LEADS_FULL)
    new = {
        "id": str(_next_id(rows)),
        "alias": args.alias,
        "platform": args.platform or "",
        "first_contact_date": args.first_date or _today(),
        "interest": args.interest or "sale",
        "stage": args.stage or "nuevo",
        "last_contact": _today(),
        "next_step": args.next_step or "",
        "notes": args.notes or "",
        "next_date": args.next_date or "",
    }
    rows.append(new)
    _write(path, LEADS_FULL, rows)
    print(
        f"Lead agregado: id={new['id']} alias={new['alias']!r} "
        f"platform={new['platform']} interest={new['interest']} stage={new['stage']} "
        f"next_step={new['next_step']!r} ({new['next_date'] or 's/f'})"
    )
    return 0


def cmd_update_lead(args: argparse.Namespace, crm: Path) -> int:
    """Update stage/interest/next step/next date/notes/platform of lead ``--id``.

    Also sets ``last_contact`` to today. Exits with an error if the id does not exist.
    """
    path = crm / "leads.csv"
    rows = _read(path, LEADS_FULL)
    target = next((r for r in rows if r["id"] == str(args.id)), None)
    if not target:
        raise SystemExit(f"ERROR: no existe lead id={args.id}")
    for field in ("stage", "interest", "next_step", "next_date", "notes", "platform"):
        val = getattr(args, field if field != "next_date" else "next_date", None)
        if val is not None:
            target[field] = val
    target["last_contact"] = _today()
    _write(path, LEADS_FULL, rows)
    print(
        f"Lead actualizado: id={target['id']} stage={target['stage']} "
        f"next_step={target['next_step']!r} ({target['next_date'] or 's/f'})"
    )
    return 0


def cmd_list_leads(args: argparse.Namespace, crm: Path) -> int:
    """Print every lead as one aligned line."""
    rows = _read(crm / "leads.csv", LEADS_FULL)
    if not rows:
        print("(sin leads)")
        return 0
    for r in rows:
        print(
            f"{r['id']:>3} | {r['alias']:<16} | {r['platform']:<10} | "
            f"{r['interest']:<8} | {r['stage']:<16} | next: {r['next_step']} "
            f"({r['next_date'] or 's/f'})"
        )
    return 0


def cmd_due(args: argparse.Namespace, crm: Path) -> int:
    """Print leads whose ``next_date`` is today or earlier (ISO dates compared as strings)."""
    today = _today()
    rows = _read(crm / "leads.csv", LEADS_FULL)
    due = [r for r in rows if r.get("next_date") and r["next_date"] <= today]
    if not due:
        print(f"Sin seguimientos vencidos/para hoy ({today}).")
        return 0
    print(f"Seguimientos al {today}:")
    for r in due:
        print(f"  - id={r['id']} {r['alias']}: {r['next_step']} (programado {r['next_date']})")
    return 0


def cmd_add_member(args: argparse.Namespace, crm: Path) -> int:
    """Append a team member to ``team.csv`` (defaults: role ``consultor``, status ``nuevo``)."""
    path = crm / "team.csv"
    rows = _read(path, TEAM_FULL)
    new = {
        "id": str(_next_id(rows)),
        "alias": args.alias,
        "role": args.role or "consultor",
        "initiation_date": args.init_date or _today(),
        "status": args.status or "nuevo",
        "last_contact": _today(),
        "next_step": args.next_step or "onboarding semana 1",
        "notes": args.notes or "",
        "next_date": args.next_date or "",
    }
    rows.append(new)
    _write(path, TEAM_FULL, rows)
    print(
        f"Miembro agregado: id={new['id']} alias={new['alias']!r} role={new['role']} "
        f"status={new['status']}"
    )
    return 0


def cmd_list_team(args: argparse.Namespace, crm: Path) -> int:
    """Print every team member as one aligned line."""
    rows = _read(crm / "team.csv", TEAM_FULL)
    if not rows:
        print("(sin equipo)")
        return 0
    for r in rows:
        print(
            f"{r['id']:>3} | {r['alias']:<16} | {r['role']:<12} | {r['status']:<10} | "
            f"inició {r['initiation_date']} | next: {r['next_step']}"
        )
    return 0


def main(argv: list[str] | None = None) -> int:
    """CLI entry point: parse the sub-command and run it against ``--crm-dir``; returns the exit code."""
    p = argparse.ArgumentParser(description="CRM helper for crm-tracker (stdlib only).")
    p.add_argument("--crm-dir", default="crm", help="path to crm/ directory")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add-lead")
    a.add_argument("--alias", required=True)
    a.add_argument("--platform")
    a.add_argument("--interest", choices=["sale", "business"])
    a.add_argument("--stage")
    a.add_argument("--first-date", dest="first_date")
    a.add_argument("--next-step", dest="next_step")
    a.add_argument("--next-date", dest="next_date")
    a.add_argument("--notes")
    a.set_defaults(func=cmd_add_lead)

    u = sub.add_parser("update-lead")
    u.add_argument("--id", required=True)
    u.add_argument("--stage")
    u.add_argument("--interest", choices=["sale", "business"])
    u.add_argument("--next-step", dest="next_step")
    u.add_argument("--next-date", dest="next_date")
    u.add_argument("--platform")
    u.add_argument("--notes")
    u.set_defaults(func=cmd_update_lead)

    sub.add_parser("list-leads").set_defaults(func=cmd_list_leads)
    sub.add_parser("due").set_defaults(func=cmd_due)

    m = sub.add_parser("add-member")
    m.add_argument("--alias", required=True)
    m.add_argument("--role")
    m.add_argument("--status")
    m.add_argument("--init-date", dest="init_date")
    m.add_argument("--next-step", dest="next_step")
    m.add_argument("--next-date", dest="next_date")
    m.add_argument("--notes")
    m.set_defaults(func=cmd_add_member)

    sub.add_parser("list-team").set_defaults(func=cmd_list_team)

    args = p.parse_args(argv)
    crm = Path(args.crm_dir)
    return args.func(args, crm)


if __name__ == "__main__":
    raise SystemExit(main())
