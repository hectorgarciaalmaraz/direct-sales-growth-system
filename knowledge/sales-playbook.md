# sales-playbook.md — Daily cold-start sales

> How the system turns content into sales without ads or a warm network. Powers the
> `sales-funnel` skill. All scripts are es-MX and pass `compliance-guard`. Floor: **≥ 1 sale/day**.

## The sales funnel
**content → comment/DM → WhatsApp conversation → offer → close → reorder/referral.**
Move people to WhatsApp for real conversations; keep public comments light.

## Offers & bundles (skincare-led)
- **Entry offer:** a low-friction first purchase (single hero product / mini-rutina).
- **Bundles/sets:** rutina por pasos (limpieza → tratamiento → hidratación → protección).
- **Reorder logic:** anticipate run-out dates; offer refills + complementary product.
- **Referral:** "trae a una amiga" / share-and-save (no pressure, no false scarcity).
> Prices/promos must be clear and honored (PROFECO). No "marketplace" listings (see compliance).

## Promo calendar (template — fill specifics in `strategy/campaigns/`)
- Monthly hero focus + one value campaign (e.g., "Mes de la hidratación").
- Seasonal moments (Día de las Madres, fin de año, regreso a clases) — plan early.
- Always anchor on **value/education**, not discounts alone.
- `⚠️ COMPLETE` actual prices and any official promos.

## DM → WhatsApp script (es-MX, compliant)
**Opening (after a keyword comment):**
> "¡Hola! Vi que te interesó la rutina 🙌 Te paso los pasos por aquí. ¿Me cuentas qué tipo de
> piel tienes (grasa, seca, mixta, sensible) para recomendarte mejor?"

**Discovery (1–2 questions, then listen):**
> "¿Buscas algo para el día a día o para un objetivo específico (hidratación, textura, limpieza)?"

**Recommendation + soft offer:**
> "Para lo que me cuentas, te recomendaría [producto/rutina]. Te dejo el detalle y el precio.
> ¿Te gustaría que te aparte uno?"

**Move to WhatsApp:**
> "Si quieres te lo organizo por WhatsApp para apartado y entrega: [wa.me/⚠️COMPLETE]."

## Buying-objection handling (honest, no pressure)
- **"Está caro":** habla de costo por uso, duración del producto, y la opción de empezar con un
  solo paso. Nunca presiones.
- **"No sé si me funcione":** ofrece la rutina adecuada a su tipo de piel y expectativas
  **realistas** (apariencia/sensorial, sin promesas médicas).
- **"Lo pienso":** acuerda un seguimiento amable (ver `crm/followups.md`), no insistas.
- **"¿Hace tal cosa médica?":** redirige a beneficios cosméticos reales; no claims médicos.

## Close
- Confirma producto, precio, forma de pago y entrega. Resume y agradece.
- Registra la venta en `ops/metrics.csv` y al prospecto en `crm/leads.csv` (vía `crm-tracker`).

## Reorder / loyalty
- Programa el siguiente contacto según duración del producto (ej. D30/D45).
- Ofrece complementos relevantes; pide referidos solo si la experiencia fue buena.
- Mantén notas mínimas y respetuosas (privacidad, ver compliance).

## Ordering & delivery (tu zona + envíos)
- `⚠️ COMPLETE` logística real (entrega en zona, punto de encuentro, paquetería).
- Comunica tiempos honestos; cumple lo prometido.

## Daily sales rhythm (ties to `ops/daily-workflow.md`)
1. Responde comentarios/DMs nuevos con el guion.
2. Da seguimiento a conversaciones abiertas (cadencia de `crm/followups.md`).
3. Haz 1 oferta clara al día como mínimo.
4. Registra resultados. Apunta objeciones nuevas para mejorar el guion (`system-upgrader`).
