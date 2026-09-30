# Direct Sales Growth OS — Startup Package (v0.1.0)

> Entrega inicial (§15 del MASTER-PROMPT). Resumen de lo construido + cómo arrancar.
> Reporte generado al terminar el build inicial. Idioma de contenido: **es-MX**. Publicación: **manual**.

## 1. Qué se construyó

**Estructura completa** en la raíz del proyecto:
`config/ · knowledge/ (+ platform-guides/) · strategy/ (+ campaigns/) · content/ (+ templates/,
scripts/, prompts/, day-01/) · crm/ · ops/ · external-skills/ · .claude/skills/ · assets/`

**Configuración (single source of truth):** `config/business-profile.md` + `goals-kpis.md`,
`brand-voice.md`, `platforms.md`, `ai-tools.md`.

**Conocimiento:** `company-playbook.md` (plantilla del plan de carrera, a llenar desde fuentes oficiales),
`compliance.md` (norma §9), `organic-growth.md`, `sales-playbook.md`, `recruitment-playbook.md`,
y 4 guías de plataforma (IG/FB/TikTok/YouTube).

**Estrategia:** `roadmap-to-top-rank.md` (fases por indicadores, sin timelines),
`content-system.md` (3 capas 70/20/10), `weekly-plan.md`, **plan de 30 días**
(`content-plan-30d.md` + `calendar-30d.csv`).

**20 Agent Skills** en el build inicial (hoy 21 con `offer-writer`) en `.claude/skills/` (formato SKILL.md, descripciones bilingües "pushy"):
- **Core (14, §6.2):** content-planner, script-writer, caption-writer, repurpose-engine,
  video-prompt-studio, image-prompt-studio, voice-studio, sales-funnel, recruitment-funnel,
  crm-tracker, metrics-analyst, compliance-guard, skill-installer, system-upgrader.
- **Extended (6, §6.3):** hook-writer, carousel-builder, persona-designer, lead-magnet-builder,
  roadmap-strategist, pdf-export.

**Scripts deterministas (Python stdlib, Windows-safe):** `build_calendar.py`, `update_crm.py`,
`compute_metrics.py`, `validate_skill.py`, `bump_version.py` — todos probados.

**CRM & Ops:** `leads.csv` / `team.csv` (encabezados correctos), `pipeline.md`, `followups.md`,
`daily-workflow.md`, `weekly-review.md`, `metrics.csv`, `changelog.md` (**v0.1.0**),
`skill-registry.md`, `updates-inbox.md`.

**Compliance:** `compliance-guard` integrado; revisa todo lo publicable; sin claims de
ingreso/médicos.

## 2. Plan de 30 días + carpeta "Day 1" (lista para publicar)
- **30 días:** `strategy/content-plan-30d.md` (balance 70/20/10, pilares, series, ≥1 pieza de
  oportunidad/semana, 2 lead magnets) + `strategy/calendar-30d.csv`.
- **Day 1** (`content/day-01/`): idea "Tu tipo de piel decide tu rutina" para las **4
  plataformas** (guion + caption + hashtags + CTA + horario + prompts IA + notas Premiere).
  **Reporte de compliance: compliant ✓, sin banderas rojas.**

## 3. Cómo usar (README)
- **Diario (~60–90 min):** "dame el contenido de hoy" → batch 4 plataformas; publica manual;
  atiende DMs (`sales-funnel`/`recruitment-funnel`); "agrega este prospecto" (`crm-tracker`);
  registra `ops/metrics.csv`. Ver `ops/daily-workflow.md`.
- **Semanal:** "haz la revisión semanal" → `metrics-analyst` + `system-upgrader` +
  `roadmap-strategist`. Ver `ops/weekly-review.md`.
- **Actualizar el sistema:** edita `config/` o deja notas en `ops/updates-inbox.md`.
- **Instalar skills externas:** `skill-installer` (3 caminos + protocolo de seguridad); PDF vía
  `external-skills/README.md`.
- Guía completa: `README.md`.

## 4. Pendientes a completar/verificar (ver `CONFIG-TODO.md`)
**⚠️ COMPLETE (datos del operador):** handles IG/FB/TikTok/YouTube, link de WhatsApp, compañía y rango
exacto, nombre/marca, tiempo diario, producto hero, logística de entrega, assets/prompt banks,
persona AI, diferenciador personal.
**⚠️ VERIFY (hechos de la compañía, fuentes oficiales):** nombres exactos del plan de carrera,
requisitos vigentes del rango más alto, puntos/umbrales por
rango, estructura de comisiones, reglas de venta online del contrato, detalle COFEPRIS/PROFECO,
contenido/costo del kit de inicio.

## 5. Nota de especificación
§6.2 dice "15 skills core" pero su tabla lista **14**; se construyeron las 14 nombradas (no se
fabricó una 15ª sin especificar). Total de skills entregadas: **20** (14 core + 6 extended).

---
**Versión del sistema: v0.1.0** · Próximo paso sugerido: completar `config/business-profile.md`
y arrancar con la carpeta `content/day-01/`.
