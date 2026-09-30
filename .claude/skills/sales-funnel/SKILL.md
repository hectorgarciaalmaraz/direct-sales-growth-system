---
name: sales-funnel
description: Diseña flujos DM→venta, scripts de WhatsApp, manejo de objeciones y ofertas del día. Úsalo cuando el operador diga "cómo le respondo a esta clienta", "script de venta/WhatsApp", "maneja esta objeción", "oferta del día", "cómo cierro" (venta, vender, objeción, WhatsApp, DM, cierre). Output en es-MX.
---

# sales-funnel

## When to use
"cómo le respondo a esta clienta", "script de venta/WhatsApp", "maneja la objeción 'está
caro'", "dame la oferta del día", "cómo cierro la venta".

## Inputs (reads from)
- `knowledge/sales-playbook.md` (funnel, guiones, objeciones, cierre, reorder)
- `knowledge/persuasion-playbook.md` (7 secuestros humanos + efecto tingle — úsalo para armar
  demos, ofertas y cierres; invoca `offer-writer` para la descripción persuasiva del producto)
- `config/business-profile.md` (foco de producto, WhatsApp, zona)
- `config/brand-voice.md` (tono)
- `crm/leads.csv`, `crm/followups.md` (estado del prospecto y cadencia)

## Process
1. Identifica la etapa (apertura, descubrimiento, recomendación, objeción, cierre, reorder).
2. Genera el mensaje es-MX adecuado, suave y específico, moviendo a WhatsApp cuando aplique.
3. Si hay objeción, responde con honestidad (sin presión, sin promesas/claims).
4. Sugiere el **siguiente paso** y la cadencia de seguimiento (D0/D1/D3/D7).
5. Recuerda registrar venta en `ops/metrics.csv` y prospecto vía `crm-tracker`.

## Output format
```
ETAPA: ___
Mensaje (es-MX): "<texto listo para pegar>"
Siguiente paso: ___ (fecha sugerida)
Si objeción → variante: "<texto>"
```
Ofrece 2 variantes de tono cuando ayude.

## Compliance
- Sin claims de ingreso/médicos; precios/promos claros; nada de spam. Invoca `compliance-guard`
  antes de "listo".

## Examples
**Input:** "Una clienta dice 'está caro', ¿qué le digo?"
**Output:** mensaje es-MX que habla de costo por uso y opción de empezar con un solo paso, sin
presión, + siguiente paso de seguimiento a 3 días.
