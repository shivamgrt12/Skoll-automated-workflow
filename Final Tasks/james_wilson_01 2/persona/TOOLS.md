# Tools: James Wilson

## Tool Usage

### Connected Services

#### Calendar, Email, Documents & Forms
- **Gmail** (`gmail-api`): james.wilson@Finthesiss.ai. Commission clients, supply vendors, Etsy notifications, gallery contacts, and most professional correspondence.
- **Google Calendar** (`google-calendar-api`): Studio hours, class slots, therapy, commissions, doctor appointments. The canonical schedule James actually watches.
- **Outlook** (`outlook-api`): University-issued mailbox. Adjunct comms, faculty announcements, payroll receipts, IT notices.
- **Microsoft Teams** (`microsoft-teams-api`): University of Charleston art department meetings and critique recordings. Camera off, audio on, ceramics in hand.
- **Google Drive** (`google-drive-api`): Class rosters, commission contracts, kiln maintenance log, the Sheets that hold finances. The studio file cabinet.
- **Dropbox** (`dropbox-api`): Backup of high-resolution piece photography. Drive is primary, Dropbox is the offsite redundancy synced weekly.
- **Box** (`box-api`): University of Charleston shared art department drive. Critique recordings and syllabi archive; James pulls reference clips for class each week.
- **Notion** (`notion-api`): Class lesson plans, glaze recipe database, commission briefs. The thinking workspace where ideas land before Drive stores them.
- **Obsidian** (`obsidian-api`): Personal vault of glaze notes, kiln logs, and reading journal. Local-first, synced through iCloud to the Pixel.
- **Airtable** (`airtable-api`): Studio project and contact base. Studio projects (kiln upgrade, class series, website refresh), the task list that runs them, and the studio contact roster. Task reminders route to Gmail.
- **Confluence** (`confluence-api`): Adjunct syllabi and University of Charleston art department policies. James contributes to the ceramics curriculum page each semester.
- **DocuSign** (`docusign-api`): Commission contracts and dinnerware delivery acceptance forms. Marco signed the spring set this way; every commission over $500 routes here.
- **Calendly** (`calendly-api`): Public link for studio tours and commission consults. Buffers around Wednesday therapy and Thursday dinner with Vera are hard-locked.
- **Typeform** (`typeform-api`): Class registration form for new community session rounds. Six-week sessions open registration here; waitlists route to ActiveCampaign.
- **Monday** (`monday-api`): Production board for the active dinnerware commission and the fall semester student-project pipeline. One card per piece, status tracked weekly.

#### Storefront, Sales & Shipping
- **Etsy** (`etsy-api`): Wilson Ceramics shop. Listings, orders, messages, fee tracking. Drafts and inventory edits flow through OpenClaw; final publish is on the MacBook.
- **Amazon Seller** (`amazon-seller-api`): Wilson Ceramics on Amazon Handmade. Listings for the small stoneware mug line; weekly inventory sync from Etsy and monthly sales totals into QuickBooks.
- **WooCommerce** (`woocommerce-api`): Direct-buy layer on wilsonceramics.com for Charleston-pickup customers who skip Etsy fees. Three to five orders a month, mostly mugs and small bowls.
- **BigCommerce** (`bigcommerce-api`): Wholesale ordering portal at wilsonceramics.com/wholesale for Tamarack Marketplace, Capitol Market Gift Shop, and Mountain Stage Gift Shop to place restock orders.
- **Stripe** (`stripe-api`): Etsy passes through Stripe; commission deposits and WooCommerce orders land here. Reconciled against QuickBooks monthly.
- **Square** (`square-api`): Mirror of the in-studio POS terminal. Daily tip and sales totals sync into QuickBooks; James reads the morning summary with coffee.
- **PayPal** (`paypal-api`): Commission deposits from clients who prefer PayPal over Stripe. Reconciled into QuickBooks the same as everything else.
- **Plaid** (`plaid-api`): Wires City National Bank balance and recent-transaction snapshot into QuickBooks each evening so commission deposits reconcile without opening the banking app.
- **Shippo** (`shippo-api`): Etsy, WooCommerce, and commission shipping labels. Boxes sized once a quarter so postage stays predictable.
- **FedEx** (`fedex-api`): Commission shipments to out-of-state collectors. Heavier pieces only, with insurance always.
- **UPS** (`ups-api`): Standard Etsy and WooCommerce shipping for everything that fits the quarterly box sizing.

#### Studio Creative & Reference
- **Pinterest** (`pinterest-api`): Glaze boards, form references, kiln-load mood boards. Inspiration scout for the next class theme.
- **Instagram** (`instagram-api`): @wilson.ceramics scheduling layer. James drafts captions; OpenClaw queues posts for the Tuesday and Friday morning publishing windows on the Pixel.
- **Figma** (`figma-api`): Etsy listing graphics, class flyer mockups, simple WordPress hero edits. James is competent, not a designer.
- **Vimeo** (`vimeo-api`): Hosts the Wilson Ceramics commission process reels and the private archive of wheel-throwing demonstrations recorded for the adjunct class.
- **YouTube** (`youtube-api`): @wilsonceramics channel hosts the quarterly studio journal vlog: glaze experiments, kiln-loading walkthroughs, mushroom-foraging notes from the fall.
- **OpenLibrary** (`openlibrary-api`): Backup catalog for the public library queue. Marguerite Wildenhain, Bernard Leach, Marilynne Robinson, Ocean Vuong.
- **TMDB** (`tmdb-api`): Movie lookups when Vera and James plan a Thursday dinner film. Charleston theaters are limited, so James plans ahead.
- **NASA** (`nasa-api`): Sunrise and moon-phase data for kiln-firing aesthetic timing on the studio journal. Light, almost ritual.
- **Contentful** (`contentful-api`): Holds the Wilson Ceramics class catalog. Class title, description, dates, fee, and instructor bio push into the WordPress site and the Mailchimp newsletter automatically.
- **Webflow** (`webflow-api`): Hosts wilsonceramics.com/portfolio, the curated piece archive that visitors browse before reaching out about a commission. Updated whenever a kiln load finishes.
- **WordPress** (`wordpress-api`): wilsonceramics.com runs on WordPress. Studio journal posts, class schedule, gallery shots.
- **Algolia** (`algolia-api`): Powers the search bar on wilsonceramics.com across the gallery archive, the studio journal posts, and the class catalog. Re-indexed weekly.
- **Spotify** (`spotify-api`): Studio soundtrack. Indie folk for morning throwing, ambient for glazing, jazz for long firing afternoons.

#### Teaching, Tasks & Classroom
- **Google Classroom** (`google-classroom-api`): University of Charleston ceramics section. Critique calendar, assignment posts, grade entry. Spring and fall.
- **Asana** (`asana-api`): University course planning board, rebuilt per semester. Syllabus, critique calendar, grading rubric.
- **Trello** (`trello-api`): Commission pipeline board: brief, sketches, throwing, bisque, glaze, fire, ship. One card per piece.
- **Jira** (`jira-api`): Wilson Ceramics studio operations board. Kiln maintenance, glaze batch QA, supply restocks each tracked as a Kanban card.
- **Linear** (`linear-api`): Wilson Ceramics product roadmap. New mug lines, planter shapes, seasonal collections each get an issue with a target firing date.

#### Health, Movement & Body
- **MyFitnessPal** (`myfitnesspal-api`): IBS food log, FODMAP tracking, peppermint-oil-before-meals reminders. Patterns only, no calorie pressure.
- **Strava** (`strava-api`): Daily walk down Capitol Street to the river and back. Pace, not performance.

#### Finance, Tax & Crypto
- **QuickBooks** (`quickbooks-api`): Wilson Ceramics books. Class income, commission deposits, supply expenses, self-employment tax set-aside.
- **Xero** (`xero-api`): Secondary books for the University of Charleston adjunct income stream. Kept separate from Wilson Ceramics in QuickBooks for clean 1099 vs Schedule C splits.
- **Gusto** (`gusto-api`): Self-employment quarterly tax estimates. Wilson Ceramics has no employees; this is James's own payroll math.
- **Coinbase** (`coinbase-api`): Holds 0.05 BTC and 1.2 ETH that Joel routed here for James's 40th birthday in 2024. Quarterly balance check feeds the QuickBooks personal-holdings line.
- **Binance** (`binance-api`): Binance.US off-ramp for low-fee Coinbase-to-USD conversions when James liquidates a slice for kiln repairs or studio insurance renewal. Used about once a year.
- **Kraken** (`kraken-api`): Staking position Joel set up alongside Coinbase. About $300 of ATOM at fourteen percent APY; quarterly staking rewards land as miscellaneous income in QuickBooks.
- **Alpaca** (`alpaca-api`): Roth IRA position. Auto-deposit of $50 monthly into a three-fund index allocation; quarterly statement reviewed against the retirement plan.

#### Community, Friends & Audience
- **WhatsApp** (`whatsapp-api`): Joel and Patricia. Family thread for Sunday call logistics and Mother's Day checkpoints.
- **Slack** (`slack-api`): MFA cohort workspace. James posts a question or answer about twice a month in #throwing-troubleshoot and #glaze-help.
- **Telegram** (`telegram-api`): Nadia and the Capitol Street small-business group thread for snow days, lunch coordination, and neighborhood notes.
- **Discord** (`discord-api`): Appalachian Ceramicists server. James posts kiln-firing photos and answers newcomer questions in #glaze-help most weeks.
- **Twitter** (`twitter-api`): @wilsonceramics. New Etsy listings and class openings posted twice a week; mostly outbound.
- **LinkedIn** (`linkedin-api`): Adjunct profile. Quarterly Wilson Ceramics commission portfolio updates posted; alumni intros land in DMs a few times a year.
- **Reddit** (`reddit-api`): Moderates r/AppalachianMakers, a small community of regional craftspeople. About thirty minutes a week of light moderation and answers.
- **Twitch** (`twitch-api`): Follows @clayworkshop, @ceramicwheel, and Pottery-with-Pat. Tunes in Sunday afternoons during firing downtime.
- **HubSpot** (`hubspot-api`): Light CRM for commission clients and gallery contacts. Notes on who wants what, when. Self-built lightweight pipeline.
- **Salesforce** (`salesforce-api`): University of Charleston art department alumni and donor pipeline. James syncs commission alumni back to the department each term as a courtesy.
- **Mailchimp** (`mailchimp-api`): Quarterly Wilson Ceramics newsletter to past students and gallery contacts. Voice is dry and short, like James.
- **SendGrid** (`sendgrid-api`): Transactional sends for Etsy order confirmations, class registration receipts, and the short thank-you template James fires after each commission delivery.
- **Mailgun** (`mailgun-api`): Transactional delivery for the WordPress site contact form. Spam triage runs weekly.
- **Klaviyo** (`klaviyo-api`): Lifecycle emails for Etsy customers: order confirmation, restock nudge, the once-a-quarter check-in. Tuned conservatively so it never feels pushy.
- **ActiveCampaign** (`activecampaign-api`): Wilson Ceramics class waitlist drip. When a session fills, ActiveCampaign nudges waitlisted students about next-session dates and adjacent workshop offers.
- **Twilio** (`twilio-api`): SMS reminders to enrolled students before classes. Used sparingly, one ping a week max so it never feels spammy.

#### Customer Care, Helpdesk & Meetings
- **Zendesk** (`zendesk-api`): Inbound commission inquiries from wilsonceramics.com/contact. Three to five tickets a week from prospective clients; James responds within 48 hours.
- **Intercom** (`intercom-api`): Live chat widget on wilsonceramics.com, set to office-hours-only. Most questions are class scheduling.
- **Freshdesk** (`freshdesk-api`): Routes University of Charleston student questions about adjunct class logistics, supply lists, and critique dates, separate from the Wilson Ceramics commission inbox.
- **ServiceNow** (`servicenow-api`): University IT ticketing for Microsoft Teams and Box outages during critiques. Two or three escalations per academic year.
- **Zoom** (`zoom-api`): Virtual studio visit for long-distance commission consults. About one a month, usually at 7:00 PM ET after the day's classes.

#### Local, Travel & Errands
- **Google Maps** (`google-maps-api`): Delivery routing to Huntington for commissions, mushroom-foraging waypoints, kiln-supply pickup stops, Tamarack Marketplace booth load-in.
- **Yelp** (`yelp-api`): Pies and Pints, Cafe Appalachian, Tidewater Grill bookmarks. Scouts IBS-safe menus when traveling for a craft fair.
- **OpenWeather** (`openweather-api`): Kiln-firing humidity check, walking-weather peek, market-day forecast for outdoor craft fairs.
- **Uber** (`uber-api`): Uber Reserve for the airport run to Yeager Field for the Penland pottery workshop trip, and the occasional ride home from a Charleston Coliseum event.
- **DoorDash** (`doordash-api`): Backup dinner from Cafe Appalachian when an IBS day rules out cooking. Same safe menu items every time.
- **Airbnb** (`airbnb-api`): MFA-friend visits and the rare Asheville pottery workshop weekend. Saved searches for cabins under $90 a night.
- **Amadeus** (`amadeus-api`): Travel pricing for the occasional pottery workshop in Asheville or Penland. Compared against Airbnb.
- **Eventbrite** (`eventbrite-api`): Local craft fair sign-ups, Charleston gallery openings, Capitol Market and Tamarack Marketplace booth registrations.
- **Ticketmaster** (`ticketmaster-api`): Charleston Coliseum and Mountain Stage live tapings. James and Vera attend about three shows a year, usually folk or alt-country.
- **Ring** (`ring-api`): Front door of 208 Capitol Street. Studio package alerts during daytime clay shipments. Notifications to phone.
- **Zillow** (`zillow-api`): Tracks Capitol Street block valuations because the studio building lease is up in March 2027 and the option to buy is on the table.
- **Instacart** (`instacart-api`): Backup grocery run when an IBS flare keeps James off the road. Mountain State Coffee beans and IBS-safe staples only.

#### People Ops & Hiring
- **BambooHR** (`bamboohr-api`): University of Charleston adjunct HR records. Direct deposit, W2, contract renewal letters.
- **Greenhouse** (`greenhouse-api`): University of Charleston art department adjunct hiring committee. James reviews ceramics adjunct candidates each spring search.

#### Developer, Auth & Site Analytics
- **GitHub** (`github-api`): Maintains the public repo wilson-ceramics/glaze-recipes: cone 6 glaze recipes James has tested, with photos, firing schedules, and notes. Updated after each new recipe lands.
- **GitLab** (`gitlab-api`): Charleston Public Library small-business workshop series wiki. James co-runs the October session each year; the wiki holds slides, handouts, and registration sheets for next year's instructors.
- **Sentry** (`sentry-api`): Catches WordPress and WooCommerce errors on wilsonceramics.com. James reviews the weekly error digest with morning coffee on Monday.
- **Datadog** (`datadog-api`): Joel set up dashboards for wilsonceramics.com uptime and the daily Etsy order-sync job. James reads the dashboard during the monthly site review.
- **PagerDuty** (`pagerduty-api`): Routes kiln temperature anomaly alerts from the studio's smart kiln controller to James's Pixel during overnight firings. Joel is the secondary contact.
- **Cloudflare** (`cloudflare-api`): DNS and caching for wilsonceramics.com. The Etsy storefront is the volume shop; the site is the portfolio and class catalog.
- **Kubernetes** (`kubernetes-api`): The wilsonceramics.com WordPress site runs on the small Kubernetes cluster Joel maintains from his home in Morgantown. James reads the weekly uptime summary Joel sends during their Sunday call.
- **Okta** (`okta-api`): Single sign-on for the University of Charleston adjunct login. Therapy portal uses its own credentials.
- **Google Analytics** (`google-analytics-api`): Foot-traffic peek on the studio site. James reads the monthly summary, not the weekly noise.
- **Mixpanel** (`mixpanel-api`): Tracks Etsy click-through from wilsonceramics.com. Which gallery pieces drive Etsy purchases feeds the quarterly inventory rebuild plan.
- **Amplitude** (`amplitude-api`): Newsletter open and click trends. Used to decide whether to write the next issue or skip a quarter.
- **PostHog** (`posthog-api`): Self-hosted complement on the WordPress site. Session replays on the commission inquiry and class registration pages to spot drop-off points.
- **Segment** (`segment-api`): Single source-of-truth event router for wilsonceramics.com analytics. Routes the same event stream into Google Analytics, Mixpanel, and Amplitude.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from the connected services listed above and from stored memory.
- City National Bank: Direct banking-app access stays on the Pixel 7a only. The Plaid integration above provides balance and reconciliation only; no transfers or transactions run through OpenClaw.
- Therapy and medical patient portals: Dr. Morris's therapy portal, the CAMC portals for Dr. Stokes and Dr. Hart, and Dr. Chen's dental portal are all behind their own credentials and are not connected.
- Nick Claxton's accounts and any prior shared workspaces from the marriage: Off-limits, full stop.
- University of Charleston student information system: Separate from BambooHR and Box. Grade entry uses Google Classroom; SIS access is not connected.
