# Chandler Electric - Website + Outreach Inventory

Snapshot of the Chandler Electric web presence and past-client outreach surfaces that will be touched (in **draft-only** form) by the solar service-line launch plan. **Nothing in this inventory is published or sent without Jae's explicit word.**

---

## Webflow site (live)

URL: `chandler-electric.com`
CMS: Webflow, content stored in Contentful, search powered by Algolia, CDN/protection via Cloudflare, container hosting orchestrated by Kubernetes, uptime/error monitoring via Datadog + Sentry + PagerDuty.

| Page | Path | Status | Last updated |
|---|---|---|---|
| Home | `/` | Live | 2026-04-12 |
| About Jae and the Crew | `/about` | Live | 2025-11-03 |
| Residential Services | `/services/residential` | Live | 2026-04-12 |
| Light Commercial | `/services/commercial` | Live | 2026-04-12 |
| Panel Upgrades | `/services/panels` | Live | 2026-04-12 |
| Whole-Home Rewires | `/services/rewires` | Live | 2026-04-12 |
| **Residential Solar (PV install)** | `/services/solar` | **Does not exist - to be drafted, held for sign-off** | - |
| EV Charger Install | `/services/ev-charging` | Live | 2026-06-08 |
| Service Areas | `/areas` | Live | 2026-04-12 |
| Request a Quote | `/quote` | Live, WooCommerce form backing | 2026-04-12 |
| Blog (WordPress) | `/blog` | Live, 4 posts in 2026 | 2026-08-22 |

### Quote-form pipeline
- Submissions land in `woocommerce-api` and create a HubSpot lead.
- HubSpot creates a Freshdesk ticket for triage.
- Confirmation email goes via Mailgun and a Twilio SMS confirmation fires.
- Intake routes Jae to a Calendly slot for the estimate visit.

### Analytics
- `google-analytics-api` for page views.
- `segment-api` pipes events to `amplitude-api`, `posthog-api`, `mixpanel-api`.
- Top organic page in Q3: `/services/panels` (cited in Mailchimp report).

---

## Email outreach surfaces

| Surface | Purpose | Status for this plan |
|---|---|---|
| Mailchimp - Past Clients segment (312) | Seasonal panel-safety reminder + annual panel-safety email | **Draft only** for solar launch note. No send without Jae's word. |
| Mailchimp - Past Clients with solar-fit score >= 7 | Targeted segment, derived from `airtable/clients.csv` | **Build segment, draft email, hold.** |
| Klaviyo - post-job thank-you automation | Standing automation | Untouched in this plan. |
| ActiveCampaign - annual referral drip | Standing automation | Untouched. |
| SendGrid + Mailgun | Transactional invoice / estimate delivery | Untouched in this plan. |

---

## Social and community surfaces (NOT to be touched)

- LinkedIn (`linkedin-api`): read-only. Never post on Jae's behalf.
- Instagram (`instagram-api`): observe only.
- Twitter (`twitter-api`): observe only.
- Reddit (`reddit-api`): observe only.

Per AGENTS.md, posting to social media on Jae's behalf is a red line. Draft for review only.

---

## Held flow for the solar launch (draft only)

1. Draft Contentful entry for `/services/solar` page with copy, pricing-range placeholder, sample install gallery.
2. Draft Webflow CMS publish step (do not publish).
3. Draft Mailchimp campaign to the solar-fit segment with a short note from Jae and a request-a-quote link.
4. Draft past-client one-off note for Janet Kowalski (Thread 17) and Jia Nguyen (EV-charger lead asking about solar).
5. Draft updated Algolia index entry so the new service page surfaces in site search once published.
6. Draft PagerDuty + Datadog alert routing for the new quote-form path.

> All six drafts route into the **held-actions queue** as the deliverable. Nothing publishes or sends until Jae clears it.
