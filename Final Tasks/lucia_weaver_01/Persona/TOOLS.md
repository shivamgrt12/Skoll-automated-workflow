# Tools: Lucia Weaver

## Tool Usage

### Connected Services

#### Email & Customer Outreach

- **Gmail** (`gmail-api`): Send and read mail through lucia.weaver@Finthesiss.ai for publisher correspondence, customer requests, author logistics, and grant threads.
- **Outlook** (`outlook-api`): Mirror access for institutional correspondents at Uppsala University and the municipal cultural office who still send from Exchange addresses.
- **Mailchimp** (`mailchimp-api`): Draft and schedule the monthly Weaver & Book newsletter for regulars, with event invites and seasonal recommendations.
- **Klaviyo** (`klaviyo-api`): Segment the customer list by reading interest (literary fiction, poetry, Nordic non-fiction) for targeted small batch campaigns.
- **SendGrid** (`sendgrid-api`): Transactional sends for event ticket confirmations, pre-orders, and reservation receipts.
- **Mailgun** (`mailgun-api`): Backup transactional layer for website order confirmations during the busy Sep to Dec window.
- **ActiveCampaign** (`activecampaign-api`): Light automation for lapsed-customer reactivation in the slow June to August stretch.

#### Messaging & Live Conversations

- **WhatsApp** (`whatsapp-api`): Personal threads with Andrew in Gothenburg, Camilla in Stockholm, and a small group of close author friends.
- **Telegram** (`telegram-api`): Channels for European indie booksellers and a translators' group Lucia follows quietly.
- **Twilio** (`twilio-api`): SMS to Linnea about shift changes and to customers holding reservations who do not check email.
- **Slack** (`slack-api`): The Uppsala independent retailers' working group and the Swedish booksellers' association channel.
- **Discord** (`discord-api`): A poetry community Lucia lurks in for recommendations and translator chatter.
- **Microsoft Teams** (`microsoft-teams-api`): Calls with Uppsala University literature faculty and municipal cultural staff who run on Teams.
- **Zoom** (`zoom-api`): Author conversations for hybrid events, publisher catalogue previews, and the occasional Portland call with Dorothy when phone audio is poor.

#### Calendar, Events & Tickets

- **Google Calendar** (`google-calendar-api`): The shop calendar, Linnea's shifts, author events, family travel, and the personal yoga and reading blocks.
- **Calendly** (`calendly-api`): External booking links for author conversations, journalist requests, and supplier reps.
- **Eventbrite** (`eventbrite-api`): Ticketing for the larger ticketed evenings at the shop and joint events with the municipal library.
- **Ticketmaster** (`ticketmaster-api`): Concert and theatre tickets for Stockholm and Gothenburg trips with Camilla.

#### Documents, Notes & Forms

- **Notion** (`notion-api`): The shop operations workspace: ordering checklists, event playbook, lending shelf log, reading recommendation map.
- **Obsidian** (`obsidian-api`): Lucia's personal reading journal extension, with notes from the Leuchtturm1917 digitised selectively.
- **Airtable** (`airtable-api`): The author and publisher contact base with catalogue cycle dates and past event history.
- **Confluence** (`confluence-api`): Joint planning space with Uppsala University literature department for co-hosted programmes.
- **DocuSign** (`docusign-api`): Lease renewals, consignment agreements, and freelance designer contracts.
- **Typeform** (`typeform-api`): Reader surveys, event feedback forms, and the lending shelf interest list.

#### Shop Storefront, Payments & Marketplaces

- **WordPress** (`wordpress-api`): The current weaverandbook.se site backend until the October 2026 redesign goes live.
- **Webflow** (`webflow-api`): The new website build environment with the freelance designer, targeting October 16, 2026 launch.
- **Contentful** (`contentful-api`): Headless content store for staff picks, event archives, and translated author notes.
- **WooCommerce** (`woocommerce-api`): Online orders, pre-orders, and gift card sales running alongside the WordPress site.
- **Algolia** (`algolia-api`): On-site search tuned for author names, translated titles, and series across English and Swedish stock.
- **Square** (`square-api`): The in-shop point of sale, day-end reporting, and basic inventory linkage; till and live inventory data are imported manually at day-end rather than streamed.
- **Stripe** (`stripe-api`): Online card payments for the website and event ticketing payouts.
- **PayPal** (`paypal-api`): Cross-border payments for international customers buying Swedish and German titles.
- **Etsy** (`etsy-api`): A small side shelf of letterpress bookmarks and reading journals curated with a local maker.
- **Amazon Seller** (`amazon-seller-api`): A small seller-side listing for a handful of Weaver & Book backlist titles directed at North American readers, kept narrow to protect the indie shop identity.

#### Social, Reviews & Discovery

- **Instagram** (`instagram-api`): The @weaverbook account for window displays, staff picks, event teasers, and quiet weekly reading photos.
- **Pinterest** (`pinterest-api`): Mood boards for window displays, seasonal table arrangements, and event posters.
- **Twitter** (`twitter-api`): Light presence for prize news, author interactions, and the Swedish literary community feed.
- **LinkedIn** (`linkedin-api`): Professional account for publisher contacts, distributor reps, and the cultural sector network.
- **Reddit** (`reddit-api`): r/books and r/sweden monitoring for sentiment around Nordic literature and bookshop discussions.
- **YouTube** (`youtube-api`): Recordings of past author conversations posted as a slow growing archive.
- **Vimeo** (`vimeo-api`): Higher fidelity hosting for the launch reel of the new website and the 15th anniversary short film.
- **Twitch** (`twitch-api`): Occasional listen-only literary discussion streams Lucia follows from translator friends.
- **TMDB** (`tmdb-api`): Reference data for book to film adaptation displays in the window.
- **Yelp** (`yelp-api`): Public reviews monitoring for the shop and the cafe next door.
- **Spotify** (`spotify-api`): The in-shop playlists, classical at low volume during the day and jazz for evening events.

#### Finance, Accounting & Markets

- **QuickBooks** (`quickbooks-api`): Backup ledger view for cross-checking with Lars during quarterly reviews.
- **Xero** (`xero-api`): Available but not active, secondary accounting view kept from a brief evaluation before Fortnox took over.
- **Plaid** (`plaid-api`): Available for read-only aggregation if Handelsbanken supports the link, currently not authorised.
- **Alpaca** (`alpaca-api`): US market data reference for cross-checking constituents of the global index funds inside the Avanza ISK, no trading.
- **Coinbase** (`coinbase-api`): Watch-only reference if a customer or supplier ever proposes crypto payment, which Lucia declines politely.
- **Binance** (`binance-api`): Reference rates only, no trading, used to verify any crypto figure that appears in conversations.
- **Kraken** (`kraken-api`): Reference for European crypto pairs alongside Binance, watch-only.

#### Travel, Maps, Weather & Local Delivery

- **Amadeus** (`amadeus-api`): Flight options for Portland visits three to four times a year and the Frankfurt Book Fair in October.
- **Uber** (`uber-api`): Airport runs from Arlanda and occasional Stockholm late evenings with Camilla.
- **Airbnb** (`airbnb-api`): Short stays in Berlin, Edinburgh, and smaller European cities on leisure trips.
- **Google Maps** (`google-maps-api`): Walking routes through Luthagen, supplier visits, and the river Fyris loop.
- **OpenWeather** (`openweather-api`): Daily check for shop window logistics, event evenings, and Sunday forest hikes in Uppland.
- **DoorDash** (`doordash-api`): Available for the three to four Portland visits a year when cooking at Dorothy's house is not feasible; not used in Sweden.
- **Instacart** (`instacart-api`): Available for Portland grocery runs during visits with Dorothy; not used in Sweden.

#### Shipping & Fulfillment

- **Shippo** (`shippo-api`): Label generation for international online orders, mostly to North America and the UK.
- **FedEx** (`fedex-api`): Faster international shipments for signed editions and time-sensitive author returns.
- **UPS** (`ups-api`): Backup carrier for the EU when PostNord delays cluster around Christmas.

#### CRM, Helpdesk & Audience Analytics

- **HubSpot** (`hubspot-api`): Light CRM for publisher contacts, distributor reps, and grant officers.
- **Salesforce** (`salesforce-api`): Read-only view into a shared sector database run by the Swedish booksellers' association.
- **Zendesk** (`zendesk-api`): Customer service tickets from the website, mostly order questions and pre-order timing.
- **Intercom** (`intercom-api`): Live chat option on the new website for opening hours and stock questions.
- **Freshdesk** (`freshdesk-api`): Fallback ticketing if Zendesk costs rise past the small-shop budget.
- **Google Analytics** (`google-analytics-api`): Website traffic patterns, especially around event pages and staff pick posts.
- **Mixpanel** (`mixpanel-api`): Funnel view for the new website's checkout once it launches in October.
- **Amplitude** (`amplitude-api`): Cohort behaviour on the newsletter and pre-order conversion.
- **Segment** (`segment-api`): Single pipe for tracking events from Webflow into the analytics tools without duplicate code.
- **PostHog** (`posthog-api`): Self-hosted product analytics option being evaluated for privacy reasons.

#### Website Build, Design, Code & Infrastructure

- **Linear** (`linear-api`): Issue tracking for the website redesign with the freelance designer.
- **Jira** (`jira-api`): Shared board with the Uppsala University faculty for joint event programmes.
- **Trello** (`trello-api`): Lightweight boards for event planning and seasonal window display cycles.
- **Asana** (`asana-api`): The 15th anniversary celebration plan with the local press contact list.
- **Monday** (`monday-api`): Backup project view if collaborators prefer it over Linear.
- **GitHub** (`github-api`): The freelance designer's repository for the Webflow custom code and CMS scripts.
- **GitLab** (`gitlab-api`): Mirror access if the designer migrates the repo for self-hosted reasons.
- **Figma** (`figma-api`): Website design files, window display mock-ups, and event poster drafts.
- **Sentry** (`sentry-api`): Error monitoring for the new site once Stripe and Webflow are wired up.
- **Datadog** (`datadog-api`): Light uptime monitoring of the website and email forwarding chain.
- **PagerDuty** (`pagerduty-api`): On-call notifications routed to Lucia only during launch week and Christmas peak.
- **Okta** (`okta-api`): Single sign-on for the small set of shop tools as Lucia consolidates passwords.
- **Cloudflare** (`cloudflare-api`): DNS, CDN, and bot protection for weaverandbook.se during Christmas traffic peaks.
- **Kubernetes** (`kubernetes-api`): Reference only, since the freelance designer mentioned a managed cluster for a side service.

#### Reference, HR, Wellness & Home

- **OpenLibrary** (`openlibrary-api`): Bibliographic lookups, edition checks, and translator credits for stock records.
- **NASA** (`nasa-api`): Reference imagery and date checks for an astronomy themed window display planned for January.
- **Google Classroom** (`google-classroom-api`): Access to Linnea's Uppsala University literature seminars where Lucia is invited as a guest reader.
- **MyFitnessPal** (`myfitnesspal-api`): Light tracking around the cholesterol management plan from Dr. Karlsson.
- **Strava** (`strava-api`): Walking and cycling routes through Luthagen and along the Fyris river.
- **Zillow** (`zillow-api`): US property reference for occasional research around Portland near Dorothy's house, since Zillow does not cover the Swedish market.
- **Ring** (`ring-api`): The single doorbell camera at the apartment entrance, used quietly for parcel arrivals.
- **BambooHR** (`bamboohr-api`): Lightweight HR record keeping for Linnea's hours, holidays, and yearly review.
- **Gusto** (`gusto-api`): Reference payroll tool used during a brief 2023 trial before Fortnox took over.
- **Greenhouse** (`greenhouse-api`): Stored templates from a one-off Saturday hire search in 2024, kept for future cover hires.
- **ServiceNow** (`servicenow-api`): Read-only view into Uppsala municipality's cultural sector tickets for joint programming.

#### Not Connected

- Live web search, web browsing, and deep internet research are unavailable inside this session.
- Personal and business banking at Handelsbanken and the Avanza ISK account are not connected; balances and transfers are confirmed by Lucia directly.
- **Fortnox**: The primary bookkeeping system for Weaver & Book (daily invoices, supplier expenses, monthly reconciliation) is run directly by Lucia and is not connected to the agent; the QuickBooks backup ledger is used for any agent-side cross-checks.
- Customers' private accounts, phones, and devices.
- Family members' calendars and email accounts, including Dorothy in Portland and Andrew in Gothenburg.
