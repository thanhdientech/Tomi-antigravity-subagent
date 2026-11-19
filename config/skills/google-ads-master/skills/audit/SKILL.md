---
name: google-ads-audit
description: >
  Audits and scores an existing Google Ads account across conversion tracking, wasted spend, account
  structure, keywords/Quality Score, ads & assets (incl. PMax, AI Max, Demand Gen), and settings.
  Read-only. Generalized fork of the ads-google audit: reads everything from account-context.yaml and
  applies the operator's guardrails — no brand/vertical hardcoding. Use when the user says "audit",
  "score my account", "what's wrong with my ads", "wasted spend", "account review", "health check".
---

# Google Ads — Audit

Read-only diagnostic. Score the account, surface issues by severity, and — critically — **never fire a
finding on an unverified assumption**. Reuse the live MCP detection proven in `setup`.

## STEP 0 — Load context (MANDATORY, before any scoring)
1. Read `account-context.yaml` from the working directory. If missing, run `setup` first.
2. Pull from it: `google_ads.customer_id`, `brand_terms`, `competitor_terms`, `margin_tiers`,
   `data_source` (for landing-page URL checks), `measurement`, and **`guardrails`**.
3. Output is written to the **working directory** (`GOOGLE-ADS-AUDIT.md`), never into the plugin.

## ⚠️ The six guards (apply to EVERY check — they prevent the most common wrong findings)
These are generic; `guardrails` in the context may strengthen or add to them. Honor both.

- **GUARD-1 Conversions — check the WHOLE picture, not the action list.** Inspect *campaign-level*
  conversion goals + which actions each active campaign actually fires (segment by
  `segments.conversion_action_name`), and each action's source. A primary action no campaign uses is
  inert; a second purchase action kept *secondary* (e.g. GA4 purchase alongside the Shopify channel "App
  Purchase") is the CORRECT anti-double-count setup, not a bug. Only flag a real micro-conversion goal
  or two value-carrying purchase sources both primary and both firing.
  **Before flagging ANY conversion-action contamination (out-of-brand / micro / duplicate), check
  `primary_for_goal`.** A non-primary action does not enter Smart Bidding and does not affect performance —
  it's harmless; surface it as a NOTE (tidy-up), never a scored finding. Only a PRIMARY out-of-brand/micro
  action that an active campaign optimizes toward is a real issue. See `%USERPROFILE%\.gemini\config/skills/google-ads-master/skills/google-ads-shared/references/conversion-tracking-logic.md`.
- **GUARD-2 Negatives — FOUR sources, merge ALL.** (1) `campaign_criterion` (negative=true) — campaign-level;
  (2) `campaign_shared_set` → `shared_set` → `shared_criterion` — SHARED LISTS (the bulk: e.g. "Account Level
  Negative", "OPI Negative", brand blocks); (3) `customer_negative_criterion` — ACCOUNT-LEVEL negatives applied
  account-wide; (4) `campaign_criterion.brand_list.shared_set` — brand exclusions. Only flag a gap if terms are
  absent across ALL FOUR; if a shared/account list covers them, cite it, don't flag. **A `campaign_criterion`-only
  pull is the #1 false-positive in this audit — it looks "thin" when coverage is actually 100+ terms/campaign.**
  After merging all four, declare `pulled:[...,"negatives_complete"]` so the report renders a real verdict;
  without that assertion a campaign-only bundle renders VERIFY (re-pull), never a false "weak negatives".
- **GUARD-3 Budget scaling — check `change_event` first.** Before recommending a budget/bid increase,
  pull recent change history (~14d). A recent budget/bid/asset/structure change → recommend cooldown,
  not scale. (Strengthen with any `change-event-cooldown` guardrail in context.)
- **GUARD-4 Ad strength — confirm ENABLED + impressions.** Before flagging POOR ad strength, confirm
  `ad_group.status` AND `ad_group_ad.status` are ENABLED and the group has impressions. Paused =
  intentional; do not flag.
- **GUARD-5 ROAS — apply margin tiers from context.** Read `margin_tiers`; a line with a tier accepts its
  `min_roas` (house brands run lower ROAS by design). Never apply a generic ROAS threshold to such a
  line or a strategic campaign. If unsure, ASK rather than flag.
- **GUARD-6 No false "absence".** MCP results can be truncated (token cap or your `limit`). Before
  claiming "no video / no signal / no negative / no X", re-query filtered on the enum NAME (e.g.
  `field_type = 'YOUTUBE_VIDEO'`) or pull with returned-rows < limit (proof of completeness). NEVER
  infer presence/absence by decoding enum integers from memory. Track failed fetches as a G-SYS1
  diagnostic; never silently skip a check — explain why data is unavailable.

## Audit scope — only what's LIVE in the window (build this FIRST, before any check)
Establish the **active campaign set**: campaigns that are ENABLED **AND had impressions > 0 during the
audit window**. Exclude removed, paused, and ENABLED-but-dormant (zero-impression / long-off) campaigns.
Then **scope EVERY other pull to that set** — asset groups, ad groups, ads/ad-strength, keywords, search
terms. Entity-level `status = ENABLED` is NOT sufficient: a campaign turned off years ago can still contain
ENABLED asset groups / ad groups, and auditing them produces stale, misleading findings. Filter downstream
queries by `campaign.id IN (active set)`, or pull them WITH metrics over the window and drop zero-impression
rows app-side (metrics can't go in a GAQL WHERE). Never audit a campaign that hasn't served in the window.

## Model dispatch (run cheap, decide expensive) — see `%USERPROFILE%\.gemini\config/skills/google-ads-master/skills/google-ads-shared/references/model-tier-dispatch.md`
- **Scout (`haiku`)** — STEP 0 context read; the `money_leak_report.py` render (→ the single `AUDIT.html`) after the Judge writes `audit-result.json`; single URL/landing 200 checks.
- **Routine (`sonnet`)** — build the active-campaign set; the account data-bundle pull (campaigns, assets, change history); the dual-source search-term pull (per-PMax `campaign_search_term_insight` loop). Dispatch as `general-purpose` sub-agents (they keep MCP); tell them to **return raw rows, not score**.
- **Judge (main session)** — applying GUARD-1…6, every PASS/WARN/FAIL call, the score, the Gap-to-100 ledger, Quick Wins. **Never delegate a guard or a verdict** — a Scout pulls numbers, the Judge says what they mean.

## Process
1. **Pre-flight**: load context + guards; **build the active campaign set** (above); stage the GUARD data
   pulls (campaign conversion goals, merged negatives, `change_event`, `ad_group.status`) scoped to it.
2. **Collect** account data via the Google Ads MCP, **scoped to the active campaign set**. Honor GAQL gotchas
   in `%USERPROFILE%\.gemini\config/skills/google-ads-master/skills/audit/references/gaql-notes.md` (dedup keywords; ENABLED-only +
   impressions-in-window; explicit YYYY-MM-DD date ranges; `search_term_view` can't use a 90-day DURING).
   **MANDATORY pulls — a missing one = a false finding, not a clean account (this is the checklist a dispatched
   Scout MUST be handed in full):**
   - campaigns + metrics (active set), budgets, bidding strategy + tROAS
   - conversion_action (account) + per-campaign `segments.conversion_action_name` usage (GUARD-1)
   - asset_group / ad_group_ad ad-strength; keyword_view + Quality Score (deduped)
   - **campaign extensions coverage** (A9): `SELECT campaign.id, campaign.status, campaign_asset.field_type,
     campaign_asset.status FROM campaign_asset WHERE campaign.status='ENABLED' AND campaign_asset.status='ENABLED'`.
     `field_type` gives the coverage (SITELINK / CALLOUT / STRUCTURED_SNIPPET / PRICE / IMAGE). **Two gotchas,
     both seen live:** (1) `campaign.status` MUST be in the SELECT because it's filtered (else
     `EXPECTED_REFERENCED_FIELD_IN_SELECT_CLAUSE`); (2) do NOT also select `asset.type` here — it throws
     INVALID_ARGUMENT on many MCPs (pull asset text separately if needed). Count `field_type` **per campaign**
     (not just presence) so "thin extensions" findings use real counts. If it still errors, flag extensions
     **UNVERIFIED — verify in UI**, never assume present/absent.
   - search terms **both** sources: `search_term_view` + per-PMax `campaign_search_term_insight`
   - **negatives from ALL FOUR sources (GUARD-2) — NOT just `campaign_criterion`:**
     (a) `campaign_shared_set` (which shared lists attach to each campaign — **count only `status=2` ENABLED;
     many lists are `status=3` REMOVED/old**) → `shared_criterion` (the terms in each ENABLED list);
     (b) `customer_negative_criterion` (account-level negatives applied to every campaign — a separate resource,
     easy to miss; the first ND pull omitted it and produced a false "weak negatives" finding that had to be
     corrected mid-audit). A brand block / cross-brand block / location block usually lives in a SHARED or
     ACCOUNT-level list, so a `campaign_criterion`-only pull shows "no negatives" when coverage is actually
     extensive. **Never flag G07/G14/G-PM5/G-PM6 (brand exclusion / negative coverage) without having pulled
     `shared_criterion` AND `customer_negative_criterion`. After merging, declare `pulled:[...,"negatives_complete"]`.**
   - **PMax Brand exclusions are a SEPARATE layer from negative keywords — pull them explicitly:**
     `campaign_criterion` selecting `campaign_criterion.brand_list.shared_set` + `.negative`
     (filter `campaign_criterion.brand_list.shared_set IS NOT NULL`), then resolve each `shared_set.name`.
     These rows have an EMPTY `keyword.text`, so a keyword-text-only pull DROPS them and you'll wrongly
     report "no brand exclusion". Check whether a brand list matching the own brand (a list named after the
     own brand) is excluded on each PMax campaign. An account can run BOTH a brand negative-keyword list AND a brand-list
     exclusion (belt-and-suspenders) — read both before judging.
   - `change_event` (~14d)
   - **channel split** (A8): `segments.ad_network_type` per campaign — **this WORKS for PMax too** (network 2
     Search/Shopping dominates; small YouTube/Display/cross). NEVER report channel as "verify in UI". Pull
     `metrics.conversions` alongside cost — a cost-only pull makes every network look like 0-conv burn.
   - **device split** (A10): `segments.device` per campaign (2 Mobile · 3 Tablet · 4 Desktop · 5 CTV · 6 Other).
   - **dayparting** (A3/A4): `segments.hour` + `segments.day_of_week` per campaign + metrics — for the hourly
     heatmap and best/worst hour/day. And **ad schedule**: `campaign_criterion.ad_schedule.*` + `bid_modifier`
     (a flat `bid_modifier=0` across the window = NO dayparting bid strategy — a real opportunity finding).
   - **geo — ALL regions** (A3): `geographic_view` scoped to active campaigns, `metrics.cost_micros > 0`, **no
     top-N limit**. Then resolve EVERY `segments.geo_target_region` id to a name via `geo_target_constant`
     (id, name, canonical_name). Raw `geoTargetConstants/NNNNN` ids in the report = an unfinished pull, never ship them.
   - **asset TEXT + per-asset metrics** (A9) — pull the TEXT and cost, NOT just counts (a counts-only pull is
     wrong; the verbatim text + per-asset spend is what surfaces "this headline spent $X at 0 conv"):
     `SELECT campaign.id, asset_group_asset.field_type, asset.text_asset.text, metrics.cost_micros,
     metrics.conversions, metrics.conversions_value, metrics.clicks FROM asset_group_asset WHERE
     campaign.status='ENABLED' AND asset_group_asset.status='ENABLED' AND segments.date BETWEEN ...` (HEADLINE
     ft2 / DESCRIPTION ft3 / LONG_HEADLINE ft18). `asset_group_asset` DOES return per-asset metrics — a
     text-only or count-only pull just *looks* empty (gaql-notes). For **Search RSAs**, `ad_group_ad.ad.
     responsive_search_ad.headlines` is a RepeatedComposite the serializer can't return — get RSA asset text +
     metrics from **`ad_group_ad_asset_view`** instead (don't write "verify in UI"). The ONLY genuine UI-only
     asset field is `asset_group_asset.performance_label` (UNRECOGNIZED on some API versions).
   - **extension TEXT** (A9) — not just field_type counts: pull the sitelink/callout/snippet/price **text**
     so the report shows the actual extensions. Either `campaign_asset` joined to the `asset` text fields
     (`asset.sitelink_asset.link_text`, `asset.callout_asset.callout_text`, `asset.structured_snippet_asset.values`,
     `asset.price_asset.*`) or the `asset` resource by id. bundle key `ext_text:[{campaign_id,field_type,text}]`.
   - **conversion lag** (A12): `segments.conversion_lag_bucket` — the "can I trust short-window ROAS?" gate.
   - **settings & measurement that DO read** (pull these — they were once wrongly punted to UI): **location type**
     `campaign.geo_target_type_setting.positive_geo_target_type` — **official enum: 5=PRESENCE_OR_INTEREST,
     6=SEARCH_INTEREST (both leaks → recommend Presence-only), 7=PRESENCE (correct, NOT a leak)**. Do NOT invert
     this: 7 is the GOOD value. (Verified live + against the v21 proto 2026-06-28.) **Enhanced Conversions** `customer.conversion_tracking_setting.enhanced_conversions_for_leads_enabled`
     + `.accepted_customer_data_terms`; **final URLs** via `landing_page_view` / `expanded_landing_page_view`;
     **RSA text + per-asset metrics** via `ad_group_ad_asset_view`; **placement exclusions** via
     `campaign_criterion.placement.url`; **content-label exclusions** (digital content labels DV-G/PG/T/MA) via
     `campaign_criterion` WHERE `type='CONTENT_LABEL'` (`content_label.type`) — **this READS; an empty result =
     none configured, NOT unreadable** (do not punt it to UI). bundle key `content_labels:[{campaign_id,content_label_type}]`.
     (Exact queries: `references/gaql-notes.md`.)
   - **competitive pressure — impression share (PUBLIC, always pull)** (D-competitive): per active campaign pull
     `metrics.search_impression_share`, `metrics.search_rank_lost_impression_share`,
     `metrics.search_budget_lost_impression_share` (+ abs-top) with a date range. rank-lost IS = losing the
     auction to COMPETITORS on Ad Rank; budget-lost IS = losing to budget (a scaling lever). Put on each
     `active_campaigns` row. These are public metrics — never punt to UI.
   - **competitor DOMAINS — Auction Insights (try, then degrade)** (competitor input): the "phiên đấu giá"
     competitor list IS in the API — `segments.auction_insight_domain` + `metrics.auction_insight_search_*`
     (impression_share / overlap_rate / outranking_share / position_above_rate / top & abs-top %). **BUT these
     are RESTRICTED "not publicly available" metrics → most dev tokens get `METRIC_ACCESS_DENIED` unless Google
     allowlisted the token.** So: TRY the pull; on success write bundle key `auction_insights:[{domain,
     impression_share,overlap_rate,outranking_share,position_above_rate}]` (the report renders a Competitors card
     and you MERGE the domains into the setup competitor list). On `METRIC_ACCESS_DENIED`, do NOT call it an API
     gap — note "Auction Insights metrics not allowlisted on this token" and fall back to the impression-share
     signal above + the competitors the user gave at setup. (Set `meta.own_domain` so your own row is tagged.)
   - **⚠️ "verify in UI" is ONLY these confirmed-blocked fields** (every variant tested 2026-06-28) — do NOT
     mark anything else UI-only: Final URL Expansion toggle (`url_expansion_opt_out` UNRECOGNIZED), asset
     automation (`asset_automation_settings` PROHIBITED/RepeatedComposite), the **video brand-safety inventory
     mode** (`campaign.video_brand_safety_suitability` UNRECOGNIZED on this version — Expanded/Standard/Limited),
     PMax `asset_group_asset.performance_label` (UNRECOGNIZED — use
     `asset_group.ad_strength` + per-asset cost/conv), and **Consent Mode v2 / server-side-CAPI** (tag-side by
     design — verify in GTM, NOT a pull failure). EVERYTHING ELSE is in the API: a fetch that returns nothing =
     wrong method (field/resource/missing `metrics.*`/enum-to-drop), **retry** — see `references/gaql-notes.md`.
     A "we can't see it, check the UI" on API-available data is the #1 way this audit loses a user's trust.
   - **GAQL gotcha:** any field used in a `WHERE` filter MUST also appear in the `SELECT` clause, or the API
     returns `EXPECTED_REFERENCED_FIELD_IN_SELECT_CLAUSE` (e.g. filtering on `campaign.status` requires
     selecting it). If a field is rejected, drop just that field and re-run — don't abandon the whole pull.
   - **COMPLETENESS — loop every campaign, never truncate.** Per-campaign pulls (`asset_group_signal`,
     `asset_group_asset`, `campaign_search_term_insight`) must cover **ALL** PMax/Search campaigns — do NOT stop
     "to save time" at the first few. A partial pull (e.g. signals for 3 of 7 PMax) makes the generator emit
     FALSE "0 audience signals" findings for the un-pulled ones. Big results: save to a file + parse, don't drop.
   - **DECLARE what you pulled.** `bundle.json` MUST carry a top-level **`pulled: [...]`** listing every
     dimension you FULLY pulled (all campaigns) — e.g. `["active_campaigns","channel","device","geo","dayparting",
     "schedule","extensions","signals","negatives","assets","products","conversion_lag","change_events"]`.
     **Omit any dimension you could not complete** — the generator renders those VERIFY ("not pulled — re-run")
     instead of fabricating GOOD/FIX. Honesty-by-construction: an absent `pulled` entry is safe; a half-filled
     dimension passed off as complete is what burns the user.
3. **Validate coverage**: confirm ≥30 days of data and a Search Terms Report before scoring; if a source
   is down, degrade gracefully (flag it, continue) per the fallback chain in `setup`.
4. **Evaluate** each applicable check as PASS / WARNING / FAIL — applying GUARD-1…6 so nothing fires on an
   assumption. Use `%USERPROFILE%\.gemini\config/skills/google-ads-master/skills/audit/references/google-audit-checks.md` for the check catalog and severities.
5. **Score** per `%USERPROFILE%\.gemini\config/skills/google-ads-master/skills/audit/references/scoring-system.md` (weighted by severity × category).
6. **Report** with the per-category Gap-to-100 ledger and an action plan.

---

> 📖 **Chi tiết đầy đủ:** Xem [DETAIL.md](./references/DETAIL.md) — chứa bảng tra cứu, checklist và ví dụ mở rộng.
