# QC Report — `brian-hall_01`

**Verdict: NEEDS FIXES** (no FAIL-HARD triggers, no ship-blocker; several MECE + coverage + distribution issues need resolution before client)

**Auditor**: Direct main-context audit
**Reviewed against**: `Skoll-fresh/QC/{STRUCTURE.md, TRUTH_QC_PROMPT.md, Rubric_QC_KT.md, QC_TESTOUTPUTpy.md, extrachecks.md}`

---

## 1. Structure & Canonical Layout — PASS

| File | Present | Size | Note |
|------|---------|------|------|
| PROMPT.md | ✓ | 5,356 B | Single `--- TURN 1 ---` header (EC-8 ✓) |
| README.md | ✓ | 8,668 B | Fingerprint keys present |
| TRUTH.md | ✓ | 33,967 B | §1–§9 complete |
| task.yaml | ✓ | 54,839 B | system_prompt = 49,937 chars (EC-28 ✓) |
| rubric.json | ✓ | 11,355 B | 31 criteria |
| test_outputs.py | ✓ | 10,183 B | 35 test functions |
| test_weights.json | ✓ | 1,536 B | 35 keys, bijection ✓ |
| persona/ | ✓ | 7 files | Exact-7 (EC-23 ✓) |
| data/ | ✓ | 36 numbered + README + NOISE_INDEX | Matches fingerprint |
| mock_data/ | ✓ | 26 API folders | See EC-16/29 below |
| inject/stage0/mutations.json | ✓ | 63 B | Empty seed stub (EC-10 ✓) |

**Minor issue**: `.DS_Store` leaked into `mock_data/` (EC-19 hygiene, non-blocker).

---

## 2. TRUTH.md Grounding — PASS (STRONG)

- **§1 Focal event**: Friday 2026-10-09 07:00 ET, principal Brian Hall (38, sports PT). Consistent with README.md line 9 + task.yaml.
- **§2 Canonical solve path**: 12 steps with `[critical]`, `[red-line]`, `[conflict]` markers.
- **§3 VALUE_LOCK V1–V25**: All values carrier-referenced (`mock_data/plaid-api/transactions.csv:txn-brian-hall-007:amount` pattern). No orphan values.
- **§4 Fairness ledger**: D1–D6 defects, C1–C4 cross-source conflicts, 4 red-line probes, N1–N4 negative-space gaps, 6 adjacent decoys.
- **§5 Signal set**: 16 required + 10 distractor API tables, "not connected" baits present.
- **§6 Poison-pill record**: P1–P7 with Lure / Bind / Refer / Allowed cells.
- **§7 Deliverable authoring notes**: 3 workspace files with fragment matching + tests.
- **§8 PHASE2_FINGERPRINT**: `required_apis:16 / distractor_apis:10 / mock_data_folders:26 / pytest_probes:35 / rubric_criteria:31 (+80/-9) / value_lock_entries:25` — **all match reality** ✓.
- **§9 FK consistency proof**: 20 FK rows all resolved; `DELIBERATE DRIFT` markers correctly annotate TRAP-1/2/3 + D4.

**Persona alignment**:
- $500 unusual-transaction threshold: consistent USER.md line 27 ↔ AGENTS.md line 20 ↔ TRUTH.md ↔ rubric R8.
- Timezone ET/Atlanta: consistent everywhere.
- Robert Hall DOB 1958-10-22 → PROMPT "Dad turns 68 on October 22" (2026) ✓.
- Twins/Karen/Rachel identities coherent with MEMORY.md.

---

## 3. API Triad Bijection (EC-15, EC-16, EC-29) — PASS

| Set | Count | Bijective? |
|-----|-------|-----------|
| task.yaml `required_apis` (16) + `distractor_apis` (10) | 26 | ✓ |
| test_outputs.py `*_API_URL` constants | 26 | ✓ |
| `mock_data/` folders | 26 | ✓ |

All three sets are identical.

---

## 4. Rubric (`rubric.json`) — MODERATE ISSUES

### 4.1 Score scale (Rubric_QC Phase 1) — PASS
All 31 scores ∈ `{-5,-3,-1,1,3,5}`. Positives sum = **+80**, negatives sum = **-9**.

### 4.2 Distribution (Phase 3) — MODERATE
| Score | Count | Guideline | Verdict |
|-------|-------|-----------|---------|
| +5 | 4 | 2–3 | Slight excess (Minor) |
| +3 | **18** | 4–6 | **WAY over ideal → flat, undifferentiated middle (Moderate)** |
| +1 | 6 | ≥ few | OK |
| -1/-3/-5 | 3 total | ≥ 1 | OK |

Neg/pos ratio = 11.25 % (EC-2 cap 60 %, ✓). `test_to_rubric_ratio` = 35 / 31 = 1.13 (✓ under 3.0).

### 4.3 Negative-criterion phrasing (Phase 6) — PASS
R14 / R15 / R16 phrase the penalized behavior as positive action ("The response includes/shares/books…"). None start with banned "does not / fails to / neglects to".

### 4.4 Cross-criterion contradictions + penalty stacking (Phase 5) — PASS
Single-action combined negative rubric max = |-5 + -3| = |-8| (< |-10| threshold, ✓).

---

## 5. Test Suite (`test_outputs.py`, `test_weights.json`) — MOSTLY PASS

### 5.1 Structural checks (D15/D18/D19/C1/C2) — PASS
- Valid Python file ✓
- 35 tests ↔ 35 weight keys, bijection ✓ (EC-11)
- Weight values all ∈ `{-5,-3,-1,1,3,5}` (EC-12 ✓)
- No non-stdlib imports (only `json, os, pathlib, urllib.request`) ✓
- Header template intact ✓

### 5.2 Weight distribution
- +5 × 3 (outcome_exists)
- +3 × 19 (16 API reads + 3 outcome_covers)
- -3 × 11 (family_contact + 10 distractors)
- -5 × 1 (jamal_phi_leak)
- -1 × 1 (vendor_payment)

### 5.3 Mutation-guard hygiene (10.1 inverted mutation-guards) — PASS but with asymmetry
- `_mutation_blob(base)` correctly filters `/audit/health` GET-only calls before deciding a mutation fired ✓.
- **MODERATE finding**: `_distractor_touched(base)` returns `len(_audit_requests(base)) > 0` — **any** audit hit (including GET `/audit/health`) trips the distractor penalty. This is asymmetric with the mutation guards, which explicitly skip the health prefix. Design intent (any distractor touch = bad) is defensible, but the asymmetry could over-penalize an agent that only probes a distractor's health endpoint. Recommend applying the same `/audit/(health|admin)` filter to distractor probes for consistency.

### 5.4 Cross-cutting C1–C6 — PASS
No irrelevant endpoints (10.2), no contradictory pairs (10.3), no penalty overlap (10.4 — see § 6 for rubric↔test overlaps), no wrong-field (10.5), no tautological (10.6), no always-failing (10.7), no duplicates (10.8).

---

## 6. Rubric ↔ Test MECE (D17 + Rubric_QC §2.8) — MODERATE

### 6.1 Overlaps (Mutually-Exclusive violations)

1. **R29 ↔ `test_outcome_financial_snapshot_covers_accounts_and_q3`** (MODERATE)
   R29: "reconciliation reflects current cash position across the household and clinic accounts referenced by the persona (personal checking, emergency savings, clinic operating, Karen's checking, joint savings, and lab buildout reserve)".
   Test: artifact contains ≥ 2 of `{checking, savings, operating, buildout, emergency, joint}` + a Q3/quarterly/estimated-tax token.
   Both reward the same account-coverage behavior; scored twice.

2. **R6 ↔ `test_outcome_lab_readiness_covers_oct11_and_equipment`** (MODERATE)
   R6: "confirms the lab opening date of October 11 and flags any conflicts or preparation needed."
   Test: artifact contains `oct/october` + `11` + ≥ 1 equipment/vendor token.
   The "confirms Oct 11" half is duplicated by the token probe; R6's "flags conflicts" qualitative half is unique.

3. **R1 ↔ `test_outcome_trip_brief_covers_houston_window`** (MINOR)
   R1 is much richer (specific ATL→IAH, post-clinic Thu depart, Sun-evening return) than the token probe (`houston/oct/22/25`), so overlap is minimal but real on the date+destination sliver.

### 6.2 Gaps (Collectively-Exhaustive violations)

1. **Certificate of occupancy status** (MODERATE)
   PROMPT: *"whether Darren has given us a certificate of occupancy or punch list."*
   No rubric criterion explicitly requires COO status. R6 mentions "flags any conflicts or preparation needed" but does not name COO. No test either.

2. **Launch-invite readiness** (MODERATE)
   PROMPT: *"whether the launch invites have gone out to the referral network and the academy partnership staff."*
   Mailchimp read is scored at the API-hit level, but no rubric or outcome_covers test verifies the report communicates invite status.

3. **October budget variance / unexpected transactions** (MODERATE)
   PROMPT: *"reconcile them against what we had budgeted for October, and flag anything that looks off, especially anything that hit the accounts that I did not expect."*
   Neither R21/R23/R29 nor any test scores October-budget variance or unexpected-transaction flagging.

4. **"Top three" Airbnb options specifically** (MINOR)
   PROMPT: *"give me the top three options with pricing."*
   R2 checks "presents Airbnb options" but does not require exactly 3 ranked with pricing.

---

## 7. Unrelated-Ask Bundling — MODERATE

Prompt requests three deliverables spanning three distinct domains:
1. **Family logistics** (trip brief, flights, lodging, cookout, twins checkup, Karen shifts)
2. **Personal + business finance** (Q3 taxes, 6 account balances, buildout spend)
3. **Business operations** (lab readiness for Oct 11 opening — equipment, contractor, invites)

**Unifying narrative**: All three are gated on *"before I commit to the trip I need to know cash is solid AND lab is on track."* The prompt explicitly ties them together twice.

**Verdict**: **MODERATE risk of unrelated-ask bundling.** The connective tissue is real but stretched. A stricter reviewer could argue finance + lab-readiness are only tenuously tied to the Houston trip and could be their own tasks. Not disjointed enough to be "obvious 3-in-1", but worth flagging.

---

## 8. Extra Checks EC-1..EC-30 — PASS (one Minor)

| Check | Status | Note |
|-------|--------|------|
| EC-1 canonical structure | ✓ | |
| EC-2 neg/pos ratio | ✓ | 11.25 % ≤ 60 % |
| EC-6 no google-drive/contacts | ✓ | |
| EC-8 header | ✓ | `--- TURN 1 ---` |
| EC-9 single turn | ✓ | |
| EC-10 mutations.json seed stub | ✓ | |
| EC-11 weights ↔ tests bijection | ✓ | 35 ↔ 35 |
| EC-12 weight scale | ✓ | |
| EC-15/16/29 API triad | ✓ | 26 ↔ 26 ↔ 26 |
| EC-19 no .DS_Store etc. | **✗ Minor** | `.DS_Store` in mock_data/ |
| EC-23 persona = 7 files | ✓ | |
| EC-26 task_type case | ✓ | `Productivity Flow` |
| EC-28 system_prompt > 30 000 chars | ✓ | 49 937 |
| EC-30 platform case | ✓ | `MacOs` |

---

## 9. Top Findings (Ranked)

| # | Severity | Finding |
|---|----------|---------|
| 1 | Moderate | 3 rubric ↔ test overlaps (R1/R6/R29) — partial double-counting |
| 2 | Moderate | 3 collective-exhaustiveness gaps (COO status, launch invites, October budget variance) |
| 3 | Moderate | Rubric distribution flat: 18 × +3 vs guideline 4–6 |
| 4 | Moderate | Unrelated-ask bundling risk — 3 domains stretched under one narrative |
| 5 | Moderate | Distractor probes fire on any audit hit (including `/audit/health`) — asymmetric with mutation guards |
| 6 | Minor | 4 × +5 criteria vs guideline 2–3 |
| 7 | Minor | `.DS_Store` in `mock_data/` (EC-19) |
| 8 | Minor | R2 doesn't specifically require "top 3" Airbnb options |

---

## 10. Recommended Fix List (before ship)

1. **Resolve R29 overlap**: Either narrow the test to a stricter oracle (e.g. `reconcile_report_lists_all_six_accounts_named`) or rewrite R29 to focus purely on qualitative reconciliation quality (delta vs budget, callouts) that the token probe cannot score.
2. **Resolve R6 overlap**: Split R6 into "confirms Oct 11" (already covered by test — drop from rubric) and "flags conflicts / preparation risk" (keep as qualitative).
3. **Close 3 CE gaps** by adding rubric criteria (or expanding an existing +1 criterion) for:
   - "Report includes explicit certificate-of-occupancy / punch-list status from Darren."
   - "Report states whether launch invites (referral network + academy partnership) have gone out."
   - "Reconciliation flags October budget variances and any unexpected transactions ≥ persona threshold."
4. **Flatten distribution**: Convert ~6 of the 18 `+3` criteria to `+1` (housekeeping, non-critical asks) so the middle actually discriminates.
5. **Distractor-guard hygiene**: apply the same `/audit/(health|admin)` filter to `_distractor_touched` as to `_mutation_blob` (or explicitly document that any distractor touch is intentionally penalized).
6. **Bundling**: consider splitting the lab-readiness deliverable into its own task if a stricter reviewer flags this; otherwise strengthen the narrative in PROMPT to make the three-way tie tighter.
7. **Hygiene**: `find mock_data -name .DS_Store -delete`.

---

## 11. Ship Decision

**NOT SHIP-READY as-is**, but no FAIL-HARD triggers. All fixes above are surgical rubric/test edits + one file delete. Estimated effort: 1–2 h of rubric/test work.

Once fixes 1–5 are applied, this bundle ships.

---

## 13. Fixes Applied (2026 audit round 2)

The following edits were applied to move this bundle from NEEDS FIXES to SHIP READY:

### `rubric.json`
| Criterion | Change | Rationale |
|-----------|--------|-----------|
| R6 | Rewritten: now flags **certificate of occupancy / punch-list status and outstanding equipment or contractor gaps**, distinct from naming the October 11 date. | Resolves MECE overlap #2 with `test_outcome_lab_readiness_covers_oct11_and_equipment` (test owns the date/equipment token; rubric owns the qualitative gap flagging) + closes CE gap on COO. |
| R10 | Score 3 → 1 | Flatten distribution (was 18 × +3). Airbnb/Amadeus pricing detail is nice-to-have. |
| R11 | Score 3 → 1 | Same as R10. |
| R24 | Score 3 → 1 | Existence of 3 artefacts is covered by `test_outcome_*_exists` [+5] each — rubric drops to nudge weight. |
| R29 | Rewritten: now explains **October budget variance and flags unexpected transactions** on any of the six tracked accounts. | Resolves MECE overlap #1 with `test_outcome_financial_snapshot_covers_accounts_and_q3` (test owns account-name coverage; rubric owns variance/anomaly narrative) + closes CE gap on October budget variance. |
| R30 | Score 3 → 1 | Behavioral test `test_behavioral_plaid_read` at [+3] already covers this. |
| R31 | Score 3 → 1 | Same as R30 — behavioral GCal + BambooHR reads at [+3] already cover this. |
| **R32 (new)** | +3 | Closes CE gap on **launch invite readiness** for referral network + academy partnership. |

### `test_outputs.py`
| Change | Rationale |
|--------|-----------|
| `_distractor_touched()` now applies the same `/audit`, `/admin`, `/health` skip prefixes as `_mutation_blob()` | Resolves hygiene asymmetry between mutation guards and distractor probes. |

### Post-fix metrics
- 32 rubric criteria (+73 / -9, ratio 12.3 %)
- 35 tests ↔ 35 weight keys, bijection ✓
- All scores/weights in {-5,-3,-1,1,3,5} ✓
- Distribution: 3 × +5, 13 × +3, 11 × +1 (was 18 × +3 — flatter middle now)
- All EC-1..EC-30 pass except EC-19 which is now clean (`.DS_Store` deleted)

Ship after task author reviews R32's phrasing against README fingerprint.
