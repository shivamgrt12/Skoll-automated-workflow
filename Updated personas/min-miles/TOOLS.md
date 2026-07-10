# Tools: Min Miles Park

## Tool Usage

### Connected Services

#### Mail, Calendar & Scheduling

- **Gmail** (`gmail-api`): Primary business mailbox at min.miles@Finthesiss.ai. Javier Romero, Isabel Morales, Professor Castillo, export buyers, vendors, and regulatory bodies.
- **Google Calendar** (`google-calendar-api`): Canonical schedule. Grove walks with Pedro, Professor Castillo visits, cooperative meetings, Friday family dinner, harvest milestones.
- **Outlook** (`outlook-api`): Read-only view of an Outlook mailbox used by two European export contacts who prefer it.
- **Calendly** (`calendly-api`): Public scheduling page used only for export buyer intro calls and Professor Castillo consultation slots.
- **DocuSign** (`docusign-api`): EU organic certification paperwork, cooperative agreements, irrigation grant forms, and buyer contracts.

#### Messaging, Meetings & Voice

- **WhatsApp** (`whatsapp-api`): Primary personal channel linked to 555-4400. Soo-Jin, Hana, Ethan, David, Jenny, Pedro, and local Baena contacts.
- **Microsoft Teams** (`microsoft-teams-api`): External Teams calls with the German and UK importers when they request it.
- **Zoom** (`zoom-api`): Backup video for export buyer calls and the occasional Professor Castillo remote consult.
- **Slack** (`slack-api`): Small workspace for the export-focused producer circle he joined in 2025. Read-mostly.
- **Discord** (`discord-api`): One small Andalusian growers server he reads weekly. Quiet observer.
- **Telegram** (`telegram-api`): Reserved for occasional contact with extended family in Korea.
- **Twilio** (`twilio-api`): SMS fallback for two-factor codes and time-critical harvest crew notifications.
- **SendGrid** (`sendgrid-api`): Transactional email for tasting room booking confirmations and buyer order receipts.
- **Mailgun** (`mailgun-api`): Outbound mail relay for automated grove-app notifications.

#### Files, Notes & Knowledge

- **Google Drive** (`google-drive-api`): Estate documents, organic audit packets, buyer contracts, irrigation plans, finance spreadsheets, Soo-Jin's agritourism material.
- **Dropbox** (`dropbox-api`): Photo archive of the estate through the seasons. Master files from the Fujifilm X-T2.
- **Box** (`box-api`): Shared folder with Professor Castillo for soil reports and pest scouting data.
- **Notion** (`notion-api`): Personal estate dashboard, mill room museum planning, harvest year-over-year notes.
- **Obsidian** (`obsidian-api`): Local field notebook on the HP Pavilion. Plot-by-plot observations, pruning records, varietal notes.
- **Confluence** (`confluence-api`): Read access to one shared cooperative knowledge space on organic transition guidance.
- **Airtable** (`airtable-api`): Buyer pipeline, export prospect tracker, harvest yield log by plot.
- **Contentful** (`contentful-api`): CMS behind the Finca Miles tasting page Soo-Jin runs.

#### Grove Science, Weather & Maps

- **OpenWeather** (`openweather-api`): Forecasts for irrigation timing, frost risk in winter, harvest-window shifts, and pest risk windows.
- **NASA** (`nasa-api`): Satellite imagery and drought indices for the Subbetica, useful for climate adaptation context.
- **Google Maps** (`google-maps-api`): Routing for supply runs to Cordoba, buyer visits to Sevilla, and grove access tracks.
- **Kubernetes** (`kubernetes-api`): Read-only access to the cooperative's shared analytics cluster running yield models.
- **Sentry** (`sentry-api`): Error reporting for the Olivia Pro grove monitoring app integration.
- **Datadog** (`datadog-api`): Lightweight monitoring of the HydroSense irrigation controller and weather station uptime.
- **PagerDuty** (`pagerduty-api`): Alerts for irrigation controller faults and weather station outages during harvest.

#### Cooperative, Buyer & Sales Operations

- **HubSpot** (`hubspot-api`): External HubSpot instance used by the cooperative's export programme. Track outreach to specialty importers.
- **Salesforce** (`salesforce-api`): Read-only contact view shared by Romero Gourmet for order coordination.
- **Mailchimp** (`mailchimp-api`): Finca Miles tasting newsletter Soo-Jin sends to the agritourism list quarterly.
- **Klaviyo** (`klaviyo-api`): Email preference management with two specialty food retailers Finca Miles supplies.
- **Linear** (`linear-api`): Tracker for the organic certification transition milestones and irrigation Phase 2 tasks.
- **Jira** (`jira-api`): External Jira used by the EU rural development grant contractor on the irrigation project.
- **Trello** (`trello-api`): Cooperative agenda board and motion tracker.
- **Asana** (`asana-api`): Buyer follow-up board for the export expansion goal.
- **Monday** (`monday-api`): Cooperativa Oleicola Sierra Morena committee task tracker, shared.
- **Typeform** (`typeform-api`): Agritourism booking forms and harvest crew sign-up.

#### Storefront, E-Commerce & Marketing Analytics

- **BigCommerce** (`bigcommerce-api`): The direct-to-consumer Finca Miles storefront Soo-Jin runs.
- **WooCommerce** (`woocommerce-api`): Secondary storefront the agritourism site uses for tasting bookings.
- **Etsy** (`etsy-api`): Small Etsy presence for the gift-pack premium oil line Soo-Jin maintains.
- **Amazon Seller** (`amazon-seller-api`): Read-only watch on the cooperative's Amazon presence, used as competitive awareness.
- **WordPress** (`wordpress-api`): Finca Miles main site, currently low-maintenance.
- **Webflow** (`webflow-api`): Landing page builder Soo-Jin has been evaluating for the agritourism rebuild.
- **Algolia** (`algolia-api`): Product search on the BigCommerce storefront.
- **Mixpanel** (`mixpanel-api`): Visitor analytics for the agritourism site.
- **PostHog** (`posthog-api`): Self-hosted analytics alternative under evaluation.
- **Amplitude** (`amplitude-api`): Product analytics view Soo-Jin tests for the gift-pack funnel.
- **Google Analytics** (`google-analytics-api`): Light analytics on the Finca Miles site.
- **Segment** (`segment-api`): Event pipeline routing tasting-page activity into analytics.
- **ActiveCampaign** (`activecampaign-api`): Newsletter automation Soo-Jin evaluates for the agritourism list.

#### Finance, Brokerage & Payments

- **Stripe** (`stripe-api`): Card payments for tasting bookings and the direct storefront.
- **Square** (`square-api`): Card payments at Soo-Jin's Baena market stall.
- **PayPal** (`paypal-api`): Cross-border payments from UK and Swiss buyers.
- **Plaid** (`plaid-api`): Read-only aggregation of the CaixaBank account for the monthly budget reconciliation.
- **QuickBooks** (`quickbooks-api`): Estate bookkeeping. Operating costs, payroll for seasonal workers, equipment ledger.
- **Xero** (`xero-api`): Secondary bookkeeping for the agritourism arm Soo-Jin manages separately.
- **Intercom** (`intercom-api`): Account-management chat with CaixaBank.
- **Alpaca** (`alpaca-api`): A small experimental brokerage account he opened and rarely touches.
- **Coinbase** (`coinbase-api`): A tiny experimental crypto position he treats as tuition rather than investment.
- **Binance** (`binance-api`): Read-only price view for the experimental crypto position.
- **Kraken** (`kraken-api`): Backup exchange view, unused for transactions.

#### Shipping, Delivery & Errands

- **FedEx** (`fedex-api`): Outbound sample shipments to UK and Swiss specialty importers.
- **UPS** (`ups-api`): Tracking equipment and replacement parts from European suppliers.
- **Shippo** (`shippo-api`): Multi-carrier label generation for gift-pack orders and customer returns.
- **DoorDash** (`doordash-api`): Rarely used. Backup when harvest exhaustion kills the cooking plan.
- **Instacart** (`instacart-api`): Used by Soo-Jin for the occasional Cordoba grocery run during harvest crunch.

#### Identity, Service Desks & Operations

- **Okta** (`okta-api`): Single sign-on for the EU rural development grant portal and the certification body's audit system.
- **Cloudflare** (`cloudflare-api`): DNS and edge protection for the Finca Miles domain.
- **ServiceNow** (`servicenow-api`): External ServiceNow used by the irrigation contractor for ticketing.
- **Zendesk** (`zendesk-api`): Support tickets with Spanish utility, internet, and telecom providers.
- **Freshdesk** (`freshdesk-api`): Support channel for the HydroSense vendor and the Olivia Pro grove app.
- **GitHub** (`github-api`): Read-only. Watching one open-source grove-monitoring tool the cooperative experiments with.
- **GitLab** (`gitlab-api`): Read-only view of a regional research lab's olive disease modelling project.
- **Figma** (`figma-api`): Read-only access to the labels and packaging Soo-Jin's designer shares.

#### Home, Real Estate & Health

- **Ring** (`ring-api`): Cortijo gate camera, used to confirm deliveries and crew arrival times.
- **Zillow** (`zillow-api`): Background awareness on Andalusian rural land values, useful when the cooperative discusses parcel consolidation.
- **MyFitnessPal** (`myfitnesspal-api`): Loose tracking, used in cycles. Consistency patterns only, not calorie pressure.
- **Strava** (`strava-api`): Saturday football and the daily perimeter walk. Private profile.

#### HR, Hiring & Forms

- **BambooHR** (`bamboohr-api`): External BambooHR used by Romero Gourmet for procurement contact coordination.
- **Greenhouse** (`greenhouse-api`): Watches one agronomy job listing the cooperative posts on his behalf.
- **Gusto** (`gusto-api`): Seasonal crew payroll for the harvest workers.

#### Media, Reading & Social

- **Google Classroom** (`google-classroom-api`): Auditing an EU organic compliance refresher course.
- **OpenLibrary** (`openlibrary-api`): Reading log for Korean-Spanish literature and farming memoirs.
- **YouTube** (`youtube-api`): Pruning technique videos, sensory analysis refreshers, and the occasional Real Betis highlight.
- **Vimeo** (`vimeo-api`): Following a small documentary maker covering Andalusian agricultural heritage.
- **TMDB** (`tmdb-api`): Weekend K-drama picks with Soo-Jin.
- **Twitch** (`twitch-api`): Rare. Real Betis match streams when the local broadcast misses one.
- **Spotify** (`spotify-api`): K-pop, Korean traditional, acoustic guitar reference tracks, ambient for grove paperwork.
- **Instagram** (`instagram-api`): Read-only. Follows other small Andalusian producers and Soo-Jin's market posts.
- **Pinterest** (`pinterest-api`): Boards for the agritourism tasting room design Soo-Jin is planning.
- **Reddit** (`reddit-api`): r/olives, r/farming, r/Korea lurker.
- **Twitter** (`twitter-api`): Read-only feed of EU agricultural policy, Andalusian weather watchers, and Real Betis.
- **LinkedIn** (`linkedin-api`): Professional profile and the export-producer network. Posts rarely, reads weekly.
- **Eventbrite** (`eventbrite-api`): Expoliva, regional oliviculture conferences, and the occasional Cordoba cultural evening.
- **Ticketmaster** (`ticketmaster-api`): Real Betis tickets and the occasional concert with Soo-Jin.
- **Yelp** (`yelp-api`): Restaurant scouting in unfamiliar cities during buyer trips.
- **Uber** (`uber-api`): Airport runs from Cordoba and Sevilla for export travel.
- **Amadeus** (`amadeus-api`): Flight search for buyer visits to Germany, the UK, and the long-deferred Korea trip.
- **Airbnb** (`airbnb-api`): Short stays during European buyer trips when small hotels are not available.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. The agent works only from connected mock APIs and stored memory.
- The Cooperativa Oleicola Sierra Morena internal systems, including the pooling ledger and member-only governance documents, are not connected.
- Buyer-internal procurement systems (Romero Gourmet's ERP and the German importer's portal) are not connected.
- The EU rural development grant administration system is accessed only via the Okta-mediated portal, never directly.
- Soo-Jin's private accounts are off-limits.
- Hana's and Ethan's personal devices and accounts are off-limits.
- Social media publishing on Min's behalf is disabled. All social content is draft-only for his review.
