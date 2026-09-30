---
name: repurpose-engine
description: Adapta una sola idea/asset a Instagram, Facebook, TikTok y YouTube (formato, duración, hook, hashtags, text lockups). Úsalo cuando el operador diga "adáptalo para las 4 plataformas", "repurposea esto", "pásalo a TikTok/IG/FB/YT", "una idea para todas las redes" (repurpose, adaptar, 4 plataformas). Output en es-MX.
---

# repurpose-engine

## When to use
"adáptalo a las 4 plataformas", "repurposea esto", "pásalo a TikTok/YT/FB", "de una idea a
todas las redes".

## Inputs (reads from)
- `config/platforms.md` (formatos, duración, horarios, SEO por plataforma)
- `knowledge/organic-growth.md` (matriz de repurposing)
- `knowledge/platform-guides/*`
- El guion/idea/asset de origen (de `content/scripts/` o del mensaje)

## Process
1. Toma la **idea maestra** o guion existente.
2. Para cada plataforma genera: formato, duración objetivo, **ajuste de hook**, caption/SEO,
   hashtags y **text lockups** — sin re-subir idéntico.
3. Señala qué cambia (p.ej. TikTok dice la keyword en seg 1; YT keyword en título; FB más
   explicativo; IG visual-first).
4. Entrega la **matriz por plataforma** lista para producir.

## Output format
Tabla/bloques:
```
IDEA MAESTRA: ___
[Instagram]  Formato/dur · Hook · Caption+hashtags · Lockups · Horario
[Facebook]   ...
[TikTok]     ...
[YouTube]    ... (+ nota long-form evergreen si aplica)
```

## Compliance
- Cada variante debe cumplir §9; invoca `compliance-guard` antes de "listo".

## Examples
**Input:** "Adapta el reel de '3 errores del sérum' a las 4 plataformas."
**Output:** matriz IG/FB/TikTok/YT con hooks y captions ajustados, hashtags por red, lockups, y
sugerencia de un YouTube long-form "Guía del sérum" para SEO evergreen.
