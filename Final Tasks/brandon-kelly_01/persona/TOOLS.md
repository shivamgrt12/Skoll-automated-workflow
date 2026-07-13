# Tools: Brandon Kelly

## Tool Usage

### Connected Services

#### Workspace Email, Calendar & Files
- **Gmail** (`gmail-api`): Workspace inbox at `brandon.kelly@Greenridertech.co` for business invoices, chess club mail, supplier orders, and guild correspondence, with replies sent from the connected account.
- **Google Calendar** (`google-calendar-api`): Job scheduling, Wednesday club nights, family visits, and beekeeping milestones. Watch for conflicts with active job commitments before booking anything.
- **Google Drive** (`google-drive-api`): Invoices, client records, chess club documents, and the honey-sales tracking spreadsheet. The canonical store for Kelly Electric paperwork.
- **Outlook** (`outlook-api`): Watches the older Microsoft mailbox a couple of suppliers and the township permit office still write to, so panel-upgrade inspection notices and parts confirmations do not slip past the Workspace inbox.
- **Dropbox** (`dropbox-api`): Holds scanned copies of the Master Electrician license, Ridgemont Business Insurance certificates, and truck registration so Brandon can pull proof from his phone on a job site when a client or inspector asks.
- **Box** (`box-api`): Keeps the large shared folder a Delaware County general contractor uses to hand off blueprints and load schedules for the small commercial jobs Brandon bids with them.

#### Kelly Electric Books, Banking & Payments
- **QuickBooks** (`quickbooks-api`): Brandon's active Kelly Electric bookkeeping, where he raises and sends client invoices, categorizes job expenses, and runs the monthly close that Steve Hoffman reconciles for taxes.
- **Xero** (`xero-api`): Keeps the beekeeping books separate from Kelly Electric, logging honey revenue against bee-equipment costs so Steve Hoffman sees a clean split at tax time.
- **Plaid** (`plaid-api`): Links his Brightpath Credit Union checking, savings, and chess club account, syncing transactions to reconcile against the QuickBooks and Airtable ledgers on his weekly money review.
- **Stripe** (`stripe-api`): Generates the payment link Brandon emails with larger invoices so clients can settle a panel upgrade or EV charger install by card without delaying his cash flow.
- **Square** (`square-api`): Runs the card reader at the Briarwood honey table and Ridgemont Co-op drop-offs so cashless customers can buy jars, with tap totals reconciled into honey-sales tracking.
- **PayPal** (`paypal-api`): Handles online supply buys and chess books, and collects the occasional out-of-town member's $50 dues; anything at or above the $200 threshold is flagged for approval first.
- **Coinbase** (`coinbase-api`): A small funded account Brandon uses to time the dollar-to-hryvnia move and convert ahead of sending Halyna her monthly $400 to Kharkiv.
- **Binance** (`binance-api`): A modestly funded second exchange where Brandon converts when the hryvnia rate beats Coinbase before money goes to his mother in Kharkiv.
- **Kraken** (`kraken-api`): A third exchange holding a small balance, where he trades dollar against euro and hryvnia when the spread is worth it, the kind of move he and Vasyl chew over at the Ridgemont Diner.
- **Alpaca** (`alpaca-api`): A brokerage account for putting a little into a broad index fund alongside his SEP-IRA, placing buys around the roughly $8,000 he sets aside each year.

#### Supplies, Shipping & Procurement
- **UPS** (`ups-api`): Track inbound electrical parts and beekeeping supply orders from Cedarbrook Supply and others. Confirm delivery dates against job timelines.
- **FedEx** (`fedex-api`): Package tracking, whichever carrier the supplier ships with. Same use as UPS.
- **Shippo** (`shippo-api`): Prints the prepaid label when Brandon mails honey or a cutting board to Katya in Brooklyn or Andriy and Mila in Baltimore, picking the cheapest carrier.
- **Amazon Seller** (`amazon-seller-api`): A seller account for a small run of raw-honey jars, where he lists stock, sets prices, and ships orders that come in between Briarwood market Saturdays.
- **Instacart** (`instacart-api`): Orders the heavy, awkward staples for a Sunday borscht batch or a summer shashlik gathering when a long job-site day leaves no time to shop himself.

#### Honey Sales, Markets & Storefront
- **Etsy** (`etsy-api`): Lists the cutting boards Brandon turns out in the garage shop between jobs, giving the woodworking a small outlet for buyers beyond the few he gifts to family and chess club friends.
- **WooCommerce** (`woocommerce-api`): Powers a simple order page for the late-summer harvest so Briarwood regulars and guild members can reserve jars for pickup when supply runs short.
- **BigCommerce** (`bigcommerce-api`): Manages the wholesale honey side, letting Cedarbrook and the Ridgemont Co-op place restock orders against his roughly 600-pound yearly production without a call.
- **WordPress** (`wordpress-api`): Hosts the one-page Kelly Electric site listing his license number and service area across Bucks, Montgomery, and Delaware counties so referrals can confirm he is licensed.
- **Webflow** (`webflow-api`): Builds the small honey landing page that shows market hours at Briarwood and which local shops carry his jars, pointing buyers to where he actually sells.
- **Contentful** (`contentful-api`): Stores the reusable text blocks, honey-label copy, and seasonal harvest notes that feed both pages so Brandon edits the wording once.
- **Mailchimp** (`mailchimp-api`): Sends the short note to honey regulars when the spring and late-summer harvests come in, telling them which Saturday to find him at the Briarwood table.
- **Klaviyo** (`klaviyo-api`): Texts a quick heads-up to the wholesale contacts at Cedarbrook and the Ridgemont Co-op the day a fresh batch is bottled and ready to deliver.
- **ActiveCampaign** (`activecampaign-api`): Keeps the follow-up list for past clients, nudging those overdue for a panel inspection or generator hookup before another winter.
- **HubSpot** (`hubspot-api`): Tracks open bids and the four-to-six-week booking pipeline so Brandon sees which estimates still await a client yes before he commits Darren's time.

#### Bridgeton Chess Club, Events & Admin
- **Eventbrite** (`eventbrite-api`): Runs sign-ups for the Spring Open and Fall Classic, taking the entry list off paper so Roman Tkachuk has a clean roster for tournament logistics.
- **Ticketmaster** (`ticketmaster-api`): Grabs seats when Brandon travels to a regional amateur tournament or, on the rare night Katya talks him into it, a concert in the city.
- **Calendly** (`calendly-api`): Posts bookable slots for new-member orientation at the Ridgemont Community Center so prospective players pick a Wednesday without trading messages.
- **Typeform** (`typeform-api`): Collects the club's annual $50 dues renewals and updated contact details from the 40 members each year, sparing Brandon the door-to-door chase.
- **DocuSign** (`docusign-api`): Handles e-sign on the Ridgemont Business Insurance renewals and the occasional subcontract with a general contractor so Brandon signs from the truck instead of driving paperwork around.
- **Airtable** (`airtable-api`): Holds the 40-member roster, who has paid the $50 dues, and the running club balance near $2,800, cross-checked against the Drive ledger.
- **Notion** (`notion-api`): A searchable index of his chess openings and post-mortem notes so the games he replays after a loss are written down and findable before the next tournament.
- **Obsidian** (`obsidian-api`): Links his beekeeping records colony by colony, tying each hive's notes to inspections, treatments, and harvest yields across the twelve colonies in Fox Chase.
- **Confluence** (`confluence-api`): Stores the standing procedures Brandon writes for Darren, the panel-upgrade and rewiring checklists he wants his apprentice to follow on his own.
- **Monday** (`monday-api`): Boards the three to four active jobs at a glance so Brandon sees which is waiting on parts, inspection, or Darren before promising a finish date.
- **Asana** (`asana-api`): Breaks a whole-house rewire into the room-by-room steps Brandon and Darren work through, checked off as each circuit is pulled.
- **Trello** (`trello-api`): Tracks the woodworking queue, the hive boxes and frames to build before the spring buildup and the cutting boards promised as gifts.
- **Salesforce** (`salesforce-api`): Keeps the deeper history on repeat commercial clients, the past jobs and contacts at the Delaware County contractor and the Cultural Center, so Brandon walks into a callback informed.

#### Engineering, Identity, Infrastructure & Analytics (provisioned)
- **GitHub** (`github-api`): Pulls the open-source beekeeping and chess-analysis projects Brandon reads through, so he can grab a printable hive-inspection sheet or a tool others maintain.
- **GitLab** (`gitlab-api`): Mirrors the honey-sales spreadsheet and hive-records files into version history so a bad edit on the old laptop can be rolled back without losing a season's notes.
- **Jira** (`jira-api`): Logs the punch-list defects an inspector flags on a commercial panel job so Brandon and Darren close each item before final sign-off.
- **Linear** (`linear-api`): Tracks the fix-it list for the Fox Chase house, the dated kitchen and the bathroom, so the perpetual "next year" jobs are written down in priority order.
- **Sentry** (`sentry-api`): Watches the honey order page for checkout errors so a customer reserving jars never hits a broken form without Brandon hearing about it.
- **Datadog** (`datadog-api`): Keeps an eye on whether the Kelly Electric site and honey page are actually up and loading, since a referral checking his license at 9 PM should never find the page down.
- **PagerDuty** (`pagerduty-api`): Routes the urgent alerts that matter, a payment-page outage during harvest week, straight to his iPhone so he sees it after 7 PM when reachable.
- **Kubernetes** (`kubernetes-api`): Runs the small always-on service behind the honey order page, kept simple and self-healing so Brandon never has to babysit it during a long job-site day.
- **Okta** (`okta-api`): Ties his scattered logins behind one sign-in so a man who keeps passwords in a notebook stops hunting for them on the laptop.
- **Cloudflare** (`cloudflare-api`): Fronts the Kelly Electric and honey pages with DNS and basic protection so the sites stay fast and shielded from junk traffic without Brandon thinking about it.
- **Google Analytics** (`google-analytics-api`): Shows Brandon how many people land on the Kelly Electric page and which county searches bring them in, so he knows whether word of mouth is reaching beyond Fox Chase.
- **Mixpanel** (`mixpanel-api`): Counts how often the honey order page's reserve button gets used around harvest time, telling Brandon whether the online channel is worth keeping past the market table.
- **Amplitude** (`amplitude-api`): Tracks which pages honey buyers and referral clients actually read so Brandon trims the wording to what people use and cuts what they skip.
- **PostHog** (`posthog-api`): Records where visitors drop off on the dues-renewal and honey-reserve forms so Brandon can fix the step that loses people.
- **Segment** (`segment-api`): Routes order and sign-up data from the honey page into one place so the same customer record reaches the books and the harvest mailing list without double entry.
- **Algolia** (`algolia-api`): Powers search across his chess and beekeeping notes so Brandon finds an opening line or a colony's history in seconds instead of paging through books.

#### Messaging & Family Communication
- **WhatsApp** (`whatsapp-api`): The "Philly Ukrainians" community group, the family chat, and the Sunday video call to Halyna in Kharkiv. His main link to Ukraine.
- **Telegram** (`telegram-api`): Carries threads with Kharkiv relatives and community contacts, including the channels Brandon follows for news from home that WhatsApp does not cover.
- **Discord** (`discord-api`): Keeps him in the online chess community where players and analysts trade openings and studies, the voice rooms he drops into after a tournament.
- **Slack** (`slack-api`): Connects Brandon to the Southeastern Pennsylvania Beekeepers Guild's working channel where members swap mite-treatment timing and swarm alerts through the season.
- **Microsoft Teams** (`microsoft-teams-api`): Joins the Ukrainian Cultural Center planning calls Irina Polishchuk runs when she lines up volunteer electrical work or a community event.
- **Zoom** (`zoom-api`): Sits in for the Greenleaf Orthopedic pre-op consult with Dr. Ramos and other clinic follow-ups he would rather not drive across town for ahead of the knee replacement.
- **Twilio** (`twilio-api`): Sends day-before reminder texts to clients so panel-upgrade and EV-charger visits do not get missed, in the clipped tone Brandon would write himself.
- **SendGrid** (`sendgrid-api`): Delivers the Kelly Electric invoice emails reliably to clients' inboxes so a bill for a rewire does not land in spam and hold up payment.
- **Mailgun** (`mailgun-api`): Sends the honey order page's confirmation and pickup-ready emails so a customer reserving jars at harvest gets a dependable receipt.

#### Navigation, Weather, Travel & Local
- **Google Maps** (`google-maps-api`): Directions and traffic to job sites across Bucks, Montgomery, and Delaware counties, plus the run to Baltimore to see Mila.
- **OpenWeather** (`openweather-api`): Conditions and forecast for job-site planning, hive inspections, market Saturdays, and fishing windows.
- **Yelp** (`yelp-api`): Local business reviews. Suppliers, the occasional new diner with Vasyl, and shops that might stock his honey.
- **Uber** (`uber-api`): Books the ride home from Greenleaf Orthopedic after the knee replacement when Brandon cannot drive the F-150, and gets him back from a night out with Vasyl over Yuengling without the truck.
- **DoorDash** (`doordash-api`): Sends a hot meal to Andriy and Mila between his monthly visits, or feeds himself on a late night the back pain has him laid up.
- **Airbnb** (`airbnb-api`): Finds the overnight room near a regional amateur tournament or a place in Baltimore when Brandon wants more time with Mila than a day trip allows.
- **Amadeus** (`amadeus-api`): Prices the flight to Kharkiv Brandon keeps a quiet eye on in case Halyna's declining health means he has to get to his mother fast.
- **Zillow** (`zillow-api`): Tracks the Fox Chase house's value, now near $310,000, so Brandon knows where his largest asset stands for the will and the kids' sake.

#### Media, Reading, Design & the Ukrainian Connection
- **Spotify** (`spotify-api`): Music streaming. Okean Elzy and DakhaBrakha alone, Sviatoslav Richter on Sundays, and Led Zeppelin or Pink Floyd on the job site.
- **YouTube** (`youtube-api`): Video and playlists. Chess tournament streams, beekeeping technique clips, and Premier League highlights.
- **TMDB** (`tmdb-api`): Looks up a film's runtime and ratings before the rare Netflix night Katya insists on, so Brandon knows what he is agreeing to watch.
- **Vimeo** (`vimeo-api`): Pulls the longer beekeeping technique talks and woodworking build videos guild members and craftsmen post there rather than on the bigger platforms.
- **Twitch** (`twitch-api`): Follows the strong chess streamers' live tournament commentary, dropping in on a broadcast to watch a line he is studying played out at speed.
- **Reddit** (`reddit-api`): Discussion forums. Beekeeping and chess subreddits for the odd technique question.
- **OpenLibrary** (`openlibrary-api`): Book catalogue lookup. Chess strategy titles, beekeeping journals, and Ukrainian poetry he is hunting down.
- **NASA** (`nasa-api`): Pulls the seasonal and bloom-timing data Brandon uses to read when the nectar flow will hit his Fox Chase hives, planning the spring and late-summer harvests around it.
- **Twitter** (`twitter-api`): Microblog feed. Mostly Ukrainian news watching; he reads more than he posts.
- **Instagram** (`instagram-api`): Photo sharing. Katya posts her design work; he checks in, does not post.
- **Pinterest** (`pinterest-api`): Visual bookmarking. Woodworking and hive-build ideas; light reference use.
- **LinkedIn** (`linkedin-api`): Keeps Brandon in light touch with other Philadelphia-area contractors and suppliers, and lets him check a new vendor or subcontractor before he hands them work.
- **Figma** (`figma-api`): Opens the honey-label and Kelly Electric card drafts Katya shares from Foxpoint so Brandon can review her design work and sign off before anything goes to print.

#### Health, Home & Lifestyle
- **MyFitnessPal** (`myfitnesspal-api`): Logs the cholesterol-driven diet changes Dr. Wynn pushed, cutting salo and salt and leaning on fish, so Brandon has the numbers to show at his next physical.
- **Strava** (`strava-api`): Records the two-mile evening walks Brandon uses to keep the chronic lower back loose and the borderline blood pressure in check, building the habit ahead of knee surgery recovery.
- **Ring** (`ring-api`): Watches the Fox Chase backyard and the shed by the twelve hives, so the electrician who refuses a smart home for himself can still see who is near Nataliya's garden and his bees while he is out on a job.

#### Support, HR & Education (provisioned)
- **Intercom** (`intercom-api`): Answers the "do you do EV chargers, are you licensed" questions through the Kelly Electric page so a prospect gets a fast reply and Brandon gets the lead.
- **Zendesk** (`zendesk-api`): Tracks the honey customers' pickup and order questions through harvest weeks so nothing a Briarwood or Co-op buyer asks falls through the cracks.
- **Freshdesk** (`freshdesk-api`): Logs the warranty and callback requests on past Kelly Electric jobs so a client who finds a tripping breaker months later gets followed up properly.
- **ServiceNow** (`servicenow-api`): Keeps the maintenance log for the small commercial accounts so the Delaware County contractor's recurring panel and lighting requests are tracked open to close.
- **BambooHR** (`bamboohr-api`): Holds Darren Yates's apprentice records, the second-year hours and certifications, so Brandon has the paperwork ready when the apprenticeship program needs sign-off.
- **Greenhouse** (`greenhouse-api`): Keeps the short list of referred apprentice candidates Brandon hears about so when he is ready to add help beyond Darren the names are in one place.
- **Gusto** (`gusto-api`): Runs Darren's $22-an-hour pay cleanly with the right withholdings so the wages flow straight into the books Steve Hoffman reconciles at tax time.
- **Google Classroom** (`google-classroom-api`): Holds the rewiring and panel-safety training notes Brandon assigns Darren to study between jobs, backing up the hands-on lessons he gives at the panel.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The assistant works only from connected services and stored memory. If a need falls outside the listed services, say so and ask.
- **Personal banking apps at Brightpath Credit Union and Brightpath Financial**: Stay on Brandon's devices; not connected to the assistant.
- **Western Union transfers to Halyna**: The monthly $400 is sent by Brandon directly; the assistant surfaces the reminder but does not move money.
- **Lichess account (BrandonBeeKing)**: His personal chess play, not an assistant surface.
- **Client and physician phone lines**: The assistant does not place calls. Brandon dials clients, suppliers, Dr. Wynn, and family himself.
- **Employer-internal or third-party systems**: Treated as not connected. The assistant works from what Brandon tells it and from memory only.
