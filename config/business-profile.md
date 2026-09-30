# business-profile.md — SINGLE SOURCE OF TRUTH

> **Edit this file to update the whole system.** Every skill reads from here. Change a value,
> and content, funnels, and strategy adapt. Items marked `⚠️ COMPLETE` are operator-only —
> fill them in. Items marked `⚠️ VERIFY` are company facts to confirm officially (see
> `CONFIG-TODO.md`). The values below are a **fictional example operator** (Sofía Ejemplo) so
> the system can be demoed end to end; replace them with your own.

## Identity
- **project_name:** `direct-sales-growth-os`
- **company_name:** `⚠️ COMPLETE` — the direct-sales company you represent
- **operator_role:** Independent direct-sales beauty consultant — *Consultora de Belleza Independiente*
- **display_name / brand:** **Sofía Ejemplo** *(ejemplo ficticio)*
- **recruits:** anyone interested in the opportunity (open to all)
- **current_rank:** entry-level consultant — recién iniciada (rank names in `knowledge/company-playbook.md`)
- **target_rank:** `⚠️ COMPLETE` — the company's top leadership rank (north star)

## Market & language
- **country:** México
- **city / area:** Ciudad de México (entregas personales en tu zona — `⚠️ COMPLETE`)
- **shipping:** envíos a todo el país (paquetería)
- **output_language:** `es-MX` (Mexican Spanish) — all generated content
- **identifier_language:** English / kebab-case (folders, skills, scripts, YAML keys)

## Starting point (cold start)
- **team:** none or very small
- **audience:** none / building from zero
- **warm_network:** none to activate
- **key_differentiator:** **mamá que emprende en sus tiempos libres** *(ejemplo)* — the personal
  angle that makes you memorable. Other examples: estudiante que paga sus estudios, persona que
  cambió de carrera, profesionista con un negocio paralelo. It feeds `config/brand-voice.md`
  and `content/hook-bank.md`; never use it deceptively.

## Growth model
- **channels:** Instagram, Facebook, TikTok, YouTube
- **mode:** organic only (no paid ads for now)
- **visibility:** faceless-hybrid (3-layer model, see `strategy/content-system.md`)
- **publishing:** manual (no posting APIs)
- **repurposing:** one "master idea" → 4 platforms
- **current_focus:** `balanced` — options: `sales-first`, `recruiting-first`, `balanced`.
  `recruiting-first` gives more weight to pillar 3 (opportunity) and the recruiting funnel.

## 3-layer content ratios (default 70/20/10)
> Adjustable at any time. Operators comfortable on camera who prioritise recruiting often move
> toward more layer C (e.g. 60/15/25) — people join people.
- **layer_a_faceless:** 70% — value/product/education, voiceover + b-roll/AI visuals (volume)
- **layer_b_presenter:** 20% — branded AI presenter persona (see `persona-designer`)
- **layer_c_real_you:** 10% — your real appearances: milestones, BTS, your story, testimonials,
  opportunity presentations (key for recruiting)

## Focus product
- **primary:** skincare-led (rutinas, cuidado de la piel)
- **secondary:** color/maquillaje + sets/kits
- **hero_sku (entrada):** **Desmaquillante** — low-friction entry purchase → conversation →
  full routine.
- **hero_sku (ticket/recompra):** **línea de tratamiento / cuidado de la piel por pasos**
  (limpieza → tratamiento → hidratación → protección). Goal: move from entry product to routine.
- `⚠️ VERIFY` exact product names, sizes and current prices in the company's official catalog
  before publishing them.

## Handles & contact *(ejemplos ficticios — reemplázalos)*
- **instagram:** `@sofia.ejemplo`
- **facebook:** `⚠️ COMPLETE` — see the name/category/bio suggestion in `CONFIG-TODO.md`
- **tiktok:** `@sofia_ejemplo`
- **youtube:** canal **"Sofía Ejemplo"**
- **whatsapp_link:** `https://wa.me/52XXXXXXXXXX` (`⚠️ COMPLETE` with your number, digits only
  with country code)
- `⚠️ VERIFY` the consultant agreement's rules on using the company's brand name in profile/page
  names and online advertising.

## Time & cadence
- **daily_time_budget:** **60–90 min/día** (default) — see `ops/daily-workflow.md`:
  - ~30–40 min production (content batch + editing)
  - ~20–30 min **conversations** (DMs, comments, WhatsApp, follow-ups) ← highest leverage
  - ~10 min CRM + metrics
  - +60 min once a week for the weekly review
- **posting_cadence_target:** see `config/platforms.md` (volume + consistency)

## AI tools available (see `config/ai-tools.md`)
- **video:** Higgsfield (Kling 3, Seedance 2), Veo 3.1 (Google Pro)
- **voice:** ElevenLabs
- **editing:** Adobe Premiere Pro
- **persona:** operator can build branded AI personas

## AI presenter persona (layer B)
- **type:** `⚠️ COMPLETE` — a branded virtual presenter or an AI clone of the operator (only with
  their own consent and voice).
- **use:** short recurring segments (30 s tips) and support pieces; it does not replace real
  layer-C content in sensitive recruiting content (honesty first).
- Define it with `persona-designer` → save to `assets/persona/`.

## Reusable operator assets
- **prompt_banks / styles:** none assumed. Build a brand style from scratch; store references in
  `assets/`.

## Floor KPIs (minimums, not ceilings — see `config/goals-kpis.md`)
- **sales_floor:** ≥ 1 sale/day
- **recruit_floor:** ≥ 1 recruit/new initiation per week
- **north_star:** `target_rank` (multi-year org-building goal)

## Compliance posture (see `knowledge/compliance.md`)
- No income/earnings claims · no guarantees · no medical/therapeutic claims
- Respect the company's IP + consultant agreement + code of ethics
- Platform ToS · privacy (minimal CRM data) · inclusive messaging
