---
name: offer-writer
description: Redacta descripciones de venta persuasivas para un producto de la compañía o para la INICIACIÓN al negocio, con beneficio emocional + 3 características sensoriales + valor diferencial + CTA. Úsalo SIEMPRE que el operador vaya a vender o a invitar a alguien - cuando diga "descripción de venta", "descríbeme este producto", "copy para vender [X]", "texto persuasivo", "ficha de producto", "cómo lo presento", "descripción para la iniciación", "véndeme esto" (vender, venta, producto, descripción, persuasivo, iniciación, oferta). Aplica los 7 secuestros humanos + efecto tingle. Output en es-MX, elegante y compliant.
---

# offer-writer

## When to use
**Dispara en cada intento de venta o iniciación.** Frases típicas: "descripción de venta",
"copy para vender el desmaquillante", "cómo le presento este producto", "texto persuasivo",
"ficha del producto", "descripción para invitar al negocio", "véndeme esto".

Si el operador pide contenido de venta y no menciona "descripción", **actívate igual**.

## Inputs (reads from)
- `knowledge/persuasion-playbook.md` ← **base obligatoria** (7 secuestros + efecto tingle)
- `knowledge/compliance.md` ← límites innegociables
- `config/business-profile.md` (producto hero, WhatsApp, zona, nombre)
- `config/brand-voice.md` (tono cálido, profesional, sin clichés)
- `knowledge/sales-playbook.md` o `knowledge/recruitment-playbook.md` según el caso

## ⚠️ Canales permitidos (importante)
Estas descripciones son para **tus canales propios**: WhatsApp, DM de IG/FB/TikTok, tu página
de Facebook, tu catálogo y tus publicaciones.
**NO** las uses para publicar en marketplaces no autorizados (Amazon, Mercado Libre, Shopee,
Facebook Marketplace de reventa, etc.) — muchos contratos de consultora lo restringen
(§3 compliance, `⚠️ VERIFY E`).

## Process
1. Identifica el objeto: **PRODUCTO** o **INICIACIÓN** (negocio).
2. Elige el **ángulo emocional** real del cliente (no la característica técnica) — §1 del
   playbook.
3. Redacta la estructura de 4 bloques (abajo).
4. Integra **al menos un tingle** (táctil, visual o sensorial) cuando sea producto.
5. Verifica urgencia: **debe ser real** (fecha de promo real, stock real, cupo real). Si no
   existe una razón verdadera, usa urgencia suave ("te lo aparto hoy") — **nunca inventes
   escasez**.
6. Entrega **2–3 variantes etiquetadas** (ej. *Elegante* / *Directa* / *Cercana*).
7. Invoca `compliance-guard` antes de marcar "listo".

## Output format
```
OBJETO: <producto | iniciación>  ·  Canal: <WhatsApp | IG/FB | catálogo>

── VARIANTE A: <etiqueta> ──
🎯 Beneficio emocional:
   <1–2 líneas. Habla de cómo se va a ver/sentir. Sin claims.>

✨ 3 características distintivas (lenguaje sensorial):
   1. <textura / aroma / sensación / resultado visible>
   2. <...>
   3. <...>

💎 Estado y valor diferencial:
   <1 línea: qué lo hace distinto y por qué vale la pena.>

👉 CTA:
   <breve, con urgencia REAL, con siguiente paso concreto + WhatsApp>

[Tingle sugerido: <demo táctil/visual a mostrar>]

── VARIANTE B: ... ──
```

## Reglas de lenguaje (no negociables)
- ❌ Claims médicos: "cura", "elimina el acné/las arrugas", "trata", "previene", "borra".
- ❌ Claims de ingreso (en iniciación): "ingreso garantizado", "gana $X", "independencia
  financiera", "empoderamiento económico".
- ❌ Escasez falsa, "milagro", "100% efectivo", "comprobado" sin respaldo oficial.
- ✅ Sensorial y de apariencia: "se siente", "luce", "textura", "frescura", "suavidad",
  "luminosa", "sin tallar".
- ✅ En iniciación: aprendizaje, comunidad, acompañamiento, manejar tu tiempo, construir algo tuyo.
- ✅ Precios: solo si están confirmados (`⚠️ COMPLETE`), claros y honrados (PROFECO).

## Compliance
Invoca **siempre** `compliance-guard` antes de devolver el texto. Si el operador pide una frase
prohibida, ofrécele la versión reformulada y explícale por qué en una línea.

## Examples

**Input:** "Hazme la descripción de venta del desmaquillante."
**Output (variante A, Elegante):**
```
🎯 Beneficio emocional:
   Llegar cansada y aun así irte a dormir sintiendo la piel limpia — sin tallar, sin pelear
   con el rímel, sin excusas.

✨ 3 características distintivas:
   1. Fórmula bifásica: se activa al agitar y retira el maquillaje de una sola pasada.
   2. Textura ligera que no deja sensación grasosa ni resequedad alrededor del ojo.
   3. Rinde por semanas: un algodón basta por noche.

💎 Estado y valor diferencial:
   Producto nuevo, sellado — el paso 1 de toda rutina, el que casi todas se saltan.

👉 CTA:
   ¿Te lo aparto hoy y te lo entrego esta semana? Escríbeme:
   https://wa.me/52XXXXXXXXXX  ← whatsapp_link de config/business-profile.md

[Tingle sugerido: algodón + rímel a prueba de agua, una pasada — que vea cómo se derrite.]
```

**Input:** "Descripción para invitar a alguien al negocio."
**Output (variante A, Honesta):**
```
🎯 Beneficio emocional:
   Aprender algo tuyo, a tu ritmo, sin dejar lo que ya haces — y con alguien que sí te
   acompaña al inicio.

✨ 3 características distintivas:
   1. Empiezas con capacitación y material: no te sueltan sola.
   2. Tú manejas tus tiempos y decides qué tan lejos llevarlo.
   3. Un equipo de personas con vidas ocupadas que se apoyan entre sí.

💎 Estado y valor diferencial:
   Es un negocio real de venta directa: ganas por vender producto y, si quieres, por formar
   equipo. Sin pagar por reclutar.

👉 CTA:
   Te lo explico en 15 minutos, sin compromiso y sin promesas. ¿Te late esta semana?
   https://wa.me/52XXXXXXXXXX
```
