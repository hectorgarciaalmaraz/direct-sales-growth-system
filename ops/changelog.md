# changelog.md — System version & changes

## v0.5.0 — 2026-09-30
- **Cambio:** Versión pública genérica: marca de la compañía, datos del operador y contenido del Día 1 reemplazados por una persona ficticia (Sofía Ejemplo) y placeholders; playbook de la compañía convertido en plantilla (`company-playbook.md`) y roadmap generalizado al rango más alto (`roadmap-to-top-rank.md`); diferenciador personal convertido en campo configurable (`key_differentiator`); capas de vuelta al default 70/20/10.
- **Razón:** publicar el sistema como portafolio sin datos reales del operador ni de la compañía.
- **Impacto:** el sistema funciona para cualquier consultora de venta directa de belleza; un operador real llena `config/business-profile.md` y `knowledge/company-playbook.md`.

## v0.4.0 — 2026-09-22
- **Cambio:** Nueva skill offer-writer + knowledge/persuasion-playbook.md (7 secuestros humanos + efecto tingle); plan 30d re-fechado a 24-sep
- **Razón:** Operador pidio integrar el framework de persuasion de Craig Clemens a ventas e iniciaciones
- **Impacto:** Copy de venta/iniciacion mas persuasivo con adaptaciones de compliance; demos con tingle ancladas al desmaquillante

## v0.3.0 — 2026-09-02
- **Cambio:** Config personalizada con los datos del operador + Día 1 regenerado
- **Razón:** el operador entregó handles, WhatsApp, rango, logística, persona y tiempo disponible
- **Impacto:** contenido y embudos salen con CTAs reales; entrada de venta = desmaquillante; capa B = clon de IA del operador

## v0.2.0 — 2026-09-02
- **Cambio:** Config: mezcla de capas 70/20/10 -> 60/15/25 y enfoque recruiting-first
- **Razón:** Operador comodo apareciendo (capa C) y prioriza reclutar
- **Impacto:** más contenido de oportunidad/diferenciador personal y presencia real para acelerar equipo

**Current version:** v0.5.0

> Versionado semántico. Cada cambio significativo a skills/playbooks se registra con fecha,
> razón e impacto. `system-upgrader` actualiza este archivo con `scripts/bump_version.py`.

## v0.1.0 — 2026-06-24
- **Cambio:** Build inicial del sistema desde MASTER-PROMPT.md (§0–§15).
- **Incluye:**
  - Estructura completa (`config/`, `knowledge/`, `strategy/`, `content/`, `crm/`, `ops/`,
    `external-skills/`, `.claude/skills/`).
  - `config/` (5), `knowledge/` (6 + 4 guías de plataforma), `strategy/` (3) + campañas.
  - 14 skills core nombradas en §6.2 + 6 skills extendidas (§6.3) = 20 skills.
  - Scripts deterministas stdlib: `build_calendar.py`, `update_crm.py`, `compute_metrics.py`,
    `validate_skill.py`, `bump_version.py`.
  - CRM (`leads.csv`, `team.csv`, `pipeline.md`, `followups.md`) y ops (workflows, métricas,
    registro de skills, bandeja de updates).
  - `compliance-guard` invocable por las demás skills.
- **Razón:** entregar el sistema operativo de crecimiento orgánico para el negocio de venta directa.
- **Impacto:** sistema listo para el flujo diario; pendientes marcados en `CONFIG-TODO.md`
  (`⚠️ COMPLETE` / `⚠️ VERIFY`).
- **Nota de especificación:** §6.2 menciona "15" skills core pero su tabla lista 14; se
  construyeron las 14 nombradas (no se fabricó una 15ª sin especificar).
