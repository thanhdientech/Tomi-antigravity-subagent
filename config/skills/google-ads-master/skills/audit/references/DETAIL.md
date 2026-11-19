# audit — Chi Tiết Đầy Đủ

> File này chứa bảng tra cứu, checklist và ví dụ mở rộng của skill `audit`.
> Được tách từ SKILL.md để tuân thủ giới hạn 24KB của Antigravity.
> Xem hướng dẫn chính tại [SKILL.md](../SKILL.md)

---

## Money-Leak deep-dive (MANDATORY — this is what makes the audit worth paying for)
Beyond scoring, run the money-leak diagnostics in `%USERPROFILE%\.gemini\config/skills/google-ads-master/skills/google-ads-shared/references/diagnostic-playbook.md`
(A1 bid/target health · A2 budget pacing & allocation · A3 geo waste · A4 dayparting · A5 search-term/spam/
wrong-brand · A6 structure/setup · A7 Quality Score · A8 PMax channel/placement · A9 ad copy/assets/extensions ·
A10 settings hygiene · A11 audience signals/search themes · A12 conversion-lag gate · A13 change-history timeline ·
**A14 product feed & Shopping performance**). **For ECOM, A14 is the highest-$ diagnostic.** It has THREE
layers, each from a different source — degrade cleanly, don't lump them as "needs Merchant":
  1. **Product PERFORMANCE/identity (Ads, always available)** — `shopping_performance_view` returns full product
     data through the Merchant LINK (item_id, title, brand, type, condition + cost/impr/conv). The "which product
     burns / converts" leak. The products ARE in Google Ads — never say "no product data".
  2. **Out-of-stock (STORE connector)** — cross-ref the spending item_ids against the store's live inventory
     (Shopify/Woo). OOS spenders = pure waste, and this needs NO Merchant connector — only the store you already
     connected. Do this whenever a store is connected.
  3. **Approval STATUS (Merchant Content API only)** — disapproved / GTIN / policy issues are NOT a GAQL field.
     If a Merchant connector is present, pull it; if not, flag ONLY this layer as verify-via-Merchant (not the
     whole of A14).
  **A14 gets its OWN rendered HTML — `A14-PRODUCT-CHECK.html` — not just markdown.** When a store is connected,
  join the zero-conversion burn products (layer 1) against live store inventory (layer 2) into ONE per-item JSON
  (one row per burning product) with these fields per item: `campaign`, `title`, `brand`, `cost_30d`,
  `clicks_30d`, `imp_30d`, `product_onlineStoreUrl` (the live PDP link — MANDATORY so the user can click to
  check each SKU), `variant_sku`, `variant_price`, `variant_compareAtPrice`, `variant_inventoryPolicy`,
  `total_available_all_locations`, `classification` (`OOS_DENY` | `LOW_STOCK` | `IN_STOCK_NEEDS_PDP_AUDIT`),
  `reason`. Then render:
  `python %USERPROFILE%\.gemini\config/skills/google-ads-master/skills/audit/scripts/a14_product_report.py <items>.json --out-dir <workdir>
  --account "<name>" --window "<range>"` → a visual, self-contained `A14-PRODUCT-CHECK.html`: KPI strip, one
  color-coded section per classification (OOS=red / low-stock=amber / in-stock=blue), a burn bar per row, and a
  **full SKU appendix where every product title links to its live storefront URL**. ALWAYS pull the PDP URL +
  SKU (`product.onlineStoreUrl` / variant SKU from the store) — a A14 product list without clickable URLs is
  incomplete; the user must be able to verify each item in one click. Each diagnostic yields a **Money-Leak
  Report** row: leak · evidence
(real numbers) · diagnosis (root cause, not symptom) · **$/month at risk** (formula shown) · exact fix ·
discipline · confidence. Decode `bidding_strategy_system_status` FIRST (one field separates budget-capped vs
tROAS-too-high vs starved vs learning). A generic "score 85" without these specific, dollar-quantified leaks is
the low-value audit we are explicitly NOT shipping. The diagnostics feed both the category scores and the
Money-Leak Report in the output.

**One-command pipeline (model-tier dispatch) → ONE comprehensive report:** dispatch a **Routine** sub-agent
(`general-purpose`, sonnet) to run the PULL MANIFEST in
`%USERPROFILE%\.gemini\config/skills/google-ads-master/skills/audit/scripts/money_leak_report.py` (its docstring lists every GAQL query + the
`bundle.json` schema) → it writes `bundle.json`. **Write `audit-result.json` (the score — STEP 5) into the SAME
directory** so the generator merges score + money-leak. Then **Scout**-run
`python %USERPROFILE%\.gemini\config/skills/google-ads-master/skills/audit/scripts/money_leak_report.py bundle.json --out-dir <workdir>` to
generate `MONEY-LEAK-REPORT.md` + `DETAILED-ACCOUNT-REPORT.md` AND the **single comprehensive `AUDIT.html`** —
score donut + grade, the 6 weighted category bars (fixable/unverified findings), money-leak $ chart + findings,
a **visual per-campaign section** (ROAS-vs-target bar with target tick, status pill, channel-split bar,
extension/signal chips), Merchant feed table, quick wins, change timeline, verify-in-UI. It auto-detects
`audit-result.json` next to the bundle (or pass `--audit-result`); without it AUDIT.html degrades to
money-leak-only. **AUDIT.html is THE — and the ONLY — HTML deliverable: one file, score + full check + leaks +
per-campaign visuals together.** Do not render any second HTML report (no `audit-report.html`); there is exactly
one HTML output per audit.
Then the **Judge** (you) adds verify-in-UI verdicts. **When a pull returns nothing, assume wrong method (field
name / resource / missing `metrics.*` / repeated-enum serialize), not an API limit — retry before writing
"verify-in-UI"** (see gaql-notes principle).

## What to analyze (category weights)
- **Conversion Tracking (25%)** — campaign-level goals (GUARD-1), Enhanced Conversions, Consent Mode v2,
  value tracking, attribution, offline import (lead gen), conversion lag. Cross-check Google Ads vs GA4
  (flag >35% divergence) when `measurement.ga4` is enabled.
- **Wasted Spend / Negatives (20%)** — review search terms from **BOTH sources** (`search_term_view` does
  NOT contain PMax terms): `search_term_view` for Search/Branded campaigns + `campaign_search_term_insight`
  **looped per active PMax/Demand-Gen campaign** (it requires a single `campaign_id` filter; see
  gaql-notes.md). Merged negative coverage (GUARD-2), brand/non-brand separation (use `brand_terms`), broad
  match only with Smart Bidding, geo precision. Source negatives from actual irrelevant search terms; prefer
  Exact/Phrase; recommend shared lists. Only flag wasted on Search terms with >$10 spend AND 0 conv; for
  PMax, flag irrelevant categories with clicks but no conversions. **Never propose blocking brand terms.**
- **Account Structure (15%)** — business-logic organization, tightly themed ad groups, ≥3 RSAs/group,
  PMax asset-group/signal structure, naming consistency.
- **Keywords & Quality Score (15%)** — match-type strategy, QS distribution (≥7 target), cannibalization
  (watch cross-campaign + use `brand_terms`), impression share. Apply the legacy-BMM heuristic (BROAD +
  Manual CPC = legacy, not intentional broad).
- **Ads & Assets (15%)** — RSA headlines/descriptions count & strength (GUARD-4), pin discipline,
  extensions (sitelinks/callouts/snippets/image), PMax/AI Max/Demand Gen specifics (below).
- **Settings & Targeting (10%)** — Smart Bidding vs deprecated ECPC, budget pacing, ad schedule, device
  adjustments, location = "Presence" not "Presence or Interest", network settings.

## Deep dives (only if those campaign types exist)
- **PMax** — asset-group diversity, audience signals, URL-expansion control, search themes, Insights tab,
  and **brand handling — VERIFY, don't just "confirm"**. When a Brand Search campaign runs alongside PMax,
  do NOT flag "missing brand exclusion" on the surface. First DIG IN and check ALL THREE block mechanisms:
  (a) **campaign-level negative keywords** (`campaign_criterion`, `negative=true`, type KEYWORD);
  (b) a **shared negative list** (`campaign_shared_set` → `shared_criterion`) — brand blocks are MOST often a
  named shared list (e.g. "Brand Keywords — do not apply to Branded campaign") applied to PMax + non-brand campaigns
  and excluded from the Branded campaign; (c) a **brand-exclusion brand list** (brand-list criteria). Check
  whether the account's `brand_terms` are actually blocked by ANY of these.
  **If brand is already blocked → it's a PASS; re-score, don't flag.** Only flag G07/G-PM3 if brand
  terms are genuinely unblocked (and corroborate with G-PM3: are >15% of PMax conversions on brand terms?).
  Honor any `pmax-brand-exclusion` guardrail.
- **AI Max for Search** — `campaign.ai_max_setting.enable_ai_max`, broad-match+Smart-Bidding combo, search
  term matching distribution, AI Brief, text-customization rules, FUE controls, brand exclusions. DSA/ACA
  auto-migration pre-flight (Sept 2026) — stage LOW→HIGH risk; strong negatives are a prerequisite.
- **Demand Gen** — video+image asset mix, audience signals, funnel-aligned conversion goals (no frequency
  capping — monitor manually).

## Key thresholds
| Metric | Pass | Warning | Fail |
|--------|------|---------|------|
| Quality Score (avg) | ≥7 | 5-6 | <5 |
| CTR (Search) | ≥6.66% | 3-6.66% | <3% |
| CVR (Search) | ≥7.52% | 3-7.52% | <3% |
| CPC (Search) | ≤$5.26 | $5.26-8.00 | >$8.00 |
| Wasted Spend | <10% | 10-20% | >20% |
| Ad Strength | Good+ | Average | Poor |
(Thresholds are **ecommerce-Search defaults** and niches vary widely — apparel ≠ electronics ≠ supplements.
**Derive bands from the account's OWN historical data first**; fall back to these only for a brand-new account,
and state the basis. Never FAIL a campaign on a benchmark its niche legitimately runs below.)

## Report architecture — PER-CAMPAIGN VISUAL EXPLAINER (see `%USERPROFILE%\.gemini\config/skills/google-ads-master/skills/google-ads-shared/references/per-campaign-report-template.md`)
The audit is a **per-campaign visual explainer**, not a generic account summary. Document order: **Account
panel → one chart-rich block per active campaign → Action Plan**.

**The 3-step rule for EVERY item — ① DATA shown → ② VERDICT (GOOD / WATCH / FIX / VERIFY) → ③ ACTION (only
if needed).** There is NO separate "money-leak summary" block: the leak IS the verdict+action on the section
it belongs to (evaluated inline). Every quantitative metric renders as its own **inline-SVG chart**, never a
wall of text:
- ROAS vs target → **semicircle gauge** (fill = ROAS, tick = target) · Budget pacing → **radial ring**
- Channel mix → **donut** · Device & Geo → **horizontal bars colored by ROAS** · Schedule → **24-hour heatmap**
- Extension/signal counts → **meter bars** vs the recommended count.
Each campaign block shows a **scorecard** (N good · N watch · N fix · N verify) and covers: performance +
decoded `bidding_strategy_system_status`, channel, device, geo, schedule, products × Merchant, audience
signals + search themes, ad copy (headline/description text), extensions **with text**, negatives + shared
lists, final URLs/FUE, change/cooldown — each field marked **[API]** or **[VERIFY]** (read-only API can't
see it). The **account panel lists & rates EVERY account-level setting** (conversion tracking, Enhanced
Conv, Consent, account/brand negative lists, Content Suitability, structure, conversion-lag) the same 3-step
way. **Localize per campaign**; only cross-campaign / account-wide items (budget misallocation, tracking,
content suitability, structure) sit in the account panel. Flat/modern style (no heavy gradients).

The blueprint (every section, its chart, data source, verdict thresholds) is
`references/per-campaign-report-template.md`. The generator (`money_leak_report.py`) builds it: account
panel + Σ(campaign block) + action plan → one self-contained `AUDIT.html`. It auto-detects `audit-result.json`
next to the bundle for the score + the account panel's category verdicts.

## Output — `GOOGLE-ADS-AUDIT.md` (to the working dir)
1. **Health Score** 0-100 + grade, with the six category bars.
2. **Per-category Gap-to-100 ledger** (MANDATORY for any category < 100). Split every non-PASS into:
   - 🔧 **Fixable (verified)** — check ID, status, severity, **points recoverable**, concrete fix.
   - 🔍 **Unverified** — API/MCP can't see it (Enhanced Conversions recording, Consent Mode mode, gtag
     firing). Do NOT score as FAIL; mark "verify in UI" and state the ceiling if confirmed. A low score
     driven by unverified items is not breakage — say so.
3. **Money-Leak Report** (the headline deliverable) — the A1-A14 findings as rows ranked by $/month
   recoverable, each with evidence + root-cause diagnosis + exact fix + discipline + confidence. Top 3 = Quick
   Wins. This is what the operator reads first.
4. **Detailed Account Report** (the differentiated value — granular, not just a score). Beyond the summary:
   - **Account summary** + *what is protecting it* (e.g. "no Display burn BECAUSE Content Suitability blocks junk
     apps" — explain the cause, don't just report the healthy symptom).
   - **Per active campaign**, a deep ledger: bidding/tROAS + **decoded `bidding_strategy_system_status`**, ROAS
     vs target, channel split (A8), device split (A10), geo top/bottom (A3), dayparting flags (A4), extension
     inventory — sitelinks/callouts/snippets counts (A9), ad-copy notes incl. duplicates/Ad-Strength (A9), and
     the **settings layer (A10)** — Final URL Expansion + URL exclusions, asset automation / text customization,
     text/brand guideline (exists? appropriate?), content-suitability / placement exclusions, device exclusions.
     **Mark each field API-read or verify-in-UI.**
   - **Per-campaign Verify-in-UI checklist** — the settings the read-only API can't see (FUE, asset automation,
     content suitability, text-guideline content) listed as explicit checkboxes. Never silently skip a setting.
5. Wasted-spend estimate (monthly $), PMax/AI Max notes.
6. **Findings feed `optimizer` and `plan`** — but audit itself changes nothing.

### Also emit a structured result — it feeds the ONE comprehensive HTML report
- Write **`audit-result.json`** (schema: `%USERPROFILE%\.gemini\config/skills/google-ads-master/skills/google-ads-shared/templates/audit-result.json`): health_score, grade, per-category
  scores + fixable/unverified findings, quick_wins, wasted_spend_monthly, notes. **Put it next to `bundle.json`.**
- The client report is **`AUDIT.html`** from `money_leak_report.py` (above): a **per-campaign visual explainer**
  that auto-merges this score JSON (account panel + category verdicts) with the per-campaign chart blocks
  (gauge / ring / donut / bars / heatmap) where every item is **data → verdict → action**. ONE self-contained
  file. **Do NOT ship the score and the money-leak as two separate HTML files** — the audit is one document.
- **There is exactly ONE HTML report: `AUDIT.html`.** The old score-only `audit_to_html.py`/`audit-report.html`
  path has been REMOVED — do not look for it or generate a second file.

## To build / refine later
- [x] **Per-campaign visual-explainer `AUDIT.html`** — `scripts/money_leak_report.py` renders the chart-rich,
  data→verdict→action report (gauge/ring/donut/bars/heatmap + account panel + scorecards). This is the SOLE HTML
  report; the legacy `audit_to_html.py` was removed. Done.
- [x] Full granular check-ID catalog (G01…G61 + extensions) in `%USERPROFILE%\.gemini\config/skills/google-ads-master/skills/audit/references/google-audit-checks.md`. Done.
- [ ] Vertical-specific benchmark bands in `%USERPROFILE%\.gemini\config/skills/google-ads-master/skills/google-ads-shared/references/`.
- [ ] Per-keyword QS + RSA pin/headline-count detail for Search campaigns (currently summarized).
- [ ] Geo as a US choropleth (currently colored bars).
