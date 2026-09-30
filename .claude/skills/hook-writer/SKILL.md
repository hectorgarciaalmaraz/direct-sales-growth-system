---
name: hook-writer
description: Genera bancos de hooks por plataforma/ángulo (alimenta content/hook-bank.md). Úsalo cuando el operador diga "dame hooks", "ganchos para [tema/plataforma]", "primeras líneas/frases de apertura", "ideas de hook de mi diferenciador" (hooks, ganchos, aperturas). Output en es-MX, compliant.
---

# hook-writer

## When to use
"dame hooks/ganchos", "aperturas para TikTok/IG/YT", "hooks de mi diferenciador",
"primeras líneas para [tema]".

## Inputs (reads from)
- `content/hook-bank.md` (banco actual), `config/brand-voice.md` (tono + ángulo)
- `knowledge/organic-growth.md` (tipos de hook), `config/platforms.md` (1ª línea/SEO)

## Process
1. Toma tema, pilar, plataforma y ángulo (curiosidad / pattern interrupt / valor / prueba
   social / oportunidad / diferenciador personal).
2. Genera **8–12 hooks es-MX** ≤12 palabras, front-load de curiosidad, sin claims.
3. Etiqueta por tipo y plataforma; marca cuáles dicen la keyword (TikTok/YT SEO).
4. Agrega los mejores a `content/hook-bank.md`.

## Output format
```
TEMA/ÁNGULO: ___ · Plataforma: ___
1. "<hook>"  [tipo]
2. ...
(8–12)
Sugeridos para banco: #, #, #
```

## Compliance
- Sin promesas/claims. Invoca `compliance-guard` antes de "listo".

## Examples
**Input:** "Hooks para TikTok del sérum, ángulo educativo."
**Output:** 10 hooks es-MX (varios con la keyword 'sérum' en seg 1), etiquetados, + 3 sugeridos
para el banco.
