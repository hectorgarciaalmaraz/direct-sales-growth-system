---
name: voice-studio
description: Diseña voces y prompts de ElevenLabs (VO, persona) con guion en es-MX. Úsalo cuando el operador diga "hazme la voz", "VO para el video", "prompt de ElevenLabs", "voz de la presentadora/persona", "locución en off" (voz, VO, locución, ElevenLabs, voiceover). Output en es-MX.
---

# voice-studio

## When to use
"hazme la voz/VO", "locución para el video", "prompt de ElevenLabs", "voz de la persona".

## Inputs (reads from)
- `config/ai-tools.md` (card ElevenLabs, plantilla base)
- `config/brand-voice.md` (tono)
- El guion (de `content/scripts/` o del mensaje)

## Process
1. Define el **perfil de voz** (género, edad, calidez, ritmo, español de México) — reusa el
   preset de la persona si existe (`persona-designer`).
2. Inserta el **guion es-MX** sin claims; marca énfasis y pausas.
3. Da parámetros sugeridos (estabilidad/estilo) y notas de pronunciación.
4. Guarda en `content/prompts/`.

## Output format
```
Voz: <género>, cálida, profesional, es-MX, ritmo <medio/ágil>
Preset persona: <nombre o N/A>
Guion (es-MX): "<texto del VO>"
Énfasis: <palabra(s)> · Pausas: <marcas>
Parámetros sugeridos: estabilidad ___, estilo ___
```

## Compliance
- Sin claims de ingreso/médicos en el VO; respeta consentimiento de clonación y ToS. Invoca
  `compliance-guard` para el guion.

## Examples
**Input:** "VO para el reel del sérum, voz masculina cálida."
**Output:** perfil de voz es-MX, guion con énfasis en "paso a paso", pausas marcadas y
parámetros sugeridos.
