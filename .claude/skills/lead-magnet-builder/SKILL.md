---
name: lead-magnet-builder
description: Diseña lead magnets (guías, retos, checklists) + secuencia de captura por WhatsApp. Úsalo cuando el operador diga "hazme un lead magnet", "guía/reto/checklist gratis", "imán de prospectos", "secuencia para capturar contactos" (lead magnet, imán, guía gratis, reto, captura). Output en es-MX, compliant.
---

# lead-magnet-builder

## When to use
"hazme un lead magnet", "una guía/checklist/reto gratis", "imán de prospectos", "secuencia de
captura por WhatsApp".

## Inputs (reads from)
- `knowledge/organic-growth.md` (lead magnets, lista desde cero), `knowledge/sales-playbook.md`
- `config/brand-voice.md`, `config/business-profile.md` (WhatsApp, foco)
- `pdf-export` (si se quiere versión PDF del entregable)

## Process
1. Elige el imán (guía de rutina, reto 7 días, checklist por tipo de piel) alineado al pilar y
   al hero product.
2. Crea el **contenido del entregable** (es-MX, valor real, sin claims).
3. Diseña la **secuencia de captura**: CTA en contenido → comentario keyword → DM → WhatsApp →
   entrega → seguimiento (cadencia de `crm/followups.md`).
4. Respeta **privacidad** (datos mínimos, consentimiento) y ToS (sin spam).
5. (Opcional) invoca `pdf-export` para versión PDF.

## Output format
```
LEAD MAGNET: <título> · pilar: ___
Contenido (es-MX): <esquema/guía>
Secuencia de captura: CTA → keyword → DM → WhatsApp → entrega → D1/D3 seguimiento
Mensajes (es-MX) por paso
```

## Compliance
- Sin claims; consentimiento y datos mínimos. Invoca `compliance-guard`.

## Examples
**Input:** "Reto de 7 días de hidratación como lead magnet."
**Output:** estructura del reto (7 días), CTA "comenta 'RETO'", secuencia DM→WhatsApp con
mensajes es-MX, y opción de exportar a PDF con `pdf-export`.
