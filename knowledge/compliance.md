# compliance.md — The normative compliance source

> This is the standard. The `compliance-guard` skill enforces it on **every publishable
> output**. When a rule depends on current company policy, `⚠️ VERIFY` against the company's
> official sources (consultant back-office portal, the independent consultant/leader agreement,
> the code of ethics).

## 1. No income / earnings claims or guarantees
- **Never** say or imply: "gana $X", "ingreso garantizado", "hazte rico/a", "dinero fácil",
  "deja tu empleo", "retorno asegurado", specific earnings, or income within a timeframe.
- Discuss the opportunity **honestly and qualitatively**. Cite figures **only** if officially
  backed by the company, and then **with the required disclaimers**. Default: no numbers in public.
- Recruiting copy speaks to learning, community, flexibility, and effort — **never** to
  guaranteed outcomes.

## 2. No medical / therapeutic product claims (cosmetics only)
- Products are **cosméticos**, not medicine. **Never** claim to cure, treat, heal, prevent, or
  diagnose any condition (acné, rosácea, manchas, arrugas as a "treatment", etc.).
- Avoid absolute/【before-after-as-proof-of-cure】 framing. Allowed: cosmetic, sensorial,
  appearance language ("luce más hidratada", "se siente suave", "ayuda a la apariencia de…").
- **México — COFEPRIS:** respect cosmetic advertising rules; no disallowed health claims.
  `⚠️ VERIFY current COFEPRIS specifics.`

## 3. Brand & IP (the company you represent)
- Use the company's trademarks/logos/assets **correctly** and only as permitted; don't imply you
  are the corporation or an official spokesperson.
- Follow the company's **consultant agreement** and **code of ethics**,
  including rules on **online advertising and selling** — notably the **restriction on selling
  via unauthorized marketplaces** (e.g., generic e-commerce/marketplace listings). `⚠️ VERIFY
  current rules` before publishing anything that sells.
- Identify yourself as an **independent consultant**, not as the company itself.

## 4. Truthfulness (PROFECO / FTC-style standards)
- **Real testimonials only** (with permission); no fabricated reviews or results.
- **Clear prices and promos** — no bait, no hidden conditions, honor what's advertised.
- No deceptive scarcity or false urgency.

## 5. Platform Terms of Service
- **No spam**, no mass unsolicited DMs, no buying followers/engagement, no engagement pods, no
  banned automation or account-risking tactics.
- Respect each platform's rules on links, affiliate/branded-content disclosure, and audio use.
- **Disclosures** where applicable (e.g., paid partnerships — not used here, but if ever).

## 6. Privacy & data
- Store **minimal** prospect data in the CRM (`crm/leads.csv` uses an `alias`, not full PII).
- No unnecessary sensitive information; handle third-party data responsibly; honor opt-outs.
- Don't screenshot/publish private conversations without consent.

## 7. Inclusion
- Messaging is **open to everyone**. The operator's differentiator (`key_differentiator`) is a
  positive angle — honest and respectful, **never** deceptive or mocking.

## `compliance-guard` output contract
For any reviewed content, return:
1. **Verdict:** `compliant` | `adjust` | `reject`.
2. **Reasons:** which rule(s) above, specifically.
3. **Corrected, publish-ready version** (es-MX) when `adjust`/`reject` — preserve intent, remove
   the violation.

## Quick red-flag lexicon (auto-flag → rewrite)
`gana $`, `ingreso garantizado`, `hazte rico`, `dinero fácil`, `resultados garantizados`,
`cura`, `elimina (arrugas/acné/manchas)`, `trata`, `previene`, `milagro`, `100% efectivo`,
`antiedad que borra`, `bono asegurado`, marketplace listings (Amazon/ML/etc.) for selling.
> Flagging a term doesn't always mean reject — it means **review and rewrite** to a compliant,
> cosmetic/honest phrasing.
