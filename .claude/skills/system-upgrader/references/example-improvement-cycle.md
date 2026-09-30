# Worked example — one improvement cycle (system-upgrader)

> Demostración del loop de mejora de §8, ejecutado durante el build (Phase 4) como referencia.
> Muestra los 4 pasos: señal → propuesta → prueba ligera → aplicar + versionar + log.

## 1. Recolectar señales
- Fuente: `metrics-analyst` (revisión semanal) + observación de activación de skills.
- **Señal de ejemplo:** "El operador pide guiones diciendo *'qué digo en el video'* sin la
  palabra 'guion'. Riesgo de **sub-activación** de `script-writer` si su `description` no incluye
  esa frase."

## 2. Proponer mejora
- **Cambio concreto:** reforzar la `description` de `script-writer` con la frase es-MX
  *"qué digo en el video"* (más "pushy", más trigger phrases).
- *(En este build la description de `script-writer` ya incluye esa frase — la mejora está
  aplicada de origen; este documento ilustra el procedimiento para futuras mejoras.)*

## 3. Prueba ligera (2–3 prompts realistas)
Ejecuta mentalmente/realmente contra la skill modificada y muestra resultados al operador:
- Prompt: "qué digo en el video del sérum" → ¿activa `script-writer`? ✔
- Prompt: "hazme el script del tiktok de hidratación" → ✔
- Prompt: "guion para el reel del negocio (diferenciador personal)" → ✔
Si alguno falla, vuelve al paso 2 (mejora la description / trigger phrases).

## 4. Aplicar + versionar + registrar
- Aplica el cambio (editar el `SKILL.md`).
- Sube versión y registra (ejecutado en dry-run durante el build):
  ```
  python .claude/skills/system-upgrader/scripts/bump_version.py \
    --file ops/changelog.md --part patch \
    --message "script-writer: +trigger 'qué digo en el video'" \
    --reason "Evitar sub-activación" --impact "Mejor activación en es-MX"
  ```
  Resultado del dry-run: `v0.1.0 → v0.1.1` con la entrada de changelog correspondiente.
  *(El build mantiene la versión viva en `v0.1.0`; ejecuta el comando sin `--dry-run` cuando
  apliques una mejora real para que quede en `changelog.md`.)*

## Notas
- Las instrucciones en `ops/updates-inbox.md` se procesan con este mismo loop (clasificar →
  aplicar → versionar → log).
- Cambios a contenido publicable pasan por `compliance-guard`.
- Si una necesidad recurrente aparece, `system-upgrader` puede **crear una skill nueva** con
  `assets/skill-template/SKILL.md`.
