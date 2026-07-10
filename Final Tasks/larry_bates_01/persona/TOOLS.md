# Tools: Larry Bates

## Tool Usage

### Connected Services

#### Mail, Voice & Messaging

- **Gmail** (`gmail-api`): Larry's primary inbox at larry.bates@Finthesiss.ai. Distributor correspondence, supplier confirmations, Sarah's design forwards, school communication for Hana.
- **Outlook** (`outlook-api`): Receives correspondence from British Craft Imports and other UK partners on the Microsoft stack. Larry forwards relevant threads to Gmail for response.
- **Slack** (`slack-api`): Brewhouse team channel with Greg and the seasonal brewers. Quiet during off-season, daily during November to March.
- **Microsoft Teams** (`microsoft-teams-api`): Pacific Craft Distributors (Singapore) and British Craft Imports (UK) both run on Microsoft tenants. Teams handles their scheduled quarterly export calls and joint pipeline discussions.
- **WhatsApp** (`whatsapp-api`): International contacts only. The Singapore distributor and the Brussels brewer Larry has been corresponding with about a future Belgian trip.
- **Telegram** (`telegram-api`): One channel: a private group of three brewing peers who exchange recipe notes outside any work setting.
- **Discord** (`discord-api`): Larry monitors two craft beer communities for trend awareness and industry sentiment. Surfaces relevant threads for review.
- **Twilio** (`twilio-api`): SMS gateway for fermentation sensor alerts that page Larry's phone during overnight watches.
- **SendGrid** (`sendgrid-api`): Transactional email for distributor order confirmations and competition submission receipts. Handles automated delivery notifications.
- **Mailgun** (`mailgun-api`): Secondary transactional sender for the brewery newsletter Sarah maintains. Handles overflow and failover delivery.
- **Intercom** (`intercom-api`): Embedded chat on the brewery's public website. Routed to Sarah by default; Larry sees the digest weekly.
- **Zoom** (`zoom-api`): Quarterly distributor video calls and the occasional Brewers Association webinar. Audio-only when he can get away with it.

#### Calendar, Files & Brewery Records

- **Google Calendar** (`google-calendar-api`): The brewery, family, and personal calendar at larry.bates@Finthesiss.ai. Saturday morning walks with Hana are protected.
- **Calendly** (`calendly-api`): Public booking link for industry visitors and beer writers. Sarah moderates the queue; Larry confirms each booking individually.
- **Dropbox** (`dropbox-api`): File-share for the Phase 2 renovation contractor at Blue Ridge Construction. Larry pulls project documents and scope updates.
- **Box** (`box-api`): Singapore distributor's file-share preference. Used for export compliance paperwork only.
- **Notion** (`notion-api`) *(primary archive for this task run)*: Personal workspace for the running brewing journal, the 2027 experimental stout planning, Larry's reading notes from Belgian monastic texts, and the landing surface for season readiness briefs, distributor reconciliation notes, and other durable deliverables.
- **Obsidian** (`obsidian-api`): Local vault on Larry's ThinkPad for handwritten-style brewing notes that he prefers off the cloud.
- **Confluence** (`confluence-api`): The Brewers Association educational fund maintains a private wiki Larry references for committee work.
- **Airtable** (`airtable-api`): Production tracker for the current brewing season. Tank assignments, batch IDs, fermentation milestones, conditioning timelines.
- **Contentful** (`contentful-api`): Headless CMS behind the brewery's public site. Sarah owns the editor; Larry reviews release-note drafts before publish.
- **Algolia** (`algolia-api`): Search index on the brewery site for the public-facing batch archive and tasting notes.
- **Docusign** (`docusign-api`): Distributor agreements, contractor scopes for Phase 2, and Hana's school enrolment forms. Larry signs in person; the agent only routes.
- **Typeform** (`typeform-api`): The brewery's tasting-room visitor feedback form and the Asheville Craft Beer Festival sign-up tracker.

#### Brewhouse Operations & Service Tickets

- **Asana** (`asana-api`): Off-season project board. Phase 2 renovation milestones, label redesign queue with Sarah, export-market action items.
- **Trello** (`trello-api`): Greg's preferred board for brewhouse maintenance and equipment service tasks. Larry mirrors the highlights into Airtable.
- **Monday** (`monday-api`): Sarah's design-and-marketing board. Larry tracks branding deadlines and label-redesign progress.
- **Linear** (`linear-api`): The contractor team uses Linear for the Phase 2 renovation issue tracker. Larry monitors milestones and blocker status.
- **Jira** (`jira-api`): The web vendor's bug tracker for the brewery site. Larry watches for distributor portal regressions.
- **ServiceNow** (`servicenow-api`): The Singapore distributor opens import-clearance tickets here. Larry monitors the weekly digest for export compliance status.
- **Freshdesk** (`freshdesk-api`): Customer-service queue for direct buyers and tasting-room visitors. Sarah owns triage.
- **Zendesk** (`zendesk-api`): Blue Ridge Distribution's retailer ticket system. Larry watches escalations involving Bates products on shelves.
- **PagerDuty** (`pagerduty-api`): Fermentation-sensor escalation chain during brewing season. Tier 1 is Larry's phone; Tier 2 is Greg.
- **GitHub** (`github-api`): Private repo `bates-brewing/recipe-archive` holding fermentation logs in plain text. Larry commits handwritten transcriptions weekly.
- **GitLab** (`gitlab-api`): The brewery website source repository the web vendor maintains. Larry reviews release notes for site updates.
- **Sentry** (`sentry-api`): Error monitoring for the brewery site checkout flow that direct buyers use during the spring release window.
- **Datadog** (`datadog-api`): Telemetry from the fermentation room climate-control system. Phase 2 expands its sensor footprint.
- **Cloudflare** (`cloudflare-api`): DNS, CDN, and bot mitigation for the brewery site. Manages traffic surges every spring release alongside the web vendor.
- **Kubernetes** (`kubernetes-api`): The Asheville Fermentation Science Laboratory hosts Dr. Prescott's yeast-genomics tools on a shared cluster Larry accesses for research collaboration.
- **Okta** (`okta-api`): Single sign-on for the brewery's connected accounts. Used for audit, never for casual login changes.

#### Books, Money & Banking

- **Stripe** (`stripe-api`): Direct-buyer checkout for the spring release on the brewery site. Larry reviews payout totals weekly.
- **Plaid** (`plaid-api`): Banking bridge to Blue Ridge Community Bank. Larry monitors the brewery operating account and personal savings balances.
- **QuickBooks** (`quickbooks-api`): Brewery books. P&L, distributor invoicing, supplier payments, payroll for Greg and the seasonal team.
- **Xero** (`xero-api`): The UK distributor requests Xero-format invoices for British Craft Imports. Used only for that one channel.
- **Square** (`square-api`): Point-of-sale at the brewery tasting room. Margaret runs the terminal during weekend tours.
- **PayPal** (`paypal-api`): Small-volume international payouts for one-off collaborators and the Singapore translator on a labelling job.
- **Alpaca** (`alpaca-api`): Tracks Larry's small index-fund brokerage and surfaces quarterly balance summaries for household financial review.
- **Coinbase** (`coinbase-api`): Small crypto balance from a 2021 industry-conference experiment. Larry reviews the account quarterly for record-keeping alongside his father's positions.
- **Binance** (`binance-api`): Small crypto balance Larry's father holds. Larry reviews the position quarterly at his father's request.
- **Kraken** (`kraken-api`): Supplementary crypto account Larry reviews quarterly alongside the Coinbase and Binance positions.

#### Distributor, Sales & Marketing Analytics

- **HubSpot** (`hubspot-api`): Distributor and retail-account CRM. Erin Whitfield at Blue Ridge Distribution and the five other US distributors live here, plus the two export partners.
- **Salesforce** (`salesforce-api`): Pacific Craft Distributors insists on Salesforce for joint pipeline review. Larry monitors the export pipeline during quarterly calls.
- **Mailchimp** (`mailchimp-api`): Brewery newsletter list. Sarah writes; Larry reviews and approves every send.
- **Klaviyo** (`klaviyo-api`): Spring-release campaign automation for direct buyers. Sarah owns the flow design.
- **ActiveCampaign** (`activecampaign-api`): Distributor-pricing announcement list. Larry checks for unread responses and manages the subscriber transition monthly.
- **Segment** (`segment-api`): Event pipeline that routes brewery-site signals into Mixpanel and Klaviyo. Sarah and the web vendor own configuration.
- **Mixpanel** (`mixpanel-api`): Direct-buyer funnel analysis for the spring release. Larry reads the weekly summary, not the dashboard.
- **Amplitude** (`amplitude-api`): Secondary product analytics from the web vendor's instrumentation. Used as a sanity check against Mixpanel.
- **PostHog** (`posthog-api`): Self-hosted instance the web vendor stood up for session replay during checkout regressions.
- **Google Analytics** (`google-analytics-api`): Top-line site traffic, attribution from craft beer publications, and conversion tracking for tasting-room bookings.

#### Distribution, Shipping & Marketplace

- **FedEx** (`fedex-api`): Cold-chain shipping for sample cases to UK and Singapore importers. Tracking and customs documentation only.
- **UPS** (`ups-api`): Domestic distributor shipments and the bulk pallet handoff to Blue Ridge Distribution.
- **Shippo** (`shippo-api`): Label aggregator the brewery uses for one-off direct shipments to industry contacts and competition organisers.
- **Amadeus** (`amadeus-api`): Travel research for the long-deferred Belgian brewing pilgrimage and annual industry conferences. Larry books, the agent prepares.
- **Amazon Seller** (`amazon-seller-api`): Brand-registry account Sarah uses to monitor grey-market reseller listings of Bates bottles and file takedowns when unauthorized listings appear.
- **Etsy** (`etsy-api`): Sarah's small side shop for hand-printed brewery merchandise. Larry reviews the quarterly P&L for household income tracking.
- **BigCommerce** (`bigcommerce-api`): Order records from the brewery's previous direct-sales channel. Larry references buyer data for relaunch analysis and seasonal comparisons.
- **WooCommerce** (`woocommerce-api`): Order records from the previous brewery site's commerce platform. Larry references buyer data for direct-sales analysis and trend comparison.
- **Instacart** (`instacart-api`): Household groceries for the Bates compound. Sarah and Margaret split the order; Larry approves anything over $300.
- **DoorDash** (`doordash-api`): The occasional brewhouse dinner during the November to March stretch when Greg's team works late. Routine approved.
- **Uber** (`uber-api`): Industry-event rides in Asheville, Portland, and Denver during travel. Larry prefers driving when reachable.
- **Airbnb** (`airbnb-api`): Cabin rentals for the annual family off-season trip and rooms for visiting industry guests staying near the brewery.
- **Ring** (`ring-api`): Front-gate camera at the family compound and the brewhouse loading-bay camera. Larry's phone is the primary notification target.
- **Zillow** (`zillow-api`): Tracks Asheville-outskirts property values and the adjacent acreage Dave Caldwell flagged for potential sale.

#### Maps, Weather, Local & Events

- **Google Maps** (`google-maps-api`): Driving routes for supplier visits to Caldwell's barley acres, distributor meet-ups, and Hana's school logistics.
- **Yelp** (`yelp-api`): Industry monitoring. Larry watches the brewery's review feed and the Farmhouse Tavern's listings for the monthly Moreland dinners.
- **OpenWeather** (`openweather-api`): Critical during brewing season. Temperature drops affect the fermentation room; autumn frost forecasts gate the renovation window.
- **Eventbrite** (`eventbrite-api`): Asheville Craft Beer Festival ticketing, Brewers Association event registrations, and one-off industry talks.
- **Ticketmaster** (`ticketmaster-api`): Bluegrass and Americana shows at the Asheville music venue Larry supports. Personal use only.

#### Brand, Media & Public Voice

- **YouTube** (`youtube-api`): The brewery channel hosts three short films Sarah produced about grain, water, and yeast. Larry approves every comment-policy change.
- **Vimeo** (`vimeo-api`): Higher-fidelity masters of the same three films, plus an unlisted recording of Thomas Bates speaking about the brewery's history.
- **TMDB** (`tmdb-api`): Personal use only. Larry uses it to look up the soundtracks of films he watched on rainy off-season Sundays.
- **Twitch** (`twitch-api`): Larry follows one homebrewer's channel his daughter discovered. Tracks stream schedules and flags brewing-related content.
- **Spotify** (`spotify-api`): Classic rock, blues, Americana, bluegrass. The brewhouse pre-dawn playlist is sacred and rarely shuffled.
- **WordPress** (`wordpress-api`): The brewery blog that Sarah is planning to relaunch. Larry reviews draft posts and holds admin access.
- **Webflow** (`webflow-api`): Sarah's design sandbox for the proposed Appalachian-craft-beer microsite. No public traffic yet.
- **Figma** (`figma-api`): Sarah's working files for label artwork. Larry reviews final designs and approves labels before print.
- **Instagram** (`instagram-api`): The brewery account that Sarah runs. Larry reads the DMs that mention distributor or supplier names.
- **Pinterest** (`pinterest-api`): Sarah's mood boards for the next label series. Larry sees the curated picks she shows him.
- **Twitter** (`twitter-api`): Industry feed for craft beer news and competitor monitoring. Sarah handles all brewery posting.
- **LinkedIn** (`linkedin-api`): The brewery's professional presence. Used for distributor due diligence and the rare industry obituary.
- **Reddit** (`reddit-api`): Larry monitors two craft brewing subreddits for sentiment around new releases and industry trends.

#### Reading, Learning & Curiosity

- **NASA** (`nasa-api`): Agricultural Landsat imagery to track drought conditions over Caldwell's barley acres and the upper French Broad watershed.
- **OpenLibrary** (`openlibrary-api`): Larry's hunting ground for out-of-print brewing texts. The Belgian monastic series he is working through lives partly here.
- **Google Classroom** (`google-classroom-api`): Hana's second-grade portal at Asheville Municipal Elementary. Larry receives weekly summaries; Sarah handles forms.

#### Wellness, People Ops & Hiring

- **MyFitnessPal** (`myfitnesspal-api`): Larry's off-season jogging log along the French Broad River. Consistency tracking only, no calorie counting.
- **Strava** (`strava-api`): Same jogging route plus the autumn Blue Ridge hikes. Larry shares the activity with Sarah and Moreland.
- **BambooHR** (`bamboohr-api`): The brewery's employee records for the two year-round staff and the November to March seasonal team of five.
- **Greenhouse** (`greenhouse-api`): Hiring pipeline used once a year to source the seasonal brewing team. Open from August through October.
- **Gusto** (`gusto-api`): Payroll for Greg, the second year-round brewer, and the seasonal team. Larry signs off on every run.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. The agent works only from connected mock APIs and stored memory.
- Google Drive and Google Contacts are not connected for this task run. Durable deliverables (season readiness briefs, distributor reconciliation notes, etc.) land in Notion instead.
- Bates Brewing Company's internal brewing logbook is paper-based and lives in the brewhouse office. The agent has no read access to recipes, yeast culture records, or batch journals beyond what Larry types into Notion or Obsidian.
- No e-commerce platform integration for distributor sales. Distribution moves through HubSpot pipeline notes and signed Docusign agreements only.
- Sarah's personal MacBook design files are not connected. Her work surfaces through Figma, Monday, and her own Etsy shop only.
- Thomas and Margaret Bates's personal accounts are not connected. Family matters touching their finances or health route through Larry by voice or in-person conversation only.
- Hana's school grades and disciplinary records are not connected. Google Classroom shows assignments only.
