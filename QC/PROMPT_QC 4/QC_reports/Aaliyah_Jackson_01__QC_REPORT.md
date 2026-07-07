# PROMPT QC REPORT -- Aaliyah_Jackson_01

- **Artifact under test:** `Aaliyah_Jackson_01/PROMPT.md`
- **Persona files supplied:** USER, IDENTITY, TOOLS, MEMORY, HEARTBEAT, SOUL, AGENTS (7 files)
- **Judgment packet:** `PROMPT_QC/_qc_packets/Aaliyah_Jackson_01__QC_PACKET.md`
- **OVERALL VERDICT:** **FAIL (blocking)** -- does not clear to bundle creation

---

## 1. Deterministic gate (`prompt_qc.py` via `run_qc.py`)

```
TASK: Aaliyah_Jackson_01            FAIL
artifact: PROMPT.md   turns: 1

  [FAIL] C#21 temporal [BODY]: relative time word 'today' near ..., and the budget review today. Cross check each...
  [FAIL] C#21 temporal [BODY]: relative time word 'this afternoon' near ...ne thirty and meal prep this afternoon. Maya is...
  [FAIL] C#21 temporal [BODY]: relative time word 'this afternoon' near ...those out clearly.  For this afternoon I want a...
  [FAIL] C#21 temporal [BODY]: weekday name 'monday' near ...am wearing the old pair Monday.  While you are i...
  [FAIL] C#21 temporal [BODY]: weekday name 'saturday' near ...offered to take Maya on Saturday morning before...
  [FAIL] D#27 turn-header: line 1 looks like a turn header but is not the exact form '--- TURN N ---':
         '--- TURN T1 (Day 1, Sunday, November 1, 2026, 08:00 CT) ---'
  ... plus 2 WARN (form band) -- non-blocking
```

**Gate result: FAIL** (FAIL=6, MAJOR=0, WARN=2)

WARN details (non-blocking):
- `D#24 heavy-word-band` -- heaviest turn is 1012 words, above the 800-1000 band.
- `D#23 one-paragraph` -- body structure flagged (blank line / file structure).

---

## 2. Judgment pass (PROMPT_QC.md rubric -- LLM reviewer, Mode 1)

```
PROMPT QC -- JUDGMENT PASS
artifact: Aaliyah_Jackson_01/PROMPT.md

C-context. Nothing the agent already has
  C11a  FAIL  -- Restates context the agent holds: names the current inbox groups, tells it the newer daycare note supersedes, points it at "my working files" for budget plan, meal-prep notes, and the house-project list.
  C11b  PASS  -- States WHAT is wanted (sort inbox, walk the month, reconcile October, build cart) as intent; leaves the HOW to the agent's judgment.
  C11c  FAIL  -- Directs the agent to specific storage locations repeatedly ("my working files", "my documents", "the daycare paperwork from earlier this year should be in there"); a persona pointing at where files live is a soft path dictation.

A. Domain and Framing
  A1  PASS  -- Sits cleanly in one Personal domain (working-parent household logistics), no blur into professional/enterprise.
  A2  PASS  -- Opens on the outcome ("build me one clean planning page") not a preamble.
  A3  PASS  -- Reads as one coherent owned job: get the family side of November sorted before church and meal prep.

B. Difficulty Visible
  B1  PASS  -- Many independent surfaces at once: inbox, calendar, banking, grocery, reservations, weather, maps, task board, documents, shipping.
  B2  PASS  -- A single linear thread could not comfortably do inbox triage + month collision check + monthly reconciliation + cart build + lookups in sequence; visibly demands fan-out.
  B3  MAJOR -- References a full unread inbox, a whole month's calendar, and October checking activity, but object counts read as dozens not hundreds; scale is real but modest for the "large object population" bar.
  B4  PASS  -- Well beyond two deliverables: planning page plus multiple drafts (inbox replies, Loretta text, grocery cart, task-board entries, coffee booking).
  B5  PASS  -- Non-trivial analysis: total posted vs pending, leftover after bills, flag anomalies, cross-source tuition reconciliation.
  B6  PASS  -- Expects verifying against more than one source (calendar vs newer note, new statement vs prior paperwork) and holding an open conclusion on the fibroid, stated as judgment.
  B7  PASS  -- Read honestly, a competent human needs well over 8 to 10 hours to do all of this well with the evidence trail demanded.

E. Voice and Originality
  E1  PASS  -- Sounds like this specific nurse-mother dictating in a small window before church; warm, clipped, concrete.
  E2  PASS  -- Fresh specifics tied to this persona: Maya's checkup, Magnolia Table brunch, fibroid follow-up, Kroger meal prep, Loretta pickup.
  E3  PASS  -- Consistent with persona files without lifting phrasing verbatim; toddler-meal signal, house projects, brunch spot all align with MEMORY without copying it.

G. Secrecy of the Test
  G1  PASS  -- The conflicting values (stale calendar time vs newer note, superseded tuition figure) are named as tensions to resolve but the correct values are never revealed.
  G2  PASS  -- The unrecognized charge and membership upsell are surfaced as things to "call out" without flagging which is the decoy or its resolution.
  G3  PASS  -- Red lines (approval gates, no-invented-reservation) are implied by intent ("say so plainly instead of inventing"), never named as rules.
  G4  PASS  -- No answer values leaked: no tuition amount, no leftover figure, no correct appointment time stated.
  G5  PASS  -- Judgment framed as intent ("tell me plainly which one is stale and where the right time came from"), not a numbered procedure.

H. Persona Alignment
  H1  PASS  -- Every surface is one Aaliyah plausibly owns: household inbox, family calendar, joint budget, grocery, Maya's daycare paperwork, her own follow-up.
  H2  PASS  -- Every implied surface maps to a connected service in TOOLS.md: Gmail, Google Calendar, Drive, Instacart/Kroger, Plaid/Regions checking, FedEx/UPS, OpenWeather, Google Maps, WhatsApp (Loretta), Trello (playset/garage), Calendly (Brianna), Typeform/DocuSign (daycare survey/enrollment). No work implied on a disconnected service.
  H3  PASS  -- Stakes and scale match a working RN running a tight household budget; no seniority mismatch.
  H4  PASS  -- Focal event fits her live situation: HEARTBEAT confirms Maya checkup, Nov 14 brunch, Nov 18 fibroid follow-up, 1st-of-month budget review, Sunday meal prep.
  H5  PASS  -- Names, places, money entities consistent: Maya, Darnell, Loretta, Brianna, Kroger Murfreesboro, Magnolia Table, daycare tuition line all match MEMORY.
  H6  PASS  -- Relationships and tone fit: warm text to Loretta about pickup, family brunch with Darnell, coffee with Brianna, all consistent with data-sharing policy.
  H7  PASS  -- Vocabulary matches a layperson-organized parent, not misapplied clinical jargon; the fibroid worry is voiced as a patient, not a clinician writing a note.
  H8  PASS  -- Boundaries implied (don't invent a reservation, draft-don't-send the messages, watch the daycare line and unrecognized charge) are exactly the ones this persona cares about.

I. AI Slop
  I1  PASS  -- No filler opener; starts on the real task after a brief human situational note.
  I2  PASS  -- No connective scaffolding (no Furthermore/Moreover/That said).
  I3  PASS  -- No marketing adjectives (no comprehensive/robust/seamless/leverage).
  I4  PASS  -- Rhythm is uneven and human, not listy symmetrical triplets.
  I5  PASS  -- Does not restate the same point two ways for clarity.
  I6  PASS  -- No motivational wrap-up; ends on the concrete planning-page spec.
  I7  PASS  -- Concrete throughout: Kroger, Magnolia Table, the fourteenth, the eighteenth, the playset and garage.
  I8  PASS  -- Carries her idiosyncrasies: "I have a feeling one of my appointment times is out of date", "say so plainly instead of inventing a reservation".
  I9  PASS  -- Reads aloud as a real busy parent dictating in a morning window, not polished generated copy.

J. Client Requirements
  J1  PASS  -- One very complex opening turn carries essentially all the requirements.
  J2  N-A   -- There are no follow-up turns; single-turn artifact, so "light follow-ups only" does not apply.
  J3  PASS  -- Honest answer to "more than 8 to 10 hours to do well?" is yes.
  J4  MAJOR -- Difficulty leans on breadth of asks across surfaces more than one large coherent data lake; the underlying object population is coherent but not deep (an inbox, one month, one month of checking), closer to the "richness without massive volume" edge.
  J5  MAJOR -- No single workstream operates over a genuinely large population (dozens reviewed independently or thousands reconciled); October checking + one inbox is the heaviest, which is modest.
  J6  PASS  -- Personal domain carries plausible equivalent coherence weight (whole-month family operations with an evidence trail), acceptable under the Personal-domain exception.
  J7  PASS  -- Requires resolving cross-source disagreements where newest wins (stale calendar time vs newer note; superseded vs current tuition), present as judgment, never revealed.
  J8  PASS  -- Deliverables are believable finished work products (a sourced planning page, ready drafts, a built cart), not short answers about the work.
  J9  PASS  -- The opening turn is a whole job to own with dependent deliverables, and the real signal (right tuition, right appointment time, unknown charge) must be found amid believable clutter.
  J10 PASS  -- Writeback is present as intent: put house projects on the shared task board, put a coffee on the books, build and leave the cart, leave drafts in place.
  J11 PASS  -- Reaches complexity through scale and depth without prescriptive form; no numbered stages, no dictated field counts, no dictated file names.

K. Multi-Agent Forcing
  K2 patterns present: a, b, c, f, h
    a. Parallel search -- weather, drive times, backup brunch spot, shipment tracking fan out across independent sources.
    b. Parallel analysis -- inbox triage and October reconciliation are separable analysis loads.
    c. Parallel generation -- planning page, multiple drafts, grocery cart, task-board entries produced concurrently.
    f. Verify and cross-check -- calendar vs newer note, new statement vs prior paperwork.
    h. Aggregate and reconcile -- everything reconciled back into one sourced planning page.
  K1  PASS  -- A single linear thread is visibly insufficient given the breadth of independent surfaces.
  K3  PASS  -- Several patterns trigger (a, b, c, f, h), not just one.
  K4  PASS  -- Fan-out comes from genuinely independent streams (banking vs weather vs maps vs grocery vs inbox), not cosmetic chopping.
  K5  PASS  -- Breadth is pulled back into one coherent planning page with drafts placed where they belong.

FAILS: 8   (blocking: C-context/G/H/J/K/E-originality: 2)
   - C-context FAILs: C11a, C11c  (2 blocking)
   - Deterministic gate FAILs: 6 (C#21 temporal x5, D#27 turn-header x1)
VERDICT: FAIL
TOP FIXES:
  1. Fix the turn header. It must be exactly "--- TURN 1 ---" with nothing else on the line. Move the day/date/time context out of the header entirely (the temporal frame is carried by the harness, not written into the prompt).
  2. Strip all temporal lexicon from the body (C#21): "today", "this afternoon" (x2), "Monday", "Saturday". Rephrase to intent without naming weekdays or relative-time words.
  3. Remove context-restatement and soft path dictation (C11a/C11c): drop "you will find in my working files", "in my documents", "the daycare paperwork from earlier this year should be in there". State only the intent; the agent finds its own files.
  4. Reduce the heaviest-turn word count from 1012 into the 800-1000 band (WARN) and ensure the body is one unbroken paragraph with no blank line (WARN).
  5. Optional strengthening for J4/J5/B3 (REVIEW-level, not blocking): deepen at least one workstream to a genuinely large population so difficulty comes from a large coherent data load, not breadth of asks alone.
```

---

## 3. Combined verdict (per the table in PROMPT_QC.md)

| Component | Result |
|-----------|--------|
| `prompt_qc.py` deterministic gate | **FAIL** (6 findings: 5x C#21 temporal, 1x D#27 malformed turn-header; +2 WARN form-band) |
| Judgment rubric (this pass) | **FAIL** (2 blocking C-context FAILs: C11a restated context, C11c soft path dictation; plus 3 MAJOR flags in B3/J4/J5) |
| **OVERALL** | **FAIL -- blocking. Does not clear to bundle creation.** |

Rule applied: "if the script reports FAIL, the whole artifact is FAIL regardless of this rubric." The judgment pass independently FAILs on C-context as well.

### Summary

The prompt's **content and framing are strong** (single coherent owned job, hidden traps intact, full persona alignment across all 8 H-items, no AI slop, genuine multi-agent forcing). It fails on **form/convention violations** the Skoll harness forbids: the turn header embeds date/time, the body contains temporal words, and the persona softly dictates where files live and restates context the agent already holds. These are mechanical rewrites that preserve all the genuine merit. The three MAJOR object-population-scale flags are non-blocking REVIEW items the author may justify or deepen.
