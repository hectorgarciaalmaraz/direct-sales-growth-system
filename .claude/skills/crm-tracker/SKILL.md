---
name: crm-tracker
description: Agrega y da seguimiento a prospectos, leads y equipo; agenda próximos pasos. Úsalo cuando el operador diga "agrega este prospecto/lead", "registra a esta persona", "actualiza el CRM", "¿a quién le toca seguimiento hoy?", "mueve a [etapa]" (CRM, prospecto, lead, seguimiento, pipeline, equipo). Escribe en crm/*.csv.
---

# crm-tracker

## When to use
"agrega este prospecto/lead", "registra a esta persona", "actualiza el CRM", "¿a quién le toca
seguimiento hoy?", "mueve a [etapa]", "inició una nueva consultora".

## Inputs (reads/writes)
- `crm/leads.csv` (id, alias, platform, first_contact_date, interest, stage, last_contact,
  next_step, notes)
- `crm/team.csv` (id, alias, role, initiation_date, status, last_contact, next_step, notes)
- `crm/pipeline.md` (definiciones de etapas), `crm/followups.md` (cadencias)
- `config/business-profile.md`

## Process
1. Determina la acción: **add / update / list / due** sobre `leads` o `team`.
2. Usa el script determinista `scripts/update_crm.py` para no editar CSV a mano:
   - `add-lead`, `list-leads`, `update-lead`, `due` (próximos pasos vencidos/hoy)
   - `add-member`, `list-team`
   El script **crea el CSV con encabezados** si no existe.
3. Respeta **privacidad**: usa `alias`, no datos sensibles innecesarios (ver compliance).
4. Sugiere el siguiente paso según `crm/followups.md` (D0/D1/D3/D7).

## Output format
Confirma la operación y muestra la fila resultante o la lista. Ejemplo:
```
Lead agregado: id=003 alias="Ana_IG" platform=instagram interest=sale stage=nuevo
next_step="enviar rutina" (2026-06-26)
```

## Scripts
- `scripts/update_crm.py` — ver `python update_crm.py --help`.

## Compliance
- Datos mínimos; sin PII innecesaria. No genera contenido publicable (no requiere
  `compliance-guard`), pero respeta `knowledge/compliance.md` (privacidad).

## Examples
**Input:** "Agrega a 'Ana' de Instagram, interesada en compra, primer contacto hoy."
**Output:** ejecuta `add-lead` → fila nueva en `crm/leads.csv` con next_step sugerido.
