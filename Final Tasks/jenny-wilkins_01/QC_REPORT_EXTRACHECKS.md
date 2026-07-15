# QC Report — Extrachecks (EC-1..EC-30)

**Bundle:** jenny-wilkins_01
**Gate:** /Skoll-automated-workflow/QC/extrachecks.md (30 checks, task-agnostic)
**Verdict:** PASS (after fixes applied). No FAIL-HARD remaining, no Major remaining.

---

## Fixes applied during this pass

1. **EC-29 / EC-15 / EC-16 (was FAIL-HARD): mock_data folder count.**
   `mock_data/` held 98 `*-api` folders but `task.yaml` declares only 38 (13 required + 25 distractor). 60 undeclared orphan folders were present, none wired to any `*_API_URL` or probe, none referenced in any graded surface (rubric.json / test_outputs.py / test_weights.json / TRUTH.md / task.yaml / PROMPT.md — verified 0 references).
   Root cause: `persona/TOOLS.md` over-declared ~101 services as "Connected"; mock_data mirrored TOOLS.md instead of task.yaml. Reference `Perfect_input_bundle` proves the intended rule (folders == required + distractor exactly).
   **Fix:** the 60 orphan folders were removed (backed up outside the bundle). `mock_data/` now = 38 folders.
   **Re-verify:** EC-29 38==38 PASS; EC-15 no orphans / no missing PASS; EC-16 triad (task.yaml == `*_API_URL` set == folders) PASS.

2. **EC-4 / persona alignment: TOOLS.md trimmed.**
   `persona/TOOLS.md` rewritten so "Connected Services" lists exactly the 38 declared services (verified: connected handle set == task.yaml 38, zero orphan claims, zero banned services claimed as connected). Removed services folded into an honest "Not Connected" section (cloud storage, banking, brokerage/IRA, insurance/Medicare, library internal systems, family private accounts). Jenny's voice preserved.

3. **Deterministic mock gates re-run on trimmed bundle:** overlay validator (38 apis, 0 errors/0 warnings), boot check (38 services boot clean PASS), placeholder scan (0 findings — the prior activecampaign false-positive is gone since activecampaign was an orphan).

---

## Check-by-check

| Check | Result | Notes |
|------|--------|-------|
| EC-1 structure conformance | PASS | Sanctioned file set only. |
| EC-2 rubric neg <= 60% pos | PASS | neg 16 <= 0.6×64 = 38.4. |
| EC-2b test positive coverage per API | PASS | 6 read-coverage positives + deliverable/outcome tests. |
| EC-3 TRUTH grounding/alignment | PASS | Closed in Phase 3 TRUTH QC. |
| EC-4 rubric<->persona/prompt alignment | PASS | TOOLS.md now consistent with task.yaml. |
| EC-5 truncation / zero-byte | PASS | None. |
| EC-6 no google-drive/contacts used | PASS | Banned folders absent; TOOLS.md no longer claims them. |
| EC-7 no class defs / flat weights | PASS | test_outputs.py no classes; test_weights.json flat object. |
| EC-8 prompt header form | PASS | `--- TURN 1 ---` (fixed in Phase 1). |
| EC-9 single-turn prompt-only | PASS | |
| EC-10 inject empty seed stub | PASS | mutations.json = {mutations:[]}. |
| EC-11 weights<->tests bijection | PASS (FAIL-HARD clear) | 23 == 23. |
| EC-12 scale | PASS (FAIL-HARD clear) | all weights/scores in {-5,-3,-1,1,3,5}. |
| EC-13 stdlib-only audit-driven tests | PASS | json/os/glob/urllib only. |
| EC-14 distractor probe coverage | PASS | test_distractor_apis_touched (-5) bucket references all 25 distractors; none positively rewarded. |
| EC-15 mock_data integrity | PASS (fixed) | 38 folders, no orphans, no missing, no drive/contacts/people. |
| EC-16 API triad consistency | PASS (fixed) | task.yaml == *_API_URL (38) == folders (38). |
| EC-17 cross-file count consistency | PASS | TRUTH data_rows fixed to ~660+ in Phase 3; no grading-total drift. |
| EC-18 rubric schema validity | PASS | 7 fields, enums valid, sign matches is_positive. |
| EC-19 no OS/editor junk in bundle | PASS | No .DS_Store/__pycache__ inside bundle. |
| EC-20 no oracle/answer leakage | PASS | Gold only in TRUTH.md. |
| EC-21 deliverable surfaces match connectivity | PASS | Two markdown deliverables; local file writes only. |
| EC-22 no AI-tell prose / em-dash | PASS | PROMPT/README/TRUTH/rubric clean. |
| EC-23 persona exactly 7 files | PASS | AGENTS/SOUL/MEMORY/IDENTITY/USER/TOOLS/HEARTBEAT. |
| EC-24 data/ modality + multimodal wiring | PASS | 5 images flagged by soft low-B/px heuristic = false positive (real high-res photos, no AI signals); images referenced nowhere (no dangling ref). |
| EC-25 two-flavor bait handling | PASS | Callable distractors have folder+URL+negative probe; persona-only baits (Webster, Fidelity, Medicare, library internal) have no folder/URL/probe. |
| EC-26 task_type controlled value | PASS (FAIL-HARD clear) | single valid value. |
| EC-27 task_description single paragraph | PASS | no blank-line break. |
| EC-28 system_prompt > 30000 chars | PASS (FAIL-HARD clear) | |
| EC-29 folder count == req+dis | PASS (fixed, FAIL-HARD clear) | 38 == 38. |
| EC-30 platform MacOs/linux | PASS | valid value. |

---

## Verdict

**PASS.** The one FAIL-HARD (EC-29) and its associated EC-15/EC-16 Major findings are resolved by removing the 60 undeclared mock_data folders and trimming persona/TOOLS.md to the 38 declared services. The Stage-6 image FAIL is a dismissed false positive (real photographs; low bytes-per-pixel explained by high resolution; no AI provenance signals; images unreferenced). All deterministic mock gates re-pass on the trimmed bundle.
