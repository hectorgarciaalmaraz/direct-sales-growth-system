---
name: image-prompt-studio
description: Crea prompts de imagen (producto, carrusel, portada) siguiendo los estilos del operador. Úsalo cuando el operador diga "hazme el prompt de imagen", "imagen para el carrusel/portada/producto", "render del producto", "qué le pongo a la IA de imagen" (prompt imagen, carrusel, portada, producto). Output en es-MX (lockups) + prompts.
---

# image-prompt-studio

## When to use
"hazme el prompt de imagen", "imagen para el carrusel/portada", "render de producto",
"cover para el reel/short".

## Inputs (reads from)
- `config/ai-tools.md` (estilos, lockups, negative prompts)
- `config/business-profile.md` (assets/estilos: clay-kawaii, soft-pink, magazine)
- `content/templates/carousel.md` (si es carrusel)

## Process
1. Define el propósito (producto, slide de carrusel, portada) y la relación de aspecto.
2. Escribe el prompt: sujeto/escena, composición, luz, **estilo de marca**, mood, calidad,
   **negative prompt**.
3. Inserta **text lockup es-MX** (≤6 palabras) cuando la imagen lo requiera (portadas/slides).
4. Para carruseles: un prompt por slide, consistentes en estilo.
5. Guarda en `content/prompts/`.

## Output format
```
PROPÓSITO: ___ · Aspect: 4:5 / 9:16 / 1:1
Prompt: <subject> + <composition> + <lighting> + <estilo marca> + <mood> + <quality>
Lockup (es-MX): "___"
Negative: texto deforme, manos extra, logos falsos, marcas de agua
```
Carrusel → lista de prompts por slide. Ofrece 2 estilos si ayuda.

## Compliance
- Sin claims en el texto de la imagen; sin uso indebido de marca. Invoca `compliance-guard`
  para lockups.

## Examples
**Input:** "Portada del carrusel 'Rutina en 3 pasos' estilo soft-pink."
**Output:** prompt 4:5, fondo rosa suave, frasco centrado, luz difusa, lockup "Rutina en 3
pasos", negative prompt incluido.
