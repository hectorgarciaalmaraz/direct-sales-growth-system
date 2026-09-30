---
name: script-writer
description: Escribe guiones de video corto en es-MX (versión faceless y versión con presentador), con hook/cuerpo/CTA. Úsalo cuando el operador diga "escríbeme el guion", "haz el script del reel/tiktok/short", "qué digo en el video", "guion para [idea]" (guion, script, reel, tiktok, short, video). Output en es-MX.
---

# script-writer

## When to use
"escríbeme el guion", "haz el script", "qué digo en el video", "guion del reel/tiktok/short".
Incluso si no dice "guion" pero pide el contenido hablado de un video.

## Inputs (reads from)
- `config/business-profile.md` (foco de producto, diferenciador personal, handles, WhatsApp)
- `config/brand-voice.md` (tono, do/don't, ejemplos)
- `strategy/content-system.md` (capa A faceless / capa B-C presentador)
- `content/hook-bank.md`, `content/idea-bank.md`
- `content/templates/{reel,tiktok,short}.md`

## Process
1. Toma la idea maestra (pilar, capa, plataforma, objetivo de CTA).
2. Escribe **2 versiones**: (a) **faceless** (VO + texto en pantalla + b-roll) y
   (b) **presentador** (persona AI o tú), ambas con hook/cuerpo/CTA.
3. Hook en 1–2 s; cuerpo en 3–5 beats; CTA suave y específico (a comentario/DM/WhatsApp).
4. Marca los **text lockups** (es-MX, ≤6 palabras) y notas de VO/tono.
5. Guarda en `content/scripts/` con nombre `YYYY-MM-DD_<slug>_<plataforma>.md`.

## Output format
```
IDEA: ___ · Pilar: ___ · Capa: ___ · Plataforma: ___ · Objetivo: ___

— Versión FACELESS —
Hook (1–2s, on-screen+VO): ___
Cuerpo:
  1. ___  [b-roll: ___] [lockup: "___"]
  2. ___
  3. ___
CTA: ___
Notas VO (ElevenLabs): voz ___, ritmo ___

— Versión PRESENTADOR —
Hook: ___
Cuerpo (diálogo es-MX): ___
CTA: ___
```
Ofrece 2–3 variantes de hook si ayuda.

## Compliance
- Sin claims de ingreso/médicos. Antes de marcar "listo", invoca `compliance-guard`.

## Examples
**Input:** "Haz el guion del reel '3 errores al aplicar el sérum'."
**Output:** versión faceless (VO + lockups "Error 1/2/3") y versión presentador, hook en 1s,
CTA "comenta 'SÉRUM' y te paso los pasos", notas de VO y b-roll de textura.
