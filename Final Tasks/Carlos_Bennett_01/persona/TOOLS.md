# Tools: Carlos Bennett

## Tool Usage

### Connected Services

> **API-callable feeds (authoritative — the only services with live mock endpoints):**
> `airtable-api`, `amazon-seller-api`, `asana-api`, `bamboohr-api`, `docusign-api`, `fedex-api`, `gmail-api`, `google-calendar-api`, `greenhouse-api`, `gusto-api`, `hubspot-api`, `linear-api`, `mailchimp-api`, `monday-api`, `outlook-api`, `paypal-api`, `plaid-api`, `quickbooks-api`, `salesforce-api`, `sendgrid-api`, `shippo-api`, `square-api`, `stripe-api`, `trello-api`, `ups-api`, `xero-api` (26 total).
>
> Every other service named in the subsections below is **narrative context only** — describing Carlos's real-life tool habits and household setup. Those services have no mock feed to call and should not be treated as available data sources during a run.

#### Communications & Inbox

- **Gmail** (`gmail-api`): Primary thread for Claire Walsh's bookings, guitar repair clients, Coast Guard correspondence, Gulf Coast Marine Insurance, and Rick Morgan. Account `carlos.bennett@Finthesiss.ai`.
- **Outlook** (`outlook-api`): Handles corporate charter coordinators and marine suppliers who route confirmations through Outlook, syncing relevant threads back to the Gmail side.
- **SendGrid** (`sendgrid-api`): Sends batched repair-pickup notifications to guitar clients when the workshop pipeline runs three or more instruments deep.
- **Mailgun** (`mailgun-api`): Delivers transactional email confirmations for guitar repair deposits and parts-order receipts from the Bennett Guitar Works side.
- **Twilio** (`twilio-api`): SMS to Russ on engine alarms, Nolan on weather reads, and last-minute charter confirmations when email is too slow.
- **WhatsApp** (`whatsapp-api`): Reaches out-of-state vintage guitar collectors and specialty parts contacts who prefer WhatsApp for instrument photos and price negotiations.
- **Slack** (`slack-api`): Carries the Bayport harbor captains' shared channel for dock scheduling, storm-prep coordination, and off-season maintenance swap alerts.
- **Microsoft Teams** (`microsoft-teams-api`): Joins corporate charter group channels when a business booking coordinates trip logistics, headcounts, and departure preferences through Teams.
- **Telegram** (`telegram-api`): Connects with vintage guitar parts sellers and luthier supply contacts who run their trade channels on Telegram.
- **Discord** (`discord-api`): Follows luthier forum servers for fret-leveling techniques, bridge-plate sourcing threads, and vintage pickup winding discussions.
- **Zoom** (`zoom-api`): Runs remote video consults with out-of-state guitar clients shipping instruments in for restoration, walking them through the damage assessment before quoting.

#### Calendar, Scheduling, Forms

- **Google Calendar** (`google-calendar-api`): The four-spine calendar lives here. Charter season block (April 1 to Nov 30 default), repair deadlines, family weeks, Coast Guard milestones.
- **Calendly** (`calendly-api`): Offers a self-serve booking window for off-peak charter dates and guitar repair drop-off slots, syncing confirmations to the main calendar.
- **Typeform** (`typeform-api`): Collects charter intake forms from corporate groups, capturing roster details, dietary needs, and gear preferences before the trip.

#### Files, Documents, Notes

- **Google Drive** (`google-drive-api`): Boat maintenance log spreadsheet, guitar repair invoice files, Coast Guard packet, charter booking records, seasonal revenue tracker.
- **Dropbox** (`dropbox-api`): Receives high-resolution instrument photos from guitar repair clients before drop-off, so Carlos can assess damage and source parts ahead of time.
- **Box** (`box-api`): Stores charter liability waivers and corporate group rosters shared by business clients who keep their trip files in Box.
- **Notion** (`notion-api`): Holds the guitar repair knowledge base with setup specs, neck-angle reference charts, and vintage serial number lookups Carlos pulls during restoration work.
- **Obsidian** (`obsidian-api`): Keeps Carlos's offline repair notes, tonewood grading references, and fret-wire gauge charts accessible from the workshop bench without a network connection.
- **Confluence** (`confluence-api`): Archives the Bennett Guitar Works repair procedures, parts sourcing contacts, and seasonal boat maintenance checklists in a structured reference format.
- **Airtable** (`airtable-api`): Tracks the guitar parts inventory with current stock levels, reorder thresholds, and supplier lead times for StewMac, Allparts, and LMI.

#### Charter Operations, Weather, Maps

- **OpenWeather** (`openweather-api`): Bayport coastal forecast, tide-window cross-checks, and front-edge thunderstorm reads for the 3:30 AM briefing.
- **Google Maps** (`google-maps-api`): Truck routing to Brooksville, Spring Hill, Tampa, and the parts run loop, plus dock and ramp lookups for visiting captains.
- **NASA** (`nasa-api`): Satellite imagery for Gulf surface conditions and bait-tide context when the local feeds disagree.

#### Guitar Parts, Marketplaces, Shipping

- **Amazon Seller** (`amazon-seller-api`): Pulls parts pricing, checks string set availability, and tracks delivery windows for fast-ship orders when the specialty suppliers are backordered.
- **Etsy** (`etsy-api`): Sources hand-wound pickups, specialty inlay pieces, and vintage-correct hardware from luthier craftspeople selling through the marketplace.
- **BigCommerce** (`bigcommerce-api`): Manages the Bennett Guitar Works product catalog, listing available repair services and restored instruments for clients browsing online.
- **WooCommerce** (`woocommerce-api`): Runs the checkout and payment processing for online repair deposits and parts sales through the Bennett Guitar Works storefront.
- **Shippo** (`shippo-api`): Compares carrier rates and generates shipping labels when a restored instrument needs to ship to an out-of-state client.
- **FedEx** (`fedex-api`): Standard carrier for finished instruments going to Tampa, Atlanta, and points north.
- **UPS** (`ups-api`): Default carrier for incoming parts from StewMac and LMI, plus backup for outbound instrument shipments.

#### Marketing & Web Presence

- **Instagram** (`instagram-api`): Shares repair-bench progress shots and finished restoration photos that Diane cross-posts from the Bennett Guitar Works Facebook page.
- **Pinterest** (`pinterest-api`): Pins guitar restoration before-and-after galleries and vintage instrument reference photos that drive referral traffic to the Bennett Guitar Works page.
- **Mailchimp** (`mailchimp-api`): Sends seasonal charter availability updates and off-peak booking specials to past clients on Claire Walsh's referral list.
- **Klaviyo** (`klaviyo-api`): Manages automated follow-up sequences for guitar repair clients, sending pickup reminders, care instructions, and satisfaction check-ins after delivery.
- **ActiveCampaign** (`activecampaign-api`): Tracks the guitar repair client lifecycle from inquiry through quote, deposit, repair, and pickup, triggering status updates at each stage.
- **WordPress** (`wordpress-api`): Hosts the Bennett Guitar Works landing page with repair service descriptions, the restoration gallery, and the client inquiry form Diane manages.
- **Webflow** (`webflow-api`): Manages the charter booking landing page layout and seasonal schedule display that Claire Walsh shares with prospective corporate clients.
- **Contentful** (`contentful-api`): Stores and delivers the content blocks for the online listings, keeping repair descriptions, pricing tiers, and the restoration portfolio current.

#### Finance, Payments, Investing

- **QuickBooks** (`quickbooks-api`): Charter ledger and the guitar shop invoicing live here, separated by class so tax time is honest.
- **Xero** (`xero-api`): Syncs with Rick Morgan's quarterly financial reviews, providing an additional ledger view that separates charter and guitar shop revenue for tax planning.
- **Stripe** (`stripe-api`): Processes online repair deposits and out-of-state client payments for guitar restorations, with transaction records feeding into QuickBooks.
- **Square** (`square-api`): The dock reader Russ runs when a charter client tips on card, plus in-person repair payments at the workshop.
- **PayPal** (`paypal-api`): Receives advance payments from out-of-state guitar repair clients and handles charter deposits from Claire Walsh's online referrals.
- **Plaid** (`plaid-api`): Connects the Coastal Bank checking and savings views into the bookkeeping side for a unified financial picture.
- **DocuSign** (`docusign-api`): Charter liability waivers, vendor invoices over $1,000, and the occasional Coast Guard packet attachment.
- **Alpaca** (`alpaca-api`): Mirrors the traditional IRA portfolio Rick Morgan manages at Gulf Financial Partners, providing Carlos a current balance and allocation view.
- **Coinbase** (`coinbase-api`): Monitors cryptocurrency market summaries for context when Rick Morgan raises digital asset allocation during quarterly retirement planning reviews.
- **Binance** (`binance-api`): Provides supplementary exchange data alongside Coinbase for the broader asset-class picture Rick Morgan covers in financial planning sessions.
- **Kraken** (`kraken-api`): Rounds out the digital asset market view with additional exchange rates and trends when Carlos and Rick Morgan discuss alternative investment options.

#### Music, Entertainment, Travel

- **Spotify** (`spotify-api`): B.B. King, Stevie Ray Vaughan, Muddy Waters, CCR, Allman Brothers, Hank Williams, George Jones. The workshop playlist runs through this.
- **YouTube** (`youtube-api`): Fret-leveling reference clips, Cummins diesel diagnostic videos, and the occasional Harbor Ramblers practice upload.
- **Vimeo** (`vimeo-api`): Hosts long-form restoration walkthrough videos for guitar clients who want the full repair process documented before and after.
- **TMDB** (`tmdb-api`): Pulls recommendations for old Westerns and fishing shows when Carlos and Diane settle in for an evening after the workshop closes.
- **Ticketmaster** (`ticketmaster-api`): College football season tickets with Diane and the rare blues show within driving distance.
- **Eventbrite** (`eventbrite-api`): Tracks the Bayport waterfront events Carlos sits in on with the Harbor Ramblers and local community gatherings.
- **Twitch** (`twitch-api`): Follows live-streamed luthier workshops and guitar building demonstrations from craftspeople Carlos tracks in the restoration community.
- **OpenLibrary** (`openlibrary-api`): Tracks the reading list Diane adds to before every trip, finding Gulf War novels and fishing memoirs Carlos packs in the canvas duffel.
- **Amadeus** (`amadeus-api`): Books flights for the rare trip beyond driving distance, comparing fares and seat options for the one or two annual trips that leave the Gulf Coast radius.
- **Airbnb** (`airbnb-api`): Finds waterfront rentals for the long weekends Carlos and Diane take along the Gulf Coast, filtering for dog-friendly spots since Biscuit comes along.
- **Uber** (`uber-api`): Tampa airport runs and the occasional ride home after a tailgate.
- **DoorDash** (`doordash-api`): Delivers dinner on the long charter days when Carlos docks late and the kitchen gets skipped, pulling from saved favorites in Bayport and Spring Hill.
- **Instacart** (`instacart-api`): Handles the grocery run when charter season and the repair pipeline both peak, delivering to the cottage so Carlos stays on the bench or the dock.

#### Family, Home, and Neighborhood

- **Zillow** (`zillow-api`): Local market context when Marcel or Luc ask whether a friend's listing is fair. The cottage is not on the market.
- **Ring** (`ring-api`): Front-porch and dock-side cameras Diane talked Carlos into during a parts-theft scare last year.
- **Yelp** (`yelp-api`): Sanity-check reviews on a new restaurant before he and Diane try it, plus reads on out-of-town stops.
- **Reddit** (`reddit-api`): Follows the luthier and Cummins diesel subreddits for niche repair fixes, vintage parts leads, and marine engine diagnostic threads.
- **Twitter** (`twitter-api`): Monitors NOAA weather alerts, Bayport harbor updates, and Hernando County emergency notices that surface faster on Twitter than through official channels.
- **LinkedIn** (`linkedin-api`): Looks up corporate charter contacts Claire Walsh forwards, verifying titles and company details before Carlos confirms the booking.
- **Google Classroom** (`google-classroom-api`): Tracks Elise's school updates, permission slips, and pickup schedules that Luc or Ashley flag when Carlos is on grandparent duty.

#### Health & Body

- **MyFitnessPal** (`myfitnesspal-api`): Logs meals and sodium intake on the days Dr. Mitchell asks Carlos to track, feeding the quarterly check-in data for the cholesterol and hypertension reviews.
- **Strava** (`strava-api`): Tracks the physical activity from dock work, boat loading, and property maintenance that Carlos logs as daily exercise for Dr. Mitchell's wellness records.

#### CRM, Support, and Business Operations

- **HubSpot** (`hubspot-api`): Maintains the guitar repair client database with contact details, instrument history, and service preferences that feed the repeat-customer pipeline.
- **Salesforce** (`salesforce-api`): Syncs with corporate charter coordinators who manage their team outings and booking approvals through Salesforce, keeping Carlos's availability current on their end.
- **Intercom** (`intercom-api`): Routes live chat inquiries from the Bennett Guitar Works online presence, directing repair questions and booking requests to Carlos during workshop hours.
- **Freshdesk** (`freshdesk-api`): Tracks guitar repair support tickets from initial inquiry through completion, with automated status updates sent to clients at each milestone.
- **Zendesk** (`zendesk-api`): Manages charter client feedback and post-trip follow-ups, collecting satisfaction notes that Claire Walsh uses to refine the booking pipeline.
- **ServiceNow** (`servicenow-api`): Processes service requests from corporate charter clients who route trip modifications and equipment needs through their company's ticketing system.
- **BambooHR** (`bamboohr-api`): Manages seasonal crew records for Russ Taylor, tracking pay periods, charter days worked, and tip pool allocation during the April-through-November season.
- **Greenhouse** (`greenhouse-api`): Holds the posting template for seasonal mate positions, ready to activate when Russ Taylor needs a fill-in or a second crew member becomes necessary.
- **Gusto** (`gusto-api`): Processes Russ Taylor's seasonal payroll, handling the weekly base pay and tip pool percentage calculations during charter season.

#### Developer, DevOps, and Analytics Stack

- **GitHub** (`github-api`): Follows Marcel's recipe project repository and luthier community forks for fret-calculator scripts and neck-angle computation tools.
- **GitLab** (`gitlab-api`): Hosts version-controlled backups of the boat maintenance logs and guitar repair documentation that sync from the Drive spreadsheets.
- **Linear** (`linear-api`): Tracks the guitar repair pipeline as a project board, with each instrument moving through intake, assessment, parts sourcing, repair, and client pickup stages.
- **Jira** (`jira-api`): Integrates with corporate charter clients who track their team-building trips and logistics through Jira, syncing departure dates and headcount changes.
- **Trello** (`trello-api`): Organizes the seasonal boat maintenance checklist into cards, tracking each system through the off-season overhaul from hull to safety gear.
- **Asana** (`asana-api`): Manages the Coast Guard renewal workflow, breaking the license, medical certificate, drug test, and inspection into tracked tasks with deadline reminders.
- **Monday** (`monday-api`): Coordinates the shared task board with Claire Walsh for charter season scheduling, tracking confirmed bookings, deposits, and crew assignments.
- **Figma** (`figma-api`): Mocks up bridge-plate templates, pickguard designs, and headstock inlay patterns that Diane helps lay out before Carlos routes them in the workshop.
- **Sentry** (`sentry-api`): Monitors the Bennett Guitar Works inquiry form and the charter booking page for submission errors, flagging failures before a client inquiry is lost.
- **Datadog** (`datadog-api`): Tracks uptime and response metrics for the charter booking portal and guitar works online presence, alerting when performance degrades.
- **PagerDuty** (`pagerduty-api`): Routes urgent engine alarm notifications to Russ Taylor's phone and escalates unacknowledged alerts to Carlos, backing up the VHF channel.
- **Okta** (`okta-api`): Manages secure login for corporate charter clients accessing their trip details, waivers, and group rosters through the booking portal.
- **Cloudflare** (`cloudflare-api`): Handles DNS, SSL, and traffic protection for the Bennett Guitar Works online presence and the charter booking page.
- **Kubernetes** (`kubernetes-api`): Manages the backend services for the charter booking portal and guitar works site, scaling capacity during peak season inquiry volume.
- **Google Analytics** (`google-analytics-api`): Tracks visitor traffic and referral sources for the Bennett Guitar Works page and charter booking links, feeding the monthly performance review.
- **Mixpanel** (`mixpanel-api`): Measures how prospective guitar repair clients interact with the online inquiry form, showing which services generate the most contact submissions.
- **Amplitude** (`amplitude-api`): Analyzes charter booking funnel performance, measuring conversion rates from initial inquiry through confirmed deposit across seasonal periods.
- **PostHog** (`posthog-api`): Monitors engagement patterns on the Bennett Guitar Works online presence, showing how visitors navigate the restoration gallery and service listings.
- **Segment** (`segment-api`): Routes customer data between the charter booking system, guitar repair CRM, and email marketing tools, keeping client records consistent across platforms.
- **Algolia** (`algolia-api`): Powers the search function on the Bennett Guitar Works listings, letting visitors find specific repair services and restoration examples by instrument type.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. The agent works only from connected mock APIs and stored memory.
- The Bennett Guitar Works Facebook page is managed by Diane Crawford; the agent does not post, comment, or message through it.
- The marine GPS chartplotter and VHF radio on the Lucky Strike are standalone on-boat hardware. Carlos operates them directly.
- The NOAA Weather radio and the iPhone NOAA app are not API-connected; Carlos checks them in hand.
- The Walsh Charter Services internal booking system is Claire Walsh's source of truth; the agent cross-references against the Gmail thread only.
- The USCG renewal portal at the National Maritime Center is submitted by Carlos directly; the agent drafts the packet checklist.
- Coastal Bank's online banking interface is not connected directly. The Plaid feed provides the account view.
- Diane Crawford's personal accounts and Coastal Family Dentistry's systems are not connected and not to be touched.
