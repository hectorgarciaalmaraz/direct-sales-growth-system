---
name: carousel-builder
description: Crea carruseles de valor (texto por slide + prompts de imagen). Úsalo cuando el operador diga "hazme un carrusel", "carrusel de [tema]", "slides para IG/FB", "post de varias imágenes" (carrusel, slides, carousel). Output en es-MX, optimizado para guardados, compliant.
---

# carousel-builder

## When to use
"hazme un carrusel", "slides para IG/FB de [tema]", "post educativo de varias imágenes".

## Inputs (reads from)
- `content/templates/carousel.md` (estructura)
- `config/brand-voice.md`, `config/ai-tools.md` (estilo de imagen)
- `knowledge/organic-growth.md` (carruseles = guardados)

## Process
1. Define tema, pilar y objetivo (educar → guardados).
2. Escribe **6–10 slides**: portada (hook+keyword), contexto, 3–5 pasos/ideas, resumen, CTA
   (guardar/comentar).
3. Por slide, da el **texto es-MX** (corto) y un **prompt de imagen** consistente en estilo.
4. Añade caption keyworded + hashtags + mejor horario (vía `caption-writer`).

## Output format
```
TEMA: ___ (objetivo: guardados)
Slide 1 (portada): texto "___" · prompt imagen: ___
Slide 2: texto "___" · prompt: ___
... (6–10)
Caption + hashtags + horario
```

## Compliance
- Sin claims en slides/caption. Invoca `compliance-guard`.

## Examples
**Input:** "Carrusel 'Cómo elegir tu limpiador según tu tipo de piel'."
**Output:** 8 slides (portada + 4 tipos de piel + tips + CTA guardar), textos es-MX y prompts
soft-pink consistentes, + caption con CTA a comentar 'LIMPIADOR'.
