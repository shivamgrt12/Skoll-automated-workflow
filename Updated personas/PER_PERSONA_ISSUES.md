# Per-Persona Quality Audit Report

> Comprehensive scan of all 36 personas at `/Users/apple/Desktop/New Personas/Updated mock/`  
> Each section lists **only persona-specific** issues. Universal issues in §1 are **not repeated**.

---

## Severity Legend

| Icon | Level | Meaning |
|------|-------|---------|
| 🔴 | Critical | Data is wrong, contradictory, copied from another persona, or contaminated |
| 🟠 | Moderate | Structural/type issues that reduce API realism |
| 🟡 | Minor | Cosmetic, non-standard formatting, or missing optional fields |

---

## §1 — Universal Issues (All 36 Personas)

These affect **every single persona** and are not repeated below.

| # | Sev | API | Issue |
|---|-----|-----|-------|
| U1 | 🟠 | Stripe | `paid` field is string `"true"`/`"false"` instead of boolean |
| U2 | 🟠 | Stripe | Missing `object` field on all resources (e.g., `"object": "charge"`) |
| U3 | 🟠 | Stripe | Missing `metadata`, `livemode`, `default_source`, `invoice_settings` fields |
| U4 | 🟠 | Stripe | Bare JSON arrays — no API response envelope/pagination wrapper |
| U5 | 🟠 | GitHub | Labels stored as semicolon-delimited strings instead of arrays of objects |
| U6 | 🟠 | Slack | `reactions` field has wrong format (see per-persona for specific variant) |
| U7 | 🟠 | OpenWeather | All numeric values (`temp`, `pressure`, `humidity`) stored as strings |
| U8 | 🟠 | Airbnb | All values (`price`, `beds`, `baths`, `max_guests`) stored as strings |
| U9 | 🟡 | WhatsApp | `template_name` present on personal/non-business messages (should be business-broadcast only) |

---

## §2 — Per-Persona Issues

---

### angela-peterson
> Marine biologist · Pacific Reef Research Institute · Honolulu HI  
> Email: `angela.peterson@greenridertech.co`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — first issue is `"Reduce p99 latency on /search endpoint"` (irrelevant to marine biology) |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` with 27+ other personas |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates (impossible state) |
| 4 | 🔴 | Calendar | Bloated to 18,182 lines (~1,212 events) — routine inflation |
| 5 | 🟠 | Stripe | All `amount` values are strings (e.g., `"320000"` instead of `320000`) |
| 6 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 7 | 🟠 | Stripe | Persona name embedded in charge IDs: `ch_angela-peterson_ba2ac99a51` |
| 8 | 🟠 | GitHub | 3 duplicate labels (e.g., `"p2;p2"`) |
| 9 | 🟠 | HubSpot | 7 deals with `createdate` after `lastmodifieddate` (temporal impossibility) |
| 10 | 🟡 | Slack | Reactions field is empty string `""` |
| 11 | 🟡 | Spotify | Track IDs are concatenated slugs: `black.goldesperanz` |
| 12 | 🟡 | WhatsApp | `template_name` set to `"outreach-default"` on all messages |
| 13 | 🟡 | Home | Mixed file naming scheme: `doc_a.pdf`, `data_01.xml`, `item_b.tsv` |

**Strengths:** Excellent home artifacts (portfolio website, coral reef XML dataset, swim log). Strong persona coherence in content.

---

### asha-gallegos
> Broadcast journalist · Off-Mic podcast · Rhythm FM 94.7 · Johannesburg ZA  
> Email: not found in AGENTS.md

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Stripe | Invoice impossible state: `amount_paid` (165606) > `amount_due` (125915) |
| 2 | 🔴 | Stripe | Shared charge IDs with 6 other personas: `ch_004d9b92879ce0aee8` (copy-paste cluster) |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 4 | 🟠 | Slack | Reactions format: `emoji:users` string (e.g., `"thumbsup:U04TEAM"`) |
| 5 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 6 | 🟡 | WhatsApp | `template_name` is empty string `""` |
| 7 | 🟡 | Home | `a1.pdf, a2.pdf` naming scheme |

**Strengths:** ✅ Stripe amounts are **integers** (1 of only 4 personas). ✅ GitHub issues have **persona-appropriate** titles (`"Playout scheduler skips overnight ad breaks"`). ✅ Unique GitHub issue ID (`85655740168`). ✅ No HubSpot temporal bugs. ✅ Excellent cultural authenticity (ZAR, SA phone numbers, Joburg neighborhoods). Smallest calendar (976 lines) — realistic size.

---

### brandon-kelly
> Electrician (Kelly Electric) · beekeeper · chess club · Baltimore/Bridgeton  
> Email: `brandon.kelly@Greenridertech.co`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Stripe | Shared charge IDs with 6 other personas: `ch_004d9b92879ce0aee8` |
| 2 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 3 | 🟠 | Stripe | All `amount` values are strings |
| 4 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 5 | 🟠 | Slack | Reactions format: `emoji:users` string |
| 6 | 🟡 | Spotify | Prefixed track IDs: `trk-001` (unique format, only persona with this) |
| 7 | 🟡 | WhatsApp | `template_name` set to `"service_request"` on all messages |
| 8 | 🟡 | Home | `file_N` naming scheme |

**Strengths:** ✅ GitHub issues have **persona-appropriate** titles (`"CSV import skips rows with zero brood frames"` — beekeeper context). ✅ No GitHub duplicate labels. ✅ No HubSpot temporal bugs. ✅ No Stripe product duplication. ✅ Persona-coherent charge descriptions (electrical work: "200A Panel Upgrade", "EV Charger Install Level 2").

---

### brian-hall
> Physical therapist (Peak Performance PT) · CrossFit · Atlanta GA  
> Email: `brian.hall@Greenridertech.com`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Calendar | **Worst calendar bloat**: 21,542 lines (~1,436 events) |
| 2 | 🔴 | Calendar | **855 habit-dump events**: "Clinic 7:00 AM to 6:30 PM" ×262, "CrossFit 5:15 AM" ×209, "Wake" with full routine ×daily |
| 3 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 4 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 5 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 6 | 🟠 | Stripe | All `amount` values are strings |
| 7 | 🟠 | Stripe | Timestamps as **ISO 8601** strings (different from majority using Unix epoch) |
| 8 | 🟠 | Stripe | Persona name embedded in all IDs: `ch_brian-hall_`, `cus_brian-hall_`, `pi_brian-hall_` |
| 9 | 🟠 | GitHub | 3 duplicate labels |
| 10 | 🟠 | HubSpot | 2 deals with temporal impossibility |
| 11 | 🟡 | Slack | Reactions field contains `"standard"` (non-reaction content) |
| 12 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 13 | 🟡 | WhatsApp | Contact name leaked into `template_name`: `"Tamika Reynolds"` |
| 14 | 🟡 | Home | `fileNN` naming scheme (`file01.pdf`) |

---

### brian-patterson
> College student · Syracuse University  
> Email: `brian.patterson@greenridertech.com`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 4 | 🟠 | Stripe | All `amount` values are strings |
| 5 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 6 | 🟠 | Stripe | Persona name embedded in IDs |
| 7 | 🟠 | GitHub | 3 duplicate labels |
| 8 | 🟠 | HubSpot | **10 deals** with temporal impossibility |
| 9 | 🟠 | Calendar | 6,092 lines — moderately bloated |
| 10 | 🟡 | Slack | Reactions format: `:thumbsup:` (simple emoji name) |
| 11 | 🟡 | WhatsApp | `template_name` set to `"appointment_reminder"` on all messages |
| 12 | 🟡 | Home | `file_N` naming scheme |

---

### brian-santos
> Midwife · Mountain Morning Teas (tea business) · Asheville NC  
> Email: not found in AGENTS.md

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` (irrelevant to midwifery) |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 4 | 🔴 | Calendar | 11,956 lines — heavily bloated |
| 5 | 🟠 | Stripe | All `amount` values are strings |
| 6 | 🟠 | Stripe | Timestamps as **ISO 8601** strings |
| 7 | 🟠 | Stripe | Persona name embedded in IDs |
| 8 | 🟠 | GitHub | 3 duplicate labels |
| 9 | 🟡 | Slack | Reactions format: `:tea:x1` (emoji + count string) |
| 10 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 11 | 🟡 | WhatsApp | `template_name` set to `"unset"` |
| 12 | 🟡 | Home | `fileNN` naming scheme |

**Strengths:** ✅ No HubSpot temporal bugs. ✅ Excellent home artifacts (Mountain Morning Teas e-commerce site, 1,404 lines of HTML).

---

### calvin-roth
> Lawyer / Public defender · Wicker Park · Chicago IL  
> Email: not found in AGENTS.md

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 4 | 🟠 | Stripe | All `amount` values are strings |
| 5 | 🟠 | Stripe | Timestamps as **ISO 8601** strings |
| 6 | 🟠 | GitHub | 3 duplicate labels |
| 7 | 🟠 | HubSpot | 1 deal with temporal impossibility |
| 8 | 🟡 | Slack | Reactions format: `:thumbsup:` (simple emoji name) |
| 9 | 🟡 | WhatsApp | `template_name` is empty string `""` |
| 10 | 🟡 | Home | `dNN` naming scheme (`d01.pdf`) |

**Strengths:** ✅ Spotify track IDs use **Base62 format** (1 of only 6 personas — correct format). ✅ Persona-specific charge IDs: `ch_calvin_strava_2025renewal`. ✅ Calendar is reasonable size (1,561 lines). ✅ Excellent home artifacts (personal running website).

---

### carlos-bennett
> Charter boat captain · guitar repair · Bayport  
> Email: not found in AGENTS.md (uses `@Finthesiss.ai` in calendar)

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Calendar | **Backtick contamination**: 885 markdown backticks in JSON (e.g., `` `carlos.bennett@Finthesiss.ai` `` in `calendar_id`) |
| 2 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 3 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 4 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 5 | 🔴 | Stripe | Product suffix duplication: 4 unique products duplicated as `-g1` through `-g4` (20 records from 4 actual) |
| 6 | 🟠 | Stripe | All `amount` values are strings |
| 7 | 🟠 | Stripe | Timestamps as **ISO 8601** strings |
| 8 | 🟠 | Stripe | Persona name embedded in IDs: `cus_carlos-bennett_mykonos-original` |
| 9 | 🟠 | GitHub | 3 duplicate labels |
| 10 | 🟡 | Slack | Reactions field contains `"general"` (non-reaction content) |
| 11 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 12 | 🟡 | WhatsApp | `template_name` set to `"standard"` |

---

### gary-pittman
> Retired church custodian · Aberdeen SD  
> Email: `gary.pittman@Finthesiss.ai`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` (irrelevant to retired church custodian) |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 4 | 🔴 | Calendar | 7,967 lines — bloated |
| 5 | 🟠 | Stripe | All `amount` values are strings |
| 6 | 🟠 | Stripe | Timestamps as **ISO 8601** strings |
| 7 | 🟠 | Stripe | Persona name embedded in IDs |
| 8 | 🟠 | GitHub | 3 duplicate labels |
| 9 | 🟡 | Slack | Reactions field contains topic text: `"Church maintenance update"` (non-reaction content) |
| 10 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 11 | 🟡 | WhatsApp | Contact name leaked into `template_name`: `"Gary Pittman"` |

**Strengths:** ✅ No HubSpot temporal bugs. ✅ Excellent Slack message content (realistic church maintenance coordination in Aberdeen, SD).

---

### grace-hatfield
> Rural legal-aid attorney · field hockey coach · quilter · Syracuse NY  
> Email: `grace.hatfield@Greenridertech.com`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 4 | 🔴 | Calendar | 11,042 lines — heavily bloated |
| 5 | 🔴 | Stripe | Product suffix duplication present (16 dups) |
| 6 | 🟠 | Stripe | All `amount` values are strings |
| 7 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 8 | 🟠 | Stripe | Persona name embedded in IDs |
| 9 | 🟠 | Stripe | Highest `paid` string count: 188 |
| 10 | 🟠 | GitHub | 3 duplicate labels |
| 11 | 🟡 | Slack | Reactions: persona-prefixed ID `"grace-hatfield-0000"` |
| 12 | 🟡 | Spotify | Track IDs are concatenated slugs with artist name artifacts (e.g., `max.richterhter` — typo) |
| 13 | 🟡 | WhatsApp | `template_name`: persona-prefixed ID `"grace-hatfield-0000"` |
| 14 | 🟡 | Spotify | Playlists duplicated with `-2`, `-3`, `-4` suffixes |

**Strengths:** ✅ No HubSpot temporal bugs.

---

### jake-thornton
> Midwife · cooking instructor (Jake's Table) · Atlanta GA  
> Email: `jake.thornton@greenrider.co`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Calendar | **42 contaminated fields**: event descriptions contain `"Part of Jake's Table Southern-fusion cooking classes"` and `"Notes from Jake Thornton's midwifery practice"` bleed across events (e.g., "Dentist" event description references midwifery) |
| 2 | 🔴 | Calendar | Invalid timezone: `-07:13` |
| 3 | 🔴 | Calendar | Duplicate events with suffixes (e.g., `"Dentist-9608"`) |
| 4 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 5 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 6 | 🟠 | Stripe | All `amount` values are strings |
| 7 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 8 | 🟠 | HubSpot | **10 deals** with temporal impossibility |
| 9 | 🟠 | GitHub | 9 duplicate labels (highest after phil-lane) |
| 10 | 🟡 | Slack | Reactions field is empty string `""` |
| 11 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 12 | 🟡 | WhatsApp | Contact name leaked into `template_name`: `"Jake Thornton"` |
| 13 | 🟡 | Home | Bare number naming: `01.tsv`, `16.pdf` |

**Strengths:** ✅ GitHub has no open+closed_at bug. ✅ Stripe charge IDs use Base62-like format (`ch_NdwstYeheRHzLTM2caK7`).

---

### james-davis
> Auto mechanic · Mustang restoration · El Paso TX  
> Email: `james.davis@Finthesiss.ai`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Calendar | 15,826 lines — very heavily bloated |
| 2 | 🟠 | Stripe | All `amount` values are strings |
| 3 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 4 | 🟠 | Stripe | Persona name embedded in IDs |
| 5 | 🟠 | HubSpot | 5 deals with temporal impossibility |
| 6 | 🟡 | Slack | Reactions field is empty string `""` |
| 7 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 8 | 🟡 | WhatsApp | `template_name` is empty string `""` |
| 9 | 🟡 | Home | Bare number naming scheme |

**Strengths:** ✅ GitHub issues have **persona-appropriate** titles (`"Refresh-token rotation under load"`). ✅ GitHub first ID is `3000001` (different from majority `9100001`). ✅ No GitHub duplicate labels. ✅ No open+closed_at bug.

---

### jason-campbell
> Cardiologist · TAVR research · Jacksonville FL  
> Email: `jason.campbell@Finthesiss.ai`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 4 | 🔴 | Calendar | 6,031 lines — bloated |
| 5 | 🟠 | Stripe | All `amount` values are strings |
| 6 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 7 | 🟠 | Stripe | Persona name embedded in IDs |
| 8 | 🟠 | GitHub | 3 duplicate labels |
| 9 | 🟠 | HubSpot | 1 deal with temporal impossibility |
| 10 | 🟡 | Slack | Reactions format: `:thumbsup:1` (emoji + count) |
| 11 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 12 | 🟡 | WhatsApp | `template_name` set to `"practice_update"` on all messages |
| 13 | 🟡 | Home | Bare number naming scheme (fewest files: 45) |

---

### jason-kim
> International trade (Kim Trade Services) · Akron OH  
> Email: not found in AGENTS.md

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 2 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 3 | 🟠 | Stripe | All `amount` values are strings |
| 4 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 5 | 🟠 | Calendar | 1 habit-dump event |
| 6 | 🟡 | Slack | Reactions format: `thumbsup` (simple name, no colons) |
| 7 | 🟡 | WhatsApp | `template_name` set to `"shipment_update"` on all messages |

**Strengths:** ✅ GitHub issues have **persona-appropriate** titles (`"Mobile nav menu doesn't close after tapping a link"`). ✅ No GitHub duplicate labels. ✅ No HubSpot temporal bugs. ✅ Spotify track IDs use **Base62 format** (correct). ✅ Airbnb listings are persona-coherent (Port Clinton/Marblehead/Catawba Island — Lake Erie area).

---

### jason-rivera
> Restaurant owner (Paterson/Wayne NJ) · commercial property  
> Email: `jason.rivera@Finthesiss.ai`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 4 | 🟠 | Stripe | All `amount` values are strings |
| 5 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 6 | 🟠 | GitHub | 3 duplicate labels |
| 7 | 🟠 | HubSpot | **8 deals** with temporal impossibility |
| 8 | 🟡 | Slack | Reactions field is empty string `""` |
| 9 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 10 | 🟡 | WhatsApp | `template_name` field missing entirely |
| 11 | 🟡 | Calendar | Smallest calendar: 722 lines |

---

### jennifer-long
> Pediatric OT (Long Pediatric Therapy) · Tacoma WA  
> Email: `jennifer.long@Finthesiss.ai`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 2 | 🔴 | Stripe | Shared charge IDs with 4 other personas: `ch_3Aurora01` (copy-paste cluster B) |
| 3 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 4 | 🟠 | Stripe | All `amount` values are strings |
| 5 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 6 | 🟠 | GitHub | 3 duplicate labels |
| 7 | 🟠 | HubSpot | 2 deals with temporal impossibility |
| 8 | 🟡 | Slack | Reactions format: `emoji:users` string |
| 9 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 10 | 🟡 | WhatsApp | `template_name` set to `"order_shipped"` on all messages |
| 11 | 🟡 | Home | `dNN` naming scheme |

**Strengths:** ✅ No open+closed_at bug in GitHub issues. ✅ Lowest Stripe `paid` count (7 — smallest dataset).

---

### jennifer-williams
> Poet · shift worker · Providence RI  
> Email: `jennifer.williams@Finthesiss.ai`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Stripe | Shared charge IDs with 4 other personas: `ch_3Aurora01` (copy-paste cluster B) |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 3 | 🟠 | Stripe | All `amount` values are strings |
| 4 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 5 | 🟠 | HubSpot | 1 deal with temporal impossibility |
| 6 | 🟡 | Slack | Reactions format: `emoji:users` string |
| 7 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 8 | 🟡 | WhatsApp | `template_name` set to `"order_shipped"` on all messages |
| 9 | 🟡 | Home | `dsk_NN` naming scheme (`dsk_01.xlsx`) |

**Strengths:** ✅ GitHub issues have **persona-appropriate** titles (`"Add the three winter poems to the collection page"`). ✅ No GitHub duplicate labels. ✅ No open+closed_at bug.

---

### jessica-spencer
> Interior designer (Spencer Interiors) · Phoenix/Scottsdale AZ  
> Email: `jessica.spencer@Finthesiss.ai`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 2 | 🔴 | Stripe | Shared charge IDs with 4 other personas: `ch_3Aurora01` (copy-paste cluster B) |
| 3 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 4 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 5 | 🔴 | Stripe | Product suffix duplication present (16 dups) |
| 6 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 7 | 🟠 | GitHub | 3 duplicate labels |
| 8 | 🟠 | HubSpot | 4 deals with temporal impossibility |
| 9 | 🟡 | Slack | Reactions format: `+1:1` (emoji + count) |
| 10 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 11 | 🟡 | WhatsApp | `template_name` contains description: `"Spencer Interiors: material sourcing update logged for this cycle."` |
| 12 | 🟡 | Home | `file_N` naming scheme |

**Strengths:** ✅ Stripe amounts are **integers** (1 of only 4 personas).

---

### jessica-taylor
> Freelance designer  
> Email: `jessica.taylor@Finthesiss.ai`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Stripe | **Massive templated duplication**: same 8 base charges duplicated with `-v9` through `-v20` suffixes, then cookie-cutter pattern repeats for 4 clients (Verdant Provisions, Pinnacle Collective, Bloom Skin Co, Kiln + Loom Ceramics) — exact same 20 line items with only client name changed |
| 2 | 🔴 | Stripe | Product suffix duplication present (16 dups) |
| 3 | 🟠 | Calendar | 3,571 lines — moderate |
| 4 | 🟡 | Slack | Reactions: `"reactions-13966"` (sequential ID string) |
| 5 | 🟡 | Spotify | Sequential track IDs: `track_0001` (unique format) |
| 6 | 🟡 | WhatsApp | `template_name`: `"template_name-54300"` (meta-reference) |

**Strengths:** ✅ Stripe amounts are **integers** (1 of only 4). ✅ GitHub issues have **persona-appropriate** titles. ✅ GitHub first ID is `3000001` (different from majority). ✅ No GitHub duplicate labels. ✅ No open+closed_at bug. ✅ No HubSpot temporal bugs.

---

### joan-hampton
> Midwife · Galway, Ireland  
> Email: `joan.hampton@Finthesiss.ai`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Spotify | **Identical library to margaret-farmer**: byte-for-byte copy starting with Bon Iver "Skinny Love" (`skinny.lovebon.iver`) |
| 2 | 🔴 | Stripe | Invoice impossible states: `amount_paid` (14900) > `amount_due` (12500) AND `amount_paid` (14900) > `amount_due` (13000) — two occurrences |
| 3 | 🔴 | Stripe | Shared charge IDs with 6 other personas: `ch_004d9b92879ce0aee8` (copy-paste cluster A) |
| 4 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` (irrelevant to midwifery) |
| 5 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 6 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 7 | 🟠 | Stripe | All `amount` values are strings |
| 8 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 9 | 🟠 | HubSpot | 5 deals with temporal impossibility |
| 10 | 🟠 | Calendar | 1 habit-dump event |
| 11 | 🟡 | Slack | Reactions field is empty string `""` |
| 12 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 13 | 🟡 | WhatsApp | `template_name` is empty string `""` |

**Strengths:** ✅ No GitHub duplicate labels. ✅ Excellent AGENTS.md (EUR thresholds, Galway-specific routing).

---

### joanne-lawton
> Retired nurse / herbalist · Portland ME  
> Email: `joanne.lawton@gmail.com`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 2 | 🔴 | Stripe | Shared charge IDs with 4 other personas: `ch_3Aurora01` (copy-paste cluster B) |
| 3 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 4 | 🟠 | Stripe | All `amount` values are strings |
| 5 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 6 | 🟠 | GitHub | 3 duplicate labels |
| 7 | 🟠 | HubSpot | 1 deal with temporal impossibility |
| 8 | 🟡 | Slack | Reactions missing/empty |
| 9 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 10 | 🟡 | WhatsApp | `template_name` is empty string `""` |

**Strengths:** ✅ No open+closed_at bug in GitHub issues.

---

### john-patel
> ER physician · Houston TX  
> Email: `john.patel@gmail.com`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Spotify | **Shared library with juan-hernandez**: both start with `so.whatmiles.da` (Miles Davis "So What") — identical first tracks |
| 2 | 🔴 | Stripe | Shared charge IDs with 4 other personas: `ch_3Aurora01` (copy-paste cluster B) |
| 3 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 4 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 5 | 🟠 | Stripe | All `amount` values are strings |
| 6 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 7 | 🟠 | GitHub | 3 duplicate labels |
| 8 | 🟠 | HubSpot | 3 deals with temporal impossibility |
| 9 | 🟡 | Slack | Reactions format: `emoji:users` string |
| 10 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 11 | 🟡 | WhatsApp | Contact name leaked into `template_name`: `"Priya Patel"` |

---

### jordan-mcdaniel
> Carpenter · Wilmington NC  
> Email: `jordan.mcdaniel@gmail.com`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🟠 | Stripe | All `amount` values are strings |
| 2 | 🟠 | Slack | Reactions format: `emoji:users` string (`"wave:U04DERRICK,U04TONYA"`) |
| 3 | 🟡 | Spotify | Track IDs use Base62 format ✅ |
| 4 | 🟡 | WhatsApp | `template_name` contains message type: `"text"` |

**Strengths:** ✅ GitHub issues have **persona-appropriate** titles (`"tour dates page still shows the october show"`). ✅ GitHub first ID is `3000001`. ✅ No GitHub duplicate labels. ✅ No open+closed_at bug. ✅ No HubSpot temporal bugs. ✅ Spotify uses correct Base62 IDs. ✅ Persona-specific charge IDs: `ch_JmcHollis01`. **One of the cleanest personas overall.**

---

### joseph-fields
> HVAC technician · Columbus OH  
> Email: `joseph.fields@gmail.com`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 4 | 🟠 | Stripe | All `amount` values are strings |
| 5 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 6 | 🟠 | GitHub | 3 duplicate labels |
| 7 | 🟠 | HubSpot | 2 deals with temporal impossibility |
| 8 | 🟡 | Slack | Reactions field contains non-reaction text: `"Notes from the job site; parts ordered and tracked."` |
| 9 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 10 | 🟡 | WhatsApp | Contact name leaked into `template_name`: `"Megan Fields"` |

---

### juan-hernandez
> Retired · amateur historian · Gettysburg PA  
> Email: `juan.hernandez@gmail.com`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Spotify | **Shared library with john-patel**: both start with `so.whatmiles.da` (Miles Davis "So What") |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 4 | 🟠 | Stripe | All `amount` values are strings |
| 5 | 🟠 | Stripe | Timestamps as **ISO 8601** strings |
| 6 | 🟠 | Calendar | 1 habit-dump event |
| 7 | 🟡 | Slack | Reactions missing/empty |
| 8 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 9 | 🟡 | WhatsApp | `template_name` set to `"appointment_reminder"` on all messages |

**Strengths:** ✅ GitHub issues have **persona-appropriate** titles (`"1900 census: surname 'Hollis' misspelled"` — excellent for historian). ✅ No GitHub duplicate labels. ✅ No HubSpot temporal bugs. ✅ Smallest Airbnb listing file (193 lines).

---

### justin-rivera
> IT professional · West Hartford CT  
> Email: `justin.rivera@gmail.com`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 4 | 🟠 | Stripe | All `amount` values are strings |
| 5 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 6 | 🟠 | GitHub | 3 duplicate labels |
| 7 | 🟡 | Slack | Reactions: persona-prefixed ID `"justin-rivera-default-0000"` |
| 8 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 9 | 🟡 | WhatsApp | Persona-prefixed IDs on ALL messages: `"justin-rivera-default-0000"` |

**Strengths:** ✅ No HubSpot temporal bugs.

---

### margaret-farmer
> Ceramicist · Kyoto, Japan  
> Email: not found in AGENTS.md

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Spotify | **Identical library to joan-hampton**: byte-for-byte copy starting with Bon Iver "Skinny Love" (`skinny.lovebon.iver`) |
| 2 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` (irrelevant to ceramics) |
| 3 | 🔴 | Stripe | Shared charge IDs with 6 other personas: `ch_004d9b92879ce0aee8` (copy-paste cluster A) |
| 4 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 5 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 6 | 🟠 | Stripe | All `amount` values are strings |
| 7 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 8 | 🟠 | HubSpot | **14 deals** with temporal impossibility (worst of all personas) |
| 9 | 🟡 | Slack | Reactions format: `emoji:users` string |
| 10 | 🟡 | Spotify | Track IDs are concatenated slugs with artist artifacts (`bon.iveriver`) |
| 11 | 🟡 | WhatsApp | `template_name` is empty string `""` |
| 12 | 🟡 | Home | Three-digit naming: `027.pdf`, `031.tsv` |

**Strengths:** ✅ No GitHub duplicate labels. ✅ Excellent AGENTS.md (JPY 40000 threshold, Kyoto-specific).

---

### nate-wright
> Physician assistant · Harborview ED · Stamford CT  
> Email: `nate.wright@Finthesiss.ai`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Calendar | **427 contaminated fields**: `"Working note — Harborview ED, Stamford CT"` and medical notes appearing in `recurrence` and `description` fields of unrelated events |
| 2 | 🔴 | Calendar | **56 habit-dump events**: `"Black drip coffee on waking, two to three cups across the day"` and `"Vitamin D3 2000 IU and fish oil 1000 mg"` as individual daily calendar events |
| 3 | 🔴 | Stripe | **24 contaminated fields**: `"Working note"` text appearing in Stripe data fields |
| 4 | 🔴 | Stripe | Timestamp field contains **text instead of timestamp**: `"Working note — Harborview ED, Stamford CT"` in `created` field |
| 5 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 6 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 7 | 🟠 | Stripe | All `amount` values are strings |
| 8 | 🟠 | Stripe | Persona name embedded in IDs |
| 9 | 🟠 | GitHub | 3 duplicate labels |
| 10 | 🟠 | HubSpot | 1 deal with temporal impossibility |
| 11 | 🟡 | Slack | Reactions format: `emoji:users` string |
| 12 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 13 | 🟡 | WhatsApp | `template_name` contains timestamp: `"2025-10-02T15:18:00Z"` |

**⚠️ nate-wright is the most data-contaminated persona in the set.** SOUL.md content (medical practice notes, daily habits) has leaked across multiple API files.

---

### paul-rivera
> Retired pilot · Scottsdale AZ  
> Email: `paul.rivera@voissync.ai`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Stripe | Shared charge IDs with 6 other personas: `ch_004d9b92879ce0aee8` (copy-paste cluster A) |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 4 | 🟠 | Stripe | All `amount` values are strings |
| 5 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 6 | 🟡 | Slack | Reactions field is empty string `""` |
| 7 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 8 | 🟡 | WhatsApp | `template_name` is empty string `""` |
| 9 | 🟡 | Home | Duplicate files: `a06(1).pptx`, `file_4(1).pdf`, `file_5(1).pdf` (most home files: 67) |

**Strengths:** ✅ GitHub issues have **persona-appropriate** titles (`"flightlog-cli: parse logbook entries with non-UTC timestamps"` — excellent for pilot). ✅ No GitHub duplicate labels. ✅ No HubSpot temporal bugs.

---

### phil-lane
> Front desk · Birchwood Valley Inn · Brattleboro VT  
> Email: not found in AGENTS.md

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 4 | 🔴 | Calendar | 12,497 lines — heavily bloated |
| 5 | 🟠 | Stripe | All `amount` values are strings |
| 6 | 🟠 | Stripe | Timestamps as **ISO 8601** strings |
| 7 | 🟠 | Stripe | Persona name embedded in IDs |
| 8 | 🟠 | GitHub | **11 duplicate labels** (worst of all personas) |
| 9 | 🟠 | HubSpot | 1 deal with temporal impossibility |
| 10 | 🟡 | Slack | Reactions: 👍 emoji literal |
| 11 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 12 | 🟡 | WhatsApp | Contact name leaked into `template_name`: `"Phil Lane"` |
| 13 | 🟡 | Home | `file_N` naming scheme |

---

### sam-osborne
> Detective / metalworker · Gallup NM  
> Email: not found in AGENTS.md (uses `@voissync.ai`)

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 2 | 🔴 | Calendar | 6,766 lines — bloated |
| 3 | 🟠 | Stripe | Timestamps as **ISO 8601** strings |
| 4 | 🟠 | Stripe | Persona name embedded in IDs |
| 5 | 🟡 | Slack | Reactions format: `+1` (simple name) |
| 6 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 7 | 🟡 | WhatsApp | `template_name` field missing entirely |

**Strengths:** ✅ Stripe amounts are **integers** (1 of only 4 personas). ✅ GitHub issues have **persona-appropriate** titles (`"Tweak homepage hero copy"`). ✅ No HubSpot temporal bugs. ✅ No GitHub duplicate labels. ✅ Largest Airbnb listing file (481 lines — most complete).

---

### shannon-perry
> Sports medicine clinician · track coach · Birmingham AL  
> Email: `shannon.perry@Finthesiss.ai`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 2 | 🟠 | Stripe | All `amount` values are strings |
| 3 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 4 | 🟡 | Slack | Reactions format: `emoji:users` string |
| 5 | 🟡 | WhatsApp | `template_name` set to `"family_checkin"` on all messages |

**Strengths:** ✅ GitHub issues have **persona-appropriate** titles (`"Add column for wind-legal vs wind-aided 100m marks"` — excellent for track coach). ✅ No GitHub duplicate labels. ✅ No HubSpot temporal bugs. ✅ Spotify track IDs use **Base62 format** (correct). ✅ Stripe `balance.json` has proper nested structure with `object`, `livemode`, `available`, `pending` fields — **only well-formed Stripe file in entire dataset**. ✅ Excellent WhatsApp content quality. **One of the cleanest personas overall.**

---

### shawn-dawson
> Union steward (Irongate/Local 247) · church deacon · softball coach  
> Email: not found in AGENTS.md

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Stripe | Shared charge IDs with 6 other personas: `ch_004d9b92879ce0aee8` (copy-paste cluster A) |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 4 | 🟠 | Stripe | All `amount` values are strings |
| 5 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 6 | 🟡 | Slack | Reactions format: `eyes:3` (emoji + count) |
| 7 | 🟡 | WhatsApp | `template_name` is empty string `""` |
| 8 | 🟡 | Home | Letter+number naming: `a13.pdf`, `e4.xlsx` |

**Strengths:** ✅ GitHub issues have **persona-appropriate** titles (`"Fix BMI rounding for metric units"`). ✅ No GitHub duplicate labels. ✅ No HubSpot temporal bugs. ✅ Spotify track IDs use **Base62 format** (correct).

---

### steve-petersen
> Retired teacher · union board · Mon Valley (Pittsburgh area)  
> Email: `steve.petersen@Finthesiss.ai`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 2 | 🔴 | Stripe | Shared charge IDs with 6 other personas: `ch_004d9b92879ce0aee8` (copy-paste cluster A) |
| 3 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 4 | 🔴 | Slack | **Message duplication**: lines 6-8 duplicated at lines 51-53 (same welding class story repeated) |
| 5 | 🔴 | Calendar | Habit-dump: `"Wake up, black coffee, Mon Valley Herald"` as daily events |
| 6 | 🟠 | Stripe | All `amount` values are strings |
| 7 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 8 | 🟠 | HubSpot | 3 deals with temporal impossibility |
| 9 | 🟡 | Slack | Reactions format: `emoji:users` string |
| 10 | 🟡 | WhatsApp | `template_name` set to `"order_shipped"` on all messages |

**Strengths:** ✅ No open+closed_at bug in GitHub issues. ✅ Spotify track IDs use **Base62 format** (correct).

---

### stuart-myer
> Brewery owner (Driftwood Brewing) · environmental activist · Portland OR  
> Email: not found in AGENTS.md

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | GitHub | Template contamination — `"Reduce p99 latency on /search endpoint"` |
| 2 | 🔴 | GitHub | Shared first issue ID `9100001` |
| 3 | 🔴 | GitHub | Open issues have `closed_at` dates |
| 4 | 🔴 | Calendar | 10,472 lines — heavily bloated |
| 5 | 🟠 | Stripe | All `amount` values are strings |
| 6 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 7 | 🟠 | GitHub | 3 duplicate labels |
| 8 | 🟡 | Slack | Reactions format: `beers` (simple name — persona-appropriate at least) |
| 9 | 🟡 | Spotify | Track IDs are concatenated slugs |
| 10 | 🟡 | WhatsApp | `template_name` set to `"order_update"` on all messages |
| 11 | 🟡 | Home | Bare number naming: `12.png`, `18.docx` |

**Strengths:** ✅ Stripe charge IDs use Base62-like format (`ch_jBWLsUbixrCR86CD`).

---

### yves-quinn
> Hotel worker / caterer · Beaverton OR  
> Email: `yves.quinn@voissync.ai`

| # | Sev | API | Issue |
|---|-----|-----|-------|
| 1 | 🔴 | Calendar | 7,546 lines — bloated |
| 2 | 🔴 | Calendar | **78 habit-dump events** |
| 3 | 🟠 | Stripe | All `amount` values are strings |
| 4 | 🟠 | Stripe | Timestamps as Unix epoch strings |
| 5 | 🟠 | Stripe | Human-readable subscription IDs: `sub_cdn_Pearl` |
| 6 | 🟡 | Slack | Reactions field is empty string `""` |
| 7 | 🟡 | WhatsApp | `template_name` is empty string `""` |
| 8 | 🟡 | Home | `BN` naming scheme: `B10.pdf`, `B18.xlsx` |

**Strengths:** ✅ GitHub issues have **persona-appropriate** titles (`"Update fall market schedule"`). ✅ GitHub first ID is `3000001`. ✅ No GitHub duplicate labels. ✅ No open+closed_at bug. ✅ No HubSpot temporal bugs.

---

## §3 — Cross-Persona Copy-Paste Clusters

### Stripe Charge ID Cluster A
**Shared ID**: `ch_004d9b92879ce0aee8`  
**Affected**: asha-gallegos, brandon-kelly, joan-hampton, margaret-farmer, paul-rivera, shawn-dawson, steve-petersen  
**Impact**: 7 personas share identical charge records — evidence of data copy-paste during generation

### Stripe Charge ID Cluster B
**Shared ID**: `ch_3Aurora01`  
**Affected**: jennifer-long, jennifer-williams, jessica-spencer, joanne-lawton, john-patel  
**Impact**: 5 personas share identical charge records

### GitHub Issue ID Cluster
**Shared ID**: `9100001`  
**Affected**: 29 of 36 personas  
**Impact**: Nearly all personas start their issues list from the same seed record

### Spotify Library Duplicates
- **joan-hampton ↔ margaret-farmer**: Identical track libraries (Bon Iver "Skinny Love" first)
- **john-patel ↔ juan-hernandez**: Identical first tracks (Miles Davis "So What")
- **Suspicious**: `duration_ms: "179447"` appears as first-track duration in multiple unrelated personas

---

## §4 — Email Domain Anomalies

| Domain | Personas | Issue |
|--------|----------|-------|
| `Finthesiss.ai` | 10+ | Typo: "Finthesiss" (double 's'). Shared across unrelated personas (midwife, church custodian, cardiologist, poet) |
| `Greenridertech.com` | brian-hall, grace-hatfield | Capitalization inconsistent |
| `Greenridertech.co` | angela-peterson, brandon-kelly | Different TLD from `.com` variant |
| `greenridertech.com` | brian-patterson | Different capitalization from others |
| `greenrider.co` | jake-thornton | Yet another variant |
| `voissync.ai` | paul-rivera, sam-osborne, yves-quinn | Only 3 personas |
| `gmail.com` | joanne-lawton, john-patel, jordan-mcdaniel, joseph-fields, juan-hernandez, justin-rivera | 6 personas — more realistic but shared |
| Not found | 15 personas | Email not set in AGENTS.md |

---

## §5 — Persona Quality Rankings

### 🏆 Cleanest Personas (fewest issues)
1. **jordan-mcdaniel** — 4 issues, correct Spotify IDs, persona-appropriate GitHub, no HubSpot bugs
2. **shannon-perry** — 5 issues, correct Spotify IDs, proper Stripe balance file, excellent content
3. **asha-gallegos** — 7 issues (but has invoice bug), correct Stripe integers, unique GitHub IDs
4. **jason-kim** — 7 issues, correct Spotify IDs, persona-coherent Airbnb data
5. **shawn-dawson** — 8 issues, correct Spotify IDs, no HubSpot bugs

### ⚠️ Most Problematic Personas (most/worst issues)
1. **nate-wright** — 13 issues including 427 contaminated calendar fields, Stripe data contamination, habit dumping across APIs
2. **brian-hall** — 14 issues including 21,542-line calendar with 855 habit events
3. **joan-hampton** — 13 issues including copied Spotify library, 2 invoice bugs, shared Stripe IDs
4. **margaret-farmer** — 12 issues including copied Spotify library, 14 HubSpot temporal bugs, shared Stripe IDs
5. **jake-thornton** — 13 issues including 42 contaminated calendar fields, 10 HubSpot temporal bugs

---

## §6 — Issue Frequency Summary

| Issue | Count | % of Personas |
|-------|-------|---------------|
| Stripe `paid` as string | 36/36 | 100% |
| Stripe missing `object` field | 36/36 | 100% |
| OpenWeather string types | 36/36 | 100% |
| Airbnb string types | 36/36 | 100% |
| GitHub labels as semicolons | 36/36 | 100% |
| Slack reactions wrong format | 36/36 | 100% |
| WhatsApp template_name misused | 36/36 | 100% |
| Stripe amounts as strings | 32/36 | 89% |
| GitHub shared issue ID 9100001 | 29/36 | 81% |
| GitHub open+closed_at bug | 26/36 | 72% |
| GitHub template contamination | 25/36 | 69% |
| Spotify concatenated slug IDs | 27/36 | 75% |
| GitHub duplicate labels | 20/36 | 56% |
| HubSpot temporal impossibility | 19/36 | 53% |
| Calendar >5000 lines (bloated) | 14/36 | 39% |
| Stripe persona-embedded IDs | 12/36 | 33% |
| Stripe shared charge IDs | 12/36 | 33% |
| Calendar habit-dump events | 6/36 | 17% |
| Stripe ISO 8601 (minority format) | 8/36 | 22% |
| Stripe product duplication | 4/36 | 11% |
| Calendar field contamination | 2/36 | 6% |
| Stripe invoice impossible state | 2/36 | 6% |
| Calendar backtick contamination | 1/36 | 3% |
| Slack message duplication | 1/36 | 3% |
