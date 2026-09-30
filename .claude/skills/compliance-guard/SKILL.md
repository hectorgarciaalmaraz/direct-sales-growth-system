---
name: compliance-guard
description: Revisa cualquier contenido/funnel contra knowledge/compliance.md; marca y reescribe lo no conforme. Úsalo SIEMPRE antes de publicar y cuando el operador diga "revisa que esto cumpla", "¿esto es compliant?", "checa el copy", "revisa legal/marca" (compliance, cumplimiento, revisar, legal, claims). Otras skills lo invocan antes de devolver contenido publicable. Output en es-MX.
---

# compliance-guard

## When to use
- **Automáticamente:** cualquier skill que produzca contenido publicable lo invoca antes de
  marcar "listo".
- **A petición:** "revisa que esto cumpla", "¿es compliant?", "checa el copy/guion/caption".

## Inputs (reads from)
- `knowledge/compliance.md` (la norma — fuente única)
- `config/brand-voice.md` (reglas de lenguaje)
- El contenido a revisar (del mensaje o de `content/`)

## Process
1. Lee el contenido y escanéalo contra las 7 reglas de `compliance.md` y el **léxico de
   banderas rojas** (gana $, ingreso garantizado, cura, elimina arrugas/acné, trata, previene,
   milagro, 100% efectivo, marketplace no autorizado, etc.).
2. Clasifica: **compliant / adjust / reject**.
3. Da **razones** citando la(s) regla(s) específica(s).
4. Si `adjust`/`reject`, entrega una **versión corregida lista para publicar** (es-MX) que
   conserva la intención y elimina la violación.
5. Para datos de la compañía (rangos/números) sin confirmar, exige `⚠️ VERIFY` y evita publicarlos.

## Output format
```
VEREDICTO: compliant | adjust | reject
RAZONES:
  - <regla §X>: <qué y por qué>
VERSIÓN CORREGIDA (si aplica):
  "<texto es-MX listo para publicar>"
```

## Compliance
- Esta skill **es** el control de cumplimiento; no se invoca a sí misma.

## Examples
**Input:** "Revisa: 'Únete y gana $20,000 al mes, ¡ingreso garantizado!'"
**Output:**
```
VEREDICTO: reject
RAZONES:
  - §1 No income claims/guarantees: promete cifra e ingreso garantizado.
VERSIÓN CORREGIDA:
  "Te cuento honestamente cómo funciona la oportunidad y qué esperar. Sin promesas: depende de
   tu esfuerzo y constancia. ¿Te explico sin compromiso?"
```

**Input:** "Revisa: 'Esta crema elimina las arrugas en 7 días, garantizado.'"
**Output:**
```
VEREDICTO: reject
RAZONES:
  - §2 No medical/therapeutic claims: "elimina arrugas" + "garantizado".
VERSIÓN CORREGIDA:
  "Con una rutina constante, tu piel puede lucir más suave e hidratada. Te muestro los pasos."
```
