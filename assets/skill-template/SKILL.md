---
name: my-skill
description: <what it does> + <when to use it, with es-MX trigger phrases the operator would actually say, plus a few English keywords>
---

# My Skill

## When to use
Trigger when the operator says (es-MX): "<frase>", "<frase>"… (and English keywords).

## Inputs (reads from)
- `config/business-profile.md` (single source of truth)
- `knowledge/...`, `strategy/...`, `crm/...` (as needed)

## Process
1. Read the relevant config/knowledge.
2. Do the work.
3. Produce the output in the exact format below (content in **es-MX**).

## Output format
(exact template; content in es-MX; offer 2–3 labeled variants when useful)

## Compliance
- Before returning publishable content, invoke `compliance-guard`.

## Examples
**Input:** ...
**Output:** ...
