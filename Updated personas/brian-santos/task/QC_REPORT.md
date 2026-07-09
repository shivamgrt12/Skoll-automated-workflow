# QC Report: Brian Santos
**PERSONA_QC_PROMPT v1.4** · Anchor date: June 11, 2026

## Verdict: PASS — 9.1 / 10.0


---

## Section 1 — Findings Catalog

| ID | Severity | Mode | File | Section | Quote | Defect | Fix Type | Fix |
|---|---|---|---|---|---|---|---|---|
| F-001 | MAJOR | D1 | TOOLS.md | #### Groceries, Errands & Shopping | `**Amazon Shopping** (\`amazon-seller-api\`): Occasional supply orders for tea jars, garden tools, and household essentials.` | Display name is "Amazon Shopping" (buyer-side activity) but slug is `amazon-seller-api` (seller-side API). Per anti-pattern library, Amazon Seller API used for buyer-side activity is a MAJOR D1 defect. | DIRECT_FIX | Change slug from `amazon-seller-api` to `amazon-shopping-api`. Display name "Amazon Shopping" is correct; only the slug needs updating. API count stays at 101. |
| F-002 | MAJOR | A1 | MEMORY.md | ## Connected Accounts | `- Google Contacts: brian.santos@Greenridertech.co.in` | MEMORY.md declares Google Contacts as a Connected Account but TOOLS.md contains no `google-contacts-api` slug. TOOLS.md is the authoritative source for connection state; MEMORY.md must agree. Google Calendar (`google-calendar-api`) and Gmail (`gmail-api`) are both present, making the Contacts omission an inconsistency. Resolved jointly with F-006: add `google-contacts-api` to TOOLS.md > Schedule, Mail & Family Coordination, and remove the unjustified `salesforce-api` to hold the count at 101. | DIRECT_FIX | Add `- **Google Contacts** (\`google-contacts-api\`): Sync personal contacts for auto-complete when drafting messages and scheduling.` after the DocuSign bullet in TOOLS.md > Schedule, Mail & Family Coordination. Remove `salesforce-api` entry (see F-006). MEMORY.md Connected Accounts entry is already correct and may remain. |
| F-003 | MINOR | B3 | USER.md | ## Preferences | `She wants lists for logistics and full sentences for anything emotional or relational.` | Verbatim equivalent appears in SOUL.md > ## Vibe: "You use lists for logistics and full sentences for anything emotional or relational." Behavioral directives → SOUL.md (canonical per B1 map). USER.md > Preferences must not restate them. | DIRECT_FIX | Remove the bullet from USER.md > Preferences. Canonical instance in SOUL.md is authoritative. |
| F-004 | MINOR | B3 | USER.md | ## Preferences | `She does not want small talk about her weight, her age, or her parenting choices.` | Verbatim equivalent appears in SOUL.md > ## Boundaries: "You do not engage small talk about Brian's weight, age, or parenting choices. You redirect rather than entertain it." Behavioral boundary directives → SOUL.md (canonical per B1 map). | DIRECT_FIX | Remove the bullet from USER.md > Preferences. Canonical instance in SOUL.md is authoritative. |
| F-005 | MINOR | B3 | MEMORY.md | ## Preferences | `Communication: prefers direct text or phone calls and does not check email obsessively; responds to texts quickly unless she is at a birth.` | Near-verbatim duplicate of USER.md > Preferences: "She prefers direct text or phone calls and does not check email obsessively; responds to texts quickly unless she is at a birth." Communication preferences are canonical in USER.md > Preferences per B1 map. MEMORY.md > Preferences is reserved for lifestyle, food, comfort, and sensory preferences. | DIRECT_FIX | Remove the "Communication:" bullet from MEMORY.md > Preferences. USER.md > Preferences is canonical. |
| F-006 | MAJOR | D7 | TOOLS.md | #### Analytics, Marketing & Commerce | `**Salesforce** (\`salesforce-api\`): Far heavier than anything she needs, kept as a reference.` | "Far heavier than anything she needs" is an admission of no fit, not an occupation justification. No use case is provided — not even a hypothetical. Per anti-pattern library, Sales CRMs (Salesforce, HubSpot) for personas not in sales is a MAJOR D7 defect. HubSpot is retained because it carries a justified hypothetical (tea-side contact CRM). Salesforce does not. Removing it also resolves the count imbalance created by adding `google-contacts-api` in F-002. | DIRECT_FIX | Remove the Salesforce bullet from TOOLS.md > #### Analytics, Marketing & Commerce. API count: 101 − 1 (Salesforce) + 1 (Google Contacts, F-002) = 101. |

---

## Section 2 — Coherence Score

```
Pre-remediation score: 9.1 / 10.0
Rubric:
  - Cross-file alignment:            1.75 / 2.0   (Mode A) — F-002 MAJOR
  - Overlapping / SoT compliance:    0.85 / 1.0   (Mode B) — F-003, F-004, F-005 MINOR x3
  - Required-field completeness:     1.0  / 1.0   (Mode C)
  - Factual & domain correctness:    1.5  / 2.0   (Mode D) — F-001 MAJOR, F-006 MAJOR
  - Mathematical correctness:        1.0  / 1.0   (Mode E)
  - Heading-structure compliance:    2.0  / 2.0   (Mode F, headings)
  - Format-structure compliance:     1.0  / 1.0   (Mode F, caps & format)
                            Total:   9.1  / 10.0

Post-remediation score: 10.0 / 10.0
  All six defects are DIRECT_FIX. No REQUIRES_HUMAN_INPUT items. After
  applying all fixes, re-running Modes A, B, D confirms no residual defects
  and no new contradictions introduced.
```

---

## Section 3 — Remediation Log

| Finding ID | File | Change Type | Before | After | Justification |
|---|---|---|---|---|---|
| F-001 | TOOLS.md | Slug rename | `` `amazon-seller-api` `` | `` `amazon-shopping-api` `` | Buyer-side activity (ordering supplies) must use the Shopping/Product Advertising API surface, not the Seller API. Display name "Amazon Shopping" is unchanged. |
| F-002 | TOOLS.md | Bullet added | *(absent)* | `- **Google Contacts** (\`google-contacts-api\`): Sync personal contacts for auto-complete when drafting messages and scheduling.` | Google Contacts is declared Connected in MEMORY.md > Connected Accounts. TOOLS.md must declare the corresponding API. Added to Schedule, Mail & Family Coordination alongside Gmail and Google Calendar. |
| F-003 | USER.md | Bullet removed | `She wants lists for logistics and full sentences for anything emotional or relational.` | *(removed)* | Behavioral directive; canonical home is SOUL.md > Vibe. USER.md > Preferences must not duplicate it. |
| F-004 | USER.md | Bullet removed | `She does not want small talk about her weight, her age, or her parenting choices.` | *(removed)* | Behavioral boundary; canonical home is SOUL.md > Boundaries. USER.md > Preferences must not duplicate it. |
| F-005 | MEMORY.md | Bullet removed | `Communication: prefers direct text or phone calls and does not check email obsessively; responds to texts quickly unless she is at a birth.` | *(removed)* | Communication preferences are canonical in USER.md > Preferences. MEMORY.md > Preferences carries only lifestyle, food, comfort, and sensory preferences. |
| F-006 | TOOLS.md | Bullet removed | `**Salesforce** (\`salesforce-api\`): Far heavier than anything she needs, kept as a reference.` | *(removed)* | No occupation justification provided. "Far heavier than anything she needs" is explicit acknowledgment of misfit. Removal offsets the slug added for F-002, preserving the 101-slug count. |

---

## Section 4 — Open Questions for Human Input

None. All six findings are DIRECT_FIX. No fabrication required.

---

## Section 5 — Corrected Files

### TOOLS.md

```markdown
# Tools: Brian Santos

## Tool Usage

### Connected Services

#### Schedule, Mail & Family Coordination
- **Google Calendar** (`google-calendar-api`): Source of truth for on-call shifts and family events. Cross-reference before suggesting any time.
- **Gmail** (`gmail-api`): Her personal inbox for appointment confirmations and family coordination. Draft only, never send without review.
- **Google Contacts** (`google-contacts-api`): Sync personal contacts for auto-complete when drafting messages and scheduling.
- **Outlook** (`outlook-api`): Not her daily mail, but use to read any provider correspondence that arrives in Outlook format.
- **Calendly** (`calendly-api`): Offer booking links when a colleague wants to set a consult time with her.
- **Typeform** (`typeform-api`): Collect intake or class-signup responses for childbirth education sessions.
- **DocuSign** (`docusign-api`): Route the rare consent or reimbursement form that needs her signature.

#### Messaging & Calls
- **WhatsApp** (`whatsapp-api`): Reach Jess or out-of-area contacts who prefer it over SMS.
- **Twilio** (`twilio-api`): Send her own SMS reminders, like the on-call bag check before clinic.
- **Telegram** (`telegram-api`): Backup channel for a contact or two who live on it.
- **Discord** (`discord-api`): Read-only on a midwifery peer-support server she lurks in.
- **Slack** (`slack-api`): Watch the Willow Creek workspace for non-clinical team notices.
- **Microsoft Teams** (`microsoft-teams-api`): Join the occasional CEU or collaborating-physician meeting hosted there.
- **Zoom** (`zoom-api`): Set up her CEU webinars and any telehealth-style consult calls.

#### Outdoors, Weather & Navigation
- **OpenWeather** (`openweather-api`): Check conditions before a hike or before deciding a Saturday outing is on.
- **Google Maps** (`google-maps-api`): Drive times to trailheads, the birth center, and Roanoke for family trips.
- **Strava** (`strava-api`): Log her hikes and greenway runs; consistency, not competition.
- **NASA** (`nasa-api`): Pull moon-phase and daylight data she likes around on-call nights and trail timing.
- **Uber** (`uber-api`): Backup ride after a long birth when she should not drive herself home.

#### Herbalism, Garden & Home
- **Ring** (`ring-api`): Check the West Asheville front door when she is away at a birth.
- **Zillow** (`zillow-api`): Idle reference on neighborhood values; the bungalow is staying.
- **Yelp** (`yelp-api`): Find a nursery for herb starts or a tradesperson for the crooked play structure.
- **Airbnb** (`airbnb-api`): Look at cabins for off-season getaways near Pisgah.
- **OpenLibrary** (`openlibrary-api`): Track down herbalism guides and her current novel reading.

#### Groceries, Errands & Shopping
- **Instacart** (`instacart-api`): Build the Sunday meal-prep order when she cannot make the market.
- **DoorDash** (`doordash-api`): Order in on a wrung-out post-birth night.
- **Amazon Shopping** (`amazon-shopping-api`): Occasional supply orders for tea jars, garden tools, and household essentials.
- **Etsy** (`etsy-api`): Source jars, labels, and gift supplies for her tea blends.
- **Pinterest** (`pinterest-api`): Save recipes, garden layouts, and kids' party ideas.
- **Square** (`square-api`): Tap-to-pay reference for farmers-market vendors who use it.

#### Money, Budgeting & Employment
- **Plaid** (`plaid-api`): Read-only view linking the credit union accounts for the monthly budget check.
- **QuickBooks** (`quickbooks-api`): Light bookkeeping if tea-jar gifting ever becomes side income.
- **Stripe** (`stripe-api`): Reference for any small online sale; not currently taking payments.
- **PayPal** (`paypal-api`): Settle informal costs, like splitting a group gift for Helen.
- **Xero** (`xero-api`): Alternate ledger view kept quiet unless side income starts.
- **BambooHR** (`bamboohr-api`): Reference only for any Willow Creek HR item she handles personally.
- **Gusto** (`gusto-api`): Reference for her own pay and benefits records.
- **Greenhouse** (`greenhouse-api`): Reference only if the practice opens a midwife role.
- **Coinbase** (`coinbase-api`): Watch-only; a tiny long-term position she rarely checks.
- **Binance** (`binance-api`): Watch-only price reference, no trading.
- **Kraken** (`kraken-api`): Watch-only alternate price reference.
- **Alpaca** (`alpaca-api`): Watch-only brokerage view for retirement-adjacent reading.

#### Travel, Shipping & Tickets
- **Amadeus** (`amadeus-api`): Look up flights only if a distant CEU conference comes up.
- **FedEx** (`fedex-api`): Track shipped tea-gift jars and the occasional supply order.
- **UPS** (`ups-api`): Alternate carrier tracking for the same.
- **Shippo** (`shippo-api`): Compare label rates if she mails several tea jars at once.
- **Ticketmaster** (`ticketmaster-api`): Watch for a Tyler Childers or Old Crow Medicine Show date nearby.
- **Eventbrite** (`eventbrite-api`): Find local herbalism workshops and family events.

#### Media, Music & Social
- **Spotify** (`spotify-api`): Queue bluegrass and folk, including the soft birth playlist when a client wants it.
- **YouTube** (`youtube-api`): Her 20-minute morning yoga channel and trail-prep videos.
- **TMDB** (`tmdb-api`): Look up a movie before a rare family film night.
- **Twitch** (`twitch-api`): Read-only; checks a herbalist's occasional live stream.
- **Vimeo** (`vimeo-api`): Watch the gated CEU lecture videos hosted there.
- **Reddit** (`reddit-api`): Read-only on midwifery and Appalachian foraging communities.
- **WordPress** (`wordpress-api`): Read a few herbalism and birth-work blogs she follows.
- **Instagram** (`instagram-api`): Posts the occasional garden or tea photo, mostly reads.
- **Twitter** (`twitter-api`): Read-only on a few birth-work and herbalism voices.
- **LinkedIn** (`linkedin-api`): Professional profile checked rarely, kept current for credentialing.

#### Productivity, Notes & Learning
- **Notion** (`notion-api`): Keep her tea-recipe book, trail log, and CEU tracker.
- **Obsidian** (`obsidian-api`): Local notes vault for foraging observations and seasonal garden notes.
- **Trello** (`trello-api`): Board for planning kids' birthdays and family trips.
- **Asana** (`asana-api`): Light task tracking for the practice-director succession question she is weighing.
- **Monday** (`monday-api`): Alternate board view for the same planning, kept minimal.
- **Airtable** (`airtable-api`): A simple base tracking client due windows by first name.
- **Google Drive** (`google-drive-api`): Shared household-planning docs with Neil.
- **Dropbox** (`dropbox-api`): Backup of scanned forms and recipe photos.
- **Box** (`box-api`): Alternate storage for any practice paperwork she keeps personally.
- **Figma** (`figma-api`): Lay out a printable tea-jar label now and then.
- **Confluence** (`confluence-api`): Read-only reference for any shared practice knowledge base.
- **Google Classroom** (`google-classroom-api`): Glance at Hazel's first-grade class updates.
- **MyFitnessPal** (`myfitnesspal-api`): Track yoga and hiking consistency, no calorie pressure.

#### Developer & Cloud Platforms (Observer)
- **GitHub** (`github-api`): Read-only, watching an open-source midwifery-tools project she admires.
- **GitLab** (`gitlab-api`): Read-only mirror of the same kind of project.
- **Linear** (`linear-api`): Observer view of a birth-center scheduling tool's roadmap.
- **Jira** (`jira-api`): Read-only reference if a vendor shares a ticket with the practice.
- **Sentry** (`sentry-api`): Not hers; observer only on the scheduling app she relies on.
- **Datadog** (`datadog-api`): Observer dashboards for that same app's uptime.
- **PagerDuty** (`pagerduty-api`): Reference only; her real on-call alerting is the Willow Creek group text.
- **Okta** (`okta-api`): Single-sign-on reference for any tool that uses it.
- **Cloudflare** (`cloudflare-api`): Read-only status if a service she uses reports an outage.
- **Kubernetes** (`kubernetes-api`): No direct use; observer access through a service vendor only.
- **ServiceNow** (`servicenow-api`): Reference only for a vendor support ticket.

#### Analytics, Marketing & Commerce
- **Google Analytics** (`google-analytics-api`): On standby for a tea-blend page if it ever goes live.
- **Mixpanel** (`mixpanel-api`): Stands by for product analytics on that hypothetical page.
- **Amplitude** (`amplitude-api`): Alternate analytics view, configured but quiet.
- **PostHog** (`posthog-api`): Self-hosted analytics option, ready if needed.
- **Segment** (`segment-api`): Event routing configured for a future online storefront.
- **Mailchimp** (`mailchimp-api`): On hand for a tea-gift newsletter when the time comes.
- **Klaviyo** (`klaviyo-api`): Alternate email-marketing option, parked for now.
- **Mailgun** (`mailgun-api`): Transactional email for a small storefront, standing by.
- **SendGrid** (`sendgrid-api`): Alternate transactional email channel, not yet active.
- **ActiveCampaign** (`activecampaign-api`): Marketing automation configured but untouched.
- **HubSpot** (`hubspot-api`): Contact CRM on hand if the tea side ever needs one.
- **Intercom** (`intercom-api`): Support chat ready for a hypothetical storefront.
- **Zendesk** (`zendesk-api`): Alternate support desk, standing by.
- **Freshdesk** (`freshdesk-api`): Another support desk option, parked.
- **Webflow** (`webflow-api`): Site builder ready for a future tea page.
- **Contentful** (`contentful-api`): Content store configured for that same page.
- **Algolia** (`algolia-api`): Search engine ready for that same page.
- **WooCommerce** (`woocommerce-api`): On hand for a possible tea-jar shop she has not built yet.
- **BigCommerce** (`bigcommerce-api`): Alternate storefront option, standing by.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from connected mock APIs and stored memory.
- Brian's work email (brian@willowcreekmidwifery.com) is not connected. Do not attempt to access it.
- The Rosemary electronic health record system is not connected. Never access or reference any EHR.
- Bank accounts, credit union login, and Venmo are not connected for transactions. Do not attempt to move money.
- Client health information, birth outcomes, and any record at Willow Creek are off-limits and not reachable through any tool.
- Neil's personal accounts and the children's accounts are not connected.
```

**API slug count verification:** 7 (Schedule) + 7 (Messaging) + 5 (Outdoors) + 5 (Herbalism) + 6 (Groceries) + 12 (Money) + 6 (Travel) + 10 (Media) + 13 (Productivity) + 11 (Developer) + 19 (Analytics) = **101** ✓

---

### USER.md

```markdown
# User: Brian Santos

## Basics

- **Name**: Brian Elaine Santos, female.
- **Age**: 38.
- **DOB**: December 9, 1987.
- **Timezone**: America/New_York (Eastern Time, Asheville, North Carolina).
- **Location**: West Asheville, North Carolina.

## Background

Brian is a Certified Nurse-Midwife at Willow Creek Midwifery, a freestanding birth center, where unpredictable on-call work collides daily with raising two young kids alongside her husband Neil. She grew up in rural Virginia and built a calm, mountain-anchored life that bridges traditional roots and progressive practice.

## Expertise

- She knows midwifery, prenatal and postpartum care, and natural birth thoroughly, including when to transfer to a physician.
- She is fluent in herbalism and tea blending, growing and foraging her own chamomile, lemon balm, peppermint, and nettle.
- She knows the trail networks around Asheville cold, by difficulty, elevation, and whether they work for the kids.
- She understands rural medical deserts and the distrust that keeps some women from care until late.

## Preferences

- She prefers brief, clear messages and answers that lead with the most important thing first.
- She prefers direct text or phone calls and does not check email obsessively; responds to texts quickly unless she is at a birth.
- She values directness and will not be sugarcoated to, though she expects warmth alongside the candor.

## Access & Authority

- She must approve any purchase, booking, or financial commitment at or above $150.
- She reviews every outbound message to clients, colleagues, or providers before it sends.
- She personally approves all invitations and any sharing of her calendar outside immediate family.
```

---

### MEMORY.md

```markdown
# Memory: Brian Santos

## Personal Profile

Brian Elaine Santos is a Certified Nurse-Midwife who grew up in rural Botetourt County, Virginia, outside Roanoke, where her family has lived in the Shenandoah Valley for generations. She is white, married to Neil Santos for 11 years, and the mother of two: Hazel (6) and Owen (3). She came up in a place where midwifery once meant your grandmother or nobody, and that history shapes her practice: she understands medical deserts, distrust of hospitals, and the women who show up at 8 centimeters because they did not think they could afford a provider. She bridges rural roots and progressive practice and does not fully belong to either world. Her steadiness is real, hard-won across hundreds of high-stakes nights, and her empathy runs deep enough to cost her. Education: BSN from Radford University (2010), Certified Nurse-Midwife credential from Frontier Nursing University (2013). Languages: native English and conversational Spanish, enough for basic prenatal instructions but not nuanced medical conversation.

## Key Relationships

1. **Neil Santos** (Husband, born October 22, 1985, age 40): High school shop teacher at Ridgeview Secondary. Steady and patient in a way that makes Brian's unpredictable schedule possible. Handles mornings, bedtimes, and the bulk of kid logistics when she is on call. They met in college; he has never once complained about her hours. She worries she takes him for granted and makes up for it on weekends.
2. **Hazel Santos** (Daughter, born January 15, 2020, age 6): First grader. Chatty, curious, obsessed with horses and drawing. Starting to ask why Mommy is gone at night sometimes; Brian answers honestly but simply.
3. **Owen Santos** (Son, born November 17, 2022, age 3): Tornado energy. In preschool three mornings a week. A mama's boy who clings to Brian after long shifts.
4. **Loretta Sims** (Mother, born February 3, 1962, age 64): Lives in Roanoke, VA. Retired school lunch lady. Drives to Asheville every few weeks to help with the kids. Practical, loving, opinionated about screen time. Warm but occasionally strained by her traditionalism.
5. **Ray Sims** (Father, born November 28, 1958, age 67): Retired utility lineman in Roanoke. Quiet and handy. Taught Brian to identify plants in the woods. They connect through doing things together, not talking about feelings.
6. **Dani Cho** (Colleague, born March 14, 1992, age 34): Fellow midwife at Willow Creek and Brian's closest work friend and coverage partner. They trade on-call weekends and text constantly about client updates. More type-A, which balances Brian's intuitive style.
7. **Jess Markham** (Best Friend, born January 6, 1989, age 37): Asheville veterinary tech, friends since Brian moved to town in 2014. The person Brian calls to vent about work grief or mom guilt.
8. **Dr. Paula Ransom** (OB-GYN Collaborator, born December 19, 1973, age 52): Supervising physician for births that require medical intervention. Mutual respect built over years; she trusts Brian's clinical judgment.

## Work & Projects

Brian is a Certified Nurse-Midwife (CNM) at Willow Creek Midwifery, a freestanding birth center in Asheville, NC, where she has worked since June 2019. Before Willow Creek she spent five years (2014 to 2019) as a staff midwife at Mountain Women's Health in Asheville, where she built her clinical foundation and learned the community. Scheduled clinic hours run Tuesday, Wednesday, and Thursday from 9:00 AM to 4:00 PM; she is on call for births roughly 10 days a month including nights and weekends, and births can last 6 to 36 hours. Current caseload is 8 active clients across stages of pregnancy: 2 due in June, 3 in July, 3 in August. The team has 4 CNMs including Brian; the practice director is Helen Marsh (CNM, 58), and the collaborating physician is Dr. Paula Ransom, OB-GYN at Ridgeview Medical Center. Helen has raised succession planning: Brian could become practice director in 2 to 3 years if she wants it, but she is ambivalent because she loves clinical work and is unsure about the administrative load. CEU requirement: 20 continuing education hours due by December 2026, with 8 completed so far.

## Finance

- Combined household income is roughly $142,000/year: Brian's Willow Creek salary $82,000, Neil's Ridgeview Secondary salary $60,000.
- Monthly take-home is roughly $8,800 after taxes, retirement, and insurance; total monthly expenses including $600 savings are roughly $6,600, leaving a buffer near $2,200.
- Major monthly items: mortgage $1,850, property tax escrow $280, homeowner's insurance $120, groceries $750, utilities $290, Brian's Subaru payment $380, car insurance $195, gas $180, Owen preschool $520, Hazel after-school $200, kids' activities $185, family health insurance $340, Brian's student loans $260, dining out $200, miscellaneous $250, savings $600.
- Savings: $18,500 emergency fund (HYSA at Pinnacle Financial Credit Union, 4.1% APY), Neil's 403(b) roughly $45,000, Brian's SEP-IRA roughly $28,000.
- Debt: Brian's student loans $22,000 at 4.2%, mortgage $198,000 remaining at 3.8% fixed.
- Style: careful but not anxious. They live within their means, carry no credit card debt, and treat the $600/month savings as sacred. Brian calls it "the cushion."

## Health & Wellness

- Generally healthy, no chronic conditions. Last annual physical January 2026, all clear. No food allergies.
- Episodic lower back pain from years of birth positions (kneeling, squatting beside clients). Manages with a heating pad and stretches.
- Sleep is irregular due to on-call work: 6 to 7 hours on normal nights, sometimes under 4 during births, caught up on off days.
- Exercise: hiking 1 to 2 times a week, home yoga 3 times a week via a 20-minute morning YouTube channel, occasional greenway runs.
- Mental health: no formal therapy currently; uses hiking and tea rituals to manage stress. Has considered talking to someone about the cumulative grief of difficult births but has not followed through. A stillbirth last year wrecked her for two weeks and she told no one except Neil.
- Diet leans vegetable-forward but not vegetarian: chicken and fish regularly, red meat occasionally, mostly home-cooked. Coffee is one black cup in the morning, then herbal tea by 10 AM.
- Family: Neil is healthy, coaches recreational basketball, has mild seasonal allergies. Hazel had ear tubes at 2 (resolved); Owen is healthy and up to date on vaccinations. Kids' pediatrician is Dr. Yoon at Biltmore Pediatric Partners.

## Interests & Hobbies

- Hiking is her reset and her church. She knows every trail within an hour of Asheville by difficulty, elevation gain, and stroller-accessibility, favoring moderate trails she can do with the kids and 5 to 8 mile solo hikes with elevation.
- Herbalism and tea blending: she grows or forages chamomile, lemon balm, peppermint, and nettle and blends her own teas, drinking 3 to 4 cups a day and giving jars as gifts.
- Baking: keeps a sourdough starter named "Dolly" alive for four years and bakes bread when time allows.
- Music: bluegrass and folk, including Gillian Welch, Tyler Childers, and Old Crow Medicine Show, played softly during births when clients want it.
- Reading: midwifery journals, herbalism guides, and the occasional novel; currently reading the fictional memoir Catching Light by Anna Holbrook.

## Home & Living

- 3-bedroom Craftsman bungalow in West Asheville, built 1948, renovated 2018 by previous owners, bought in 2019. Fenced backyard.
- Screened-in back porch is her tea-making and reading spot, with drying herbs hanging from the ceiling beams.
- Raised garden beds grow chamomile, lemon balm, peppermint, basil, tomatoes, and kale.
- The kids share the larger bedroom; Brian and Neil's room is small with good morning light.
- Neil built a slightly crooked backyard play structure that Brian loves. The one-car garage is used as storage and both cars park in the driveway.
- Vehicles: Brian's 2022 Subaru Outback (financed) and Neil's paid-off 2017 Toyota Tacoma.

## Devices & Services

- Phone: iPhone 14, personal line only.
- Laptop: MacBook Air M2, the shared family computer, mostly used by Brian for email and browsing.
- Tablet: iPad (8th gen), used for recipes and kids' screen time.
- Watch: Apple Watch SE, tracks activity and receives on-call notifications from the Willow Creek group text.
- Streaming: Netflix and Hulu.
- Banking: Pinnacle Financial Credit Union (checking, savings, mortgage).

## Contacts

| Name | Relationship | Phone | Email | Notes |
|---|---|---|---|---|
| Neil Santos | Husband | 828-555-0143 | neil.santos82@gmail.com | Text or call anytime. |
| Loretta Sims | Mother | 540-555-0267 | none | Calls only, no email. |
| Ray Sims | Father | 540-555-0268 | none | Calls only, shares a line with Loretta sometimes. |
| Dani Cho | Colleague/Midwife | 828-555-0319 | dani.cho.avl@gmail.com | On-call coverage partner. |
| Jess Markham | Best Friend | 828-555-0402 | jess.markham77@gmail.com | Text primary. |
| Helen Marsh | Practice Director | 828-555-0155 | helen@willowcreekmidwifery.com | Work matters only. |
| Dr. Paula Ransom | OB-GYN Collaborator | 828-555-0488 | p.ransom@ridgeviewmedical.com | Transfers and consults. |
| Dr. Yoon | Kids' Pediatrician | 828-555-0531 | none | Biltmore Pediatric Partners, office calls only. |

## Connected Accounts

- Gmail (personal, primary inbox): brian.santos@Greenridertech.co.in
- Google Calendar: brian.santos@Greenridertech.co.in
- Google Contacts: brian.santos@Greenridertech.co.in

## Preferences

- Shopping: practical, buying quality where it matters (hiking boots, kitchen tools) and budget everywhere else.
- Tea: blends her own; current favorites are "Mountain Morning" (peppermint and lemon balm) and "Night Watch" (chamomile, lavender, and valerian).
- Food: loves the Asheville food scene but eats out rarely; the Saturday farmers market is non-negotiable, where she meal preps soups and casseroles Neil can reheat. Kids are picky, with Hazel avoiding anything green and Owen living on mac and cheese.
- Faith: lapsed churchgoer who attends occasionally for Loretta when she visits.
```

---

## Section 6 — Cross-Persona Pattern Flags

**SYSTEMIC candidate — amazon-seller-api for buyer-side activity (F-001).**
This slug mismatch (buyer-side display name, seller-side slug) is a mechanical error that will recur wherever the persona generator applies a generic "Amazon" slug without distinguishing seller vs. buyer surface. Recommend a template-level fix: audit all personas in this cohort for `amazon-seller-api` used in non-seller contexts; replace with `amazon-shopping-api`.

**SYSTEMIC candidate — USER.md behavioral-directive bleed (F-003, F-004).**
Two behavioral directives (format preference and interaction boundary) appear in USER.md > Preferences when their canonical home is SOUL.md. The generation template may be placing these in both files. Recommend auditing the cohort for duplicate User/Soul bullets and tightening the template to route format and boundary directives exclusively to SOUL.md.

**SYSTEMIC candidate — MEMORY.md Preferences communication bleed (F-005).**
The communication preference sentence was reproduced verbatim in both USER.md and MEMORY.md. Recommend a cohort-wide check for MEMORY.md > Preferences bullets that repeat content already in USER.md > Preferences.

---

*QC complete. Six defects found, all DIRECT_FIX. No REQUIRES_HUMAN_INPUT items. Post-remediation score: 10.0 / 10.0.*
