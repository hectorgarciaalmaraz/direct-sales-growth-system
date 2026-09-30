---
name: content-planner
description: Genera "ideas maestras" y un calendario de contenido (semanal o mensual) a partir de metas, pilares y el modelo de 3 capas. Úsalo cuando el operador diga "dame ideas de contenido", "planéame la semana", "arma el calendario", "qué subo esta semana/mes", "plan de 30 días", "/plan-week" (plan, calendar, content ideas). Output en es-MX.
---

# content-planner

## When to use
Cuando el operador pide planear contenido: "dame ideas", "planéame la semana/el mes", "arma el
calendario", "qué subo", "plan de 30 días". También al iniciar el sprint de arranque (§Phase 6).

## Inputs (reads from)
- `config/business-profile.md` (ratios de capas, plataformas, foco de producto, tiempo)
- `config/goals-kpis.md` (floors y KPIs de la fase)
- `strategy/content-system.md` (modelo 3 capas, balance semanal)
- `strategy/roadmap-to-top-rank.md` (fase actual → énfasis venta/recluta)
- `knowledge/organic-growth.md` (pilares, repurposing, SEO social)
- `content/idea-bank.md`, `content/hook-bank.md` (semillas)

## Process
1. Lee config + estrategia; determina ratio de capas (default 70/20/10) y fase del roadmap.
2. Elige el tema/hero de la semana (o mes) y reparte por **pilares (1–5)** y **capas (A/B/C)**.
3. Para cada día define una **idea maestra**: pilar, capa, hook (es-MX), plataforma primaria,
   plataformas a repurposear, objetivo de CTA (venta/recluta/engage) y mejor horario.
4. Asegura: ≥1 pieza de oportunidad/reclutamiento, varias de venta, mezcla de capas ≈ ratio,
   y al menos 1 acción de lead magnet/lista.
5. (Opcional, determinista) usa `scripts/build_calendar.py` para volcar el calendario a CSV.
6. Escribe el plan en `strategy/weekly-plan.md` (o un archivo de 30 días en `strategy/`) y
   agrega ideas nuevas a `content/idea-bank.md`.

## Output format
Rellena la rejilla de `strategy/weekly-plan.md`:
`Día | Idea maestra | Pilar | Capa | Hook | Plataforma primaria | Repurpose | Objetivo CTA | Mejor horario`
Para planes mensuales, una fila por día (30 filas) agrupando por semana/tema. Cierra con un
**checklist semanal** y 2–3 hipótesis a probar. Ofrece 2–3 variantes del tema si aplica.

## Compliance
- Las ideas no deben requerir claims de ingreso/médicos. Antes de entregar piezas publicables,
  invoca `compliance-guard`.

## Examples
**Input:** "Planéame la semana con foco en hidratación."
**Output:** rejilla de 7 días (TikTok/IG primarios, FB/YT repurpose), mezcla 70/20/10, 1 pieza
del diferenciador personal (recluta), 2 de venta con CTA a WhatsApp, 1 lead magnet "reto 7 días",
horarios CDMX, + checklist e hipótesis.
