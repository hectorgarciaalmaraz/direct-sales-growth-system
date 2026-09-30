# organic-growth.md — The organic growth engine

> The full strategy the content skills encode. Cold start, no ads, faceless-hybrid, manual
> publishing. Pairs with `strategy/content-system.md` (ratios) and `config/platforms.md`.

## The thesis
With no ad budget and no warm network, organic discovery comes from **volume + consistency +
strong hooks + social SEO**, compounded by **conversation loops** (comment→DM→WhatsApp) and a
growing owned list. We optimize **leading indicators** (see `config/goals-kpis.md`), not vanity.

## 1. The 3-layer content model (default 70/20/10)
- **Layer A — Faceless (~70%):** value/product/education via VO + b-roll/AI visuals, carousels,
  on-screen text, demos. Scales without a camera.
- **Layer B — Branded AI presenter (~20%):** a consistent virtual persona for a recognizable
  recurring segment (built via `persona-designer`).
- **Layer C — The real you (~10%):** occasional real appearances for trust — milestones, lives,
  behind-the-scenes, the operator's own story, testimonials. Critical for recruiting (people join
  people).
Ratios are configurable in `config/business-profile.md`.

## 2. Content pillars (mix per platform)
1. **Skincare/beauty education** (no medical claims) — pasos, ingredientes (cosmético), mitos.
2. **Product in action** — texturas, antes/después *estético*, rutinas, demos.
3. **Story / opportunity** — el negocio, lifestyle realista, comunidad, **tu diferenciador personal**.
4. **Social proof** — clientas felices, resultados estéticos, testimonios reales (con permiso).
5. **Engagement / trends** — formatos virales, retos, pattern interrupts.

Balance per week: lead with pillars 1–2 for reach, weave 3 for recruiting, 4 for trust, 5 for
discovery. Keep all within `knowledge/compliance.md`.

## 3. The hook system
- Hook lives in the **first 1–2 seconds** (and first line of every caption).
- Types: curiosity gap, pattern interrupt, bold-but-true statement, question, "lo que nadie te
  cuenta", numbered promise of value ("3 errores al aplicar el sérum").
- **Differentiator hooks** (from `key_differentiator`): "Empecé sin audiencia — esto aprendí",
  "Lo armo en mis ratos libres: así me organizo", "Lo que nadie te cuenta del negocio (desde mi
  punto de vista)."
- Hook bank lives in `content/hook-bank.md` (fed by `hook-writer`). Always compliant.

## 4. Repurposing matrix (master idea → 4 platforms)
Each idea is produced once, then `repurpose-engine` adapts it:

| Platform | Format | Length | Hook tweak | Caption/SEO | CTA |
|----------|--------|--------|------------|-------------|-----|
| Instagram | Reel / Carousel | 7–21 s | visual-first | keyworded + 3–8 hashtags | comment keyword → DM |
| Facebook | Reel / video / Group post | 30–90 s | slightly explanatory | descriptive | DM/Messenger → WhatsApp |
| TikTok | native short / series | 15–34 s | say keyword in 1st sec | spoken+on-screen keyword | comment → DM → WhatsApp |
| YouTube | Short (+long-form evergreen) | ≤60 s / 5–10 min | searchable title | title+desc+tags SEO | description link → WhatsApp |

Long-form YouTube is the **evergreen SEO** asset — make it for searchable topics.

## 5. Social SEO (discovery without ads)
- Treat **TikTok and YouTube as search engines**: say the keyword out loud, put it on-screen,
  in the caption/title/description, and in tags.
- Use **specific, local** keywords (e.g., "rutina de skincare para piel grasa", "cdmx",
  your neighborhood). Build series around recurring searches.
- IG: keyworded captions + alt text + niche hashtags. FB: descriptive captions + Groups.

## 6. Conversation & lead loops
- **comment → DM → WhatsApp:** soft keyword CTAs ("comenta 'RUTINA'"), then move to DM, then to
  WhatsApp for the real conversation (sales or business). Never mass-DM.
- **Lead magnets:** free guides/checklists/retos (e.g., "Rutina de 3 pasos PDF") to build an
  owned list from zero — capture via WhatsApp (see `lead-magnet-builder`). Respect privacy + ToS.
- **Save/share CTAs:** "guárdalo para tu rutina", "mándaselo a quien le sirva" — saves/shares
  boost reach.
- **Series & repeatable formats:** named recurring segments the algorithm and audience learn to
  expect (e.g., "Mitos de skincare", "El negocio sin filtros").

## 7. Volume velocity & cadence (cold start)
- Prioritize **TikTok + IG Reels daily**; cross-post to FB; YouTube Shorts daily + 1 long-form/
  week when capacity allows.
- Batch production (one studio session → many clips). Consistency beats perfection.
- Track posts/week in `ops/metrics.csv`; ramp volume as the workflow stabilizes.

## 8. Compounding loops (why this grows)
- More posts → more search/feed surface → more saves/shares → more reach → more comments/DMs →
  more leads → more sales/recruits → more social proof → better content → repeat.
- The owned list (WhatsApp + lead magnets) de-risks algorithm changes.
- `metrics-analyst` + `system-upgrader` turn results into the next week's improvements.

## Guardrails
Everything here ships only after `compliance-guard`: no income/medical claims, no spam/banned
tactics, real testimonials, minimal CRM data, inclusive messaging.
