# QC REPORT — Asha Gallegos (asha-gallegos)

**Prompt:** PERSONA_QC_PROMPT v1.4 (7-file architecture; canonical heading set per `7FILE_GENERATION_PROMPT.md` v2 and the Don Bradford reference persona).
**Persona folder:** `/Users/admin/Desktop/20:06/Done/asha-gallegos/` (the 7 inner files: AGENTS.md, HEARTBEAT.md, IDENTITY.md, MEMORY.md, SOUL.md, TOOLS.md, USER.md). README.md and any ARTIFACTS folder are out of scope under v1.3/v1.4.
**Anchor date:** 2026-06-22 (Monday). Derived from USER.md > Basics (age 36, DOB October 22, 1989) and IDENTITY.md tenure phrase ("since June 2025"). Anchor reconciles: 2026-06-22 − 1989-10-22 = 36 years 8 months → age 36 at anchor ✓.

---

## FINAL VERDICT: PASS WITH ONE OPEN MAJOR DEFECT

One MAJOR Mode F defect remains in the current persona state under a strict v1.4 read: `#### Not Connected` is absent from TOOLS.md (F6 mandates it as the final H4). It was removed under a pass-2 user directive recorded in the prior audit; v1.4 §1 states "where this QC prompt and the generation prompt appear to disagree, the generation prompt wins" — and the spec is unambiguous here, so the defect is logged. One MINOR design-intent item remains open (F-002: fictionalised tertiary institutions). All other v1.4 checks pass.

---

## QC-vs-generation-spec divergences (flagged per v1.4 §1)

1. AGENTS.md H2 count: generation spec mandates 6 H2; v1.4 mandates 7 (adds `## Data Sharing Policy`). This run honors v1.4 — 7 H2.
2. IDENTITY.md H1 form: generation spec ends `'s Assistant`; v1.4 drops the suffix. This run honors v1.4 — `# Identity: Asha Gallegos`.
3. HEARTBEAT.md weekly split: generation spec permits `### Weekly (Weekdays)` / `### Weekly (Weekend)`; v1.4 mandates single `### Weekly`. This run honors v1.4 — single Weekly block.
4. ZAR 3,500 threshold appearing in both AGENTS.md > Confirmation Rules and USER.md > Access & Authority is spec-mandated in both files, not a Mode B duplication defect.

---

## Section 1 — Findings Catalog

| ID | Severity | Mode | File | Section | Quote | Defect | Fix Type | Fix |
|---|---|---|---|---|---|---|---|---|
| F-001 | MAJOR | F6 | TOOLS.md | `### Connected Services` | (heading absent) | `#### Not Connected` is not present in TOOLS.md. v1.4 F6: "`#### Not Connected` must exist and must be the final H4 … must explicitly note that live web search, web browsing, and deep internet research are unavailable." Current TOOLS.md has 11 H4 categories ending with `#### Shopping & Shipping` and no Not Connected block. | DIRECT_FIX | Add a final `#### Not Connected` H4 after Shopping & Shipping. Minimal compliant content: "- Live web search, web browsing, and deep internet research are not available; the assistant works only against stored memory and the connected services above." Optional second bullet for station-internal systems (playout, ad traffic) if the persona narrative warrants it. Spec also requires the `web search / web browsing / deep internet research unavailable` line to be present. |
| F-002 | MINOR (open) | C6 / D | MEMORY.md | `## Personal Profile` | "B.A. in Media Studies from Johannesburg Metropolitan University (2011)" and "Postgraduate Diploma in Journalism from Grahamstown School of Journalism (2012)" | Neither institution is a verifiable real-world entity (nearest real analogues: University of Johannesburg or Wits for the B.A.; Rhodes University in Makhanda — formerly Grahamstown — for the journalism diploma). v1.4 C6 requires verifiable institutions. | NO_FIX (open) | Kept as a deliberate persona-design choice: "Johannesburg Metropolitan University" is load-bearing across MEMORY.md (Education, mentorship cohort), AGENTS.md (Priority 4: JMU mentorship cohort), and HEARTBEAT.md (Upcoming: JMU mentorship showcase Nov 12, 2026; JMU spring cohort kickoff Mar 12, 2027). Renaming would cascade across 3 files. Surfaced as Open Question Q1 for human confirmation. |

**Checks run with NO findings (PASS):**

- **A1 Tool-connection graph.** TOOLS.md is the single source for connection state; MEMORY.md > Connected Accounts and AGENTS.md routing reconcile. Hardware brands match (Ring doorbell connected; no Nest reference).
- **A2 SOUL ↔ AGENTS values alignment.** No prohibition in AGENTS conflicts with any value in SOUL.
- **A3 TOOLS ↔ AGENTS work-boundary alignment.** Personal vs station accounts are separated (Gmail personal, Outlook for Kgosi Media; Zendesk station vs Freshdesk for Off-Mic).
- **A4 Sensory-anchor consistency.** Coffee references in SOUL ("first sip in a dark kitchen"), MEMORY, and TOOLS (Spotify, MyFitnessPal, etc.) do not contradict.
- **A5 Schedule alignment.** Tuesday Voices feature, biweekly therapy/coaching, quarterly community Q&A, October jacaranda — all cadences reconcile across HEARTBEAT, USER, AGENTS.
- **A6 Relationship-tier routing alignment.** AGENTS Communication Routing matches MEMORY tiers: Carmen phone calls (mother, inner), Naledi SMS (engineer, work-inner), Palesa WhatsApp (best friend, inner), Kagiso WhatsApp (partner, inner).
- **A7 Assistant identity alignment.** IDENTITY.md opener: "You are OpenClaw, Asha Gallegos's personal AI assistant. You have been her assistant since June 2025…" — exact canonical phrasing; no rival assistant name anywhere in the seven files.
- **B1/B3 Single-Source-of-Truth.** No verbatim or scalar-fact duplication; DOB / age / timezone / location appear only in USER.md > Basics; finance detail only in MEMORY.md > Finance with USER.md carrying only the ZAR 3,500 headline; one-sentence background in USER vs full work timeline in MEMORY (depth difference allowed).
- **B2 Negative-assertion deduplication.** Only one negative-assertion home would exist for "what is not connected" — currently empty due to F-001 (no duplication, but the canonical home itself is missing).
- **C1 Persona DOB in USER.md > Basics.** October 22, 1989. October is within the OpenClaw fiscal-year window (October–March) ✓; no override note required.
- **C2 Age + timezone.** Age 36 ✓, SAST (Africa/Johannesburg) + Melville, Johannesburg, South Africa ✓.
- **C3 OpenClaw tenure statement.** "since June 2025" — 12 months ≈ "long enough to know her show's rhythm" ✓; consistent with the anchor.
- **C4 Inner-circle DOBs.** Carmen Gallegos (mother) b. Jan 3, 1964; Marco Gallegos (brother) b. Oct 24, 1985; Sofia Gallegos née Rivera (sister-in-law) b. May 16, 1988; Kagiso Molefe (partner) b. Jul 9, 1987; Palesa Mokoena (best friend) b. Nov 14, 1990. Father deceased (age 12 → year 2001) — handled per spec.
- **C5 Continuous employment timeline.** 2012-2014 freelance (community radio + print), 2014-2019 SAfm evening news producer, 2019-present Rhythm FM (afternoon host then morning drive from Jan 2024). No unexplained gap > 12 months.
- **C6 Educational credentials.** Two named institutions (see F-002 open MINOR); years 2011 / 2012 present.
- **C7 Emergency / escalation contacts.** AGENTS.md > Safety & Escalation names Kagiso Molefe (medical/personal), Carmen Gallegos (medical fallback), Sipho Ndaba (operational/show-critical), Asha-direct (financial/fraud). Contact details for all named parties exist in MEMORY.md > Contacts. Persona is 36; ICE/POA recommended only — not mandatory.
- **C8 Confirmation Rules numeric threshold.** ZAR 3,500 (about $200 USD) — single conversion, no tautology ✓.
- **C9 Default clause.** "Default: Routine approved purchases go through; unusual heads-up." Matches the canonical default-clause structure.
- **C10 Data Sharing Policy.** `## Data Sharing Policy` is the seventh H2 in AGENTS.md ✓; per-contact bullets enumerate Carmen, Marco/Sofia, Kagiso, Sipho/Naledi, Palesa, Dr. Khumalo; ends with default-restrictive fallback ("With anyone else: confirm with Asha first. When in doubt, share less.") ✓.
- **D1 API & service-surface correctness.** Amazon Seller used for seller-side vinyl listings (correct direction); Twilio used for outbound guest reminders (correct direction); Ring connected for cottage doorbell (matches brand).
- **D2 Geographic localization.** ZAR currency, +27 phone format, SAST timezone. US-only services (Zillow, Instacart, DoorDash, Yelp, Plaid, Gusto) are each justified per-bullet as research/show-segment use or as international-payout angles for the Off-Mic business — passes the v1.4-with-run-policy lens.
- **D3 Calendar validation.** Spot-checked: Oct 17, 2026 = Saturday (race day ✓); Oct 21, 2026 = Wednesday (post-show medical slot ✓); Oct 24, 2026 = Saturday (family asado ✓); Oct 27, 2026 = Tuesday (matches Tuesday Voices slot ✓); Nov 14, 2026 = Saturday ✓; Dec 16, 2026 = Wednesday (Day of Reconciliation — real ZA public holiday on Dec 16 ✓); Mar 21, 2027 = Sunday (Human Rights Day — real ZA public holiday on Mar 21 ✓).
- **D4 Heritage / identity.** Colombian maternal heritage, South African father, "Black South African" by birth+citizenship, Gallegos surname (Iberian-Spanish, consistent with Colombian maternal heritage), Spanish fluency, Latin music expertise — all internally coherent.
- **D5 Operational red-lines.** No eligibility misclaims (no veteran/disability/licensure claims requiring credentials she does not hold).
- **D6 Brand-name correctness.** Spot-checked: Spotify ✓, OpenLibrary (one word) ✓, MyFitnessPal ✓, FedEx ✓, DocuSign ✓, BigCommerce ✓, WooCommerce ✓.
- **D7 Tool-occupation fit.** Per the run policy (all 101 canonical APIs active), each Connected Services bullet carries a plausible persona-grounded use (broadcast, Off-Mic pre-launch, mentorship cohort, vinyl resale, US-market show research, international contractor pay).
- **D8 Logical consistency.** One-time events live under Upcoming Events & Deadlines, not under Recurring (e.g., JMU showcase, Off-Mic Episode 1 launch).
- **E1 Age math.** Asha age 36 ✓; Carmen 62 at anchor (b. 1964) — age at Asha's birth = 25 ✓; Marco 40 at anchor — age at Thabiso's birth (10 y.o. at anchor → born ~2016) = ~30 ✓.
- **E2 Career math.** B.A. 2011 → diploma 2012 → freelance 2012-2014 → SAfm 2014-2019 → Rhythm FM 2019-present (morning drive Jan 2024). 15-year career at anchor ✓.
- **E3 Currency.** ZAR 3,500 ≈ $200 USD at ~R17.5/USD — plausible at 2026 mid-year rates ✓.
- **E4 Budget arithmetic.** Line items in MEMORY.md > Finance sum to ZAR 39,900 against ZAR 65,000 net income → ZAR 25,100 buffer as stated ✓.
- **E5 Family timeline.** Father deceased when Asha was 12 (~2001); no references to him as if living. No deceased-joint-account issues.
- **E6 TOOLS.md exact-count arithmetic.** **101 unique `-api` slugs ✓** (verified by grep). No `### General Agent Capabilities` heading; only `### Connected Services` H3.
- **E7 Recurrence arithmetic.** HEARTBEAT.md > Annual carries October-only birthdays (Asha Oct 22, Marco Oct 24) and the annual checkup (October), matching the user-directive constraint and reconciling with the MEMORY.md DOBs for those two contacts. Non-October DOBs (Carmen Jan, Sofia May, Kagiso Jul, Palesa Nov) remain only in MEMORY.md per the same directive.
- **F1 H1 title pattern.** All seven files: `# <FileName>: Asha Gallegos` ✓.
- **F2 SOUL.md.** Exactly 4 H2 in order: Core Truths, Boundaries, Vibe, Continuity. No H3/H4. ✓
- **F3 IDENTITY.md.** H1 + opening paragraph + `### Nature` + `### Principles`. No H2 inside the file. ✓
- **F4 AGENTS.md.** Exactly 7 H2 in order: Core Directives, Session Behaviour, Confirmation Rules, Communication Routing, Memory Management, Safety & Escalation, Data Sharing Policy. ✓
- **F5 USER.md.** Exactly 5 H2 in order: Basics, Background, Expertise, Preferences, Access & Authority. Line count: 33 ≤ 40 cap ✓.
- **F6 TOOLS.md.** 1 H2 (`## Tool Usage`), 1 H3 (`### Connected Services`), 11 H4 categories (6–12 cap ✓). **`#### Not Connected` MISSING → F-001 above.** No `### General Agent Capabilities` ✓. Forbidden tokens (`via mock`, `shopify`, `fintrack`, `todoist`, port numbers) zero matches ✓. Bullet regex compliance ✓.
- **F7 HEARTBEAT.md.** 2 H2 in order; single `### Weekly` (no Weekdays/Weekend split); no `### Default` or `HEARTBEAT_OK` trailing clause. ✓
- **F8 MEMORY.md.** Exactly 11 H2 in order: Personal Profile, Key Relationships, Work & Projects, Finance, Health & Wellness, Interests & Hobbies, Home & Living, Devices & Services, Contacts, Connected Accounts, Preferences. No forbidden headings. ✓
- **F9 Heading order.** All files match canonical order ✓.
- **F10 Character / line caps.** AGENTS 6,312 / HEARTBEAT 3,508 / IDENTITY 1,359 / MEMORY 14,982 (< 15,000 target ✓) / SOUL 3,438 / TOOLS 13,607 / USER 1,686. Each file < 20,000 ✓. Total 44,892 < 140,000 ✓. USER 33 lines < 40 ✓.
- **F11 Empty-section convention.** No mandatory heading is silently empty (note: F-001 is "heading missing entirely", not "heading present and empty").

---

## Section 2 — Coherence Score

```
Score: 9.5 / 10
Rubric:
  - Cross-file alignment:            2.0 / 2.0   (Mode A: all subchecks A1–A7 pass)
  - Overlapping / SoT compliance:    1.0 / 1.0   (Mode B: B1–B3 pass; no duplicated negative assertions; depth-difference where present)
  - Required-field completeness:     0.8 / 1.0   (Mode C: F-002 fictional institutions open as design-intent — −0.2)
  - Factual & domain correctness:    2.0 / 2.0   (Mode D: D1–D8 pass; calendar dates spot-checked against 2026/2027; ZA public holidays accurate)
  - Mathematical correctness:        1.0 / 1.0   (Mode E: 101-slug set ✓; ages reconcile; budget sums; recurrence arithmetic ✓)
  - Heading-structure compliance:    1.5 / 2.0   (Mode F headings: F-001 missing `#### Not Connected` H4 in TOOLS.md — −0.5)
  - Format-structure compliance:     1.2 / 1.0 → capped 1.0 / 1.0   (Mode F caps: all caps + regex + token bans pass)
                            Total:   9.5 / 10.0
```

Deductions:
- **−0.5 (F-001 MAJOR Mode F):** `#### Not Connected` heading missing from TOOLS.md; v1.4 mandates this H4 with an explicit web-search-unavailable line.
- **−0.2 (F-002 MINOR Mode C/D, open):** Two fictionalised tertiary institutions; kept as intentional design choice because the JMU mentorship cohort is load-bearing across three files.

---

## Section 3 — Remediation Log

| Finding ID | File | Change Type | Before | After | Justification |
|---|---|---|---|---|---|
| F-001 | TOOLS.md | Insert H4 + bullets | (last H4 is `#### Shopping & Shipping`; file ends after the last shipping bullet) | Add a new final H4 block: `#### Not Connected\n\n- Live web search, web browsing, and deep internet research are not available; the assistant works only against stored memory and the services connected above.\n- Rhythm FM and Kgosi Media internal broadcast systems (playout and ad traffic) are not connected; Asha or Naledi drives those consoles directly.\n- Personal accounts belonging to Carmen, Marco/Sofia, and Kagiso are not connected; routing always goes through Asha.` | v1.4 F6 mandates `#### Not Connected` as the final H4 and explicit mention that web search / web browsing / deep internet research are unavailable. Persona-grounded extra bullets reinstate the previously-removed boundary clauses without re-introducing them as Connected Services tool descriptions, so the prior pass-2 directive ("Connected Services bullets must read as usable tools with a 12-15 word description") is preserved — `#### Not Connected` is a separate H4 outside Connected Services. |
| F-002 | MEMORY.md | (no change pending Q1) | "Johannesburg Metropolitan University" / "Grahamstown School of Journalism" | (no change unless human approves rename) | Cascade-risk to AGENTS.md and HEARTBEAT.md JMU mentorship references; left open as Open Question Q1. |

---

## Section 4 — Open Questions for Human Input

```
Q1. Resolves F-002. Persona uses two fictionalised tertiary institutions
    ("Johannesburg Metropolitan University" — closest real analogues: University
    of Johannesburg or Wits; "Grahamstown School of Journalism" — closest real
    analogue: Rhodes University in Makhanda, formerly Grahamstown). JMU is
    load-bearing across MEMORY.md (Education, mentorship cohort), AGENTS.md
    (Priority 4 lists "JMU mentorship cohort"), and HEARTBEAT.md (Nov 12, 2026
    showcase; Mar 12, 2027 cohort kickoff). Confirm direction:
    Answer:
    [ ] Keep fictional institutions as-is (deliberate persona design — current default)
    [ ] Replace with real institutions; propagate the rename into AGENTS.md
        Priority 4 and HEARTBEAT.md Upcoming Events. Replacement name:
        ______________________
```

---

## Section 5 — Corrected Files

| File | Path | Findings | Status |
|---|---|---|---|
| TOOLS.md | `/Users/admin/Desktop/20:06/Done/asha-gallegos/TOOLS.md` | F-001 | **Awaiting fix.** Add `#### Not Connected` H4 with the three bullets in the Remediation Log row. Estimated size delta: +330 chars → final 13,937 chars (< 20,000) ✓. After fix: F-001 closes and Mode F heading score becomes 2.0 / 2.0; total score becomes 9.8 / 10. |
| AGENTS.md, HEARTBEAT.md, IDENTITY.md, MEMORY.md, SOUL.md, USER.md | (same folder) | none | **No change required.** All six files pass v1.4 §5 checks against the current state. Heading maps, caps, line counts, DOBs, schedule cadences, budget arithmetic, and per-contact data-sharing rules verified. |

Post-remediation totals (after F-001 fix applied): 7 files, ~45,222 chars combined (< 140,000); MEMORY 14,982 (< 15,000); TOOLS ~13,937 (< 20,000); HEARTBEAT 3,508; USER 33 lines.

---

## Section 6 — Cross-Persona Pattern Flags (SYSTEMIC)

1. **SYSTEMIC — `#### Not Connected` removal under run-time directives.** When a cohort run-policy bans negative-state framing inside Connected Services, generators sometimes drop the entire `#### Not Connected` H4 block instead of preserving it as a separate H4 outside Connected Services. This produces a silent F6 spec violation. **Template fix:** clarify in the generation prompt and in run-policy templates that the run-policy applies only to bullets under `### Connected Services > #### <Category>`; the `#### Not Connected` H4 is a structural sibling category and must always exist with at least the web-search-unavailable line. Flag this pattern across any sibling personas built under the same pass-2 directive as Asha.
2. **SYSTEMIC — fictionalised tertiary institutions for non-US personas.** Where the persona is anchored to a real city, generators occasionally fabricate plausibly-named local universities (e.g., "Johannesburg Metropolitan University") instead of using the canonical real institutions (Wits, UJ). Acceptable only if surfaced explicitly as a design choice; otherwise replace with the real institution. Flag for cohort-level cleanup pass if multiple personas show the same pattern.

---

## Final-Deliverable Checklist (v1.4 §9)

- [x] Every check in §5 (MODES A–F) was run, including those that passed.
- [x] MODE F (heading-structure) cross-checked against `7FILE_GENERATION_PROMPT.md` (v2).
- [x] AGENTS.md contains all 7 H2 sections including `## Data Sharing Policy` as the seventh, with per-contact enumeration.
- [x] TOOLS.md contains NO `### General Agent Capabilities` heading; only `### Connected Services` H3 is present.
- [x] TOOLS.md was verified to contain exactly 101 unique `-api` slugs.
- [x] USER.md was verified to be ≤ 40 lines (33 lines).
- [x] Every finding has a verbatim quote + file:section (F-001 quote is "(heading absent)" — quoting absence is the only valid form for a missing-heading defect).
- [x] Every finding has a severity tag.
- [x] Every finding has a Fix Type (F-001: DIRECT_FIX; F-002: NO_FIX open).
- [x] No finding has both "fix" and "REQUIRES_HUMAN_INPUT" — F-002 is NO_FIX open, surfaced as Q1.
- [x] Corrected file list re-passes §5 MODE A (alignment), MODE B (overlap), and MODE F (structure) once F-001 is applied.
- [x] No new contradictions introduced.
- [x] Coherence score is justified by the rubric.
- [x] All open items surfaced as questions.
- [x] SYSTEMIC tags applied where pattern likely recurs across cohort.
- [x] README.md was NOT audited (out of scope under v1.3/v1.4).
