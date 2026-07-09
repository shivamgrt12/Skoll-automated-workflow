# Tools: Joseph Fields

## Tool Usage

### Connected Services

#### Schedule, Mail & Family Logistics
- **Google Calendar** (`google-calendar-api`): The custody calendar and work shifts live here. Custody weekends are marked; never let an entry overlap custody time without confirming.
- **Gmail** (`gmail-api`): Joseph's personal inbox at joseph.fields@gmail.com. Summarize school and family mail; do not send to new contacts without approval.
- **Outlook** (`outlook-api`): Manages the thread when a school or league switches to Outlook; reads, summarizes, and drafts replies to send after Joseph confirms.
- **Calendly** (`calendly-api`): Booking link for Tyler's coach and the boys' school when they offer self-scheduled meeting slots.
- **WhatsApp** (`whatsapp-api`): Backup channel for Scott, who sometimes coordinates fishing trips there. Text is still primary.
- **Telegram** (`telegram-api`): Posts Joseph's check-ins to Connor's gaming group chat and forwards the highlights worth following up on.
- **Slack** (`slack-api`): Posts carpool and snack-schedule updates to the youth-basketball parents workspace for Tyler's team logistics.
- **Discord** (`discord-api`): Posts to Connor's Minecraft server to coordinate weekend play sessions and relay messages between the boys.
- **Microsoft Teams** (`microsoft-teams-api`): Occasional meeting link from the boys' school when staff use Teams.
- **Zoom** (`zoom-api`): Parent-teacher conferences and the rare remote VA appointment.

#### Phones, Devices & Home
- **Ring** (`ring-api`): The apartment door camera. Note deliveries and flag anything that needs attention while he is on a job.
- **Twilio** (`twilio-api`): Backs SMS reminders for custody pickups and bill due dates.
- **SendGrid** (`sendgrid-api`): Sends the templated calendar summaries Joseph asked to receive by email.
- **Mailgun** (`mailgun-api`): Fallback delivery for those same reminder emails if SendGrid stalls.
- **Twitch** (`twitch-api`): Manages Joseph's follows of the streamers Connor likes and posts clips to chat so he can connect over Connor's interests.
- **YouTube** (`youtube-api`): HVAC diagnostic walkthroughs and the boys' channels. Pull repair references and watch history he shares.
- **Spotify** (`spotify-api`): Classic rock, country, and 90s alternative for the drive and the kitchen. Build the playlists he names.

#### Money & Bills
- **Plaid** (`plaid-api`): Syncs the Buckeye Federal account and runs the twice-weekly review, categorizing transactions and flagging overspend Joseph should act on.
- **QuickBooks** (`quickbooks-api`): Tracks his side-cash HVAC jobs and tool expenses for tax season.
- **Xero** (`xero-api`): Syncs shared tool purchases into the ledger Kevin set up so the brothers' books reconcile.
- **Stripe** (`stripe-api`): Collects payment on the occasional weekend cash job invoice.
- **Square** (`square-api`): Card reader for those same off-hours repair jobs when a customer cannot pay cash.
- **PayPal** (`paypal-api`): Splits fishing-trip costs with Scott and the Memorial Day cookout supplies with Kevin.
- **Coinbase** (`coinbase-api`): Manages the tiny crypto position Kevin talked him into and executes his rebalances; confirm before placing any trade.
- **Alpaca** (`alpaca-api`): Runs the monthly auto-invest into the index ETF he set up after the podcast; confirm before changing the amount.
- **Binance** (`binance-api`): Reconciles the small balance against Coinbase weekly and rotates the API keys whenever a security alert fires.
- **Kraken** (`kraken-api`): Runs the small recurring dollar-cost buy Kevin set up here; confirm each order before it places.
- **DocuSign** (`docusign-api`): Signs the apartment lease renewal and custody paperwork when it comes electronically.

#### Shopping, Supplies & Deliveries
- **Amazon Seller** (`amazon-seller-api`): Lists surplus HVAC parts on Joseph's storefront, updates pricing, and posts shipping confirmations as orders come in.
- **Instacart** (`instacart-api`): Grocery runs for custody weekends when a job runs late.
- **DoorDash** (`doordash-api`): The default pizza-night order when he is too tired to cook for the boys.
- **Uber** (`uber-api`): Backup ride when the Equinox is in the shop.
- **FedEx** (`fedex-api`): Track HVAC parts shipped to the apartment.
- **UPS** (`ups-api`): Track the rest of his parts and Connor's model-rocket kits.
- **Shippo** (`shippo-api`): Generates a return label when a wrong part ships to him.
- **Etsy** (`etsy-api`): Places his custom-decor orders like the apartment's Bengals sign and tracks each shipment to delivery.
- **Instagram** (`instagram-api`): Follows Tyler's team highlights and Patricia's recipe accounts.
- **Pinterest** (`pinterest-api`): Apartment-organizing and grill-recipe boards he saves to.

#### HVAC Trade, Repair & Field Work
- **Google Maps** (`google-maps-api`): Routes between service calls across metro Columbus and ETA estimates for custody pickups.
- **OpenWeather** (`openweather-api`): Heat-load context for jobs and the grill-or-not call on Saturdays.
- **Yelp** (`yelp-api`): Reads reviews of suppliers and the lunch spots near job sites.
- **GitHub** (`github-api`): Files and comments on issues in the thermostat-automation repo a customer shared, logging field bugs he hits on the unit.
- **GitLab** (`gitlab-api`): Syncs the mirror of that automation project and opens issues there when the customer's team works in GitLab.
- **Linear** (`linear-api`): A shared punch-list of recurring commercial-account fixes he tracks with Mike.
- **Jira** (`jira-api`): Updates and closes the property manager's maintenance tickets for the account Joseph services as he completes each visit.
- **Trello** (`trello-api`): His personal board of pending side-jobs and tool-buy decisions.
- **Asana** (`asana-api`): Tracks the multi-visit commercial install he is leading.
- **Monday** (`monday-api`): Schedules and updates his service visits on the property-management client's board as appointments are set.
- **Notion** (`notion-api`): His repair-notes wiki: model numbers, refrigerant charts, and customer histories.
- **Obsidian** (`obsidian-api`): Offline vault mirroring those repair notes for use in basements with no signal.
- **Confluence** (`confluence-api`): Maintains his own troubleshooting pages in the manufacturer documentation space, adding fixes he proves out in the field.
- **Airtable** (`airtable-api`): A parts-inventory base for what is stocked in the van.
- **Typeform** (`typeform-api`): The post-service customer satisfaction form his side jobs send out.

#### Records, Documents & Reference
- **Google Drive** (`google-drive-api`): Stores scanned certifications, the divorce decree, and tax documents.
- **Dropbox** (`dropbox-api`): Backup of warranty PDFs and equipment photos from job sites.
- **Box** (`box-api`): Uploads site photos and as-built notes to the commercial account's shared folder alongside their site plans.
- **OpenLibrary** (`openlibrary-api`): Looks up the financial-literacy and trade books he hears about on podcasts.
- **NASA** (`nasa-api`): Pulls space imagery to share with Connor, whose science streak runs to rockets and orbits.
- **TMDB** (`tmdb-api`): Checks movie details for custody-weekend film picks with the boys.
- **Reddit** (`reddit-api`): Reads the HVAC and Bengals subreddits for trade tips and game talk.
- **Twitter** (`twitter-api`): Follows Bengals beat reporters during football season.
- **LinkedIn** (`linkedin-api`): Keeps his profile current and replies to recruiter messages about HVAC roles; drafts replies for him to confirm.

#### Boys' School, Activities & Tickets
- **Google Classroom** (`google-classroom-api`): Pulls Connor's assignments and posts reminders to Joseph's calendar so he can quiz Connor on the right ones Wednesdays.
- **Eventbrite** (`eventbrite-api`): Tickets for school fundraisers and Tyler's tournament gates.
- **Ticketmaster** (`ticketmaster-api`): Tracks Bengals and NBA listings and grabs tickets within budget; confirm before purchase.
- **Strava** (`strava-api`): Logs his evening walks around the complex and Tyler's conditioning runs that Tyler shares.
- **MyFitnessPal** (`myfitnesspal-api`): Logs his meals and the vegetable push since his last physical, updating the daily streak he checks for consistency.
- **Amadeus** (`amadeus-api`): Checks flight options for the rare trip to see Scott's family or a tournament out of state.
- **Airbnb** (`airbnb-api`): Browses lodging for an out-of-town basketball tournament weekend.
- **Zillow** (`zillow-api`): Runs saved condo searches and sends Joseph new matches against the down-payment goal as they list.

#### Work Tools He Is Adjacent To
- **Salesforce** (`salesforce-api`): Files and updates warranty claims through the vendor portal as parts fail in the field.
- **HubSpot** (`hubspot-api`): Logs his calls with parts reps and updates the supplier contact records as he works deals.
- **Zendesk** (`zendesk-api`): Opens and replies to the manufacturer's tech-support tickets, attaching model numbers and photos from the job.
- **Freshdesk** (`freshdesk-api`): Files and follows up on the second manufacturer's support tickets the same way.
- **Intercom** (`intercom-api`): Starts chats with the parts supplier to confirm stock and pricing before he drives over.
- **ServiceNow** (`servicenow-api`): Picks up and resolves HVAC facilities requests in the large commercial client's system, updating each as he completes it.
- **PagerDuty** (`pagerduty-api`): Acknowledges his on-call HVAC pages and posts status updates so the briefing reflects his on-call week.
- **Sentry** (`sentry-api`): Triages errors on the thermostat-automation project, resolving the ones tied to field hardware he can explain.
- **Datadog** (`datadog-api`): Configures alert thresholds on the building-sensor dashboard for the commercial HVAC account and acts on the ones that trip.
- **Kubernetes** (`kubernetes-api`): Runs scheduled health checks against the building-automation status endpoint the client's IT vendor exposes and logs any downtime to flag for them.
- **Cloudflare** (`cloudflare-api`): Runs uptime probes on that client's web services and sends an alert when a check fails.
- **Okta** (`okta-api`): Manages his single-sign-on for the vendor portals above, refreshing sessions and rotating credentials when they expire.
- **Greenhouse** (`greenhouse-api`): Submits apprentice referrals he meets on jobs to the trade-school job board and tracks where they land.
- **BambooHR** (`bamboohr-api`): Enters apprentice candidate notes and reference checks into a contractor friend's HR tool to help vet hires.
- **Gusto** (`gusto-api`): Runs payroll for the side-cash jobs he and Kevin split, recording hours and splitting the pay each week.

#### Media, Creative & Marketing (Light Use)
- **Figma** (`figma-api`): Comments on and tweaks the flyer Connor designed for his science club, then exports it for printing.
- **Webflow** (`webflow-api`): Updates the copy and contact details on the landing page a friend built for Kevin's electric business and publishes the changes.
- **WordPress** (`wordpress-api`): The blog where Joseph drafts the occasional HVAC tip post.
- **Contentful** (`contentful-api`): Stores and updates that blog's post drafts, publishing entries when a tip is ready.
- **Algolia** (`algolia-api`): Reindexes his Notion repair notes so he can search model numbers and fixes fast from a job site.
- **Vimeo** (`vimeo-api`): Hosts a few install walkthrough videos he recorded for training.
- **WooCommerce** (`woocommerce-api`): Lists the same surplus parts on his own shop and processes orders, paired with the Amazon store.
- **BigCommerce** (`bigcommerce-api`): Mirrors the surplus-parts catalog to a second storefront and syncs stock levels between the two.
- **Mailchimp** (`mailchimp-api`): Drafts and sends the HVAC-tip blog's newsletter to its list when a new post goes up.
- **Klaviyo** (`klaviyo-api`): Runs the automated welcome email for new blog subscribers and tags them by interest.
- **ActiveCampaign** (`activecampaign-api`): Sends the occasional seasonal-maintenance reminder campaign to the blog's contacts.
- **Segment** (`segment-api`): Configures the event pipe feeding the blog's analytics and updates tracking when he adds a page.
- **Mixpanel** (`mixpanel-api`): Builds and reviews the funnels for the surplus-parts shop, adjusting events as he learns what buyers do.
- **Amplitude** (`amplitude-api`): Sets up the dashboards comparing the shop's two storefronts and updates them as numbers come in.
- **PostHog** (`posthog-api`): Maintains the self-hosted analytics for the blog, setting up the events and reports he wants to track.
- **Google Analytics** (`google-analytics-api`): Builds the monthly traffic report for the blog and emails himself the summary.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from connected mock APIs and stored memory.
- Joseph's employer systems: his work email (jfields@centralohioclimate.com), the FieldEdge dispatch system, and any company HR or scheduling tools. Never access or reference them.
- His Buckeye Federal Credit Union online banking directly, beyond the Plaid sync link.
- Megan's accounts of any kind, and the boys' personal accounts beyond the limited views noted above.
- Any phone-only apps not surfaced through a connected API.
