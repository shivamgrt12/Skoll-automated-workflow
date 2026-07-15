# Tools: Nancy Crawford

## Tool Usage

### Connected Services

#### Personal Email & Calendar

- **Gmail** (`gmail-api`): Drafts and triages Nancy's primary inbox at nancy.crawford@Finthesiss.ai for gallery, commission, and Harrington correspondence.
- **Google Calendar** (`google-calendar-api`): Holds the single source of truth for studio blocks, teaching days, gallery deadlines, and personal commitments.
- **Outlook** (`outlook-api`): Reads Harrington Arts Academy threads that cross over from the institutional inbox.

#### Files & Notes

- **Notion** (`notion-api`): Tracks piece-by-piece planning for the Ironwork solo show and the running ideas notebook.
- **Obsidian** (`obsidian-api`): Captures long-form reading notes and source threads from Nancy's offline work at the loft.
- **Confluence** (`confluence-api`): Maintains shared faculty documentation at Harrington.

#### Spreadsheets & Documents

- **Airtable** (`airtable-api`): Holds the working inventory of finished and in-progress pieces with dimensions, materials, and gallery status.
- **DocuSign** (`docusign-api`): Signs commission contracts and gallery consignment paperwork after Nancy reviews them.

#### Navigation & Weather

- **Google Maps** (`google-maps-api`): Routes studio errands across Fishtown, gallery visits, and train trips to Brooklyn or Hartford.
- **OpenWeather** (`openweather-api`): Checks the forecast for morning walks, Schuylkill bike rides, and outdoor framing or shipping days.

#### Banking & Payments

- **Stripe** (`stripe-api`): Processes direct commission invoicing when Nancy bills outside the gallery middleman.
- **Plaid** (`plaid-api`): Builds budgeting views across the Keystone CCU account and the Citi Double Cash card.
- **PayPal** (`paypal-api`): Receives buyer transactions and pays supply vendors that prefer it.
- **Square** (`square-api`): Runs in-person sales at open studios and pop-up gallery events.
- **QuickBooks** (`quickbooks-api`): Keeps the simple ledger Nina Voss reviews at tax time.
- **Xero** (`xero-api`): Mirrors the ledger as a parallel view for Nina Voss.
- **Gusto** (`gusto-api`): Runs payroll for a studio assistant when Nancy hires one.

#### Logistics & Shipping

- **FedEx** (`fedex-api`): Ships finished pieces to Marisol Espinoza at Sable & Thread in Brooklyn and to Dana Reyes at Silverline.
- **UPS** (`ups-api`): Ships pieces when FedEx pickup windows do not match Nancy's studio hours.
- **Shippo** (`shippo-api`): Generates labels for batched shipments of smaller works.
- **Instacart** (`instacart-api`): Orders grocery delivery during deadline weeks when Nancy stays in the studio.
- **DoorDash** (`doordash-api`): Orders dinner from Tau Noodle House on long studio nights.

#### Travel & Mobility

- **Amadeus** (`amadeus-api`): Researches Portugal residency travel options.
- **Uber** (`uber-api`): Books airport runs and late-night rides when SEPTA doesn't fit.
- **Airbnb** (`airbnb-api`): Books Hartford visits to Ruth and residency scouting in Portugal.

#### Communication

- **Slack** (`slack-api`): Posts to group threads the Harrington studio art department spins up.
- **Microsoft Teams** (`microsoft-teams-api`): Joins Harrington faculty meetings routed through Teams.
- **Zoom** (`zoom-api`): Hosts gallery studio visits and collector calls.
- **WhatsApp** (`whatsapp-api`): Carries Nancy's thread with Margaux from Brooklyn and on travel.
- **Telegram** (`telegram-api`): Sends and receives messages on Nancy's backup messenger channel.
- **Discord** (`discord-api`): Reads the art-community server threads Nancy follows.
- **Twilio** (`twilio-api`): Sends SMS reminders for appointments and deadlines.
- **SendGrid** (`sendgrid-api`): Sends opening-announcement emails for the Ironwork solo and other shows.
- **Mailgun** (`mailgun-api`): Delivers transactional mail as the backup route.

#### Productivity & Project Management

- **Asana** (`asana-api`): Tracks the Ironwork solo show task list, gated by gallery milestones.
- **Trello** (`trello-api`): Tracks the Silverline triptych board: design, fabrication, photography, shipping.
- **Monday** (`monday-api`): Maps a parallel cross-project planning board.
- **Linear** (`linear-api`): Tracks portfolio-site changes.
- **Jira** (`jira-api`): Tracks portfolio-site issues alongside Linear.
- **Calendly** (`calendly-api`): Books student office-hour slots during teaching weeks.
- **Typeform** (`typeform-api`): Builds application forms tied to residency calls.

#### Marketing & CRM

- **HubSpot** (`hubspot-api`): Maintains the collector contact list and gallery follow-ups.
- **Salesforce** (`salesforce-api`): Maintains the collector pipeline alongside HubSpot.
- **Mailchimp** (`mailchimp-api`): Sends opening-announcement emails to Nancy's private collector list.
- **Klaviyo** (`klaviyo-api`): Sends alternate announcement campaigns to the collector list.
- **ActiveCampaign** (`activecampaign-api`): Sends follow-up sequences after opening-night events.
- **Intercom** (`intercom-api`): Answers visitor inquiries on the portfolio site.
- **Zendesk** (`zendesk-api`): Routes portfolio-site visitor tickets alongside Intercom.
- **Freshdesk** (`freshdesk-api`): Routes overflow portfolio-site inquiries.

#### Social & Press

- **Instagram** (`instagram-api`): Posts to Nancy's studio account after Nancy approves the caption and image.
- **Pinterest** (`pinterest-api`): Saves visual research and reference boards for upcoming work.
- **YouTube** (`youtube-api`): Surfaces studio reference videos and documentaries on Nancy's reading list.
- **Twitter** (`twitter-api`): Posts exhibition announcements once Nancy approves them.
- **LinkedIn** (`linkedin-api`): Updates academic appointments and gallery-introduction context.
- **Reddit** (`reddit-api`): Reads art-community threads Nancy follows for studio research.
- **Twitch** (`twitch-api`): Streams live studio demos when Nancy schedules one.
- **Vimeo** (`vimeo-api`): Hosts documentation video from past installations.

#### Storefront & E-commerce

- **Etsy** (`etsy-api`): Lists small print editions Nancy releases.
- **BigCommerce** (`bigcommerce-api`): Runs the print-sales storefront.
- **WooCommerce** (`woocommerce-api`): Powers an alternate storefront on the portfolio.
- **Amazon Seller** (`amazon-seller-api`): Lists print editions on the marketplace.
- **Webflow** (`webflow-api`): Publishes the portfolio site Nancy keeps under their own name.
- **WordPress** (`wordpress-api`): Powers the backup CMS for the portfolio.
- **Contentful** (`contentful-api`): Powers a headless CMS option for the portfolio.

#### HR/Recruiting/Workforce

- **BambooHR** (`bamboohr-api`): Handles Harrington adjunct HR threads.
- **Greenhouse** (`greenhouse-api`): Tracks applicants for a future studio-assistant search.
- **Okta** (`okta-api`): Manages SSO into Harrington systems.
- **ServiceNow** (`servicenow-api`): Routes Harrington IT service tickets through Margaret Bell's office.

#### Developer/SRE/Observability

- **GitHub** (`github-api`): Versions the portfolio site files.
- **GitLab** (`gitlab-api`): Mirrors the portfolio repository as an alternate.
- **Datadog** (`datadog-api`): Watches portfolio-site uptime.
- **Sentry** (`sentry-api`): Reports portfolio-site errors to Owen Pratt, the portfolio's volunteer dev.
- **PagerDuty** (`pagerduty-api`): Alerts on portfolio-domain incidents.
- **Cloudflare** (`cloudflare-api`): Manages the portfolio domain configuration and cache.
- **Kubernetes** (`kubernetes-api`): Runs the containerized hosting for the portfolio.

#### Analytics & Search

- **Google Analytics** (`google-analytics-api`): Tracks portfolio-site traffic.
- **Mixpanel** (`mixpanel-api`): Tracks portfolio-visitor behavior alongside Google Analytics.
- **Amplitude** (`amplitude-api`): Provides an alternate analytics view for the portfolio.
- **PostHog** (`posthog-api`): Tracks portfolio product analytics and feature flags.
- **Segment** (`segment-api`): Routes portfolio analytics events across destinations.
- **Algolia** (`algolia-api`): Powers search on the portfolio site.

#### Design & Media

- **Figma** (`figma-api`): Drafts layout mockups for catalogue pages and exhibition postcards.
- **NASA** (`nasa-api`): Pulls celestial reference imagery for collage work.
- **TMDB** (`tmdb-api`): Tracks the indie and foreign cinema Nancy watches at art-house theatres.
- **Spotify** (`spotify-api`): Plays Coltrane, Monk, ambient electronic, and classical playlists in the studio.

#### Tickets/Events/Local

- **Eventbrite** (`eventbrite-api`): Books art-world events around Philadelphia and Brooklyn.
- **Ticketmaster** (`ticketmaster-api`): Books concert tickets in Philadelphia.
- **Yelp** (`yelp-api`): Checks restaurant options around Fishtown when Nancy hosts a visiting dealer.
- **Zillow** (`zillow-api`): Tracks studio-space listings around Fishtown.

#### Crypto & Trading

- **Coinbase** (`coinbase-api`): Holds the wallet that accepts crypto commission payments.
- **Binance** (`binance-api`): Holds the alternate crypto wallet.
- **Kraken** (`kraken-api`): Holds another crypto exchange option.
- **Alpaca** (`alpaca-api`): Holds the brokerage account for future investment activity.

#### Fitness/Health/Outdoors

- **Strava** (`strava-api`): Tracks the weekend Schuylkill bike rides and longer walks.
- **MyFitnessPal** (`myfitnesspal-api`): Plans pescatarian meals around the studio and teaching schedule.

#### Education & Classroom

- **Google Classroom** (`google-classroom-api`): Runs the Tuesday and Thursday Harrington courses, assignments, and student feedback.
- **OpenLibrary** (`openlibrary-api`): Pulls reading lists for studio research and student bibliographies.

#### Smart Home & Devices

- **Ring** (`ring-api`): Manages the doorbell-camera setup Nancy is rolling out at the Fishtown loft.

#### Not Connected

- The Harrington Arts Academy institutional email ncrawford@harringtonartsacademy.edu lives in Outlook, accessed by Nancy directly.
- Banking apps for Keystone Community Credit Union and the Citi Double Cash card stay on Nancy's phone, not linked here.
- TIAA retirement is reviewed by Nancy with Nina Voss at tax time, not linked here.
- The Independence Blue Cross ACA Silver insurance portal is handled by Nancy directly, not by you.
- Gallery point-of-sale systems at Ironwork and Sable & Thread are handled by those staff, not by you.
- Live web search, web browsing, and deep internet research are unavailable to you; you work only from connected services and stored context.
