# User guide — Direct Sales Growth OS

A digital **growth operating system** (content + strategy + CRM "cockpit") for an independent
**direct-sales beauty consultant** in Mexico. It helps you grow a mostly **faceless**, **100%
organic**, **manual-publishing** business across Instagram, Facebook, TikTok, and YouTube,
working toward the company's **top leadership rank** (`target_rank`).

It generates ready-to-publish assets in **Mexican Spanish (`es-MX`)** — scripts, captions, AI
prompts (video/image/voice), funnels, and a CRM — all **compliant by default** (no income or
medical claims). **You publish manually.** The system never posts for you.

---

## What's inside

```
config/      ← single source of truth (edit business-profile.md to update everything)
knowledge/   ← company playbook (template), compliance, organic-growth/sales/recruiting playbooks
strategy/    ← roadmap to the top rank, content system (3-layer), weekly plan, campaigns
content/     ← idea & hook banks, templates, generated scripts & AI prompts
crm/         ← leads.csv, pipeline, team.csv, follow-up cadences
ops/         ← daily/weekly workflow, metrics.csv, changelog, skill registry, updates inbox
.claude/skills/  ← the Agent Skills that do the work (auto-discovered by Claude Code)
external-skills/ ← staging for downloaded skills (review before enabling)
```

## Requirements / setup

- **Claude Code** (CLI or VS Code extension).
- **Python 3.10+** — for the bundled helper scripts. Core scripts use the **standard library
  only**, so **no `pip install` is needed**.
- **Git** (optional but recommended) — version control.

If a future script ever needs a third-party package, it will be listed in `requirements.txt`
and installed with `pip install -r requirements.txt` (Windows) /
`pip install -r requirements.txt --break-system-packages` (macOS/Linux). The core system needs
none of this.

## First thing to do

1. Open `config/business-profile.md` and replace the fictional example (Sofía Ejemplo) with your
   data: company, target rank, handles, WhatsApp link, differentiator, time budget. **Editing
   this one file updates the whole system.**
2. Fill `knowledge/company-playbook.md` from your company's official sources (ranks, requirements).
3. Skim `CONFIG-TODO.md` — it lists every unknown (`⚠️ COMPLETE`) and company fact to confirm
   (`⚠️ VERIFY`).

## Daily use (the cockpit — ~60–90 min, see `ops/daily-workflow.md`)

1. In Claude Code, ask for today's batch — e.g. **"dame el contenido de hoy"**. The content
   skills deliver scripts, AI prompts (Higgsfield/Veo/ElevenLabs), and per-platform captions.
2. Produce/edit in your tools and **publish manually**.
3. Handle comments/DMs with the sales & recruiting funnels; log leads with **"agrega este
   prospecto"** (the `crm-tracker` skill).
4. Record results — append the day's numbers to `ops/metrics.csv`.

## Weekly review (see `ops/weekly-review.md`)

Ask for the weekly review — e.g. **"haz la revisión semanal"**. The `metrics-analyst` summarizes
what worked, `system-upgrader` applies approved improvements and bumps the version, and
`roadmap-strategist` checks progress toward the top rank.

## How to request content

Just say what you want in Spanish — the skills trigger on natural phrases:
- "dame ideas de contenido para la semana" → `content-planner`
- "escríbeme el guion del reel" → `script-writer`
- "adáptalo para las 4 plataformas" → `repurpose-engine`
- "hazme el prompt de video para Higgsfield/Veo" → `video-prompt-studio`
- "revisa que esto cumpla" → `compliance-guard`

## How to update the system

- **Change behavior:** edit files in `config/` (especially `business-profile.md`).
- **Leave an instruction or drop a file:** add it to `ops/updates-inbox.md`; `system-upgrader`
  will classify it (config / knowledge / skill), apply it, and log it in `ops/changelog.md`.

## How to install external skills (see the `skill-installer` skill)

Three paths (always review before enabling — treat like installing software):
1. **Plugin/marketplace** (preferred for official skills), e.g. the official `pdf` skill via
   `document-skills`. Check current syntax with `/help`.
2. **Manual folder** — drop the skill folder (with its `SKILL.md`) into `.claude/skills/`.
3. **`.skill`/zip or GitHub repo** — unzip/clone into `external-skills/`, review, then move.

Every installed skill is recorded in `ops/skill-registry.md`.

## Compliance & honesty

Everything publishable is checked by `compliance-guard` against `knowledge/compliance.md`:
no income/earnings claims, no guarantees, no medical/therapeutic product claims, respect for
the company's trademarks and consultant agreement, platform ToS, and privacy. The
system motivates with **realism** — it never promises income or timelines.
