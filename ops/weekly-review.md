# weekly-review.md — Weekly review (once/week)

> Revisión semanal para aprender y mejorar. Di: **"haz la revisión semanal"**. Maneja datos,
> no promesas.

## 1. Resumen de la semana (`metrics-analyst`)
- Corre el análisis de `ops/metrics.csv` (usa `scripts/compute_metrics.py`):
  totales, por plataforma, y vs floors (≥1 venta/día, ≥1 recluta/semana).
- Identifica **qué funcionó / qué no** (formatos, hooks, plataformas, horarios).

## 2. Ajustar el plan
- Actualiza `strategy/weekly-plan.md` para la próxima semana.
- Ajusta ratios de capas (70/20/10) en `config/business-profile.md` si los datos lo piden.
- Define 2–3 **experimentos** para la semana entrante.

## 3. Mejoras al sistema (`system-upgrader`)
- Procesa `ops/updates-inbox.md` (notas/archivos del operador).
- Aplica mejoras aprobadas a skills/playbooks; corre pruebas ligeras.
- **Sube la versión** (`scripts/bump_version.py`) y registra en `ops/changelog.md`.

## 4. Roadmap (`roadmap-strategist`)
- Revisa progreso contra `strategy/roadmap-to-top-rank.md` (fase actual e indicadores).
- Confirma si toca cambiar de fase (por indicadores sostenidos, no por una semana suelta).

## Checklist semanal
- [ ] Resumen de métricas hecho y comparado con floors.
- [ ] `weekly-plan.md` actualizado + experimentos definidos.
- [ ] `updates-inbox.md` procesado.
- [ ] Versión actualizada en `changelog.md`.
- [ ] Fase del roadmap revisada.

## Notas de esta semana
- Hallazgos:
- Decisiones:
- Para la próxima:
