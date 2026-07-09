# Mock Data & Artifacts Quality Audit Report

**Scope:** 36 personas in `/Updated mock/`  
**Audit Date:** July 2025  
**Coverage:** mock_data (101 API directories × 36 personas), home artifacts (8 subdirs × 36 personas), identity files (IDENTITY.md, AGENTS.md, SOUL.md, MEMORY.md, USER.md, TOOLS.md, HEARTBEAT.md)  
**Personas sampled in depth:** angela-peterson, brandon-kelly, brian-hall, brian-santos, carlos-bennett, calvin-roth, gary-pittman, grace-hatfield, jake-thornton, jason-campbell, jason-kim, jason-rivera, jessica-taylor, jennifer-williams, joan-hampton, jordan-mcdaniel, juan-hernandez, justin-rivera, margaret-farmer, nate-wright, paul-rivera, phil-lane, sam-osborne, shannon-perry, shawn-dawson, steve-petersen, stuart-myer, yves-quinn

---

## Executive Summary

The 36 personas exhibit a stark quality divide. **Identity and configuration files** (IDENTITY.md, AGENTS.md, SOUL.md) are **exceptional** — deeply individuated, culturally authentic, operationally detailed. **Home artifacts** (HTML websites, data files) are **high quality** with rich persona-specific content. **Mock API data**, however, suffers from **systemic structural failures** that would break any real API consumer. Issues fall into five tiers of severity.

### Scoring Overview

| Dimension | Grade | Notes |
|---|---|---|
| Identity files (IDENTITY.md, AGENTS.md, SOUL.md) | **A** | Exceptional individuation, culturally authentic |
| Home artifacts (Desktop, Documents, etc.) | **B+** | Rich content, inconsistent naming |
| Mock data — content authenticity | **B** | Persona-coherent when not contaminated |
| Mock data — structural correctness | **F** | Systemic type failures, missing envelopes |
| Mock data — cross-persona isolation | **D** | Template leaks, identical libraries, shared engineering issues |
| Mock data — volume authenticity | **D** | Duplication inflation, habit dumping in calendars |

---

## CRITICAL ISSUES

### 1. Universal Data Type Failures — Booleans and Numbers as Strings

**Severity:** CRITICAL  
**Prevalence:** 100% of personas sampled (9/9 tested)  
**APIs affected:** Stripe, GitHub, Slack, Spotify, Airbnb, OpenWeather, Google Calendar, HubSpot

Every boolean and most numeric values across the entire dataset are stored as JSON strings instead of their correct native types. This would break any typed API client, ORM, or SDK.

**Proof — Stripe `charges.json` (brandon-kelly):**
```json
{
  "amount": "320000",          // ← should be: 320000 (integer, in cents)
  "paid": "true",              // ← should be: true (boolean)
  "refunded": "false",         // ← should be: false (boolean)
  "created": "1759161600"      // ← should be: 1759161600 (integer)
}
```

**Proof — Spotify `tracks.json` (grace-hatfield):**
```json
{
  "duration_ms": "179447",     // ← should be: 179447 (integer)
  "explicit": "false",         // ← should be: false (boolean)
  "popularity": "60",          // ← should be: 60 (integer)
  "track_number": "1"          // ← should be: 1 (integer)
}
```

**Proof — Google Calendar `events.json` (nate-wright):**
```json
{
  "all_day": "false"           // ← should be: false (boolean)
}
```

**Proof — Airbnb `listings.json` (jake-thornton):**
```json
{
  "price_per_night": "105.00", // ← should be: 105.00 (number)
  "beds": "2",                 // ← should be: 2 (integer)
  "baths": "1",                // ← should be: 1 (integer)
  "max_guests": "4",           // ← should be: 4 (integer)
  "instant_book": "true"       // ← should be: true (boolean)
}
```

**Scale of impact:** 9 out of 9 personas tested had `paid: "true"` (string) in Stripe charges. 8 of 9 had `amount` as a string. Only `jessica-taylor` had integer amounts, and even she had boolean strings. This is a 100% failure rate on type correctness.

---

### 2. Cross-Persona Data Copying — Identical Libraries Shared Between Unrelated Personas

**Severity:** CRITICAL  
**Prevalence:** Confirmed in at least 2 persona pairs; suspected wider

Two personas with completely different backgrounds share **byte-for-byte identical Spotify libraries**.

**Proof — joan-hampton (midwife, Galway, Ireland) vs. margaret-farmer (ceramicist, Kyoto, Japan):**

`joan-hampton/mock_data/spotify-api/tracks.json` (line 1-10):
```json
{
  "album_id": "for.emma.forever.a.ago",
  "artist_id": "bon.iveriver",
  "duration_ms": "179447",
  "explicit": "false",
  "name": "Skinny Love",
  "popularity": "60",
  "track_id": "skinny.lovebon.iver",
  "track_number": "1"
}
```

`margaret-farmer/mock_data/spotify-api/tracks.json` (line 1-10):
```json
{
  "album_id": "for.emma.forever.a.ago",
  "artist_id": "bon.iveriver",
  "duration_ms": "179447",
  "explicit": "false",
  "name": "Skinny Love",
  "popularity": "60",
  "track_id": "skinny.lovebon.iver",
  "track_number": "1"
}
```

These are **identical**. An Irish midwife and a Japan-based ceramicist should not share the same music library. This is a copy-paste generation artifact.

Additionally, `duration_ms: "179447"` appears as the first track across **multiple** personas despite being different songs — suggesting a template value was not randomized.

---

### 3. GitHub Template Contamination — Engineering Issues Assigned to Non-Tech Personas

**Severity:** CRITICAL  
**Prevalence:** Confirmed in 5+ of 6 personas sampled  
**Root cause:** A shared template of 3 software engineering issues was distributed to all personas regardless of profession

Non-technical personas receive GitHub issues about software engineering concepts they would never encounter:

**Proof — margaret-farmer (ceramicist, Kyoto):**
```json
{
  "title": "Reduce p99 latency on /search endpoint",
  "repo": "api-gateway",
  "milestone": "Q1 Performance",
  "labels": "documentation;wontfix",
  "id": "9100001",
  "created_at": "2025-01-15T10:00:00Z"
}
```

**Same issue in brian-santos (midwife, Asheville):**
```json
{
  "title": "Reduce p99 latency on /search endpoint",
  "repo": "mountain-morning-teas/storefront",
  "milestone": "v0.3 — holiday gift rush",
  "id": "9100001",
  "created_at": "2025-01-15T10:00:00Z"
}
```

All three template titles:
1. "Reduce p99 latency on /search endpoint"
2. "Onboarding flow stalls on email step" / "Orientation flow stalls on email step"
3. "Add dark mode tokens to design system"

**Personas with these engineering templates who are NOT engineers:**
- joan-hampton (midwife)
- margaret-farmer (ceramicist)
- gary-pittman (retired church custodian)
- brian-santos (midwife)
- jake-thornton (midwife / cooking instructor)

**Only paul-rivera** had persona-appropriate issue titles ("flightlog-cli: parse logbook entries...").

All contaminated personas share the same starting data: `id: "9100001"`, `created_at: "2025-01-15T10:00:00Z"`, `number: "100"`.

---

### 4. Calendar Habit Dumping — Personal Routines Inflated to Thousands of Individual Events

**Severity:** CRITICAL  
**Prevalence:** At least 4 personas confirmed  
**Root cause:** Lifestyle/preferences data from SOUL.md was materialized as individual daily calendar events instead of using recurrence rules or keeping it in profile data

**Proof — brian-hall: 21,542 lines, ~1,436 events:**
```json
{
  "summary": "Wake",
  "description": "Wake. Black coffee from the Chemex, then a protein smoothie with whey, banana, spinach, almond butter, and creatine. Vitamin D 4000 IU and fish oil with the morning routine.",
  "start": "2026-03-30T04:45:00-04:00",
  "recurrence": "RRULE:FREQ=DAILY"
}
```
This single "Wake" event is repeated ~262 times with incrementing dates. Each event ALSO has `recurrence: "RRULE:FREQ=DAILY"` despite being a single instance — contradicting the purpose of recurrence rules. The file also has "CrossFit 5:15 AM" × 209 times, "Clinic 7:00 AM to 6:30 PM" × 262 times.

**Proof — nate-wright: 6,737 lines, ~449 events:**
```json
{
  "summary": "Black drip coffee on waking, two to three cups across the day",
  "description": "Black drip coffee on waking, two to three cups across the day.",
  "location": "Lorca, 125 Bedford Street, Stamford, CT 06901",
  "start": "2026-06-30T09:00:00-04:00",
  "recurrence": "RRULE:FREQ=DAILY"
}
```
Coffee drinking habits as 30-minute scheduled calendar events, repeated 14+ times. Also "Vitamin D3 2000 IU and fish oil 1000 mg morning supplements" as daily events.

**Proof — angela-peterson: 18,182 lines, ~1,212 events** with "Field dive day" × 105 instances.

**Contrast — calvin-roth: 1,561 lines, ~104 events** — a reasonable, realistic calendar.

---

### 5. Massive Data Duplication via ID Suffixing

**Severity:** CRITICAL  
**Prevalence:** At least 3 personas confirmed across Stripe and Spotify  
**Root cause:** Base records are duplicated with `-g1`, `-g2`, `-v9`, `-v10`, `-2`, `-3` suffixes to inflate volume

**Proof — carlos-bennett/stripe-api/products.json:**
Only 4 unique products are duplicated with `-g1` through `-g4` suffixes (20 total entries). All duplicates share identical names, descriptions, amounts, and timestamps — only the ID suffix changes.

**Proof — jessica-taylor/stripe-api/charges.json (1,497 lines):**
The same 8 base charges (ch_1000 through ch_1007) are duplicated with suffixes `-v9` through `-v20`. Then a cookie-cutter pattern repeats the exact same 20 line items for each of 4 clients (Verdant Provisions, Pinnacle Collective, Bloom Skin Co, Kiln + Loom Ceramics), changing only the client name.

**Proof — grace-hatfield/spotify-api/playlists.json:**
Same 6 playlists duplicated with suffixes `-2`, `-3`, `-4`. Owner IDs carry generation suffixes (`gracehatfield-g1` through `-g14`).

---

## MODERATE ISSUES

### 6. Cross-Persona Timestamp Format Inconsistency

**Severity:** MODERATE  
**Prevalence:** All personas, 3+ incompatible formats within the same API

The same field (`created` in Stripe) uses different timestamp formats across personas:

| Persona | Format | Example |
|---|---|---|
| brandon-kelly | Unix epoch string | `"1759161600"` |
| jessica-taylor | Unix epoch integer | `1797618600` |
| carlos-bennett | ISO 8601 string | `"2026-01-01T00:00:00-04:00"` |
| yves-quinn | Unix epoch string | `"1770019200"` |

A real API returns one format consistently. Stripe uses Unix epoch integers. Having three different formats across personas means any shared tooling, tests, or parsers cannot work uniformly.

---

### 7. Slack Reactions Field — 4+ Different Wrong Formats

**Severity:** MODERATE  
**Prevalence:** All 4 personas checked had different incorrect formats

**Correct Slack format:**
```json
"reactions": [{"name": "thumbsup", "count": 2, "users": ["U123", "U456"]}]
```

**Actual formats found:**

| Persona | Format | Example |
|---|---|---|
| joan-hampton | Empty string | `""` |
| margaret-farmer | Colon-delimited | `"eyes:U003SOTA,U005PARK"` |
| jordan-mcdaniel | Colon-delimited variant | `"wave:U04DERRICK,U04TONYA"` |
| brian-santos | Emoji + count | `":tea:x1"` |
| gary-pittman | Thread topic string | `"Church maintenance update"` |

gary-pittman's is the most egregious — `reactions` contains the **thread topic** ("Church maintenance update", "Coffee tomorrow") instead of reaction data.

---

### 8. WhatsApp `template_name` Field — 4+ Different Wrong Uses

**Severity:** MODERATE  
**Prevalence:** All 5 personas checked had incorrect usage

In the real WhatsApp Business API, `template_name` only applies to approved business message templates (promotional broadcasts, transactional alerts). Personal messages never have this field.

| Persona | What's in `template_name` | Example |
|---|---|---|
| joan-hampton | Empty string | `""` |
| margaret-farmer | Empty string | `""` |
| shawn-dawson | Empty string | `""` |
| jordan-mcdaniel | Message type | `"text"` |
| brian-hall | Contact names | `"Tamika Reynolds"`, `"Karen Hall"` |
| justin-rivera | Persona-prefixed IDs | `"justin-rivera-default-0000"` |
| shannon-perry | Persona-prefixed IDs | `"shannon-perry-default-0000"` |

brian-hall's is the most wrong — the **sender's name** is stored in the template field.

---

### 9. Email Domain Inconsistency Across Personas

**Severity:** MODERATE  
**Prevalence:** 3 different placeholder domains, casing/TLD inconsistencies

All personas use fictional email domains, but these are inconsistent:

| Domain | Personas | Count |
|---|---|---|
| `@Finthesiss.ai` | james-davis, jennifer-long, jessica-spencer, jennifer-williams, joan-hampton, jessica-taylor, gary-pittman, jason-campbell, jason-rivera, shannon-perry, nate-wright, carlos-bennett, steve-petersen | 13+ |
| `@Greenridertech.com` / `@Greenridertech.co` / `@greenridertech.co` | brian-hall (.com), grace-hatfield (.com), angela-peterson (.co lowercase), brandon-kelly (.co capitalized) | 4+ |
| `@greenrider.co` | jake-thornton | 1 |
| `@voissync.ai` | sam-osborne, paul-rivera, yves-quinn | 3 |
| `@gmail.com` | jake-thornton (calendar) | 1 |

**Issues:**
- "Finthesiss" has a probable typo (double 's')
- `greenridertech` vs `greenrider` — are these the same fictional company?
- `.com` vs `.co` TLD inconsistency for the same domain
- Uppercase vs lowercase first letter (`Greenridertech` vs `greenridertech`)
- Unrelated personas (a midwife in Galway, a church custodian in South Dakota, a welding teacher in Pittsburgh) share the same email domain

---

### 10. Calendar Description/Metadata Contamination

**Severity:** MODERATE  
**Prevalence:** Confirmed in jake-thornton, suspected wider

Calendar event descriptions contain content from other data categories.

**Proof — jake-thornton/google-calendar-api/events.json:**
```json
{
  "summary": "Dentist",
  "description": "Part of Jake's Table Southern-fusion cooking classes in East Lake, Atlanta."
}
```
A dentist appointment has a **cooking class** description.

The duplicate of this same event has:
```json
{
  "summary": "Dentist-9608",
  "description": "Notes from Jake Thornton's midwifery practice at Magnolia Women's Health."
}
```
A dentist appointment with **midwifery practice notes** as the description.

Additionally, the duplicate has an invalid timezone offset: `"start": "2026-11-29T13:30:00-07:13"` — `-07:13` is not a valid UTC offset.

---

### 11. HubSpot Temporal Impossibilities — Modified Before Created

**Severity:** MODERATE  
**Prevalence:** Confirmed in 2 personas

**Proof — jennifer-williams/hubspot-api/deals.json:**
```
Deal 401:
  createdate: 2026-12-27
  lastmodifieddate: 2026-12-19
```
Modified 8 days **before** it was created.

**Proof — brian-hall/hubspot-api/deals.json:**
```
Deals 401 & 411:
  createdate: 2026-03-08
  lastmodifieddate: 2026-03-03
```
Modified 5 days before creation.

---

### 12. Spotify ID Format Inconsistency — 3 Incompatible Formats

**Severity:** MODERATE  
**Prevalence:** All personas, 3 mutually incompatible schemes

Real Spotify IDs are 22-character Base62 strings (e.g., `6rqhFgbbKwnb9MLmUQDhG6`).

| ID Style | Personas | Example |
|---|---|---|
| Slug with concatenation artifacts | margaret-farmer, joan-hampton, jason-rivera, carlos-bennett, grace-hatfield | `bon.iveriver`, `bruce.springsteenteen`, `ludovico.einaudiaudi`, `max.richterhter` |
| Base62-like (closest to correct) | steve-petersen, shawn-dawson | `7Ylh2D0B6fl6WmNc7cWQhh` |
| Prefixed readable | brandon-kelly | `trk-001`, `alb-okeanelzy` |

The slug format has visible **concatenation artifacts** where artist name fragments are incorrectly merged:
- `bon.iveriver` ← "Bon Iver" + truncated "iver"
- `bruce.springsteenteen` ← "Springsteen" + extra "teen"
- `ludovico.einaudiaudi` ← "Einaudi" + extra "audi"
- `max.richterhter` ← "Richter" + extra "hter"

Also, album ID `ludovico.einaudi.sorks` appears to be a typo for "works".

---

### 13. Missing API Response Envelopes

**Severity:** MODERATE  
**Prevalence:** All personas, all APIs (except shannon-perry/stripe-api/balance.json)

Every API file returns bare JSON arrays `[...]` instead of proper paginated API response envelopes.

**Expected Stripe format:**
```json
{
  "object": "list",
  "url": "/v1/charges",
  "has_more": false,
  "data": [ ... ]
}
```

**Actual format (all personas):**
```json
[ ... ]
```

The single exception found: `shannon-perry/stripe-api/balance.json` has proper nested structure with `object`, `livemode`, `available`, `pending`.

---

### 14. GitHub Issues — Structural Defects

**Severity:** MODERATE  
**Prevalence:** All personas sampled

Multiple structural issues in GitHub issues data:

**Labels as semicolon-delimited strings instead of arrays:**
```json
"labels": "documentation;wontfix"        // should be: ["documentation", "wontfix"]
"labels": "p2;p2"                        // duplicate label
"labels": "good-first-issue;good-first-issue"  // duplicate label
```

**`is_pull_request` as string:**
```json
"is_pull_request": "false"               // should be: false (boolean)
```

**`id` and `number` as strings:**
```json
"id": "9100001",                         // should be: 9100001 (integer)
"number": "100"                          // should be: 100 (integer)
```

**Closed issues with contradictory states:**
Some issues have `state: "open"` but a non-empty `closed_at` timestamp.

---

### 15. Calendar Recurrence Field Contains Random Text

**Severity:** MODERATE  
**Prevalence:** Confirmed in nate-wright, suspected wider

The first instance of a repeated event has a valid `RRULE`, but subsequent instances have random descriptive text:

**Proof — nate-wright/google-calendar-api/events.json:**
```json
// Event 1 (correct):
{ "recurrence": "RRULE:FREQ=DAILY" }

// Event 2 (wrong):
{ "recurrence": "Working note — Harborview ED, Stamford CT" }
```

The recurrence field is being used to store freeform notes instead of RFC 5545 recurrence rules.

---

## MINOR ISSUES

### 16. Home Artifact File Naming — 7 Different Schemes Across Personas

**Severity:** MINOR  
**Prevalence:** Every persona has a different scheme

| Persona | Naming Pattern | Examples |
|---|---|---|
| angela-peterson | Mixed prefixes | `doc_a.pdf`, `data_01.xml`, `item_b.tsv` |
| yves-quinn | `BN` pattern | `B10.pdf`, `B18.xlsx`, `B2.tsv` |
| stuart-myer | Bare numbers | `12.png`, `18.docx`, `27.pdf` |
| margaret-farmer | Mixed numeric | `027.pdf`, `039.docx`, `a2.mp3` |
| phil-lane | `file_N` pattern | `file_2.pdf`, `file_3.pdf` |
| calvin-roth | `dNN` prefix | `d01.pdf`, `d02.xlsx` |
| shawn-dawson | Letter + number | `a13.pdf`, `e4.xlsx`, `p5.docx` |

File counts are reasonable (46–62 files per persona), but the naming schemes are inconsistent. This is a minor cosmetic issue — real users do have inconsistent file naming.

---

### 17. Markdown Backtick Contamination in JSON Values

**Severity:** MINOR  
**Prevalence:** Confirmed in carlos-bennett

**Proof — carlos-bennett/google-calendar-api/events.json:**
```json
"calendar_id": "`carlos.bennett@Finthesiss.ai`"
```

The value contains **backtick characters** from markdown formatting that leaked into the JSON data. The backticks are part of the string value.

---

### 18. Persona Name Embedded in IDs

**Severity:** MINOR  
**Prevalence:** Confirmed in brian-hall, carlos-bennett

**Proof — brian-hall/stripe-api/charges.json:**
```json
"id": "ch_brian-hall_clinic-visit-followup_20261002"
```

**Proof — carlos-bennett/stripe-api/charges.json:**
```json
"customer": "cus_carlos-bennett_mykonos-original"
```

Real API IDs never contain the user's name. They are opaque identifiers.

---

### 19. Invalid Timezone Offsets

**Severity:** MINOR  
**Prevalence:** Confirmed in jake-thornton

**Proof — jake-thornton/google-calendar-api/events.json:**
```json
"start": "2026-11-29T13:30:00-07:13"
```

`-07:13` is not a valid UTC offset. Valid offsets are multiples of 15 or 30 minutes (e.g., `-07:00`, `-05:30`).

---

### 20. Stripe Invoice Cross-Referencing Issues

**Severity:** MINOR  
**Prevalence:** Confirmed in brandon-kelly

Subscription IDs in invoices mirror customer IDs (e.g., `sub_edd662a1be10c36a` matches `cus_edd662a1be10c36a`), suggesting they were generated from the same seed. In reality, subscription and customer IDs are independently generated.

---

### 21. Slack Message Duplication

**Severity:** MINOR  
**Prevalence:** Confirmed in steve-petersen

**Proof — steve-petersen/slack-api/messages.json:**
Lines 6–8 are duplicated at lines 51–53. The exact same message ("One of my second-period guys finally ran a clean bead today...") appears twice in the conversation.

---

## STRENGTHS

### Identity & Configuration Files — Grade: A

The `.md` files are the standout strength of this dataset. They demonstrate:

**Deep individuation:** Each persona has unique priorities, communication preferences, spending thresholds, and escalation protocols. A midwife in Galway has EUR 250 thresholds and HSE-specific rules. A retired church custodian in South Dakota has $50 thresholds. A sports medicine doctor in Atlanta has $500 thresholds.

**Cultural authenticity:** joan-hampton's AGENTS.md routes through Irish healthcare systems (HSE, consultants, community midwifery). margaret-farmer's operates in JPY with Kyoto-specific gallery relationships. brian-hall's reflects Atlanta neighborhoods and Southern family rhythms.

**Relational depth:** Data sharing policies name specific people with specific access levels. Escalation contacts include professional relationships, family hierarchies, and ICE designations that reflect real decision-making.

**Operational realism:** Confirmation rules, communication routing, and memory management policies are genuinely useful operational documents — not just filler.

### Home Artifacts — Grade: B+

HTML files found on Desktops are impressive, fully-built persona-specific websites:

- **angela-peterson:** 528-line portfolio for a marine biologist with research data, publications, and outreach
- **brian-santos:** 1,404-line e-commerce site for "Mountain Morning Teas" herbal tea business
- **calvin-roth:** 784-line personal running website
- **jake-thornton:** Cooking/recipe content

Data files (XML, TSV, CSV) contain persona-appropriate content: coral reef survey data for the marine biologist, swim training logs, financial tracking.

### Message Content Quality — Grade: B

Where the format is correct, message content is excellent:

- **gary-pittman/slack-api:** Realistic church maintenance coordination conversations in Aberdeen, SD
- **shannon-perry/whatsapp-api:** Authentic family and community messages
- **steve-petersen/slack-api:** Welding classroom anecdotes and trade school culture

---

## Issue Distribution Heatmap

| API | Type Issues | Template Contamination | Duplication | Format Issues | Overall |
|---|---|---|---|---|---|
| **stripe-api** | CRITICAL | — | CRITICAL | MODERATE | CRITICAL |
| **github-api** | CRITICAL | CRITICAL | MODERATE | CRITICAL | CRITICAL |
| **google-calendar-api** | CRITICAL | — | CRITICAL | MODERATE | CRITICAL |
| **spotify-api** | CRITICAL | — | CRITICAL | CRITICAL | CRITICAL |
| **slack-api** | MODERATE | — | MINOR | CRITICAL | CRITICAL |
| **hubspot-api** | CRITICAL | — | — | MODERATE | MODERATE |
| **whatsapp-api** | MINOR | — | — | MODERATE | MODERATE |
| **airbnb-api** | CRITICAL | — | — | — | MODERATE |
| **openweather-api** | CRITICAL | — | — | — | MODERATE |

---

## Summary of Fixes Required

### Priority 1 — Fix Across All 36 Personas × All APIs
1. Convert all boolean strings (`"true"`, `"false"`) to native booleans (`true`, `false`)
2. Convert all numeric strings (`"320000"`, `"179447"`) to native numbers (`320000`, `179447`)
3. Standardize timestamp format per API (Stripe = Unix integer, GitHub = ISO 8601, etc.)

### Priority 2 — Fix Across All 36 Personas × Specific APIs
4. Re-generate GitHub issues with persona-appropriate titles (not engineering templates)
5. Collapse calendar habit dumps into single events with proper `RRULE:FREQ=DAILY` recurrence
6. Remove duplicate records inflated via ID suffixing; generate unique records instead
7. Generate unique Spotify libraries per persona, not shared copies
8. Fix Slack `reactions` to use proper array-of-objects format
9. Fix WhatsApp `template_name` — remove from personal messages, use only on business templates

### Priority 3 — Fix Across Affected Personas
10. Fix HubSpot temporal impossibilities (`lastmodifieddate` < `createdate`)
11. Fix calendar description contamination (dentist ≠ cooking class)
12. Standardize email domains (pick one domain, one TLD, one casing)
13. Remove backtick contamination from JSON values
14. Fix invalid timezone offsets
15. Add API response envelope wrappers

### Priority 4 — Nice-to-Have
16. Standardize home artifact file naming (or document that variation is intentional)
17. Use real Base62 format for Spotify IDs
18. Remove persona names from Stripe/API IDs
19. Fix Slack `thread_ts` to use Slack timestamp format instead of text strings

---

*Report generated from manual sampling across 28 of 36 personas. Findings are representative; unsampled personas likely share the same systemic issues.*
