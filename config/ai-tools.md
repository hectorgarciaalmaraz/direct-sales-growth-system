# ai-tools.md — AI tool cards & reusable prompt templates

> The prompt skills (`video-prompt-studio`, `image-prompt-studio`, `voice-studio`) reuse these
> cards and templates. All on-screen and spoken text in generated assets is **es-MX**. Bake
> **Spanish text lockups** into clips where useful. Capabilities/limits change — `⚠️ VERIFY`
> current model versions and feature limits when in doubt.

## Card — Higgsfield (Kling 3 / Seedance 2)
- **Purpose:** stylized short-form b-roll, product motion, faceless scenes, persona shots.
- **Strengths:** aesthetic motion, character/scene consistency, trendy looks.
- **Best prompt format:** `[shot/camera] + [subject] + [action] + [setting] + [lighting] +
  [style/aesthetic] + [mood] + [duration/aspect]`. Add negative prompts; specify 9:16.
- **Limits / notes:** clip length per generation; keep one idea per clip; iterate seeds for
  consistency. `⚠️ VERIFY current limits.`
- **Base template:**
  ```
  Shot: close-up, slow push-in, 9:16 vertical.
  Subject: [producto/escena, p.ej. frasco de sérum sobre fondo rosa suave].
  Action: [movimiento sutil, gotas, textura desplazándose].
  Setting + lighting: [estudio minimalista, luz suave difusa].
  Style: [3D clay/kawaii | magazine-cover | soft-pink minimal].
  Text lockup (es-MX, on-screen): "[texto corto, ≤6 palabras]".
  Mood: aspiracional, limpio. Negative: texto deforme, manos extra, logos falsos.
  ```

## Card — Veo 3.1 (Google Pro)
- **Purpose:** higher-fidelity cinematic clips, native audio/dialogue, presenter scenes.
- **Strengths:** realism, prompt adherence, audio + lip-sync potential for the persona.
- **Best prompt format:** narrative + explicit camera/lighting + dialogue lines in quotes
  (es-MX) + ambience. State aspect 9:16 and duration.
- **Limits / notes:** quota/length per plan; review for unintended on-screen text.
  `⚠️ VERIFY current limits.`
- **Base template:**
  ```
  A [vertical 9:16] cinematic shot. [Persona/escena]. Camera: [movimiento].
  Lighting: [suave, cálida]. Dialogue (es-MX): "[línea breve de la presentadora/or VO]".
  Ambience/SFX: [música suave, sin claims]. Duration: [~8 s]. Style: branded, limpio.
  ```

## Card — ElevenLabs (voz / VO)
- **Purpose:** voiceover for faceless clips and the AI presenter persona voice.
- **Strengths:** natural es-MX VO, consistent persona voice, multilingual.
- **Best prompt format:** define voice (género, edad, calidez, ritmo) + the **es-MX script**;
  mark pacing/emphasis; keep claims-free.
- **Limits / notes:** respect voice-cloning consent + platform ToS; keep a named persona voice
  preset for consistency. `⚠️ VERIFY plan limits.`
- **Base template:**
  ```
  Voz: [femenina/masculina], cálida, profesional, español de México, ritmo medio.
  Guion (es-MX): "[texto del VO, sin claims médicos ni de ingresos]".
  Énfasis: [palabra clave]. Pausas: [donde aplique]. Estilo: cercano, claro.
  ```

## Card — Adobe Premiere Pro (edición)
- **Purpose:** assemble/edit clips, captions, text lockups, pacing, branded look.
- **Best practices baked into deliverables (Premiere notes):**
  - Hook visible in first 1 s; subtitles quemados (es-MX) siempre.
  - Cortes rápidos al ritmo de la música; safe margins 9:16.
  - Branded lower-thirds / colores (soft-pink) consistentes; CTA al final.
  - Export 1080×1920, H.264, audio normalizado.
- **Limits / notes:** licensed/royalty-free audio only; respect platform audio rules.

## Card — AI Presenter Persona (operator-built)
- **Purpose:** layer-B branded virtual presenter (≈20% of content). Defined by
  `persona-designer` (Phase 5) — name, look, wardrobe, voice (ElevenLabs preset), recurring
  segment format. Keep a reference sheet under `assets/` for consistency.

## Shared conventions for all prompt outputs
- Aspect **9:16** by default; specify duration.
- **es-MX text lockups** short (≤6 words), no claims.
- Always include a **negative prompt** (texto deforme, manos extra, marcas/logos falsos).
- Tie style to operator assets when present (`assets/`): 3D clay/kawaii, soft-pink, magazine-cover.
- Output prompts go to `content/prompts/`; everything publishable passes `compliance-guard`.
