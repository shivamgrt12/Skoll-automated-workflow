# Tools: Steven Foster

## Tool Usage

### Connected Services

#### Personal Email, Messaging & Calendar

- **Gmail** (`gmail-api`): `steven.foster@Finthesiss.ai`. Personal correspondence, finance and health portals, reading lists, travel planning.
- **Google Calendar** (`google-calendar-api`): Primary calendar. Peloton, yoga, Helen calls, Lena dinners, provider visits, the 10K, the Mendocino weekend. Hold the Saturday morning Temple Coffee window.
- **Google Drive** (`google-drive-api`): Personal Drive: financial tracking, travel itineraries, reading log spreadsheet, Rust CLI design notes, life-admin folder.
- **Outlook** (`outlook-api`): Crescent Peak Outlook lives on the Dell laptop and the agent does not enter. Receives any personal Outlook invite that gets forwarded in.
- **Microsoft Teams** (`microsoft-teams-api`): Crescent Peak runs Teams for cross-timezone meetings with the India team; agent does not enter. Receives provider or vendor meeting invitations routed through Teams.
- **Slack** (`slack-api`): Crescent Peak Slack is off-limits. Personal use covers the small jazz-and-vinyl listening server with two friends.
- **WhatsApp** (`whatsapp-api`): Reaches Lena and David when they are traveling and SMS routing gets unreliable.
- **Zoom** (`zoom-api`): Hosts the monthly mentoring call with Pris and alumni calls with old colleagues. Do not auto-join.
- **Discord** (`discord-api`): Surfaces discussions and code examples from the Rust-learning server Steven follows.
- **Telegram** (`telegram-api`): Delivers paper drops and research links from the computing-history channel Steven follows.
- **Calendly** (`calendly-api`): The personal booking link he hands to mentees and informational requests. Pris uses it to nudge the monthly slot.

#### Finance, Brokerage & Banking

- **Plaid** (`plaid-api`): Aggregates balances across Chase checking, Ally HYSA, the Fidelity 401k, and the Vanguard brokerage for the 1st-of-month review.
- **Stripe** (`stripe-api`): Processes receipts for the side-project licensing income Steven collects. No outbound charges.
- **PayPal** (`paypal-api`): Peer transfers, reimbursements to Lena for shared trip costs, and recurring charity payments.
- **Square** (`square-api`): Processes conference and workshop receipts when Steven attends events.
- **QuickBooks** (`quickbooks-api`): Light 1099 ledger for the side coding income. Reconciled at year-end with the CPA.
- **Xero** (`xero-api`): Secondary ledger reference that supports QuickBooks reconciliation and year-end review.
- **Coinbase** (`coinbase-api`): Monitors a small exploratory crypto position Steven holds to understand the on-chain stack. No trading without confirmation.
- **Binance** (`binance-api`): Provides price reference data against Coinbase for crypto market comparison.
- **Kraken** (`kraken-api`): Provides order-book comparison data for crypto market analysis.
- **Alpaca** (`alpaca-api`): Paper-trading sandbox Steven uses to test small Rust market-data scripts. No live orders.

#### Travel, Maps & Local

- **Amadeus** (`amadeus-api`): Flight searches for the Mendocino-adjacent SFO connections and the considered Barcelona winter trip. Confirm before holding any fare.
- **Airbnb** (`airbnb-api`): Cabin and apartment stays for travel with Lena and solo city trips. Confirm before booking.
- **Uber** (`uber-api`): Airport runs and the rare night out where the Tesla is not the right call. Default to UberX.
- **DoorDash** (`doordash-api`): Delivers meals on evenings when a meeting runs past dinner and cooking is not an option.
- **Instacart** (`instacart-api`): The Sunday batch-cook grocery run when the schedule does not allow a Co-op visit in person.
- **Google Maps** (`google-maps-api`): Commute timing, the two-hour run to San Jose, hiking trailheads in the Sierras, Sacramento dinner routes.
- **Yelp** (`yelp-api`): Restaurant lookups for the Thursday dinners with Lena, client lunches, and trip prep.
- **OpenWeather** (`openweather-api`): Sierra hiking weather, race-day forecast for the 10K, Mendocino coastal conditions. Flag mornings under 45 degrees so he can layer for the walk.
- **FedEx** (`fedex-api`): Tracks book deliveries and gear shipments coming to the townhouse.
- **UPS** (`ups-api`): Tracks inbound packages alongside FedEx for full delivery visibility.
- **Shippo** (`shippo-api`): Handles outbound shipping labels when Steven sends books to David or Pris.
- **Ring** (`ring-api`): Garage and front door cameras at the townhouse. Surface package deliveries; never share the feed.

#### Reading, Knowledge & Productivity

- **Notion** (`notion-api`): Personal knowledge base. Side-project design docs, the Rust CLI notes, the long-running "what comes after the career" thinking.
- **Obsidian** (`obsidian-api`): Local vault for daily thinking and reading marginalia. Syncs to Drive when home.
- **OpenLibrary** (`openlibrary-api`): Reading-queue lookups for the technology history, cognitive science, and literary fiction rotation.
- **Airtable** (`airtable-api`): Personal reading log, the side-project task board, the small wine list of bottles he is curious about. Mirrors the Google Sheet.
- **Confluence** (`confluence-api`): Crescent Peak Confluence is off-limits. Configured for personal project documentation when needed.
- **Contentful** (`contentful-api`): Manages content for the personal reading-notes site Steven is building.
- **Box** (`box-api`): Receives documents that providers or vendors route through Box.
- **Dropbox** (`dropbox-api`): Syncs the local Obsidian vault and the Rust CLI repo snapshots for offsite storage.
- **Linear** (`linear-api`): Personal task tracker for Rust CLI milestones and the long-arc retirement planning checklist. Crescent Peak Linear is off-limits.
- **Jira** (`jira-api`): Crescent Peak Jira is off-limits. Provides ticketing structure for personal contractor coordination.
- **Trello** (`trello-api`): Personal reading list and trip-planning board. Lightweight.
- **Asana** (`asana-api`): Supports travel planning with Lena when the shared task list grows beyond Trello.
- **Monday** (`monday-api`): Provides shared board capability for personal projects that involve collaborators.
- **ServiceNow** (`servicenow-api`): Crescent Peak IT ticketing lives here; agent does not enter.
- **DocuSign** (`docusign-api`): Lease-adjacent paperwork for the townhouse, brokerage forms, dental and vision intake refresh. Never initiate a signature request without explicit approval.
- **Typeform** (`typeform-api`): Conference and meetup registration forms. Never alter a live form mid-collection.

#### Health, Fitness & Cooking

- **MyFitnessPal** (`myfitnesspal-api`): Tracks nutrition and calorie intake during 10K training blocks and diet-adjustment weeks.
- **Strava** (`strava-api`): Logs daily walks, the Peloton-to-pavement training arc, and the 10K race prep. Private profile; do not auto-share.

#### Music, Media & Reading

- **Spotify** (`spotify-api`): Jazz core (late Bill Evans, Brad Mehldau live recordings), ambient electronic from the 90s, classical for focus. "Saturday" and "Focus" playlists are the standing rotations.
- **YouTube** (`youtube-api`): Rust learning channels (Jon Gjengset's *Crust of Rust* series), computing history documentaries, conference talks. Premium account.
- **Vimeo** (`vimeo-api`): Surfaces design and architecture talks referenced by colleagues and the engineering community.
- **TMDB** (`tmdb-api`): Movie and series metadata for the documentaries and limited series rotation (the *AlphaGo* documentary, *Severance*).
- **NASA** (`nasa-api`): Feeds Steven's interest in imaging missions and space exploration data.

#### Shopping, Storefronts & Household

- **Amazon Seller** (`amazon-seller-api`): Manages listings when Steven sells old books or gear through Amazon.
- **Etsy** (`etsy-api`): Sources considered gifts for Helen, Lena, and David's kids based on what they have mentioned wanting.
- **BigCommerce** (`bigcommerce-api`): Connects to specialty booksellers Steven buys from who use the BigCommerce platform.
- **WooCommerce** (`woocommerce-api`): Connects to small Sacramento booksellers Steven buys from who use the WooCommerce platform.

#### Social Platforms & Identity

- **Instagram** (`instagram-api`): Surfaces computing-history accounts and Lena's travel posts from Steven's curated follow list.
- **Pinterest** (`pinterest-api`): Supports the home-office lighting research Steven runs each winter with saved boards and pins.
- **Reddit** (`reddit-api`): Surfaces threads from r/rust, r/sacramento, r/cscareerquestions for the mentor angle, and r/coffee for the Saturday ritual.
- **Twitter** (`twitter-api`): Surfaces posts from computing historians and senior engineering managers Steven follows.
- **Twitch** (`twitch-api`): Surfaces Rust live-coding streams Steven follows while working on the CLI project.
- **LinkedIn** (`linkedin-api`): Professional profile Steven keeps current with career milestones and role changes. Connection requests require approval; no posts without review.

#### Developer Tools, Site Infra & Analytics

- **GitHub** (`github-api`): Personal repos: the Rust CLI he is building, a small notes-on-papers archive, the reading-log script. Crescent Peak GitHub is off-limits.
- **GitLab** (`gitlab-api`): Secondary code host for the Rust CLI, mirroring the GitHub repo for redundancy.
- **Kubernetes** (`kubernetes-api`): Outside his personal stack. Crescent Peak runs its own infra and the agent does not enter.
- **Cloudflare** (`cloudflare-api`): Provides DNS and CDN for the personal reading-notes site Steven is building.
- **PagerDuty** (`pagerduty-api`): Provides alert routing for any personal infrastructure Steven deploys.
- **Sentry** (`sentry-api`): Captures error tracking for the Rust CLI and any personal apps Steven ships.
- **Datadog** (`datadog-api`): Monitors performance for any personal infrastructure Steven deploys.
- **Okta** (`okta-api`): Crescent Peak SSO is off-limits; agent does not touch.
- **Google Analytics** (`google-analytics-api`): Tracks visitor analytics for the personal reading-notes site Steven is building.
- **Mixpanel** (`mixpanel-api`): Provides event-based analytics for the personal reading-notes site alongside Google Analytics.
- **Amplitude** (`amplitude-api`): Provides product analytics for the personal reading-notes site Steven is building.
- **PostHog** (`posthog-api`): Provides open-source analytics as an alternative for the personal reading-notes site.
- **Segment** (`segment-api`): Routes analytics data across providers for the personal reading-notes site.
- **Algolia** (`algolia-api`): Powers search functionality for the personal reading-notes site Steven is building.
- **Webflow** (`webflow-api`): Hosts the landing page for Steven's personal site and reading-notes project.
- **WordPress** (`wordpress-api`): Serves as a content management layer for Steven's personal site and blog drafts.
- **Figma** (`figma-api`): Produces diagrams for the Rust CLI architecture and slides for mentoring calls with Pris.

#### Outbound Email, Newsletters & Forms

- **SendGrid** (`sendgrid-api`): Sends subscriber updates for the personal reading-notes site. All bulk sends require approval.
- **Mailgun** (`mailgun-api`): Provides secondary transactional email delivery, supporting SendGrid as the primary rail.
- **Mailchimp** (`mailchimp-api`): Delivers technology history and Rust newsletters to Steven's inbox. Agent triages; never sends on his behalf.
- **Klaviyo** (`klaviyo-api`): Receives updates and order confirmations from the small Sacramento bookshops Steven subscribes to. No campaign creation.
- **ActiveCampaign** (`activecampaign-api`): Provides subscriber automation for the personal reading-notes site newsletter.

#### Events, Tickets & Home Market

- **Eventbrite** (`eventbrite-api`): Sacramento technology meetups, computing-history talks, and architecture conferences. Confirm before purchase.
- **Ticketmaster** (`ticketmaster-api`): Sacramento jazz performances and symphony nights with Lena. Anything above $500 requires explicit approval.
- **Zillow** (`zillow-api`): Townhouse comparables and the research on a future Sacramento or Sierra foothill move. Research only, no buy signal.

#### CRM, HR & Helpdesk (work-adjacent)

- **Salesforce** (`salesforce-api`): Crescent Peak CRM is off-limits; agent does not enter.
- **HubSpot** (`hubspot-api`): Manages the alumni network contact list from Steven's prior Bay Area roles.
- **Zendesk** (`zendesk-api`): Inbound support tickets for personal subscriptions and devices. Surface escalations only.
- **Freshdesk** (`freshdesk-api`): Provides secondary support ticket routing for personal subscriptions and devices alongside Zendesk.
- **Intercom** (`intercom-api`): Inbound support widgets on subscriptions he uses (Peloton, Audible-adjacent services). Surface escalations only.
- **Twilio** (`twilio-api`): SMS routing for automated reminders (refill checks, race-day check-ins). Drafts require review before sending.
- **Google Classroom** (`google-classroom-api`): Delivers the Stanford online continuing-education course Steven audits each spring.
- **BambooHR** (`bamboohr-api`): Crescent Peak HR runs on a different stack; agent does not enter.
- **Greenhouse** (`greenhouse-api`): Crescent Peak recruiting is off-limits; he does referrals through Anwar, not the system.
- **Gusto** (`gusto-api`): Manages payroll structure for personal contractors Steven engages.

#### Not Connected

- Crescent Peak Software Outlook, Slack, Microsoft Teams, Confluence, Jira, GitHub, ServiceNow, Salesforce, BambooHR, Greenhouse, and Okta. Work systems live on the Dell laptop and the agent does not enter them under any circumstance.
- Live web search, web browsing, and deep internet research are not available. The agent works from connected APIs and stored memory.
- Fidelity 401k, Vanguard brokerage, Ally Bank, and Chase. Direct portals are managed on Steven's phone; Plaid aggregates balances only.
- The Tesla app and the Sense home energy monitor. Both are managed on Steven's phone, not via agent.
- Helen Foster's, David Foster's, Nancy Foster's, and Lena Saito's private accounts. The agent does not log in on their behalf.
- Dr. Rebecca Holtz's Capitol Endocrine portal, Dr. James Fong's Midtown Medical portal, Dr. Anya Petrov's East Sacramento Dental portal, and Dr. Lisa Chang's Capitol Eye Care portal. Communication routes through Steven, not the systems.
