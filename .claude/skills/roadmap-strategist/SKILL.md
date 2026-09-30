---
name: roadmap-strategist
description: Recalcula el roadmap al rango más alto de la compañía (target_rank) según el estado actual e indicadores. Úsalo cuando el operador diga "revisa el roadmap", "¿en qué fase voy?", "qué sigue para llegar a directora", "actualiza el plan a largo plazo" (roadmap, fase, rango, directora, estrategia largo plazo). Output en es-MX, sin promesas de tiempo/ingreso.
---

# roadmap-strategist

## When to use
"revisa el roadmap", "¿en qué fase estoy?", "qué sigue para el siguiente rango", "actualiza el
plan a largo plazo", en la revisión semanal.

## Inputs (reads from)
- `strategy/roadmap-to-top-rank.md` (fases + indicadores)
- `knowledge/company-playbook.md` (ladder/umbrales — `⚠️ VERIFY` antes de citar números)
- `ops/metrics.csv` (vía `metrics-analyst`), `crm/team.csv` (equipo activo)
- `config/goals-kpis.md`

## Process
1. Lee indicadores reales (ventas, leads, reclutas, equipo activo, producción/unidad).
2. Determina la **fase actual** y si procede avanzar (por indicadores sostenidos, no una semana).
3. Define los **inputs de la próxima fase** y 2–3 prioridades accionables.
4. **Sin timelines ni proyecciones de ingreso.** Marca `⚠️ VERIFY` cualquier umbral oficial.
5. Sugiere ajustes a `strategy/` y registra cambios vía `system-upgrader`.

## Output format
```
FASE ACTUAL: ___ (por qué, según indicadores)
¿Avanzar? sí/no (qué falta)
PRÓXIMA FASE — inputs clave: 1) ___ 2) ___ 3) ___
Riesgos / `⚠️ VERIFY` pendientes
```

## Compliance
- Nada de promesas de tiempo/ingreso (§9). Invoca `compliance-guard` si genera mensajes
  publicables.

## Examples
**Input:** "¿En qué fase voy y qué sigue?"
**Output:** "Fase 1 (primeras ventas/leads), aún sin ≥1 recluta/semana sostenido → enfócate en
contenido de oportunidad + invitaciones honestas; inputs: presentaciones agendadas, iniciaciones,
retención mes-2." Sin fechas ni cifras prometidas.
