# Tools: Jeff Peterson

## Tool Usage

### Connected Services

#### Patrol, Avalanche & Weather
- **OpenWeather** (`openweather-api`): Mountain forecasts feeding the dawn advisory and tour planning.
- **NASA** (`nasa-api`): Satellite imagery and snow-cover data referenced for regional conditions.
- **PagerDuty** (`pagerduty-api`): On-call escalation for patrol incidents and SAR callouts.
- **ServiceNow** (`servicenow-api`): Files lift, facilities, and equipment incident tickets when patrol spots a problem on the hill, and tracks them to repair.
- **Datadog** (`datadog-api`): Monitors the resort's snow-telemetry feeds so a dropped weather-station sensor gets caught before it skews the morning advisory.
- **Sentry** (`sentry-api`): Watches the public avalanche-advisory web page for errors so any outage gets flagged before skiers rely on a stale page.

#### Training, Fitness & Health
- **Strava** (`strava-api`): Logging trail runs, ski tours, and the 15,000-plus vertical feet a week in winter.
- **MyFitnessPal** (`myfitnesspal-api`): High-protein whole-food tracking, consistency only, without calorie pressure.
- **Calendly** (`calendly-api`): Booking the pre-season physical and PT slots with the team physician.
- **Typeform** (`typeform-api`): Patrol fitness-test intake and incident debrief forms.

#### Avy Course & Education
- **Google Classroom** (`google-classroom-api`): Hosting Avy 1 course materials and student handouts.
- **Eventbrite** (`eventbrite-api`): Registration and RSVPs for the Avy 1 public field courses.
- **OpenLibrary** (`openlibrary-api`): Catalog lookups for mountain and survival reading like "Deep Survival".

#### Communication & Calendar
- **Gmail** (`gmail-api`): Primary email for patrol admin, course coordination, gear orders, and family.
- **Outlook** (`outlook-api`): Secondary address for vendor receipts and pro-deal account logins.
- **Google Calendar** (`google-calendar-api`): Shifts, training, courses, family visits, and races.
- **WhatsApp** (`whatsapp-api`): Quick messages with Cody, Kyle, and the patrol team.
- **Telegram** (`telegram-api`): Backup messaging for backcountry partners with spotty signal.
- **Twilio** (`twilio-api`): Automated SMS reminders for course students and shift coverage.
- **SendGrid** (`sendgrid-api`): Transactional email for course registration confirmations.
- **Mailgun** (`mailgun-api`): Backup bulk sender for larger course mailing lists.
- **Zoom** (`zoom-api`): Virtual patrol briefings and remote course-prep calls.
- **Microsoft Teams** (`microsoft-teams-api`): County SAR coordination meetings.
- **Slack** (`slack-api`): The patrol team channel for daily coordination.
- **Discord** (`discord-api`): The Summit Alpine Guides community server for trip planning.

#### Documents, Notes & Knowledge
- **Google Drive** (`google-drive-api`): Avalanche reports, course materials, SAR documents, and photography.
- **Dropbox** (`dropbox-api`): Backup of large photo libraries and scanned course handouts.
- **Box** (`box-api`): Secure storage for SAR documents shared with the county.
- **Notion** (`notion-api`): Planning hub for the Denali expedition and season goals.
- **Obsidian** (`obsidian-api`): Private notes vault for journaling and route observations.
- **Confluence** (`confluence-api`): Resort patrol procedures and protocol knowledge base.
- **DocuSign** (`docusign-api`): Signatures on the resort revenue-split agreement and SAR waivers.
- **Airtable** (`airtable-api`): Avy 1 course enrollment tracking against the 15-student cap.

#### Finance & Payments
- **Plaid** (`plaid-api`): Bank links for the monthly budget review with Cody.
- **QuickBooks** (`quickbooks-api`): Household budget and Denali-fund savings tracking.
- **Xero** (`xero-api`): Accounting for Avy 1 course revenue and the resort split.
- **Stripe** (`stripe-api`): Online card payments for course tuition.
- **Square** (`square-api`): Point of sale for in-person course gear sales.
- **PayPal** (`paypal-api`): Splitting trip costs with Cody and Kyle.
- **Coinbase** (`coinbase-api`): Holds a small long-term Bitcoin position earmarked for the Denali fund, checked during the monthly budget review with Cody.
- **Binance** (`binance-api`): Tracks crypto prices and a small Ethereum holding he rebalances once or twice a year alongside the Denali savings.
- **Kraken** (`kraken-api`): Runs a small staking position that earns a little toward gear costs, reviewed each quarter.
- **Alpaca** (`alpaca-api`): Drips a small automated index buy each payday into a brokerage sleeve set aside for the land down payment.

#### Gear, Pro Deals & Shopping
- **Amazon Seller** (`amazon-seller-api`): Seller-side listings for reselling lightly used gear and Avy 1 course handout printings; sales, inventory, and payouts only.
- **Etsy** (`etsy-api`): Custom patches and handmade gear repairs.
- **BigCommerce** (`bigcommerce-api`): The Summit Gear pro-deal storefront.
- **WooCommerce** (`woocommerce-api`): Black Diamond pro-deal ordering on a WordPress store.
- **Shippo** (`shippo-api`): Printing return labels for warrantied avalanche gear.
- **FedEx** (`fedex-api`): Tracking pro-deal gear shipments from Dynafit and Ortovox.
- **UPS** (`ups-api`): Tracking parts and Smith Optics replacement orders.

#### Travel & Local
- **Google Maps** (`google-maps-api`): Navigation and timing for trailheads, Bozeman drives, and errands.
- **Yelp** (`yelp-api`): Hours and wait times for The Bird and Rendezvous Bistro.
- **Uber** (`uber-api`): Rides after the end-of-season party so no one drives.
- **Airbnb** (`airbnb-api`): Stays for climbing trips and Wasatch ski weekends.
- **Amadeus** (`amadeus-api`): Flights for the eventual Denali expedition and out-of-state trips.
- **DoorDash** (`doordash-api`): Occasional weeknight delivery after a long shift.
- **Instacart** (`instacart-api`): Bulk grocery runs and chest-freezer restocking.

#### Photography, Media & Leisure
- **Spotify** (`spotify-api`): Folk and Americana playlists for the drive, silence in the backcountry.
- **YouTube** (`youtube-api`): Avalanche technique videos and gear reviews.
- **Vimeo** (`vimeo-api`): Hosting edited backcountry ski and climbing footage.
- **TMDB** (`tmdb-api`): Looking up films for the occasional rest-day evening.
- **Reddit** (`reddit-api`): Backcountry skiing and mountaineering communities for beta.
- **Pinterest** (`pinterest-api`): Saving cabin and gear-storage build ideas.
- **Instagram** (`instagram-api`): Posting landscape and mountain photography to the 8,000-follower account.
- **Twitter** (`twitter-api`): Follows avalanche centers and mountain-weather forecasters and posts the occasional conditions note.
- **LinkedIn** (`linkedin-api`): Professional network of patrollers, guides, and SAR contacts.
- **Twitch** (`twitch-api`): Catches gear-brand product livestreams and live avalanche-education webinars.
- **Ticketmaster** (`ticketmaster-api`): Colter Wall and Tyler Childers show tickets when they tour through.

#### Web Presence & Outreach
- **WordPress** (`wordpress-api`): The personal photography and Avy 1 course site.
- **Webflow** (`webflow-api`): The Avy 1 course landing page and registration microsite.
- **Contentful** (`contentful-api`): Structured content for the course site pages.
- **Algolia** (`algolia-api`): Search across the photo portfolio and course resources.
- **Google Analytics** (`google-analytics-api`): Basic traffic on the photography and course site.
- **Mixpanel** (`mixpanel-api`): Tracks where prospective Avy 1 students drop off in the sign-up funnel so the course page gets tightened before each enrollment window.
- **Segment** (`segment-api`): Routes Avy 1 course sign-up events into the analytics stack so registration data stays consistent across the course tools.
- **Amplitude** (`amplitude-api`): Reads the Avy 1 enrollment funnel week to week to see which outreach fills the 15-student cap fastest.
- **PostHog** (`posthog-api`): Watches session and sign-up trends on the course site to spot pages that confuse prospective students.
- **Figma** (`figma-api`): Designing course handouts, the flyer, and trail-day signage.
- **Mailchimp** (`mailchimp-api`): The Avy 1 course newsletter to past and prospective students.
- **Klaviyo** (`klaviyo-api`): Segmented email reminders for course enrollment windows.
- **ActiveCampaign** (`activecampaign-api`): Follow-up automation for Avy 1 course waitlists.
- **HubSpot** (`hubspot-api`): Lightweight contact list for Avy 1 course inquiries and the Summit Alpine Guides clients Jeff guides on the side.
- **Salesforce** (`salesforce-api`): Logs side-guiding client notes and trip outcomes for the Summit Alpine Guides work Jeff takes in summer.
- **Intercom** (`intercom-api`): Website chat widget answering prospective course-student questions.
- **Zendesk** (`zendesk-api`): Support tickets for Avy 1 course registration questions.
- **Freshdesk** (`freshdesk-api`): Backup support desk for the course site.

#### Work Systems & IT
- **GitHub** (`github-api`): Maintains a small snow-data parsing script and follows open-source avalanche and GPS tools for ideas.
- **GitLab** (`gitlab-api`): Mirror of a snow-data parsing script he tinkers with.
- **Kubernetes** (`kubernetes-api`): Checks the health of the hosted advisory app so Jeff knows the public page is live before pointing the public to it.
- **Cloudflare** (`cloudflare-api`): DNS and security for the photography and course domain.
- **Okta** (`okta-api`): Single sign-on Jeff uses each shift to reach his resort patrol accounts.
- **Jira** (`jira-api`): Files and tracks fixes for the advisory web tool with the resort's site contractor when the public page misbehaves.
- **Linear** (`linear-api`): Course-site feature tasks shared with the freelance developer who built it.
- **Trello** (`trello-api`): A simple board for the Denali expedition gear and logistics.
- **Asana** (`asana-api`): Avy 1 course prep tasks, the field plan, and handout checklist.
- **Monday** (`monday-api`): Backup planning board for the summer trail crew Jeff leads.
- **BambooHR** (`bamboohr-api`): Pulls his own seasonal employee record, time-off balance, and onboarding docs for the new patrollers he helps train.
- **Greenhouse** (`greenhouse-api`): Reviews and scores seasonal patrol candidates through the fall hiring round he interviews for as a senior patroller.
- **Gusto** (`gusto-api`): Reviews his seasonal patrol pay stubs and benefits enrollment each season.
- **Zillow** (`zillow-api`): Tracking Jackson-area land values for the eventual down payment.

#### Home & Pets
- **Ring** (`ring-api`): A single battery doorbell camera at the cabin for package and trailhead-vehicle alerts; the only connected device, not a smart-home system.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from the connected services listed above and from stored memory.
- Resort-internal patrol dispatch and avalanche-control systems are separate and not connected to the assistant.
- Personal banking apps and Cody's private accounts are not connected.
- There is no broader smart-home automation at the cabin; the only connected home device is the single Ring battery doorbell camera.
