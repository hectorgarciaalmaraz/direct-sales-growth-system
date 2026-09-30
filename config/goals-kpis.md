# goals-kpis.md — Goals, KPIs & floors

> Derived from `business-profile.md`. The system is driven by **leading indicators**, not by
> promised timelines or income. The top leadership rank is a multi-year organization-building
> goal; we measure the inputs we control and let results compound.

## North star
The company's **top leadership rank** (`target_rank` in `business-profile.md`; rank names in
`knowledge/company-playbook.md`). This is the long-horizon destination — never promised on a timeline. Progress is tracked by
the roadmap phases in `strategy/roadmap-to-top-rank.md`.

## Performance floors (minimums, not ceilings)
- **≥ 1 sale per day.**
- **≥ 1 recruit / new initiation per week.**
- Design must scale these with **no upper limit** (volume + consistency).

## Operational definitions (so counting is consistent)
- **A "sale" counts when:** a paid order is confirmed (payment received or committed for
  delivery) for a product, regardless of platform of origin. Reorders count. Log one row per
  sale day in `ops/metrics.csv` (aggregate `sales` count).
- **A "recruit / initiation" counts when:** a new person formally begins as an Independent
  consultant (signed/registered initiation — `⚠️ VERIFY` the company's exact initiation step &
  starter kit). A booked business presentation is a **lead**, not yet a recruit.
- **A "lead" counts when:** a real conversation about buying or about the business has started
  (DM/WhatsApp), captured in `crm/leads.csv` with an `interest` of `sale` or `business`.

## Leading KPIs (the inputs we actually control)
Tracked in `ops/metrics.csv` (`date, platform, posts, reach, saves, comments, dms, leads,
sales, recruits, notes`). Watch the **funnel**, not vanity metrics alone:

| Stage | Leading KPI | Why it matters |
|-------|-------------|----------------|
| Production | posts/week per platform | volume velocity drives organic discovery |
| Reach | reach, saves, shares | saves/shares signal value → algorithm reward |
| Engagement | comments, DMs opened | top of the conversation funnel |
| Pipeline | new leads/week | future sales & recruits |
| Sales | sales/day, reorders | the floor; cash flow |
| Recruiting | initiations/week, presentations booked | team = path to Director |
| Retention | active team members, month-2 retention | compounding org growth |

## KPIs by phase (see `strategy/roadmap-to-top-rank.md` for the full roadmap)
- **Phase 1 — First sales & leads:** establish posting cadence; first consistent sales; first
  10–20 leads in CRM. *Leading focus: posts/week, DMs, leads.*
- **Phase 2 — First active team:** hit recruit floor reliably; 1–3 active initiates.
  *Leading focus: presentations booked, initiations, month-2 retention.*
- **Phase 3 — Team leader / future director:** growing personal initiations + unit activity.
  *Leading focus: active team size, unit production trend.* `⚠️ VERIFY thresholds`
- **Phase 4 — Director qualification → Director:** sustain unit production + active consultants for qualification.
  *Leading focus: unit production points, active count.* `⚠️ VERIFY current numbers`
- **Phase 5 — Develop offspring directors → top rank:** grow first-line directors.
  *Leading focus: # first-line directors, # senior directors.* `⚠️ VERIFY requirements`

## Review cadence
- **Daily:** log `ops/metrics.csv`; check floors.
- **Weekly:** `metrics-analyst` summarizes; adjust `strategy/weekly-plan.md` (see
  `ops/weekly-review.md`).
- **No-promise rule:** report progress and experiments — never project income or dates.
