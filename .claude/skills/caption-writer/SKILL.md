---
name: caption-writer
description: Escribe captions/copy + hashtags + CTA + mejor horario por plataforma, listos para pegar. Úsalo cuando el operador diga "hazme el caption/copy", "el texto para el post", "los hashtags", "qué pongo en la descripción" (caption, copy, descripción, hashtags). Output en es-MX, pegado para publicar.
---

# caption-writer

## When to use
"hazme el caption", "el copy del post", "los hashtags", "qué pongo en la descripción del
reel/tiktok/short/post".

## Inputs (reads from)
- `config/brand-voice.md` (tono, do/don't)
- `config/platforms.md` (formatos, horarios, SEO por plataforma)
- `config/business-profile.md` (handles, WhatsApp, foco)
- `knowledge/platform-guides/*` (hashtags/SEO específicos)

## Process
1. Identifica plataforma(s) destino y la idea/keyword objetivo (SEO social).
2. Escribe caption con **1ª línea = 2º hook**, valor keyworded, y **CTA específico**.
3. Añade **hashtags** apropiados (IG 3–8 niche+local; TikTok pocos keyworded; YT en
   título/descr; FB descriptivo).
4. Sugiere **mejor horario** (CDMX) de `config/platforms.md`.
5. Entrega bloque **listo para pegar** por plataforma.

## Output format
```
[PLATAFORMA]
Caption:
<1ª línea hook>
<valor keyworded, 1–3 líneas>
<CTA>
Hashtags: #... #... #...
Mejor horario (CDMX): ...
```
Repite por plataforma solicitada. Ofrece 2 variantes de la 1ª línea si ayuda.

## Compliance
- Sin claims de ingreso/médicos; precios/promos claros. Invoca `compliance-guard` antes de
  entregar.

## Examples
**Input:** "Caption para IG y TikTok del reel de hidratación."
**Output:** bloque IG (caption + 6 hashtags niche/local + horario) y bloque TikTok (caption
keyworded + pocos hashtags + horario), ambos con CTA a comentar 'RUTINA'.
