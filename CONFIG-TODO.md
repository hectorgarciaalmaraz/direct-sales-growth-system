# CONFIG-TODO.md — Unknowns to fill & facts to verify

> Ledger de pendientes. **`⚠️ COMPLETE`** = dato del operador (editar
> `config/business-profile.md`). **`⚠️ VERIFY`** = hecho de la compañía a confirmar en sus
> fuentes oficiales (portal de consultoras, contrato de consultora/líder, código de ética).
> Este repositorio se publica con valores de ejemplo (persona ficticia **Sofía Ejemplo**); un
> operador real llena esta tabla al instalar el sistema.

## ⚠️ COMPLETE — datos del operador
| # | Item | Dónde se usa | Estado / recomendación |
|---|------|--------------|------------------------|
| 1 | Nombre / marca personal | `config/business-profile.md`, bios, guiones | Ejemplo cargado: **Sofía Ejemplo** (ficticio) |
| 2 | Nombre de la compañía y `target_rank` | `config/business-profile.md`, `knowledge/company-playbook.md` | Completar antes de mencionar la compañía en contenido |
| 3 | Instagram | `config/platforms.md`, captions | Ejemplo: `@sofia.ejemplo` |
| 4 | Página de Facebook | `config/platforms.md`, embudo | Ver sugerencia abajo ⬇️ |
| 5 | TikTok | `config/platforms.md`, captions | Ejemplo: `@sofia_ejemplo` |
| 6 | YouTube | `config/platforms.md`, descripciones | Ejemplo: canal "Sofía Ejemplo" |
| 7 | WhatsApp | CTAs, embudo DM → WhatsApp | Placeholder: `https://wa.me/52XXXXXXXXXX` |
| 8 | Rango actual | `strategy/roadmap-to-top-rank.md` | Default: consultora recién iniciada |
| 9 | Diferenciador personal (`key_differentiator`) | `config/brand-voice.md`, `content/hook-bank.md` | Ejemplo cargado: mamá que emprende en sus tiempos libres |
| 10 | Tiempo diario | `ops/daily-workflow.md` | Default 60–90 min/día |
| 11 | Logística de entrega | `knowledge/sales-playbook.md` | Ejemplo: entregas personales en tu zona + envíos nacionales |
| 12 | Producto hero | ventas, guiones, prompts | Recomendación: **desmaquillante como producto de entrada** → rutina completa |
| 13 | Precios vigentes | ofertas, captions | `⚠️ COMPLETE` antes de publicar cualquier precio |
| 14 | Persona IA (capa B) | `persona-designer`, `voice-studio` | Diseñar con `persona-designer` |

### 📘 Sugerencia para la página de Facebook
- **Nombre:** `Sofía Ejemplo — Consultora de Belleza Independiente`
  *(no pongas el nombre de la compañía en el nombre de la página hasta confirmar la regla del
  contrato — ver `⚠️ VERIFY H`.)*
- **Categoría principal:** *Belleza, cosméticos y cuidado personal* → subcategoría
  *Consultor(a) de belleza* o *Cosméticos*.
- **Presentación / bio (es-MX, compliant):**
  > "Consultora de Belleza Independiente. Te ayudo a armar una rutina de cuidado de la piel
  > que sí puedas sostener. Entregas personales en mi zona y envíos a todo el país. ¿Dudas o
  > pedidos? Escríbeme por WhatsApp. También formo equipo: si te interesa conocer el negocio,
  > te lo explico sin compromiso y sin promesas."
- **Botón CTA:** *Enviar WhatsApp* → `https://wa.me/52XXXXXXXXXX`
- **Info a completar:** ciudad, horario de atención, correo de contacto.

## ⚠️ VERIFY — hechos de la compañía (fuentes oficiales)
| # | Fact | File | Status |
|---|------|------|--------|
| A | Nombres y orden del plan de carrera | `knowledge/company-playbook.md` | plantilla vacía; llenar desde fuentes oficiales |
| B | Requisitos del rango más alto (`target_rank`) | `knowledge/company-playbook.md` | confirmar en el portal de la compañía |
| C | Puntos / producción de unidad por rango | `knowledge/company-playbook.md` | confirmar números vigentes |
| D | Estructura de comisiones | `knowledge/company-playbook.md` | confirmar (y **nunca** publicar como claim de ingreso) |
| E | Reglas de venta online / marketplaces | `knowledge/compliance.md` | confirmar contrato y código de ética |
| F | Especificidades COFEPRIS/PROFECO en cosméticos | `knowledge/compliance.md` | reglas generales capturadas |
| G | Kit de inicio: contenido y costo | `knowledge/recruitment-playbook.md` | confirmar vigente |
| **H** | **Uso de la marca de la compañía en nombres de perfil/página y publicidad online** | `knowledge/compliance.md`, handles | **confirmar antes de nombrar perfiles y páginas** |
| I | Nombres/presentaciones/precios exactos de producto | `config/business-profile.md` | confirmar en el portal de la compañía |

## Environment notes
- Python 3.10+ para los scripts (solo biblioteca estándar) y Claude Code para las skills.
- Sin `pip install` requerido para el core.
