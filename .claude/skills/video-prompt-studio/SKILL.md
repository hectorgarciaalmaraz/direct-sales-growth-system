---
name: video-prompt-studio
description: Crea prompts de video para Higgsfield (Kling 3 / Seedance 2) y Veo 3.1, con text lockups en español y storyboard. Úsalo cuando el operador diga "hazme el prompt de video", "prompt para Higgsfield/Kling/Seedance/Veo", "storyboard del clip", "qué le pongo a la IA de video" (prompt video, Higgsfield, Veo, Kling, Seedance). Output en es-MX (lockups) + prompts.
---

# video-prompt-studio

## When to use
"hazme el prompt de video", "prompt para Higgsfield/Veo/Kling/Seedance", "storyboard del clip".

## Inputs (reads from)
- `config/ai-tools.md` (cards y plantillas base de cada herramienta)
- `config/business-profile.md` (estilos en `assets/`, foco de producto)
- El guion/idea (de `content/scripts/` o del mensaje)

## Process
1. Define el storyboard por tomas (shot list) acorde al guion (hook → cuerpo → CTA visual).
2. Para cada toma escribe el prompt usando la plantilla de la herramienta elegida (Higgsfield/
   Kling 3/Seedance 2 o Veo 3.1): cámara, sujeto, acción, set, luz, estilo, mood, 9:16,
   duración, **negative prompt**.
3. Inserta **text lockups en es-MX** (≤6 palabras) y notas de continuidad/seed para
   consistencia.
4. Indica herramienta recomendada por toma (Higgsfield para estilizado/b-roll; Veo para
   realismo/diálogo/persona).
5. Guarda en `content/prompts/` como `YYYY-MM-DD_<slug>_<tool>.md`.

## Output format
```
STORYBOARD: <idea> · 9:16
Toma 1 (tool): <prompt completo> · lockup: "___" · negative: ___
Toma 2 (tool): ...
Toma 3 (tool): ...
Notas: continuidad, seed, música/SFX sin claims.
```
Ofrece variante de estilo (p.ej. clay-kawaii vs magazine) si ayuda.

## Compliance
- Sin texto/claims de ingreso o médicos en pantalla; sin logos/marcas falsos. Invoca
  `compliance-guard` para los lockups/diálogos antes de "listo".

## Examples
**Input:** "Prompt de video para el reel del sérum en Higgsfield."
**Output:** storyboard de 3 tomas (close-up de textura, aplicación, packshot) con prompts
Kling 3, lockups "Paso 1/2/3", negative prompt y nota de seed para consistencia.
