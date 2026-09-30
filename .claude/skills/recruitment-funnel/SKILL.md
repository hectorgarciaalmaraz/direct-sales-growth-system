---
name: recruitment-funnel
description: Crea invitaciones/iniciaciones honestas, manejo de objeciones, el diferenciador personal y la presentación del negocio. Úsalo cuando el operador diga "cómo invito a alguien al negocio", "script de reclutamiento", "presentación del negocio", "responde '¿es pirámide?'", "cómo inicio a alguien" (reclutar, invitar, negocio, iniciación, equipo). Output en es-MX, sin promesas.
---

# recruitment-funnel

## When to use
"cómo invito al negocio", "script de reclutamiento", "presentación del negocio", "responde
'¿es pirámide?'", "pasos para iniciar a alguien".

## Inputs (reads from)
- `knowledge/recruitment-playbook.md` (invitaciones, objeciones, presentación, iniciación,
  retención)
- `knowledge/company-playbook.md` (ladder/terminología — `⚠️ VERIFY` antes de citar números)
- `config/brand-voice.md` (diferenciador personal, tono honesto)
- `knowledge/persuasion-playbook.md` (7 secuestros + tingle). ⚠️ Al reclutar, el "sueño" es
  aprendizaje/comunidad/tiempo propio — **nunca** dinero ni independencia financiera. Invoca
  `offer-writer` para la descripción persuasiva de la iniciación.
- `crm/leads.csv`, `crm/team.csv`, `crm/followups.md`

## Process
1. Identifica la etapa (invitación, presentación, objeción, iniciación, primeros pasos,
   retención).
2. Genera el mensaje/flujo es-MX honesto — **sin promesas de ingreso ni resultados**.
3. Usa el diferenciador personal (`key_differentiator`) como curiosidad inclusiva.
4. Para objeciones ("¿es pirámide?", "no sé vender", "no tengo tiempo") responde con
   transparencia.
5. Sugiere siguiente paso y registra como `interest=business` vía `crm-tracker`; al iniciar,
   en `crm/team.csv`.

## Output format
```
ETAPA: ___
Mensaje/flujo (es-MX): "<texto listo para pegar>"
Guardrail de honestidad incluido: sí
Siguiente paso: ___
```
Para la presentación, entrega el guion en 6 pasos del playbook.

## Compliance
- Sin promesas de ingreso/resultados; explica venta directa con honestidad; `⚠️ VERIFY` datos
  oficiales (kit/costo/números) antes de citarlos. Invoca `compliance-guard`.

## Examples
**Input:** "Alguien pregunta si es pirámide, ¿cómo respondo?"
**Output:** mensaje es-MX que explica venta directa (ganas por vender producto real y por formar
equipo; sin pagar por reclutar; sin promesas), tono honesto, + invitación a una presentación
corta.
