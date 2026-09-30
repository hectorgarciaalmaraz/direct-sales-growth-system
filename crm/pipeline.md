# pipeline.md — Stage definitions (sales & recruiting)

> Etapas para `crm/leads.csv` (campo `stage`). `crm-tracker` mueve a los prospectos entre
> etapas. Mantén **datos mínimos** (alias, no PII innecesaria — ver `knowledge/compliance.md`).

## Campos de `leads.csv`
`id, alias, platform, first_contact_date, interest(sale|business), stage, last_contact,
next_step, notes, next_date`
- **interest:** `sale` (compra) o `business` (oportunidad).
- **next_date:** fecha ISO del próximo seguimiento (la usa `crm-tracker due`). Es un campo
  operativo de agenda, no dato sensible.

## Pipeline de VENTA (`interest=sale`)
1. **nuevo** — primer contacto/comentario; aún sin conversación real.
2. **en_conversacion** — DM/WhatsApp activo; descubriendo necesidad/tipo de piel.
3. **recomendacion** — se hizo recomendación + precio/oferta.
4. **negociacion** — resolviendo objeciones (precio, dudas).
5. **cerrado_ganado** — venta confirmada → registra en `ops/metrics.csv` (`sales`).
6. **cerrado_perdido** — no avanzó (anota razón en `notes` para aprender).
7. **recompra** — cliente para reorder/loyalty (cadencia D30/D45).

## Pipeline de RECLUTAMIENTO (`interest=business`)
1. **nuevo** — mostró interés en la oportunidad.
2. **en_conversacion** — DM/WhatsApp; invitación honesta enviada.
3. **presentacion_agendada** — quedó la presentación del negocio.
4. **presentacion_hecha** — ya vio la presentación (6 pasos del playbook).
5. **objeciones** — resolviendo dudas ("¿es pirámide?", tiempo, etc.).
6. **iniciada** — inició como Consultora → registra en `crm/team.csv` y `ops/metrics.csv`
   (`recruits`).
7. **no_avanzo** — no inició (anota razón).

## Reglas
- Cada movimiento actualiza `last_contact` y, si aplica, `next_step` + `next_date`.
- Define el siguiente paso según `crm/followups.md` (D0/D1/D3/D7), tono no insistente.
- Nada de spam ni DMs masivos no solicitados (ToS).
