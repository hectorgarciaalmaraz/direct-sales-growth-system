---
name: persona-designer
description: Define y mantiene la persona presentadora AI de marca (capa B del modelo de 3 capas). Úsalo cuando el operador diga "diseña la persona/presentadora", "crea el avatar de marca", "define la voz/look del personaje", "persona AI" (persona, presentadora, avatar, personaje, layer B). Output en es-MX; guarda ficha en assets/.
---

# persona-designer

## When to use
"diseña la persona/presentadora", "crea el avatar de marca", "define la voz y el look del
personaje", "persona AI para los videos".

## Inputs (reads from)
- `config/business-profile.md` (marca, diferenciador personal, foco)
- `config/brand-voice.md` (tono), `config/ai-tools.md` (Higgsfield/Veo/ElevenLabs)
- `strategy/content-system.md` (capa B ≈ 20%)
- `assets/` (estilos del operador, si existen)

## Process
1. Define la **ficha de persona**: nombre, arquetipo, look (rostro/edad/vestuario/paleta
   soft-pink), personalidad, y **voz** (preset ElevenLabs es-MX).
2. Define el **segmento recurrente** que presenta (p.ej. "Tips en 30s con [persona]").
3. Da **prompts base** de generación (imagen + video) para consistencia (seed/estilo).
4. Guarda la ficha en `assets/persona/` (referencia para `video-prompt-studio`/`voice-studio`).
5. Marca datos a decidir con `⚠️ COMPLETE` (nombre final, look definitivo).

## Output format
```
PERSONA: <nombre> · arquetipo: ___
Look: ___ (paleta, vestuario) · Voz (ElevenLabs es-MX): ___
Personalidad/tono: ___
Segmento recurrente: ___
Prompts base (imagen/video) + seed/estilo
```

## Compliance
- La persona no hace claims; no suplanta a la compañía. Invoca `compliance-guard` para sus
  guiones. Respeta ToS de clonación de voz.

## Examples
**Input:** "Diseña la presentadora de marca para la capa B."
**Output:** ficha con nombre `⚠️ COMPLETE`, look soft-pink, voz cálida es-MX, segmento "Tips en
30s", y prompts base con seed para consistencia.
