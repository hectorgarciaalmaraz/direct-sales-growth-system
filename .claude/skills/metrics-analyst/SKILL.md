---
name: metrics-analyst
description: Analiza resultados (qué funcionó / qué no), propone próximos experimentos y ajusta plan/KPIs. Úsalo cuando el operador diga "haz la revisión semanal", "analiza mis métricas/resultados", "qué funcionó esta semana", "qué experimento sigue" (métricas, resultados, revisión semanal, análisis, KPIs). Output en es-MX.
---

# metrics-analyst

## When to use
"haz la revisión semanal", "analiza mis métricas", "qué funcionó/qué no", "qué experimento
sigue", al correr `ops/weekly-review.md`.

## Inputs (reads from)
- `ops/metrics.csv` (date, platform, posts, reach, saves, comments, dms, leads, sales,
  recruits, notes)
- `ops/weekly-review.md` (notas), `config/goals-kpis.md` (floors/KPIs)
- `strategy/weekly-plan.md`, `strategy/content-system.md` (para ajustar ratios/plan)

## Process
1. Usa `scripts/compute_metrics.py` para resumir la semana (totales y por plataforma) de forma
   determinista (no estimes a ojo).
2. Compara contra floors (≥1 venta/día, ≥1 recluta/semana) y KPIs de la fase.
3. Identifica **qué funcionó / qué no** (formatos, hooks, plataformas) y 2–3 **experimentos**.
4. Propón ajustes concretos a `strategy/weekly-plan.md` y, si aplica, a las ratios.
5. Pasa hallazgos accionables a `system-upgrader` para mejoras a skills/playbooks.

## Output format
```
RESUMEN SEMANA (YYYY-MM-DD a YYYY-MM-DD)
Totales: posts __ reach __ saves __ comments __ dms __ leads __ sales __ recruits __
Por plataforma: ...
Vs floors: ventas/día ✔/✗ · reclutas/semana ✔/✗
Funcionó: ___ | No funcionó: ___
Experimentos próximos: 1) ___ 2) ___ 3) ___
Ajustes al plan: ___
```

## Scripts
- `scripts/compute_metrics.py` — ver `--help`.

## Compliance
- No produce contenido publicable; si sugiere copys, pásalos por `compliance-guard`.

## Examples
**Input:** "Analiza la semana."
**Output:** resumen con totales/plataforma desde `metrics.csv`, comparación con floors,
qué funcionó (p.ej. TikTok SEO), 3 experimentos y ajustes al plan.
