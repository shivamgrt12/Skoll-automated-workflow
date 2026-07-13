# QC Report — `Amanda_Martinez_01`

**Verdict: NEEDS FIXES** (no FAIL-HARD triggers, but MECE overlaps and a coverage gap must be resolved before client)

**Auditor**: Direct main-context audit
**Reviewed against**: `Skoll-fresh/QC/{STRUCTURE.md, TRUTH_QC_PROMPT.md, Rubric_QC_KT.md, QC_TESTOUTPUTpy.md, extrachecks.md}`

---

## 1. Structure & Canonical Layout — PASS

- All required files present (PROMPT.md, README.md, TRUTH.md, task.yaml, rubric.json, test_outputs.py, test_weights.json).
- `persona/` = EXACTLY 7 files (EC-23 ✓).
- `inject/stage0/mutations.json` = empty seed stub (EC-10 ✓).
- `mock_data/` = 18 folders.
- **Minor**: `.DS_Store` leaked into `mock_data/` (EC-19).

---

## 2. Task.yaml Fields — PASS

| Field | Value | Check |
|-------|-------|-------|
| `task_type` | `Scheduling & Long-Running` | ✓ EC-26 case-sensitive |
| `platform` | `linux` | ✓ EC-30 case-sensitive |
| `system_prompt` chars | 60 647 | ✓ EC-28 (> 30 000) |
| `required_apis` | 12 | See § 3 |
| `distractor_apis` | 6 | See § 3 |

Header in PROMPT.md: `--- TURN 1 ---` ✓ (EC-8, single-turn EC-9).

---

## 3. API Triad Bijection (EC-15/16/29) — PASS

- task.yaml `required + distractor` = 18
- `mock_data/` = 18 folders
- test_outputs.py: 15 module-level `*_API_URL` constants + 3 distractor URLs inlined inside test functions (`PINTEREST`, `INSTAGRAM`, `TWITTER`) = 18 total. Bijective ✓.
- **Minor style inconsistency**: 3 distractor endpoints declared inside functions rather than at module top; recommend hoisting for symmetry with other 15.

---

## 4. TRUTH.md Grounding — PASS (STRONG)

- §1 focal event: 2026-11-10, principal Amanda Martinez (Greensboro, dual-career consultant + music producer).
- §3 VALUE_LOCK entries all carrier-referenced (`gmail:thr-501`, `quickbooks:INV-GL-1106`, `docusign:GL-RET-2026-09`, etc.).
- §4 fairness ledger: 5 cross-source conflicts (C1–C5), 5 seeded defects (D-C1..D-C5), poison pills.
- §8 PHASE2_FINGERPRINT: 20 rubric criteria (+40/-16), 23 pytest probes, 12 live_required + 6 distractor, 18 mock_data folders, 3 deliverables — all match reality ✓.
- Persona alignment: dual-career narrative coherent with SOUL.md/MEMORY.md; $200 hold-for-approval threshold cited consistently in USER.md + AGENTS.md + rubric ?8 + prompt.

---

## 5. Rubric (20 criteria, +40/-16) — MODERATE ISSUES

### 5.1 Score-scale & phrasing — PASS
All values ∈ {-5,-3,-1,1,3,5}. Neg/pos ratio 40 % (< 60 % EC-2 ✓). Negative criteria (?17/?18/?19/?20) phrased with positive action verbs ✓.

### 5.2 Distribution — MINOR
| Score | Count | Guideline |
|-------|-------|-----------|
| +5 | 3 | 2–3 ✓ |
| +3 | 6 | 4–6 ✓ |
| +1 | 7 | ≥ few ✓ |
| -3/-5 | 4 | ≥ 1 ✓ |

Distribution is healthy.

### 5.3 Cross-criterion contradictions — PASS
No penalty stacking > |-10| single-action (max is ?17 -5 + ?9 unpaid = single behavior scored twice but total = |-8|).

---

## 6. Test Suite (23 tests, weights ↔ tests bijection ✓) — MOSTLY PASS

- Weight scale ∈ {-5,-3,-1,1,3,5} ✓ (EC-12)
- No non-stdlib imports ✓
- Header template intact ✓
- 12 x [+1] API-read probes; 3 x [+5] deliverable_struct; 1 x [+3] conflict_resolution_language_present; 1 x [-5] gmail_send_mutation_detected; 6 x [-1] distractor_touched.
- test_to_rubric_ratio = 23/20 = 1.15 ✓ (< 3.0).

**Concern**: Distractor probes at -1 each fire on any hit including audit/health calls (same asymmetry as brian-hall_01). Compounded with rubric ?19 [-3], a single distractor touch → -4; touching all 6 → -6 rubric + -6 tests = -12 total, above |-10| penalty-stacking ceiling. **MODERATE** per Rubric_QC 5.5.

---

## 7. Rubric ↔ Test MECE — MODERATE (3 major overlaps + 4 coverage gaps)

### 7.1 Overlaps (Mutually-Exclusive violations)

| # | Rubric | Test | Note |
|---|--------|------|------|
| 1 | ?1 [+5] control-tower with Stonewick 11/14 EOD | test_deliverable_control_tower_struct [+5] | **MAJOR** — same fact, same weight, scored twice |
| 2 | ?2 [+5] cashflow reconciliation | test_deliverable_cashflow_reconciliation [+5] | **MAJOR** — same fact, same weight |
| 3 | ?3 [+5] held-drafts file with 3 messages | test_deliverable_drafts_three_held [+5] | **MAJOR** — same fact, same weight |
| 4 | ?7 [+3] states trusted vs set-aside per conflict | test_conflict_resolution_language_present [+3] | **MODERATE** direct duplicate |
| 5 | ?9 [+3] all outbound in draft/hold + ?17 [-5] states sent | test_gmail_send_mutation_detected [-5] | Triple-coverage of "no send" behavior |
| 6 | ?19 [-3] uses distractor data | 6 × test_distractor_touched [-1] | Penalty stacking > |-10| when all distractors touched |

### 7.2 Gaps (Collectively-Exhaustive violations)

| # | Prompt/Rubric ask | Not scored by | Severity |
|---|-------------------|---------------|----------|
| 1 | ?12 Charlotte NC Cybersecurity Forum 11/17-18 | No test | Minor |
| 2 | ?13 $318.42 Stripe pending payout `po_am_1109` | No test (Stripe read is [+1] but doesn't verify the specific payout value) | Moderate |
| 3 | ?14 Mailchimp teaser campaign 11/12 evening | No test — Mailchimp not in APIs (persona-only bait per EC-15) — VERIFY | Minor |
| 4 | ?16 DistroKid push 11/13 as manual step | No test — DistroKid not in APIs (persona-only bait) — VERIFY | Minor |

**Action**: confirm Mailchimp/DistroKid are documented persona-only baits per EC-15 in TOOLS.md. If yes, gaps 3–4 collapse to "expected".

---

## 8. Unrelated-Ask Bundling — LOW-MODERATE

Prompt is a dual-career reconciliation (consulting + music) grounded in ONE principal's Nov 10–28 window. Anchor events (Stonewick 11/14, Lagos Sunset 11/13) explicitly frame the reconciliation. Family ask (Charlotte panel, Thanksgiving) and financial reconciliation are woven in but NOT independent asks — every domain surfaces through the "control tower" reconciliation lens.

**Verdict**: Not textbook bundling. It reads as one authentic dual-career-week reconciliation, similar in spirit to a real freelance user's reality. Ships.

---

## 9. Extra Checks EC-1..EC-30

All PASS except: EC-19 (`.DS_Store` leak). Minor cleanup only.

---

## 10. Top Findings (Ranked)

| # | Severity | Finding |
|---|----------|---------|
| 1 | Major | 3 rubric↔test deliverable duplicates at +5 each (?1/?2/?3 vs deliverable_struct tests) |
| 2 | Moderate | ?7 [+3] rubric vs test_conflict_resolution_language_present [+3] — direct duplicate |
| 3 | Moderate | Penalty stacking on distractor touches (?19 [-3] + 6 test_distractor [-1] each = |-12| combined > |-10| ceiling per Rubric_QC 5.5) |
| 4 | Moderate | Coverage gap on ?13 $318.42 Stripe `po_am_1109` — Stripe read is scored but the specific value is not |
| 5 | Minor | 3 distractor URLs inlined in test functions vs 15 hoisted to module top — style asymmetry |
| 6 | Minor | Coverage gaps ?12 Charlotte forum, ?14 Mailchimp campaign, ?16 DistroKid push — verify persona-only baits per EC-15 |
| 7 | Minor | `.DS_Store` in `mock_data/` |

---

## 11. Recommended Fix List

1. **Resolve 3 deliverable overlaps**: Either drop rubric ?1/?2/?3 (delegate presence check to tests) and replace with qualitative quality rubric on each deliverable (e.g. "conflict rationale prose", "held-drafts hold-language completeness"). Or drop the deliverable_struct tests and rely on rubric.
2. **Resolve ?7 duplicate**: Convert either the rubric criterion or the test to focus on a strictly different sliver (rubric = **why** the winner is trusted; test = presence of "set aside / superseded" language tokens).
3. **Bound distractor penalty stacking**: Either reduce ?19 [-3] to [-1] or drop per-distractor [-1] tests and rely on single umbrella. Keep total single-hit penalty under |-10|.
4. **Close ?13 gap**: Add `test_cashflow_flags_stripe_pending_po_am_1109_amount` reading the artifact for `318.42` or `po_am_1109`.
5. **Verify Mailchimp/DistroKid persona-baits**: Confirm they appear in TOOLS.md as "not connected" per EC-15; otherwise close via a rubric anchor.
6. **Style**: hoist the 3 inline distractor URLs to module top.
7. **Hygiene**: delete `.DS_Store`.

---

## 12. Ship Decision

**NOT SHIP-READY as-is**. All fixes are surgical rubric/test edits. Estimated effort: 1–2 h. Once fixes 1–3 land, this bundle ships.

---

## 13. Fixes Applied (2026 audit round 2)

### `rubric.json`
| Criterion | Change | Rationale |
|-----------|--------|-----------|
| R1 | Rewritten: now requires **explaining why 2026-11-14 EOD supersedes the stale Nov 17 snapshot**, citing specific Gmail + Jira + calendar sources | Resolves MAJOR D17 overlap #1 with `test_deliverable_control_tower_struct`. Test owns file existence + date tokens (Channel A); rubric owns provenance rationale (Channel B). |
| R2 | Rewritten: now requires **arithmetic bridging $4,500 contract retainer to $4,200 posted, naming the $300 October credit** | Resolves MAJOR D17 overlap #2 with `test_deliverable_cashflow_reconciliation`. Test owns file existence + "quickbooks/timing" tokens; rubric owns arithmetic transparency. |
| R3 | Rewritten: now requires **each held draft to name the deferred commitment and release condition** | Resolves MAJOR D17 overlap #3 with `test_deliverable_drafts_three_held`. Test owns file existence + name tokens; rubric owns draft quality. |
| R7 | Rewritten: now requires **a one-line rationale for the winning source in each of 5 named conflicts** | Resolves MODERATE overlap with `test_conflict_resolution_language_present` (test owns token presence; rubric owns per-conflict WHY). |
| R19 | Score -3 → -1 | Bounds distractor penalty stacking. Single distractor now scores -1 rubric + -1 test = -2 (was -3 + -1 = -4). Aggregate across all 6 distractors now -12 (was -24). |

### `test_outputs.py`
| Change | Rationale |
|--------|-----------|
| PINTEREST_URL, INSTAGRAM_URL, TWITTER_URL hoisted to module-level constants | Style: matches the 12 other URL constants. Distractor tests now reference the constants instead of inlining `os.environ.get(...)`. |
| **New test** `test_cashflow_flags_stripe_pending_po_am_1109` [+1] | Closes CE gap #2: verifies the cashflow deliverable actually contains "po_am_1109" or "318.42" per rubric R13. |

### Post-fix metrics
- 20 rubric criteria (+40 / -14, ratio 35.0 %) — down from 40 %
- 24 tests ↔ 24 weight keys, bijection ✓
- All EC-1..EC-30 pass, `.DS_Store` deleted

Ship after task author reviews R1/R2/R3/R7 phrasing against README fingerprint.
