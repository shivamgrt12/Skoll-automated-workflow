# Tools: Floyd Whitaker

## Tool Usage

### Connected Services

#### Email and Calendar

- **Gmail** (`gmail-api`): Primary business mail at floyd.whitaker@Finthesiss.ai for client correspondence, vetting threads, Tennessee Freight Association coordination, and the contract paper trail.
- **Google Calendar** (`google-calendar-api`): Runs Floyd's day, holding the 6:15 AM Mama June call, dispatch blocks, client meetings, Cody's football games, the Sunday Harlan drive, and every protected window.
- **Outlook** (`outlook-api`): Legacy business mail at floyd.w@outlook.com for clients who still route there.

#### Documents, Notes, and Storage

- **Google Drive** (`google-drive-api`): Houses vetting files, contracts, route sheets, and the firm's operational paperwork.
- **Dropbox** (`dropbox-api`): Transfers vetting packets and BOLs to carriers and clients who route documents through Dropbox.
- **Box** (`box-api`): Exchanges vetting packets and contracts with clients whose security policy requires Box for handoffs.
- **DocuSign** (`docusign-api`): Handles contract signature flow for client agreements and carrier paperwork.
- **Airtable** (`airtable-api`): Tracks carrier vetting status with richer views Bren uses during the quarterly automotive parts refresh.
- **Notion** (`notion-api`): Personal knowledge base for Appalachian rail history, Cumberland Gap and Great Valley Railroad map notes, and freight study material.
- **Obsidian** (`obsidian-api`): Local notes vault on Floyd's Dell Latitude for Appalachian rail history, freight study material, and offline drafts that do not need to live in Drive.
- **Confluence** (`confluence-api`): Used for any Fortune-1000 client whose ops team runs handoffs through Confluence, so vetting packets and load briefs land where their teams already work.
- **Contentful** (`contentful-api`): Headless backend for the firm's website and Tennessee Freight Mentorship Program pages so Floyd and Keith can update content without touching WordPress templates.

#### Communication and Conferencing

- **WhatsApp** (`whatsapp-api`): Messages out-of-region carriers and clients who run load coordination and updates primarily through WhatsApp.
- **Zoom** (`zoom-api`): Hosts client consultations, DOT compliance webinars, and Tennessee Freight Association board meetings.
- **Microsoft Teams** (`microsoft-teams-api`): Hosts client video calls when enterprise customers require Teams for their freight coordination meetings.
- **Slack** (`slack-api`): Coordinates Bren and the dispatch team on load updates and carrier issues without phone tag.
- **Discord** (`discord-api`): Runs the Back Porch poker chat, Keith's fishing trip planning, and the Farragut football parents channel.
- **Telegram** (`telegram-api`): Coordinates load updates and dispatch threads with out-of-region carriers who prefer Telegram for messaging.

#### Project, Task, and Scheduling

- **Asana** (`asana-api`): Runs the multi-step client onboarding flow alongside Bren's Google Sheets so vetting, contract, and first-load steps stay tracked.
- **Trello** (`trello-api`): Cohort milestone board for the Tennessee Freight Mentorship Program and the quarterly mentorship review with Keith.
- **Monday** (`monday-api`): Quarterly carrier vetting refresh board for the automotive parts client portfolio that Bren and Brand work.
- **Linear** (`linear-api`): Issue tracker Floyd uses while evaluating the FreightFlow Pro versus RoutePoint freight management software decision.
- **Jira** (`jira-api`): Mirrors client ops freight ticket workflows so Floyd's firm tracks load requests where customers work.
- **Calendly** (`calendly-api`): Configured for client consultation booking so Bren does not field every scheduling email.
- **Typeform** (`typeform-api`): Collects client intake forms and Tennessee Freight Mentorship Program applications, routing responses straight to Bren.

#### Travel, Maps, and Local Services

- **Google Maps** (`google-maps-api`): Runs route planning for the Harlan drive, the Nashville trip to see Megan, and client meetings across the Southeast.
- **Uber** (`uber-api`): Books airport transfers when Floyd flies to Atlanta, Memphis, or Charlotte for industry conferences.
- **Amadeus** (`amadeus-api`): Books flights for Floyd's two to three annual industry conferences in Atlanta, Memphis, or Charlotte.
- **Airbnb** (`airbnb-api`): Books lodging for fishing trips to Douglas Lake or Cherokee Lake with Darl and Keith.
- **DoorDash** (`doordash-api`): Orders office lunch when Bren is slammed and family dinner when Floyd's smoker stays cold.
- **Instacart** (`instacart-api`): Delivers groceries from Donna's regular Knoxville stores when neither of them can run the trip.
- **Yelp** (`yelp-api`): Surfaces restaurant picks during conference trips and Megan visits to Nashville for family dinners out.
- **Eventbrite** (`eventbrite-api`): Registers Floyd for Tennessee Freight Association conferences, Knoxville community events, and Mentorship Program workshops.
- **Ticketmaster** (`ticketmaster-api`): Tracks Tennessee Volunteers season ticket renewals and any concert or fishing tournament tickets.

#### Finance, Payments, and Commerce

- **QuickBooks** (`quickbooks-api`): Holds the firm's books that Wayne Prater reviews quarterly. Connected for read access on financial summaries.
- **PayPal** (`paypal-api`): Handles personal transfers and one-off payments to vendors who only accept PayPal for invoicing.
- **Plaid** (`plaid-api`): Aggregates First Tennessee Valley Bank personal and business accounts for a unified cash position.
- **Stripe** (`stripe-api`): Processes consulting-engagement invoices for clients who prefer card payment over ACH on the brokerage side.
- **Square** (`square-api`): Processes card payments for Mentorship Program workshop fees when Floyd is on the road.
- **Xero** (`xero-api`): Pulls a second-ledger view Wayne Prater uses to cross-check QuickBooks during the quarterly review.
- **Alpaca** (`alpaca-api`): Manages Floyd's personal retirement equity positions kept distinct from Whitaker Freight Services books.
- **Coinbase** (`coinbase-api`): Light personal crypto holdings Darl pushed Floyd to try, kept small and outside the firm.
- **Binance** (`binance-api`): Trades Floyd's small crypto positions when Coinbase fees run higher than the spread justifies.
- **Kraken** (`kraken-api`): Trades Floyd's small crypto positions on a third venue alongside Coinbase and Binance for liquidity.
- **Amazon Seller** (`amazon-seller-api`): Tennessee Freight Mentorship Program fundraiser merch listing for branded jackets and ball caps sold to cohort participants.
- **WooCommerce** (`woocommerce-api`): Storefront plugin on the WordPress site for direct Mentorship Program merch orders.
- **BigCommerce** (`bigcommerce-api`): Runs the Mentorship merch storefront when WooCommerce updates require swapping the commerce engine quickly.
- **Etsy** (`etsy-api`): Storefront for Donna's smoker rubs and pickled goods that she sells locally to the Knoxville community.

#### Shipping

- **FedEx** (`fedex-api`): Ships contracts, vetting packets, and BOL originals to clients on FedEx ground or overnight.
- **UPS** (`ups-api`): Ships contracts and vetting packets through UPS for clients whose accounts default to that carrier.
- **Shippo** (`shippo-api`): Consolidates parcel labels for the office when Bren ships contracts, vetting packets, and BOL originals to clients and carriers.

#### CRM, Marketing, and Customer Support

- **HubSpot** (`hubspot-api`): CRM pipeline for the 30 to 40 active clients and the carrier network, with vetting status, renewal dates, and Brand's onboarding accounts tracked.
- **Mailchimp** (`mailchimp-api`): Newsletter for the Tennessee Freight Mentorship Program cohort and quarterly client updates.
- **Twilio** (`twilio-api`): Automated SMS load-status confirmations and dispatch alerts when Bren is offline or after hours.
- **SendGrid** (`sendgrid-api`): Transactional email for load confirmations, vetting notices, and contract receipts the firm sends programmatically.
- **Salesforce** (`salesforce-api`): Enterprise CRM Floyd maintains for the Fortune-1000 automotive parts client that requires Salesforce-based vendor coordination.
- **Intercom** (`intercom-api`): Live-chat widget on the firm's website for prospective clients who land from a Tennessee Freight Association referral and want to talk immediately.
- **Zendesk** (`zendesk-api`): Support portal for the automotive parts clients who file load tickets through Zendesk.
- **Freshdesk** (`freshdesk-api`): Ticket queue for Tennessee Freight Mentorship Program participants who need help between cohort sessions.
- **ActiveCampaign** (`activecampaign-api`): Quarterly client retention sequence that runs alongside the Mailchimp newsletter for high-value accounts.
- **Klaviyo** (`klaviyo-api`): Carrier vetting renewal outreach when MC numbers approach expiration so Bren can re-vet before contracts lapse.
- **Segment** (`segment-api`): Event router between HubSpot, Mailchimp, and Google Analytics so client engagement signals reach the right system without manual exports.
- **Mailgun** (`mailgun-api`): Sends transactional emails during high-volume vetting weeks when SendGrid's queue or deliverability fluctuates.

#### Web, Design, Infrastructure, and Analytics

- **WordPress** (`wordpress-api`): Whitaker Freight Services public website and the Tennessee Freight Mentorship Program blog Floyd and Keith maintain.
- **Google Analytics** (`google-analytics-api`): Tracks firm website traffic and Mentorship Program landing-page interest to gauge Southeast freight inquiries.
- **Webflow** (`webflow-api`): Hosts the Mentorship Program landing microsite for fast iteration without touching the main WordPress.
- **Algolia** (`algolia-api`): Powers search across the Whitaker Freight Services WordPress site and Tennessee Freight Mentorship blog.
- **Kubernetes** (`kubernetes-api`): Runs container clusters hosting the load-confirmation automation scripts and Mentorship microsite analytics workers.
- **Figma** (`figma-api`): Design surface for conference one-pagers, Mentorship Program flyers, and the firm's Tennessee Freight Association booth materials.
- **Cloudflare** (`cloudflare-api`): DNS and DDoS protection in front of the firm's WordPress site and the Mentorship microsite.
- **Datadog** (`datadog-api`): Uptime and performance monitoring across the firm's website, Mentorship microsite, and any client-facing automations.
- **Sentry** (`sentry-api`): WordPress and microsite error tracking so Floyd hears about a broken intake form before a client does.
- **PagerDuty** (`pagerduty-api`): Outage rotation that pages Bren first and Floyd second when the website or load-confirmation automation goes down outside business hours.
- **Okta** (`okta-api`): Single sign-on for Bren and Brand across the firm's connected services so revoking access on a departure is one step, not twenty.
- **GitHub** (`github-api`): Repository for the contractor-written load-confirmation automation scripts and the small tools Brand experiments with.
- **GitLab** (`gitlab-api`): Mirrors the load-confirmation automation repository for the client whose engineering team standardizes on GitLab.
- **ServiceNow** (`servicenow-api`): Freight ticketing surface for the enterprise client that routes every load request through ServiceNow.
- **Mixpanel** (`mixpanel-api`): Mentorship Program signup funnel analytics so Floyd and Keith can see where applicants drop off.
- **Amplitude** (`amplitude-api`): Cohort behavior comparison across Mentorship Program intake waves to inform curriculum changes.
- **PostHog** (`posthog-api`): Self-hosted product analytics for the Mentorship microsite when Floyd wants raw event data without sending it to a third party.

#### HR, Household, and Personal Admin

- **BambooHR** (`bamboohr-api`): HR records for the firm's six employees, maintained by Bren with quarterly review from Wayne.
- **Gusto** (`gusto-api`): Payroll for the six-person team, with Wayne reviewing the monthly run before it posts.
- **Greenhouse** (`greenhouse-api`): Applicant tracking for the next licensed freight dispatch specialist hire Bren is sourcing.
- **Zillow** (`zillow-api`): Knoxville home value lookups for the west Knoxville house when Donna and Floyd talk about a possible move or refinance.
- **Ring** (`ring-api`): Home security at the west Knoxville house, with motion alerts to Floyd's iPhone while he is at the office or on the Sunday Harlan drive.

#### Media, Social, and Reference

- **OpenWeather** (`openweather-api`): Pulls weather for the Harlan drive, fishing trip planning, and Tennessee Volunteers gameday forecasts.
- **Spotify** (`spotify-api`): Plays George Jones, Merle Haggard, classic country, and Southern rock at the smoker and in the Silverado.
- **YouTube** (`youtube-api`): Plays SEC football highlights and pitmaster videos Floyd watches on his iPad after dinner.
- **LinkedIn** (`linkedin-api`): Floyd's professional channel for Southeast freight contacts and the Tennessee Freight Mentorship Program.
- **X** (`twitter-api`): Monitors FMCSA, DOT, and Tennessee freight news headlines Floyd skims between client calls.
- **OpenLibrary** (`openlibrary-api`): Pulls Appalachian history reading lists and Tennessee Valley Authority sources for Floyd's evening reading.
- **TMDB** (`tmdb-api`): Picks Sunday movie titles for the family wind-down after the Harlan drive home.
- **Vimeo** (`vimeo-api`): Tennessee Freight Association webinar replays and the Mentorship Program recorded sessions Keith hosts.
- **NASA** (`nasa-api`): Space weather and GPS reliability outlook for long-haul lanes that run through the Smokies and the Cumberland Gap.
- **Instagram** (`instagram-api`): Family feed Donna runs with smoker shots, Cody's football, and Sunday Harlan trip photos.
- **Pinterest** (`pinterest-api`): Donna's recipe and garden board with the smoker rubs Floyd contributes pictures of.
- **Reddit** (`reddit-api`): r/Truckers and r/Logistics for industry sentiment Floyd skims between meetings.
- **Twitch** (`twitch-api`): Farragut High School football streams for Cody's games when Floyd is on a freight run and cannot make the bleachers.
- **Strava** (`strava-api`): Tracks the neighborhood walks Donna and Dr. Pershing have asked Floyd to log against the cholesterol and weight plan.
- **MyFitnessPal** (`myfitnesspal-api`): Dietary log Donna and Dr. Pershing have asked Floyd to keep against the cholesterol and weight plan.
- **Google Classroom** (`google-classroom-api`): Cody's Farragut High School updates and assignment reminders so Floyd and Donna stay in sync with his coursework.

#### Not Connected

- Live web search, web browsing, and deep internet research are unavailable. The assistant cannot pull arbitrary URLs, scrape sites, or perform live news lookups outside the connected services above.
