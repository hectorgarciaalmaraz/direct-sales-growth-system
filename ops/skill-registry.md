# skill-registry.md — Installed skills inventory

> Inventario de skills (propias + externas). `skill-installer` agrega filas al instalar/revisar.
> Estados: `active` (en uso), `reviewed` (revisada, no habilitada), `quarantined` (en revisión/
> bloqueada). Las externas se revisan antes de habilitar (ver `skill-installer`).

## Propias — CORE (§6.2)
| name | origin | version | date | reviewer | status |
|------|--------|---------|------|----------|--------|
| content-planner | built-in | v0.1.0 | 2026-06-24 | build | active |
| script-writer | built-in | v0.1.0 | 2026-06-24 | build | active |
| caption-writer | built-in | v0.1.0 | 2026-06-24 | build | active |
| repurpose-engine | built-in | v0.1.0 | 2026-06-24 | build | active |
| video-prompt-studio | built-in | v0.1.0 | 2026-06-24 | build | active |
| image-prompt-studio | built-in | v0.1.0 | 2026-06-24 | build | active |
| voice-studio | built-in | v0.1.0 | 2026-06-24 | build | active |
| sales-funnel | built-in | v0.1.0 | 2026-06-24 | build | active |
| recruitment-funnel | built-in | v0.1.0 | 2026-06-24 | build | active |
| crm-tracker | built-in | v0.1.0 | 2026-06-24 | build | active |
| metrics-analyst | built-in | v0.1.0 | 2026-06-24 | build | active |
| compliance-guard | built-in | v0.1.0 | 2026-06-24 | build | active |
| skill-installer | built-in | v0.1.0 | 2026-06-24 | build | active |
| system-upgrader | built-in | v0.1.0 | 2026-06-24 | build | active |

## Propias — EXTENDED (§6.3)
| name | origin | version | date | reviewer | status |
|------|--------|---------|------|----------|--------|
| hook-writer | built-in | v0.1.0 | 2026-06-24 | build | active |
| carousel-builder | built-in | v0.1.0 | 2026-06-24 | build | active |
| persona-designer | built-in | v0.1.0 | 2026-06-24 | build | active |
| lead-magnet-builder | built-in | v0.1.0 | 2026-06-24 | build | active |
| roadmap-strategist | built-in | v0.1.0 | 2026-06-24 | build | active |
| pdf-export | built-in | v0.1.0 | 2026-06-24 | build | active |
| offer-writer | built-in (system-upgrader) | v0.4.0 | 2026-09-22 | operator | active |

## Externas
| name | origin/URL | version | date | reviewer | status |
|------|-----------|---------|------|----------|--------|
| pdf (document-skills) | anthropics/skills (plugin) o carpeta manual | ⚠️ VERIFY | pending | operator | reviewed (instalar vía `skill-installer`; usado por `pdf-export`) |

> Para instalar la skill oficial `pdf`: sigue `skill-installer` (camino 1 plugin, o camino 2
> carpeta manual). Al habilitarla, cambia su `status` a `active` y registra la versión.
