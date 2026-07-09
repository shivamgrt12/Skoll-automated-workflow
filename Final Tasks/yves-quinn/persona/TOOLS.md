# Tools: Yves Quinn

## Tool Usage

### Connected Services

#### Communications & Messaging
- **Gmail** (`gmail-api`): Read, draft, send, and search yves.quinn@voissync.ai mail for catering clients, suppliers, hotel-adjacent contacts, and family administrative threads.
- **Outlook** (`outlook-api`): The Hawthorne Grand's internal Outlook tenancy is not connected to Yves personally, so this stays quiet here.
- **WhatsApp** (`whatsapp-api`): Primary channel for Papa Luc, Nathalie, Grand-père Henri, the Montréal family group chat, and a subset of catering clients who prefer it.
- **Slack** (`slack-api`): Stands by for the occasional Patrick Doyle mentor channel; the catering business does not run on Slack.
- **Discord** (`discord-api`): Configured for a Portland food truck owners' server Yves has been considering joining; unused so far.
- **Telegram** (`telegram-api`): On hand for the rare Québec supplier who reaches out on it.
- **Microsoft Teams** (`microsoft-teams-api`): Ready for the corporate catering clients who use Teams for event briefings when Yves needs to dial in.
- **Zoom** (`zoom-api`): Run consultation calls with out-of-town corporate clients and venue site visits when in-person is not possible.
- **Twilio** (`twilio-api`): Send transactional SMS confirmations and reminders to catering clients for day-of pickup or delivery windows.
- **SendGrid** (`sendgrid-api`): Send menu PDFs and quote emails to larger client lists when Gmail send limits would otherwise gate a bulk send.
- **Mailgun** (`mailgun-api`): Alternate transactional email channel for Cuisine du Nord receipts and confirmations.

#### Calendar, Events & Files
- **Google Calendar** (`google-calendar-api`): The single source of truth for Yves's hotel rotation, catering events, farmer's market dates, Papa Luc's appointments, and family commitments.
- **Calendly** (`calendly-api`): Schedule consultation calls for new catering inquiries and tasting bookings without an email back-and-forth.
- **Eventbrite** (`eventbrite-api`): List Cuisine du Nord pop-ups and ticketed tasting events; track guest counts for market days.
- **Ticketmaster** (`ticketmaster-api`): Source show and event tickets for hotel VIP guests as part of the concierge role.
- **Google Drive** (`google-drive-api`): Store catering menus, pricing sheets, signed contracts, event photos, supplier invoices, and the food truck business plan draft.
- **Dropbox** (`dropbox-api`): On standby for the event briefs Lisa Chen occasionally shares over Dropbox links.
- **Box** (`box-api`): Stands by for the Ambervale Properties corporate catering contracts routed through Box.
- **Notion** (`notion-api`): On hand for the mentor pages Patrick Doyle shares; otherwise quiet because Yves does not write in Notion.
- **Obsidian** (`obsidian-api`): The paper notebook and Google Docs cover the same ground, so it stays idle.
- **Airtable** (`airtable-api`): Track Cuisine du Nord client database, lead pipeline, menu version history, and per-event ingredient lists.
- **DocuSign** (`docusign-api`): Send and counter-sign catering contracts, kitchen rental agreements, and any future food truck financing paperwork.

#### Project, Workplace HR & Engineering Ops
- **Trello** (`trello-api`): Track the food truck buildout punch list and the commercial kitchen transition checklist.
- **Asana** (`asana-api`): Configured but quiet; the catering business does not need a second task tracker on top of Trello.
- **Monday** (`monday-api`): Stands by for the corporate client's events team that uses Monday for catering coordination when Yves contributes.
- **Linear** (`linear-api`): Sits idle; Yves does not write code.
- **Jira** (`jira-api`): Quiet for the same reason as Linear.
- **Confluence** (`confluence-api`): Stays dark; documentation lives in Drive and Notion instead.
- **BambooHR** (`bamboohr-api`): The Hawthorne Grand's parent group runs BambooHR for hotel staff, so this stays quiet on the personal side.
- **Gusto** (`gusto-api`): On standby for the future Cuisine du Nord moment where Émile and Sienna get paid regularly as W-2.
- **Greenhouse** (`greenhouse-api`): No hiring at Cuisine du Nord yet, so it stays quiet.
- **GitHub** (`github-api`): No code to host, so it stays untouched.
- **GitLab** (`gitlab-api`): Idle for the same reason as GitHub.
- **Sentry** (`sentry-api`): No engineering surface to monitor, so this stays quiet.
- **Datadog** (`datadog-api`): Dark for the same reason as Sentry.
- **Okta** (`okta-api`): The Hawthorne Grand's SSO uses Okta for hotel internal systems Yves logs into on shift, so it stays employer-side.
- **Cloudflare** (`cloudflare-api`): Stands by behind the Webflow site DNS Patrick configured; Yves does not touch the dashboard.
- **Kubernetes** (`kubernetes-api`): No infrastructure to operate, so it sits idle.
- **PagerDuty** (`pagerduty-api`): Catering crises route through phone calls, not pages, so this stays quiet.
- **Contentful** (`contentful-api`): The Webflow site holds copy directly, so it goes untouched.
- **Algolia** (`algolia-api`): No search surface to power, so it stays dark.
- **Webflow** (`webflow-api`): The Cuisine du Nord landing page lives here on the simple site Patrick helped Yves stand up.
- **WordPress** (`wordpress-api`): The Webflow site replaced any WordPress consideration, so this sits idle.
- **Figma** (`figma-api`): On standby; Canva covers the design needs Yves actually runs.
- **Typeform** (`typeform-api`): Run the Cuisine du Nord catering inquiry intake form linked from the Instagram bio.
- **ServiceNow** (`servicenow-api`): Stands by for the corporate catering client that routes vendor IT tickets through ServiceNow.

#### Finance & Payments
- **Plaid** (`plaid-api`): On standby for linking accounts to budgeting tools; Silverpeak access stays with Yves, so this is not actively wired.
- **Stripe** (`stripe-api`): On standby; Square POS handles catering payment processing today.
- **PayPal** (`paypal-api`): Receive deposits from clients who insist on PayPal; used sparingly.
- **Square** (`square-api`): Process all in-person and online catering payments; primary POS for farmer's market days and event invoices.
- **QuickBooks** (`quickbooks-api`): Planned for Cuisine du Nord books as the business grows past TurboTax; pending Patrick's accountant referral.
- **Xero** (`xero-api`): On standby as the alternate option under consideration before QuickBooks lock-in.
- **Coinbase** (`coinbase-api`): No crypto holdings, so it stays quiet.
- **Binance** (`binance-api`): Idle for the same reason as Coinbase.
- **Kraken** (`kraken-api`): Dark for the same reason as Coinbase.
- **Alpaca** (`alpaca-api`): On standby for the future SEP-IRA conversation Patrick has flagged; no brokerage is open yet.

#### Sales, Marketing, Support & Analytics
- **HubSpot** (`hubspot-api`): On standby for the future where Cuisine du Nord's client list grows past Airtable.
- **Salesforce** (`salesforce-api`): Stands by for the corporate catering clients that run Salesforce for vendor onboarding.
- **Mailchimp** (`mailchimp-api`): Run the Cuisine du Nord seasonal mailing list for réveillon, sugar shack season, and summer markets.
- **Klaviyo** (`klaviyo-api`): On standby for evaluation as the Cuisine du Nord list grows past Mailchimp's free tier.
- **ActiveCampaign** (`activecampaign-api`): Not currently used by the catering business, so it stays idle.
- **Google Analytics** (`google-analytics-api`): Track the Webflow landing page traffic from the Instagram bio.
- **Mixpanel** (`mixpanel-api`): No product analytics surface to instrument, so it stays untouched.
- **PostHog** (`posthog-api`): Quiet for the same reason as Mixpanel.
- **Amplitude** (`amplitude-api`): Idle for the same reason as Mixpanel.
- **Segment** (`segment-api`): No event pipeline to wire up, so it sits idle.
- **Zendesk** (`zendesk-api`): On standby; not used by Cuisine du Nord.
- **Freshdesk** (`freshdesk-api`): Catering support runs through email and SMS, so this stays quiet.
- **Intercom** (`intercom-api`): Dark for the same reason as Freshdesk.

#### Home, Maps & Local
- **Ring** (`ring-api`): Manage the Ring doorbell at the Cedar Ridge apartment; useful when catering supply deliveries arrive while Papa Luc is at parish.
- **Google Maps** (`google-maps-api`): Route catering deliveries, supplier runs, and farmer's market load-in; check traffic before Hawthorne Grand evening shifts.
- **Yelp** (`yelp-api`): Research restaurant recommendations for hotel guests and track Cuisine du Nord's review presence.
- **OpenWeather** (`openweather-api`): Read tomorrow's market forecast; rain on a 1st-Saturday changes load-out, tent setup, and ice strategy.
- **Zillow** (`zillow-api`): On standby for future research on a place with a garage for catering storage when the lease comes up.

#### Travel & Shipping
- **Uber** (`uber-api`): Book rides for late-night hotel shifts when the CR-V is loaded for the next day's catering and parking is gone.
- **Airbnb** (`airbnb-api`): On hand for the hotel-adjacent professional eye when Hawthorne Grand guests compare options.
- **Amadeus** (`amadeus-api`): Search and price flight options for the Montréal trips, especially the Grand-père Henri 80th birthday flight planning.
- **FedEx** (`fedex-api`): Catering is local pickup and delivery only, so it stays quiet.
- **UPS** (`ups-api`): On hand when a specialty supplier ships dry goods (maple sugar, savory, Québec spice blends) from Montréal.
- **Shippo** (`shippo-api`): No shipping operations to coordinate, so it sits idle.

#### Shopping & Marketplace
- **DoorDash** (`doordash-api`): Configured but quiet; Cuisine du Nord delivers via the CR-V, not third-party.
- **Instacart** (`instacart-api`): Run last-minute grocery runs for catering when Yves is on a hotel shift and Papa Luc cannot drive.
- **Etsy** (`etsy-api`): On hand for vintage serving ware sourcing scans when thrift runs come up empty.
- **Amazon Seller** (`amazon-seller-api`): Cuisine du Nord does not sell on Amazon, so this stays dark.
- **BigCommerce** (`bigcommerce-api`): No storefront to run, so it goes untouched.
- **WooCommerce** (`woocommerce-api`): The Webflow site is brochure-only, so it stays quiet.

#### Media, Reading & Education
- **YouTube** (`youtube-api`): Source cooking technique videos for menu R&D and food truck buildout tutorials.
- **Spotify** (`spotify-api`): Cooking playlists for prep nights (indie rock, Celtic folk, Pogues-adjacent racket) and Papa Luc's French folk shuffle.
- **Vimeo** (`vimeo-api`): On hand for the wedding planners who deliver venue walkthroughs over Vimeo.
- **TMDB** (`tmdb-api`): Powers his cooking-competition show discovery when scrolling streaming apps.
- **Twitch** (`twitch-api`): Not on his media diet, so it stays dark.
- **OpenLibrary** (`openlibrary-api`): Look up food memoirs and business books before he buys (currently reading "Unreasonable Hospitality").
- **Google Classroom** (`google-classroom-api`): No formal coursework on his plate, so it sits idle.

#### Health, Fitness & Curiosity
- **MyFitnessPal** (`myfitnesspal-api`): On standby; Yves logs sporadically when Sienna nags him about vegetables.
- **Strava** (`strava-api`): Track walks through Forest Park with Sienna and weekend hike loops; he logs hockey nights here too.
- **NASA** (`nasa-api`): Nothing in his rhythm calls for it, so this stays quiet.

#### Social Media
- **Instagram** (`instagram-api`): Draft captions, plan content, schedule posts, and track DMs for @cuisinedunord.pdx; Yves still posts manually.
- **LinkedIn** (`linkedin-api`): Maintain the concierge and Cuisine du Nord profiles; useful for Lisa Chen's referral chain and event planner network.
- **Twitter** (`twitter-api`): Configured but quiet; not active on Twitter for the business.
- **Reddit** (`reddit-api`): Read r/foodtruck, r/Catering, and r/Portland for buildout horror stories, supplier tips, and local event chatter.
- **Pinterest** (`pinterest-api`): Source aesthetic references for plating, tablescaping, and farmer's market booth styling.

#### Not Connected
- Live web search, real-time web browsing, and deep internet research are unavailable in this assistant context.
- The Hawthorne Grand's internal hotel PMS, point of sale, and HR systems are employer-internal and not connected.
- Oregon Department of Agriculture and the relevant county permitting systems, Oregon business filings, and IRS portals are accessed only by Yves directly.
- Papa Luc's, Nathalie's, Émile's, Sienna's, and Grand-père Henri's private accounts and devices are not connected.
- Square back-office settings and Silverpeak Credit Union banking sit behind Yves's own credentials and are not assistant-managed.
