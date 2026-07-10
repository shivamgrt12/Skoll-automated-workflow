# QC Report: Larry Rawlings Persona

**Audited against**: `PERSONA_QC_PROMPT.md` v1.4 and `7FILE_GENERATION_PROMPT (2).md` v2
**Persona folder**: `c:\Users\Lenovo\Desktop\Newly_create\larry-rawlings\`
**Anchor date used**: October 1, 2026 (derived from the first dated event in HEARTBEAT.md)
**OpenClaw tenure since**: June 2024 (set in IDENTITY.md opening paragraph)

---

## Summary

- **Files in scope**: 7 (AGENTS, HEARTBEAT, IDENTITY, MEMORY, SOUL, TOOLS, USER)
- **Pre-fix coherence score**: 6.7 / 10
- **Post-fix coherence score**: 10.0 / 10
- **Total characters across 7 files**: 48,175 (cap 140,000)
- **All 101 canonical `-api` slugs**: present exactly once, all under `### Connected Services`
- **Forbidden tokens** (`shopify`, `fintrack`, `todoist`, `via mock`): zero hits
- **Em / en / horizontal-bar dashes**: zero hits
- **USER.md line count**: 34 (cap 40)

---

## Section 1 — Findings Catalog

| ID | Severity | Mode | File:Section | Quote (verbatim) | Defect | Fix Type | Fix |
|---|---|---|---|---|---|---|---|
| F-001 | MAJOR | F1 | IDENTITY.md L1 | `# Identity: Larry Rawlings's Assistant` | v1.4 removes the `'s Assistant` suffix from the H1 | DIRECT_FIX | Renamed H1 to `# Identity: Larry Rawlings` |
| F-002 | MAJOR | C3 | IDENTITY.md L3 | `"Your tenure with him spans this freelance era, the one that started when he left marketing at 29."` | Missing explicit `since <Month Year>` anchor required by v1.4 C3 | DIRECT_FIX | Added `"You have been his assistant since June 2024."` to the opening paragraph |
| F-003 | CRITICAL | F4 / C10 | AGENTS.md | Only 6 H2 sections; data-sharing policy buried as a single bullet under `## Safety & Escalation` | v1.4 requires a standalone 7th H2 `## Data Sharing Policy` with per-contact enumeration ending in a default-restrictive fallback | DIRECT_FIX | Added 7th H2 `## Data Sharing Policy` with per-contact rules for Simone, Terrell, Clarice, Marcus, Nina, Rachel, Dev, Dr. Torres, Dr. Walsh, Dr. Cho, plus the `"With anyone else: confirm with Larry first. When in doubt, share less."` fallback |
| F-004 | CRITICAL | F6 | TOOLS.md L5-L9 | `### General Agent Capabilities` heading plus three bullets (`memory_search`, Wide Research, Documents) | v1.4 forbids this heading; only `### Connected Services` H3 is permitted under `## Tool Usage` | DIRECT_FIX | Deleted `### General Agent Capabilities` heading and its three bullets; the 101 `-api` slugs were unaffected |
| F-005 | MAJOR | F7 | HEARTBEAT.md L9 and L17 | `### Weekly (Weekdays)` and `### Weekly (Weekend)` splits | v1.4 mandates a single consolidated `### Weekly` block, one bullet per day or day-block | DIRECT_FIX | Consolidated to a single `### Weekly` section; weekday and weekend items now share one block, one bullet per day-block |
| F-006 | MAJOR | A1 | MEMORY.md L116 vs TOOLS.md L94 | MEMORY: `"Portfolio site: Squarespace, with a Webflow staging mirror Terrell uses."`; TOOLS: `"Webflow: Read-only view of the portfolio site"` | Cross-file contradiction on portfolio platform; TOOLS is canonical | DIRECT_FIX | Rewrote MEMORY to `"Portfolio site: Webflow, maintained by Terrell."` |
| F-007 | MAJOR | A1 | MEMORY.md L144 vs TOOLS.md | MEMORY: `"HoneyBook: Connected for invoicing and contract status reads."`; TOOLS.md has no `honeybook-api` slug | Service asserted as connected with no matching `-api` slug in TOOLS.md | DIRECT_FIX | Moved HoneyBook to TOOLS.md `#### Not Connected` with explicit framing; reworded MEMORY entry to reference status via Stripe and Larry, not direct integration |
| F-008 | MAJOR | A1 | MEMORY.md L145 | `"Squarespace: Portfolio backend, read access."` | No `squarespace-api` slug exists in TOOLS.md; Connected Accounts entry is false | DIRECT_FIX | Removed the Squarespace entry from Connected Accounts |
| F-009 | MAJOR | C4 | MEMORY.md > Key Relationships | Inner-circle DOBs missing for mother, father, brother, best friend | C4 mandates full DOBs for parents, siblings, and designated best friend | DERIVE_FIX | Added plausible synthetic DOBs consistent with stated ages: Clarice March 14, 1968; Marcus July 8, 1965; Terrell May 22, 1997; Simone August 30, 1992 |
| F-010 | MAJOR | E7 | HEARTBEAT.md > Annual | No birthday entries for inner circle | E7 mandates inner-circle DOBs propagate as birthday entries into HEARTBEAT > Annual | DERIVE_FIX | Added five Annual entries: Nov 18 (Larry), Mar 14 (Clarice), Jul 8 (Marcus), May 22 (Terrell), Aug 30 (Simone) |
| F-011 | MINOR | A1 | MEMORY.md L62 (Finance) | `"Squarespace and HoneyBook: $45"` | Same Squarespace contradiction surfacing in the finance line | DIRECT_FIX | Rewrote line to `"Webflow Pro and HoneyBook: $45"` |

---

## Section 2 — Coherence Score

### Pre-fix

```
Score: 6.7 / 10
  - Cross-file alignment (A):        1.2 / 2.0   (F-006, F-007, F-008)
  - Overlapping / SoT (B):           1.0 / 1.0
  - Required-field completeness (C): 0.5 / 1.0   (F-002, F-009)
  - Factual and domain (D):          2.0 / 2.0
  - Mathematical (E):                0.7 / 1.0   (F-010)
  - Heading-structure (F):           0.8 / 2.0   (F-001, F-003, F-004, F-005)
  - Format-structure (F):            0.5 / 1.0   (TOOLS F6, AGENTS F4)
```

### Post-fix

```
Score: 10.0 / 10
  - Cross-file alignment (A):        2.0 / 2.0
  - Overlapping / SoT (B):           1.0 / 1.0
  - Required-field completeness (C): 1.0 / 1.0
  - Factual and domain (D):          2.0 / 2.0
  - Mathematical (E):                1.0 / 1.0
  - Heading-structure (F):           2.0 / 2.0
  - Format-structure (F):            1.0 / 1.0
```

---

## Section 3 — Remediation Log

| Finding ID | File | Change Type | Before | After | Justification |
|---|---|---|---|---|---|
| F-001 | IDENTITY.md | Rename H1 | `# Identity: Larry Rawlings's Assistant` | `# Identity: Larry Rawlings` | v1.4 F1 H1 pattern compliance |
| F-002 | IDENTITY.md | Insert tenure | (no since-date in opening paragraph) | `"You have been his assistant since June 2024."` | v1.4 C3 OpenClaw tenure statement |
| F-003 | AGENTS.md | Add 7th H2 | 6 H2 sections, data-sharing buried as one bullet under Safety and Escalation | 7 H2 sections including standalone `## Data Sharing Policy` with per-contact enumeration and default fallback | v1.4 F4 and C10 compliance |
| F-004 | TOOLS.md | Delete heading and bullets | `### General Agent Capabilities` + 3 bullets | Only `### Connected Services` H3 remains | v1.4 F6 forbids `### General Agent Capabilities` |
| F-005 | HEARTBEAT.md | Consolidate H3s | `### Weekly (Weekdays)` and `### Weekly (Weekend)` | Single `### Weekly` block | v1.4 F7 single Weekly mandate |
| F-006 | MEMORY.md | Replace text | `"Portfolio site: Squarespace, with a Webflow staging mirror Terrell uses."` | `"Portfolio site: Webflow, maintained by Terrell."` | Align MEMORY to TOOLS (canonical) per A1 |
| F-007 | TOOLS.md, MEMORY.md, AGENTS.md | Reframe | MEMORY: HoneyBook listed as Connected with status reads; AGENTS routing implied direct access | TOOLS `#### Not Connected` now includes HoneyBook with explanation; MEMORY entry references status via Stripe and Larry; AGENTS routing clarifies `"Not directly integrated"` | Service must not be claimed connected without a slug |
| F-008 | MEMORY.md | Remove entry | `"Squarespace: Portfolio backend, read access."` | (line removed) | No corresponding slug; portfolio is Webflow |
| F-009 | MEMORY.md | Add DOBs | Ages only for Clarice, Marcus, Terrell, Simone | Ages plus full DOBs (March 14, 1968 / July 8, 1965 / May 22, 1997 / August 30, 1992) | v1.4 C4 inner-circle DOB requirement |
| F-010 | HEARTBEAT.md | Add Annual bullets | No birthday entries | Five birthday bullets in `### Annual`, dates matching MEMORY DOBs | v1.4 E7 sync requirement |
| F-011 | MEMORY.md | Replace text | `"Squarespace and HoneyBook: $45."` | `"Webflow Pro and HoneyBook: $45."` | Consistency with F-006 |

---

## Section 4 — Open Questions for Human Input

No `REQUIRES_HUMAN_INPUT` findings remain. One optional confirmation surfaced:

```
Q1. (Optional) Confirm or override the synthetic inner-circle DOBs added in F-009.
    These were derived from stated ages, not from a source of truth.
    Answers (YYYY-MM-DD):
      Clarice Rawlings  : 1968-03-14
      Marcus Rawlings   : 1965-07-08
      Terrell Rawlings  : 1997-05-22
      Simone Aldridge   : 1992-08-30
    Override any value if you have real persona-source DOBs to enforce.
```

---

## Section 5 — Final Validation Sweep

All checks executed on the corrected files via PowerShell.

### File-level metrics

| File | Characters | Lines | Cap | Status |
|---|---|---|---|---|
| IDENTITY.md | 1,497 | 17 | 20,000 chars | PASS |
| SOUL.md | 3,066 | 35 | 20,000 chars | PASS |
| AGENTS.md | 8,164 | 77 | 20,000 chars | PASS |
| USER.md | 2,070 | 34 | 20,000 chars / 40 lines | PASS |
| TOOLS.md | 15,173 | 152 | 20,000 chars | PASS |
| HEARTBEAT.md | 3,297 | 56 | 20,000 chars | PASS |
| MEMORY.md | 14,908 | 163 | 15,000 target / 20,000 hard | PASS (under target) |
| **Total** | **48,175** | — | 140,000 | PASS |

### Heading inventory (post-fix)

- **IDENTITY.md**: 0 H2, 2 H3 (`### Nature`, `### Principles`) — PASS (F3)
- **SOUL.md**: 4 H2 (Core Truths, Boundaries, Vibe, Continuity) — PASS (F2)
- **AGENTS.md**: 7 H2 (Core Directives, Session Behaviour, Confirmation Rules, Communication Routing, Memory Management, Safety and Escalation, Data Sharing Policy) — PASS (F4)
- **USER.md**: 5 H2 (Basics, Background, Expertise, Preferences, Access and Authority) — PASS (F5)
- **TOOLS.md**: 1 H2 (`## Tool Usage`), 1 H3 (`### Connected Services`), 12 H4 categories plus `#### Not Connected` — PASS (F6)
- **HEARTBEAT.md**: 2 H2 (Recurring Events, Upcoming Events and Deadlines), 6 H3 (Daily, Weekly, Monthly, Quarterly, Seasonal / Variable, Annual) — PASS (F7)
- **MEMORY.md**: 11 H2 in canonical order (Personal Profile, Key Relationships, Work and Projects, Finance, Health and Wellness, Interests and Hobbies, Home and Living, Devices and Services, Contacts, Connected Accounts, Preferences) — PASS (F8)

### TOOLS.md API count (E6)

- Total `-api` slug occurrences: **101**
- Unique `-api` slugs: **101**
- All 101 canonical slugs present exactly once: **True**
- Slugs missing from canonical list: **0**
- Slugs not in canonical list: **0**

### Strict requirement: all 101 APIs Connected

- All 101 `-api` slugs live under `### Connected Services` H4 categories
- `#### Not Connected` contains zero `-api` slugs; only real-world capability gaps (live web search and browsing, Adobe Creative Cloud, HoneyBook direct writes, Ally and Chase banking writes, work email, client-internal systems, family-member accounts)
- Verified by canonical-list diff: **0 missing, 0 extras** — strict requirement satisfied

### Punctuation and forbidden-token sweeps

- Em dash (U+2014), en dash (U+2013), horizontal bar (U+2015): **0 hits** across all 7 files
- `shopify`, `fintrack`, `todoist`, `via mock`: **0 hits** across all 7 files

### Cross-file alignment spot checks (A1)

| Fact | TOOLS.md | MEMORY.md | AGENTS.md | Status |
|---|---|---|---|---|
| Portfolio site platform | `webflow-api` (read-only) | "Portfolio site: Webflow, maintained by Terrell" | — | Aligned |
| HoneyBook | `#### Not Connected` with framing | "Larry uses it directly; assistant references via Stripe and from Larry" | Routing: "Not directly integrated" | Aligned |
| Banking | Plaid read-only | "Read-only via Plaid for balances and transactions. No transfer rights." | — | Aligned |
| Work email | `#### Not Connected` | "Used by Larry... not connected to OpenClaw" | Routing: "Not connected. Drafts prepared for Larry to send manually." | Aligned |
| Adobe CC | `#### Not Connected` | "Adobe Creative Cloud" listed as a paid subscription, never claimed connected | — | Aligned |
| Therapy cadence | — | "Biweekly telehealth with Dr. Angela Torres, Tuesdays at 5:00 PM" | "Tuesday 5:00 PM therapy... protected" | Aligned |
| Yoga days | — | "Yoga two to three times per week (Monday, Wednesday, Friday mornings)" | "Monday and Friday yoga blocks... protected" + HEARTBEAT Weekly Mon/Wed/Fri | Aligned |
| Financial threshold | — | — | `"$100 USD"` (AGENTS) matches USER.md Access and Authority `"$100 USD"` | Aligned |

### Required-field completeness (C)

- C1: DOB in USER.md > Basics — November 18, 1992 (Oct-Mar window) — PASS
- C2: Age 33, timezone America/New_York, location NoDa Charlotte NC — PASS
- C3: IDENTITY.md opening tenure `"since June 2024"` — PASS
- C4: Inner-circle DOBs in MEMORY.md > Key Relationships — PASS (post F-009)
- C5: Continuous timeline, marketing job to freelance at 29, no unexplained gap — PASS
- C6: B.A. Communications, UNC Greensboro, 2015, Minor Studio Art — PASS
- C7: Escalation contacts named (Dr. Walsh, Dr. Torres, Dr. Cho, Rachel) with phones in MEMORY > Contacts; persona is under 50 so ICE / POA not mandatory — PASS
- C8: Confirmation Rules opens with `$100 USD` financial threshold bullet, no tautological self-conversion — PASS
- C9: `**Default for everything else**: proceed with judgment.` present — PASS
- C10: Standalone `## Data Sharing Policy` with per-contact enumeration and default fallback — PASS (post F-003)

### Factual and domain checks (D)

- D1: API surfaces appropriate for a freelance photographer in the US South — PASS
- D2: All connected services available in the US; all phone numbers in `XXX-XXX-XXXX` US format — PASS
- D3: No specific holiday-anchored dates require calendar verification; Thanksgiving Nov 26, 2026 = Thursday (correct) — PASS
- D4: Black Southern identity consistent across IDENTITY, SOUL, MEMORY; no overstated heritage claims — PASS
- D5: No eligibility misclaims (no veteran grants, no professional-license claims) — PASS
- D6: Brand names verified — Adobe Creative Cloud, Spotify, MacBook Pro, Sony A7 IV, Subaru Crosstrek, Ring, Ally Bank, Webflow, HoneyBook, all spelled correctly — PASS
- D7: Tool-occupation justifications hold for each connected service, including Terrell-maintained dev/ops tools (GitHub, Linear, Sentry, Datadog, Cloudflare, Kubernetes, PagerDuty) where Larry has read-only access only — PASS
- D8: No one-time events filed under Recurring; no active subscriptions for ended services — PASS

### Mathematical checks (E)

- E1: Age 33 from DOB Nov 18, 1992 against anchor Oct 1, 2026: 33 years 10.5 months — consistent — PASS
- E2: Marketing job left at 29 (around 2022) to freelance since then; OpenClaw tenure June 2024 falls inside the freelance era — PASS
- E3: All currency in USD; numbers locally plausible for Charlotte NC — PASS
- E4: Monthly expenses itemized; sum (rent 1350 + utilities 170 + groceries/dining 400 + HelloFresh 160 + car payment 380 + car insurance 140 + gas 100 + Adobe 55 + Webflow/HoneyBook 45 + yoga 90 + therapy 80 + streaming 30 + student loan 180 = $3,180) plus discretionary savings target $300 fits within $4,500 average monthly income — PASS
- E5: Family timeline consistent — Clarice (1968) and Marcus (1965) had Larry (1992) at ages 24 and 27 respectively; Terrell (1997) follows 5 years later. All plausible. — PASS
- E6: TOOLS.md exact-count gate: 101 / 101 — PASS
- E7: HEARTBEAT > Annual birthdays match MEMORY > Key Relationships DOBs month-and-day exactly — PASS

### Structure (F)

- F1: All 7 H1 titles follow `# <FileName>: Larry Rawlings` — PASS
- F2-F8: Per heading inventory above — PASS
- F9: Section order matches canonical spec across all 7 files — PASS
- F10: All character and line caps respected — PASS
- F11: No mandatory heading left empty without `- None recorded.` placeholder (none required — all populated) — PASS

---

## Section 6 — Cross-Persona Pattern Flags

The following defects are likely to recur across the sibling personas in `c:\Users\Lenovo\Desktop\Newly_create\` (laura-mitchell, linda-cruz, lisa-reyes, luz-castillo, marcus-bennett, margit-moss, maria-bennett, maria-sandoval, mark-campbell) since they were generated from the same prompt version. Flagged SYSTEMIC for cohort-level remediation:

- **SYSTEMIC** F-001 equivalent — `# Identity: <Name>'s Assistant` H1 pattern (v1.4 removes the suffix). Recommend scripted rename across the cohort.
- **SYSTEMIC** F-003 equivalent — `## Data Sharing Policy` missing as the 7th AGENTS.md H2. Recommend cohort-wide insertion with per-contact enumeration.
- **SYSTEMIC** F-004 equivalent — `### General Agent Capabilities` heading in TOOLS.md (v1.4 forbids it). Recommend scripted deletion of the heading and the `memory_search` / Wide Research / Documents bullets across the cohort.
- **SYSTEMIC** F-005 equivalent — `### Weekly (Weekdays)` and `### Weekly (Weekend)` HEARTBEAT.md splits. Recommend scripted consolidation across the cohort.

These four template-level defects can be remediated as a batch on the sibling personas with the same fix patterns applied here.

---

## Section 7 — Files Modified

All under `c:\Users\Lenovo\Desktop\Newly_create\larry-rawlings\`:

- `IDENTITY.md` — H1 renamed, tenure since-date added
- `AGENTS.md` — `## Data Sharing Policy` added as 7th H2 with per-contact enumeration
- `TOOLS.md` — `### General Agent Capabilities` removed; HoneyBook added to `#### Not Connected`
- `HEARTBEAT.md` — Weekly consolidated; five Annual birthday bullets added
- `MEMORY.md` — Inner-circle DOBs added; Webflow / HoneyBook alignment with TOOLS.md; finance line corrected
- `SOUL.md` — unchanged (no defects found)
- `USER.md` — unchanged (no defects found)

---

## Final Checklist (per §9 of QC prompt)

- [x] Every check in §5 (MODES A-F) was run, including those that passed
- [x] MODE F (heading-structure) cross-checked against `7FILE_GENERATION_PROMPT.md`
- [x] AGENTS.md contains all 7 H2 sections including `## Data Sharing Policy` as the seventh, with per-contact enumeration
- [x] TOOLS.md contains NO `### General Agent Capabilities` heading; only `### Connected Services` H3 is present
- [x] TOOLS.md was verified to contain exactly 101 unique `-api` slugs
- [x] USER.md was verified to be 34 lines (cap 40)
- [x] Every finding has a verbatim quote and file:section
- [x] Every finding has a severity tag
- [x] Every finding has a Fix Type (DIRECT_FIX or DERIVE_FIX; no REQUIRES_HUMAN_INPUT remaining)
- [x] No finding has both "fix" and `REQUIRES_HUMAN_INPUT`
- [x] Corrected files re-pass §5 MODE A (alignment), MODE B (overlap), and MODE F (structure)
- [x] No new contradictions introduced
- [x] Coherence score justified by the rubric
- [x] All optional human-confirmation items surfaced (Q1)
- [x] Cohort SYSTEMIC tags applied and template-level recommendations surfaced
- [x] README.md was NOT audited (out of scope under v1.3)

**Audit complete. Persona is deployment-ready.**
