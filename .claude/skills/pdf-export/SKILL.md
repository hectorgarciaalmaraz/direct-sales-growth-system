---
name: pdf-export
description: Exporta catálogos y lead magnets a PDF usando un skill externo de PDF (oficial `pdf` vía document-skills, o un "PDF Designer" verificado). Úsalo cuando el operador diga "expórtalo a PDF", "haz el catálogo en PDF", "convierte la guía/lead magnet a PDF", "PDF del [contenido]" (PDF, exportar, catálogo). Output en es-MX.
---

# pdf-export

## When to use
"expórtalo a PDF", "haz el catálogo en PDF", "convierte la guía/lead magnet a PDF",
"PDF del [contenido]".

## Inputs (reads from)
- El contenido fuente (de `content/...`, p.ej. un lead magnet o catálogo)
- `config/brand-voice.md` (estilo/marca), `assets/` (logos/estilos)
- El **skill externo de PDF** registrado en `ops/skill-registry.md`

## Prerequisite
Requiere un **skill de PDF instalado** (ver `skill-installer` y `external-skills/README.md`):
- Oficial `pdf` (vía `document-skills`), **o** un "PDF Designer" verificado.
Si aún no está `active`, indícalo y guía al operador para instalarlo; **no inventes** la salida.

## Process
1. Prepara el contenido es-MX (estructura del catálogo/lead magnet, secciones, imágenes).
2. **Invoca el skill de PDF** instalado para generar el archivo (ej.: "usa el skill `pdf` para
   generar el catálogo desde `content/...`").
3. Aplica estilo de marca (soft-pink, portada, tipografía) según `assets/`.
4. Guarda el PDF en `content/exports/` (en `.gitignore` por tamaño) y reporta la ruta.

## Output format
```
ENTREGABLE: <catálogo|lead magnet> · fuente: content/...
SKILL PDF: <pdf|PDF Designer> (status: active/⚠️ no instalado)
RESULTADO: content/exports/<archivo>.pdf  (o instrucción de instalación si falta el skill)
```

## Compliance
- Sin claims de ingreso/médicos; precios claros (PROFECO); uso correcto de la marca de la compañía. Invoca
  `compliance-guard` sobre el contenido antes de exportar.

## Examples
**Input:** "Exporta el reto de 7 días a PDF."
**Output:** prepara el contenido es-MX, invoca el skill `pdf` (si `active`), guarda
`content/exports/reto-7-dias.pdf`; si el skill no está instalado, da los pasos de
`skill-installer` para activarlo.
