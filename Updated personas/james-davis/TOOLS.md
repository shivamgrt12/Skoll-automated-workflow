# Tools: James Davis

## Data Generation

- **Spreadsheets**: Generates shop revenue trackers, parts inventory sheets, customer estimate templates, Mustang restoration budget logs, and Dorothy's care expense reconciliations. Outputs Excel and Google Sheets with bolded headers and printable column widths.
- **Drafts and Letters**: Generates email drafts for parts suppliers, customer follow-ups, the SBA microloan thread at Desert Plains Federal Credit Union, the CPA Robert, and First Baptist Church correspondence.
- **Estimates and Work Orders**: Generates customer estimate documents from bay notes, including labor hours, parts costs, tax math, and the standard Davis Auto Repair shop terms.
- **Calendars and Plans**: Generates printable bay schedules, Mustang Tuesday and Thursday evening plans, Rio Bravo High School mentoring lesson outlines, and Little League Thunderbolts sponsorship trackers.
- **Checklists and Trackers**: Generates pre-trip fishing packing lists, brisket cook timelines, BBQ shopping lists, annual shop insurance renewal checklists, and the SBA microloan document checklist.

## Tool Usage

### Connected Services

#### Email, Calendar & Office

- **Gmail** (`gmail-api`): Primary inbox at `james.davis@Finthesiss.ai` for parts orders, customer follow-ups, supplier communications, and church paperwork.
- **Google Calendar** (`google-calendar-api`): Single source of truth for bay schedule, family events, appointments, and the Mustang Tuesday and Thursday evening blocks.
- **Google Drive** (`google-drive-api`): Shop documents, insurance papers, Mustang restoration photos, customer estimates archive.
- **Outlook** (`outlook-api`): Watches the State Farm small-business insurance tenant for shop policy bulletins and the November 1 renewal notice.
- **Dropbox** (`dropbox-api`): Backup of shop documents and customer-supplied photos for body work estimates.
- **Box** (`box-api`): Shared workspace with Amy for the shop bookkeeping monthlies and the SBA loan document set.
- **DocuSign** (`docusign-api`): SBA microloan paperwork, shop liability waivers, and the occasional customer financing form.

#### Shop Management & Operations

- **Asana** (`asana-api`): Bay task board for the week. Eddie, Bobby, and Linda each have a swim lane.
- **Monday** (`monday-api`): Customer ticket board that Linda manages for intake, status, and pickup.
- **Trello** (`trello-api`): Personal Mustang restoration checklist with paint, upholstery, and final assembly columns.
- **Notion** (`notion-api`): Shop process notes, customer history binder, and the running scanner upgrade research thread.
- **Obsidian** (`obsidian-api`): Local notes on diagnostic patterns by make and model, twenty years of "what I saw and what it actually was" entries.
- **Airtable** (`airtable-api`): Parts inventory database covering common stocks and minimum reorder levels.
- **Linear** (`linear-api`): Follows Amy's engineering capstone project tracker, checking the milestones she shares for father-daughter context.
- **Confluence** (`confluence-api`): Pulls repair procedures and technical service bulletins from the Mitchell1 vendor knowledge base when a tricky job needs a reference.
- **Jira** (`jira-api`): Tracks where his SBA microloan application sits in Desert Plains Federal Credit Union's underwriting workflow.
- **Calendly** (`calendly-api`): Customer self-scheduling link for diagnostic intake and oil change appointments; pushes into the shop calendar.
- **Typeform** (`typeform-api`): Customer intake form for new vehicle history and contact details before the first appointment.
- **ServiceNow** (`servicenow-api`): Logs and follows insurance claims and policy questions in State Farm's small-business ticket queue.

#### Customer Service & Communication

- **WhatsApp** (`whatsapp-api`): Family group thread with Beth, Tyler, and Amy. Dorothy uses the home phone instead.
- **Slack** (`slack-api`): Davis Auto Repair internal workspace where parts suppliers post ETAs and Linda routes customer requests.
- **Microsoft Teams** (`microsoft-teams-api`): Escalates Mitchell1 vendor support cases through the shared support tenant when the workstation acts up.
- **Discord** (`discord-api`): Keeps an eye on Tyler's Border Patrol veterans community server to stay close to his son's world.
- **Telegram** (`telegram-api`): Small thread with the Mustang parts network for hard-to-find 1967 parts.
- **Zoom** (`zoom-api`): Quarterly CPA check-ins with Robert and the occasional remote diagnostic walkthrough with a customer.
- **Twilio** (`twilio-api`): Shop SMS appointment reminders Linda runs the day before each booking.
- **SendGrid** (`sendgrid-api`): Customer service follow-up emails sent from the shop's automated workflow.
- **Mailgun** (`mailgun-api`): Backup transactional sender for parts order confirmations to repeat customers.
- **Intercom** (`intercom-api`): Runs the shop's website chat widget that Linda answers through during the day.
- **Zendesk** (`zendesk-api`): Customer support ticket queue Linda runs for warranty and complaint handling.
- **Freshdesk** (`freshdesk-api`): Opens and follows Snap-on dealer support tickets for the aging MODIS scanner.
- **Figma** (`figma-api`): Pulls the shop's seasonal flyer templates that Beth's bakery designer shares for service-special promos.

#### Family, Faith & Community

- **Eventbrite** (`eventbrite-api`): First Baptist Church community events, El Paso Classic Car Show registration, and the occasional fishing tournament.
- **Ticketmaster** (`ticketmaster-api`): Dallas Cowboys home and away tickets when budget allows, plus the occasional El Paso Chihuahuas baseball outing with the family.
- **Google Classroom** (`google-classroom-api`): Posts lesson outlines and tracks the Rio Bravo High School auto shop classroom on Saturday mornings during the school year.
- **Ring** (`ring-api`): Front door doorbell at the Ysleta house, shared access with Beth.
- **Google Maps** (`google-maps-api`): Drive times to Elephant Butte Lake, Riverside Park for Little League, the Rio Bravo High School lot, and customer house calls.
- **Yelp** (`yelp-api`): Blue Plate Diner reservations, Big Bun runs, and the occasional date-night spot with Beth.
- **OpenWeather** (`openweather-api`): El Paso forecast for shop AC loads, BBQ Sunday planning, and fishing trips out to Elephant Butte.

#### Truck, BBQ & Hobbies

- **Spotify** (`spotify-api`): Country in the bay (Midland, Cody Johnson, Turnpike Troubadours) and classic rock in the garage on Mustang nights (Blackberry Smoke, The Steel Wheels, Drive-By Truckers).
- **YouTube** (`youtube-api`): Cummins and Power Stroke diesel walkthroughs, Mustang 302 V8 build references, brisket cook techniques, and Cowboys highlights.
- **TMDB** (`tmdb-api`): Family movie night picks for Sunday afternoons when the game is not on.
- **Twitch** (`twitch-api`): Catches the occasional classic-car restoration and brisket-cook stream he follows for technique on a slow evening.
- **Vimeo** (`vimeo-api`): ASE recertification course videos and the occasional Mustang restoration shop tour clip.
- **NASA** (`nasa-api`): Moon phase and tidal cross-reference for fishing trip planning out to Elephant Butte.
- **Strava** (`strava-api`): Lightweight tracking when Beth gets him out walking the neighborhood on Sunday evenings.
- **MyFitnessPal** (`myfitnesspal-api`): Logs sodium and blood pressure since the borderline-high reading at his last physical, the way Beth keeps nudging him to.
- **OpenLibrary** (`openlibrary-api`): Mystery and thriller lookups, mostly Vince Rearden, and the occasional automotive history reference.
- **Pinterest** (`pinterest-api`): Shared boards with Beth for backyard improvements and brick pit upgrades.

#### Banking, Payments & Books

- **Plaid** (`plaid-api`): Links the Wells Fargo personal accounts and the shop's small-business checking to QuickBooks for monthly reconciliation.
- **Stripe** (`stripe-api`): Card-not-present payments for the occasional customer balance over the phone.
- **PayPal** (`paypal-api`): Customer deposits from repeat clients and parts-network purchases for Mustang work.
- **QuickBooks** (`quickbooks-api`): Davis Auto Repair books that Amy reconciles weekly and Robert (CPA) reviews quarterly.
- **Xero** (`xero-api`): Reconciles against Robert's CPA ledger for the cross-business view at tax cycles.
- **Square** (`square-api`): In-shop card reader for walk-in payments and the occasional swap-meet sale of spare parts.
- **Coinbase** (`coinbase-api`): Holds the small starter position Tyler set him up with; James checks the balance every few weeks and leaves it riding.
- **Binance** (`binance-api`): Compares spot prices against Coinbase to see how the small position is moving.
- **Kraken** (`kraken-api`): Third price reference he glances at alongside Coinbase and Binance before deciding to do nothing.
- **Alpaca** (`alpaca-api`): Small brokerage account where James mirrors a single index fund Amy talked him into, his one slow retirement experiment.

#### Parts Supply, Marketplace & Logistics

- **Amazon Seller** (`amazon-seller-api`): Small side listing for surplus shop equipment and the occasional Mustang part James decides not to keep.
- **Etsy** (`etsy-api`): Checks Beth's bakery Etsy listings for custom cake-topper orders and helps her pack them when she is slammed.
- **BigCommerce** (`bigcommerce-api`): Orders shop parts through the supplier's wholesale catalog the shop runs on.
- **WooCommerce** (`woocommerce-api`): Orders sample swatches from Reynolds Custom Interiors' upholstery storefront for the Mustang interior.
- **FedEx** (`fedex-api`): Parts shipments from out-of-state Mustang specialists.
- **UPS** (`ups-api`): Standard shop parts deliveries and the occasional return shipment.
- **Shippo** (`shippo-api`): Bulk labels Linda prints for the seasonal customer thank-you postcards.

#### Workforce & Payroll

- **BambooHR** (`bamboohr-api`): Shop employee portal for Eddie, Bobby, and Linda's PTO balances and benefits.
- **Greenhouse** (`greenhouse-api`): Light hiring pipeline tracking for replacement when a junior mechanic rotates through the shop.
- **Gusto** (`gusto-api`): Shop payroll that runs biweekly Fridays for the staff.
- **Okta** (`okta-api`): Shop SSO that gates Gusto, BambooHR, and the Mitchell1 vendor portal.

#### Travel & Mobility

- **Airbnb** (`airbnb-api`): Cabin and lake-house bookings for the Elephant Butte fishing weekends and the rare family trip out of town.
- **Amadeus** (`amadeus-api`): El Paso to Dallas fare watch when Cowboys home games come up.
- **Uber** (`uber-api`): Backup ride when the F-250 is on the lift or after a long Friday at Eddie's.
- **DoorDash** (`doordash-api`): Big Bun and Blue Plate Diner runs to the shop on a late night.
- **Instacart** (`instacart-api`): Beth's grocery overflow during her busy bakery weeks.
- **Zillow** (`zillow-api`): Casual Lower Valley neighborhood value tracking and the rare commercial lot watch in case a second bay ever pencils.

#### Marketing, Sales CRM & Customer Comms

- **HubSpot** (`hubspot-api`): Shop CRM for customer history, vehicle notes, and follow-up cadences.
- **Salesforce** (`salesforce-api`): Checks the shop's wholesale standing on the parts supplier's commercial account dashboard.
- **Mailchimp** (`mailchimp-api`): Quarterly shop newsletter to repeat customers with seasonal service reminders.
- **Klaviyo** (`klaviyo-api`): Coordinates with Beth's bakery email marketing flows so the family promotions stay in sync.
- **ActiveCampaign** (`activecampaign-api`): Tracks his sponsorship and entry status in the El Paso Classic Car Show's donor outreach.

#### Web, Analytics & Developer Tools

- **GitHub** (`github-api`): Follows Amy's engineering coursework repositories so he knows what she is building.
- **GitLab** (`gitlab-api`): Keeps up with Amy's secondary class repos for the same father-daughter context.
- **Sentry** (`sentry-api`): Watches the shop website error feed Linda flags when bookings drop.
- **Datadog** (`datadog-api`): Tracks the shop website uptime dashboard the website vendor hosts.
- **PagerDuty** (`pagerduty-api`): Checks the website vendor's on-call rotation so Linda knows who is reachable if the booking widget goes down.
- **Kubernetes** (`kubernetes-api`): Glances at the status board for Amy's engineering team homelab cluster when she walks him through her capstone.
- **Cloudflare** (`cloudflare-api`): Manages DNS for `davisautorepair.com`, the shop landing page Linda maintains.
- **Mixpanel** (`mixpanel-api`): `davisautorepair.com` engagement analytics; Linda reviews monthly.
- **Amplitude** (`amplitude-api`): Reviews Beth's bakery site engagement metrics so cross-promotions land.
- **Segment** (`segment-api`): Checks the website vendor's data pipeline feeding the shop site analytics.
- **PostHog** (`posthog-api`): Reviews the website vendor's feature flags for the shop booking widget.
- **Algolia** (`algolia-api`): Powers search on `davisautorepair.com` for service categories and customer reviews.
- **Google Analytics** (`google-analytics-api`): Shop website traffic dashboard James reviews monthly with Linda.
- **Contentful** (`contentful-api`): Headless CMS backing the shop website content; Linda occasionally updates seasonal blurbs.
- **Webflow** (`webflow-api`): Reviews the shop site the website vendor builds in Webflow before seasonal updates go live.
- **WordPress** (`wordpress-api`): Follows the El Paso Daily Herald local news blog and the Cowboys beat blog through their feeds.

#### Social Media & News

- **Instagram** (`instagram-api`): Shop account for finished build photos and family glimpses; Beth handles posting.
- **Twitter** (`twitter-api`): Follows Cowboys beat reporters, NWS El Paso, and the local SBA office for news he acts on.
- **LinkedIn** (`linkedin-api`): Lightly maintained profile for vendor introductions and the occasional young mechanic referral.
- **Reddit** (`reddit-api`): Reads r/MechanicAdvice, r/ClassicMustangs, r/ElPaso, and r/Cowboys for community context and the occasional diagnostic tip.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available as connected tools: rely on the connected services listed above and on what James shares directly.
- Mitchell1 shop management system: not connected to OpenClaw; estimates and service info stay in the in-shop workstation.
- Wells Fargo online banking beyond the Plaid read link: phone and in-branch only, by James's choice.
- Beth's personal email and her bakery's POS back-office: off-limits unless James is explicitly walking through one with you.
- Dorothy's MyChart patient portal, her diabetes monitoring device cloud, and any prescription portal: off-limits unless James asks you to look at a specific appointment.
- Tyler's Border Patrol agency systems and any government identity portals: hard off-limits.
- Amy's El Paso Technical University student portal beyond the GitHub and GitLab links: off-limits unless she walks you through one.
- Snap-on dealer back-office beyond the Freshdesk ticket view: off-limits.
- Shop landline call recordings: not connected.
