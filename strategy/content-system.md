# content-system.md — The 3-layer content model (configurable ratios)

> Operationalizes `knowledge/organic-growth.md`. Ratios are read from
> `config/business-profile.md` (default **70/20/10**). Used by `content-planner`,
> `repurpose-engine`, and the prompt skills.

## The three layers (default 70 / 20 / 10)
| Layer | Share | What it is | Production |
|-------|-------|-----------|-----------|
| **A — Faceless** | ~70% | value/product/education | VO + b-roll/AI visuals, carousels, on-screen text, demos |
| **B — AI presenter** | ~20% | branded virtual persona, recurring segment | Higgsfield/Veo + ElevenLabs voice (see `persona-designer`) |
| **C — Real you** | ~10% | trust: milestones, lives, BTS, the operator's own story, testimonials | phone camera, lightly edited |

> Change ratios in `config/business-profile.md` (`layer_a/b/c`). The planner respects whatever
> is set.

## Pillars × layers (how to mix)
Each piece = one **pillar** (see organic-growth) produced in one **layer**.
- Education & product-in-action → mostly Layer A.
- Story/opportunity & the differentiator angle → Layer B or C (presenter or you).
- Social proof → A (aesthetic) or C (you with clients, w/ permission).
- Engagement/trends → A or B.

## Master idea → 4 platforms
1. `content-planner` picks the **master idea** (pillar + layer + hook + CTA goal).
2. `script-writer` writes the es-MX script (faceless + presenter variants).
3. `repurpose-engine` adapts to IG / FB / TikTok / YouTube (format, length, hook, caption,
   hashtags, text lockups).
4. `video-/image-/voice-prompt-studio` produce the AI prompts.
5. `caption-writer` finalizes per-platform captions + best time.
6. `compliance-guard` reviews everything before it's "ready".

## Weekly balance (default cadence — adjust in `weekly-plan.md`)
For a typical 7-day week aiming at volume:
- Layer A: ~5/7 days of primary pieces (plus repurposed shorts).
- Layer B: ~1–2 presenter pieces.
- Layer C: ~1 real-you piece (rotate: story / milestone / testimonial).
- Always: at least 1 opportunity/recruiting-angle piece and several sales-angle pieces.

## Series & repeatable formats (algorithm-friendly)
Maintain 2–4 named recurring series, e.g.:
- "Mitos de skincare" (education, Layer A)
- "El negocio sin filtros" (opportunity/differentiator angle, Layer C/B)
- "Rutina paso a paso" (product, Layer A)
- "Antes/después estético" (social proof, Layer A) — cosmetic only, no claims.

## Output conventions (quality bar)
Every deliverable, per platform: **hook + script/copy + hashtags + CTA + suggested best time +
AI prompts + Premiere notes**. Offer **2–3 labeled variants** when useful. es-MX. Compliant.
