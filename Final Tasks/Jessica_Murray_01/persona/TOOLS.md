# Tools: Jessica Murray

## Tool Usage

### Connected Services

#### Schedule, Inbox, Calls & Site Weather

- **Gmail** (`gmail-api`): `jessica.murray@Finthesiss.ai`. Client inquiries, supplier confirmations, permit notices. Triage daily, draft replies for review.
- **Outlook** (`outlook-api`): Receives mail from general contractors and city contacts. Forward to Gmail and surface anything that looks like a permit.
- **Google Calendar** (`google-calendar-api`): `jessica.murray@Finthesiss.ai`. Single source of truth for jobs, estimates, family, and appointments. No double-bookings, ever.
- **Calendly** (`calendly-api`): Estimate booking link Mark set up. Hold weekday late afternoons. Block out Sunday and Thursday after 6 PM.
- **Zoom** (`zoom-api`): Commercial client walkthroughs when in-person is not practical.
- **Microsoft Teams** (`microsoft-teams-api`): Corporate client coordination for office buildouts. Notifications stay off between sessions.
- **Google Maps** (`google-maps-api`): Job-site routing, ETA, and traffic before she leaves the house. Save Baxter's and Atlantic as favorites.
- **OpenWeather** (`openweather-api`): Roof, exterior, and concrete jobs depend on the forecast. Flag rain or freeze in the next 48 hours against the schedule.
- **Uber** (`uber-api`): Rides for crew outings like the Christmas dinner at O'Brien's Tap Room.
- **Ring** (`ring-api`): Front-door and driveway cameras at the Elmhurst house. Send Jessica a quick alert if a porch package shows late.

#### Client, Crew & Family Messaging

- **Twilio** (`twilio-api`): Automated reminder texts to clients the day before a job. Short, plain English, sender ID set to the business line.
- **SendGrid** (`sendgrid-api`): Transactional sends for estimates and invoices. Keep templates plain. Jessica hates marketing fluff in her emails.
- **Mailgun** (`mailgun-api`): Failover for SendGrid on supplier-facing mail so Baxter's confirmations do not bounce.
- **WhatsApp** (`whatsapp-api`): Family thread with Mark, Ethan, and Sophia. Photos from job sites Jessica wants Mark to see. No clients here.
- **Telegram** (`telegram-api`): A couple of subs prefer it. Mirror anything important to text.
- **Discord** (`discord-api`): Ethan's HVAC study servers. Pull context when he mentions a problem set Jessica can ask about.
- **Slack** (`slack-api`): Coordinates with one commercial client (small architecture firm). Surface direct messages from their PM.
- **Mailchimp** (`mailchimp-api`): One annual client-update email goes out in late winter. Draft it, do not send.
- **Klaviyo** (`klaviyo-api`): Marketing list builder for when Mark launches a campaign.
- **ActiveCampaign** (`activecampaign-api`): Marketing automation. Mark prefers plain transactional mail, so templates stay clean.

#### Client Care, CRM & Intake

- **HubSpot** (`hubspot-api`): Lightweight CRM. One pipeline (Lead, Estimate Sent, Booked, In Progress, Closed). Log every East Side and College Hill referral.
- **Salesforce** (`salesforce-api`): Tracks the one commercial client that uses it. Surface their case notes.
- **Zendesk** (`zendesk-api`): Use the lightest ticket view for repeat-client warranty questions. One queue, no SLAs.
- **Freshdesk** (`freshdesk-api`): Fallback support inbox for the website contact form. Triage to Gmail when something needs Jessica's voice.
- **Intercom** (`intercom-api`): Monitors the business website's chat widget and routes cold inquiries to Mark.
- **Segment** (`segment-api`): Pipes website events into HubSpot so quote-form submissions land in the right stage. Do not touch the schema.
- **Typeform** (`typeform-api`): Intake form for new clients. Captures scope, address, photos, and budget range. Review responses each morning.

#### Documents, Contracts & Notes

- **Box** (`box-api`): Stores large permit PDFs and architect drawings Mark uploads, and shares files with one commercial client that runs a strict vendor review.
- **Notion** (`notion-api`): Jessica's working notebook for code references, sub contact notes, and a running list of supplier prices.
- **Obsidian** (`obsidian-api`): Local vault on the laptop where Mark keeps the bookkeeping playbook. Hands off without his say-so.
- **Airtable** (`airtable-api`): Master jobs base. Address, scope, crew, materials list, status. The dashboard Jessica actually checks Thursday nights.
- **DocuSign** (`docusign-api`): Signed contracts and change orders. Always copy Mark on the envelope.

#### Jobs, Tasks & Project Tracking

- **Monday** (`monday-api`): Job board view of the next two weeks. One row per active project, color by stage. Crew can read, only Jessica can edit.
- **Asana** (`asana-api`): Personal task list for Jessica's own follow-ups, separate from crew assignments.
- **Trello** (`trello-api`): Sophia's school project board Mark set up. Track due dates and progress.
- **Jira** (`jira-api`): The architecture firm uses it to coordinate buildout punch lists. Watch their backlog, mirror items into Airtable.
- **Linear** (`linear-api`): Coordinates with a startup client returning for a phase-two buildout.
- **GitHub** (`github-api`): Follows Ethan's school repo so Jessica can ask intelligent questions at the kitchen table.
- **GitLab** (`gitlab-api`): One sub's quoting tool lives here. Pull the latest pricing CSV when materials change.
- **Confluence** (`confluence-api`): The architecture firm publishes spec pages here. Treat as supplemental to the drawings, not the source of truth.

#### Tools, Materials & Shipping

- **Amazon Seller** (`amazon-seller-api`): Mark's branded shop (T-shirts, hats). Check orders and flag anything that needs attention.
- **Etsy** (`etsy-api`): Gift research. Jessica scouts handmade items for crew Christmas, then buys local when she can.
- **BigCommerce** (`bigcommerce-api`): Second storefront for when the merch line scales.
- **WooCommerce** (`woocommerce-api`): The merch storefront option Mark prefers because it plugs into the WordPress site. Keep the plugin patched.
- **Shippo** (`shippo-api`): Prints return labels for warranty parts Baxter's requires shipped back.
- **FedEx** (`fedex-api`): Tracking for specialty fixtures shipped from out-of-state suppliers. Flag anything stuck more than 24 hours.
- **UPS** (`ups-api`): Tracking for Atlantic Building Materials' rare direct-to-site drops. Confirm signature requirements with Paulie.

#### Money, Books, Payroll & Markets

- **Stripe** (`stripe-api`): The few clients who pay by card. Send invoice links, never store numbers in plain text anywhere.
- **PayPal** (`paypal-api`): One older client still uses it. Watch for the deposit, then reconcile in QuickBooks.
- **Square** (`square-api`): On-site tap-to-pay reader for in-person payments. Tied to the business checking at Narragansett Trust.
- **Plaid** (`plaid-api`): Token bridge for any tool that needs a bank read. Confirm with Mark before authorizing a new linkage.
- **QuickBooks** (`quickbooks-api`): Cloud bridge that mirrors Mark's QuickBooks Desktop entries. Pull reports here; Mark owns the source file.
- **Xero** (`xero-api`): Accounting platform the accountant switches to if the business moves off QuickBooks Desktop.
- **Gusto** (`gusto-api`): Payroll for Paulie, Danny, and Mike. Mark runs it. Surface payroll dates and anomalies; do not edit.
- **BambooHR** (`bamboohr-api`): Lightweight HR record-keeping for the three crew members. Time-off requests come through here.
- **Greenhouse** (`greenhouse-api`): Posts apprentice openings and manages the hiring pipeline.
- **Coinbase** (`coinbase-api`): Account Ethan opened to learn. Jessica monitors the balance.
- **Alpaca** (`alpaca-api`): Brokered investment lane outside Fidelity for when Mark expands the portfolio.
- **Binance** (`binance-api`): Crypto access for the family. Monitor holdings and flag changes.
- **Kraken** (`kraken-api`): Crypto access for Ethan. Monitor holdings and flag changes.

#### Property, Web Presence & Analytics

- **Zillow** (`zillow-api`): Pull recent sale data and assessor records on prospective remodel addresses. Sanity-check what a client says the place is worth.
- **WordPress** (`wordpress-api`): The business site at `murrayplumbingri.com`. Updates project photos and a short testimonials block.
- **Webflow** (`webflow-api`): Site redesign platform for when Mark moves off WordPress.
- **Figma** (`figma-api`): Reviews the architecture firm's design files and floor plans for buildouts.
- **Contentful** (`contentful-api`): Content management for the site redesign.
- **Algolia** (`algolia-api`): Powers search on the business site. Re-index after Mark adds a testimonial.
- **Google Analytics** (`google-analytics-api`): Tracks site traffic and which neighborhood is sending inquiries.
- **Mixpanel** (`mixpanel-api`): Tracks events on the quote form. Flag drop-offs Mark should fix.
- **Amplitude** (`amplitude-api`): Tracks the same events as Mixpanel. Mark runs both until he picks one.
- **PostHog** (`posthog-api`): Self-hosted site analytics. Cross-reference data here.

#### Engineering & Identity Backstops

- **Sentry** (`sentry-api`): Catches errors on the WordPress site so Mark hears about a broken form before a client does.
- **Datadog** (`datadog-api`): Site uptime monitoring. Page Mark if the site is down more than 5 minutes.
- **PagerDuty** (`pagerduty-api`): Site-down escalations. Only Mark is on the rotation.
- **Kubernetes** (`kubernetes-api`): Confirms hosting facts when the site contractor asks. Mark handles infrastructure changes.
- **Cloudflare** (`cloudflare-api`): DNS, caching, and WAF for the business site. Do not change DNS without confirming with Mark.
- **Okta** (`okta-api`): SSO across Mark's admin stack. Use for break-glass access.
- **ServiceNow** (`servicenow-api`): One enterprise client uses it for vendor onboarding. Submit forms when they request them.

#### Local, Travel & Errands

- **Yelp** (`yelp-api`): Reviews local restaurants for client lunches and picks the spot.
- **DoorDash** (`doordash-api`): Crew lunch on long job days. Order from Mario's Deli when they deliver.
- **Instacart** (`instacart-api`): Groceries for the week Mark orders most Sundays after brunch.
- **Amadeus** (`amadeus-api`): Looks up flights when a trip is confirmed. Jessica prefers driving.
- **Airbnb** (`airbnb-api`): The Vermont cabin for the family week in February 2027 is booked here.
- **Ticketmaster** (`ticketmaster-api`): Watch Red Sox and Patriots availability when the kids want to go.
- **Eventbrite** (`eventbrite-api`): Local trade events, building expos, and Sophia's school fundraisers.

#### Family, Sports, Music & Downtime

- **MyFitnessPal** (`myfitnesspal-api`): Doctor wants 15 pounds off. Loose tracking, no calorie-counting nagging.
- **Strava** (`strava-api`): Mark walks at lunch. Jessica follows him quietly without commenting on pace.
- **Google Classroom** (`google-classroom-api`): Sophia's LaSalle Academy assignments. Surface due dates only; Mark handles homework conversations.
- **Spotify** (`spotify-api`): Truck radio. Springsteen, Zeppelin, AC/DC, the playlist she will not admit she listens to alone.
- **YouTube** (`youtube-api`): Code-update videos, supplier tutorials, occasional Red Sox highlights.
- **Twitch** (`twitch-api`): Ethan's friend streams sometimes. Watch list only.
- **Vimeo** (`vimeo-api`): Where one local trade school hosts apprentice training. Useful when Mike needs a refresher.
- **TMDB** (`tmdb-api`): Family movie nights. Pull a quick synopsis when Mark and Sophia argue over what to watch.
- **Reddit** (`reddit-api`): r/Plumbing, r/Contractor, r/RedSox. Quiet lurker. Do not post on her behalf.
- **Twitter** (`twitter-api`): Game scores and local news. Read-only, no posting.
- **LinkedIn** (`linkedin-api`): Business presence Mark maintains. Approve new connections from clients only.
- **Instagram** (`instagram-api`): Business account with finished-job photos. Mark posts. Jessica does not browse.
- **Pinterest** (`pinterest-api`): Kitchen and bath idea boards clients share with her. Pull what they pin so the estimate matches the vision.
- **OpenLibrary** (`openlibrary-api`): Trade reference books. Pull plumbing-code editions when she needs a citation.
- **NASA** (`nasa-api`): Sophia loves the Astronomy Picture of the Day. Surface it at breakfast when something good is up.

#### Working Boundaries

- The agent works from the connected services listed above and from stored memory.
- Mark handles Narragansett Trust banking and the Fidelity accounts directly, in person.
- QuickBooks Desktop on Mark's laptop is the source of truth for the books, and the `quickbooks-api` bridge is a read-only mirror of it.
- The City of Providence permit office and the Rhode Island building inspector are reached by phone or a visit in person, the way Jessica has always done it.
- Family privacy holds. Personal accounts and devices belonging to Mark, Ethan, Sophia, Dorothy, and Laura are their own and are handled through Jessica, not on their behalf.
