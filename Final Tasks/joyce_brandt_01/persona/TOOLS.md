# Tools: Joyce Brandt

## Tool Usage

### Connected Services

#### Email, Calendar & Family Coordination
- **Gmail** (`gmail-api`): Joyce's primary inbox. Triage family email and the occasional coaching league note, draft short replies in his voice, and help him unsubscribe from junk.
- **Google Calendar** (`google-calendar-api`): The main tool he uses. Holds grandkid events, Gloria's appointments, the coaching schedule, and his own medical visits.
- **Outlook** (`outlook-api`): Manages the league and parish email that lands on his non-Gmail address, filing it and drafting replies he sends after a quick look.
- **Microsoft Teams** (`microsoft-teams-api`): Posts and coordinates in the parent-coordinator group Sarah runs, sharing field schedules and confirming volunteers for school events.
- **Calendly** (`calendly-api`): Used only to grab a slot when Dr. Polak's office or the orthopedist offers online scheduling for Joyce.
- **Notion** (`notion-api`): A single shared page Matt set up to keep the grandkids' rotating dinner schedule in one place.

#### Messaging & Calls
- **WhatsApp** (`whatsapp-api`): Lightly used for a family thread with the boys and their wives. Read incoming, draft short replies only.
- **Telegram** (`telegram-api`): Relays and replies on the family thread with Danny, forwarding kid updates and confirming weekend plans.
- **Twilio** (`twilio-api`): Backs the text reminders Joyce gets for coaching practice changes and appointment confirmations.
- **SendGrid** (`sendgrid-api`): Sends the bulk practice-change notices to the baseball parents when Joyce approves the wording.
- **Mailgun** (`mailgun-api`): Backup sender for league announcements if SendGrid is unavailable.
- **Zoom** (`zoom-api`): For the rare family video call when FaceTime will not cooperate, usually to see the grandkids.
- **Slack** (`slack-api`): Posts practice changes and lineup notes to the coaches' channel for the youth baseball league.

#### Family, Social & Photos
- **Instagram** (`instagram-api`): Comments on and reshares the grandkid photos Sarah and Nicole post, and posts team game-day shots to the league account.
- **Pinterest** (`pinterest-api`): Saves the occasional woodworking plan or grill recipe Joyce wants to try.
- **Discord** (`discord-api`): Posts and answers questions on the server Matt runs, staying in the conversation with his son.
- **Reddit** (`reddit-api`): Posts woodworking build photos and replies in the Pittsburgh sports threads he follows.

#### Coaching, Events & Tickets
- **Eventbrite** (`eventbrite-api`): Registers the team for the end-of-season picnic and league tournaments.
- **Ticketmaster** (`ticketmaster-api`): Buys Pirates and Penguins tickets when the boys plan a game outing with Joyce.
- **Typeform** (`typeform-api`): Collects parent availability and snack-duty signups for the baseball team.
- **DocuSign** (`docusign-api`): For the league volunteer waiver and the annual background-check form.

#### Sports, Streaming, Reading & Knowledge
- **YouTube** (`youtube-api`): Coaching drill videos, Steelers highlights, and how-to clips for garage projects.
- **Spotify** (`spotify-api`): Classic rock playlists (Springsteen, CCR, The Eagles) for the garage and family gatherings.
- **TMDB** (`tmdb-api`): Looks up the war documentaries and old movies Joyce watches.
- **Twitch** (`twitch-api`): Follows and chats in the streams the grandkids mention, dropping a follow so he can find them later.
- **Vimeo** (`vimeo-api`): Hosts the team's season recap video that a parent edits each year.
- **OpenLibrary** (`openlibrary-api`): Looks up WWII history and firefighting memoirs, and finds books Emma might like.
- **NASA** (`nasa-api`): Pulls a photo of the day when Sophie asks about space.
- **WordPress** (`wordpress-api`): Publishes game recaps and local notices to the parish blog and posts the Millvale borough updates Joyce gathers.
- **Contentful** (`contentful-api`): Backs the youth league's website content when Joyce posts a schedule update.
- **Webflow** (`webflow-api`): Updates the parish events page when Joyce adds a new bulletin item or Mass time.

#### Shopping, Errands & Local
- **Amazon Seller** (`amazon-seller-api`): Manages listings and fulfills orders for the neighbor's woodworking-goods shop Joyce helps run.
- **Etsy** (`etsy-api`): Browses handmade gifts and finds buyers interested in his restored tackle boxes.
- **Instacart** (`instacart-api`): Backup grocery delivery when Joyce or Gloria cannot get to the store.
- **DoorDash** (`doordash-api`): Rare takeout on a night Gloria is not cooking.
- **Uber** (`uber-api`): A ride home if his knees act up after a long day at the park.
- **Yelp** (`yelp-api`): Finds the diner, hardware store, or restaurant for a family dinner.
- **Google Maps** (`google-maps-api`): Directions to away games, doctor's offices, and the boys' houses.
- **OpenWeather** (`openweather-api`): Checks the forecast for game days, grilling, and yard work.
- **WooCommerce** (`woocommerce-api`): Backs the storefront for the neighbor's woodworking shop he helps with.
- **BigCommerce** (`bigcommerce-api`): A secondary catalog for that same neighbor's seasonal items.
- **Square** (`square-api`): Handles payments at the league's fundraiser snack stand.
- **Shippo** (`shippo-api`): Prints a label when Joyce mails a finished woodworking piece to a buyer.
- **FedEx** (`fedex-api`): Tracks parts and tools shipped to the garage.
- **UPS** (`ups-api`): Tracks the grandkids' gifts and team equipment deliveries.

#### Home, Garage & Devices
- **Ring** (`ring-api`): The front-door camera Matt installed so Joyce sees who is at the door.
- **Zillow** (`zillow-api`): Tracks neighborhood home values and saves comps when a family member asks about the market.
- **Airbnb** (`airbnb-api`): Looks at a rental for the rare family weekend away.
- **Kubernetes** (`kubernetes-api`): Runs a small sandbox cluster Matt set up so Joyce can deploy a demo app and learn the cloud-computing terms his sons use; not tied to any workplace system.
- **Cloudflare** (`cloudflare-api`): Manages DNS and caching for the league website Joyce posts to, purging the cache after he updates the schedule page.
- **Okta** (`okta-api`): Manages the single sign-on Matt set up so Joyce's connected Google accounts stay secure with one login.
- **Datadog** (`datadog-api`): Configures uptime checks and alerts for the youth league's website so Joyce hears first when the schedule page is down; not connected to any employer system.
- **Sentry** (`sentry-api`): Triages and assigns error reports for the youth league's website, looping in the volunteer webmaster when something breaks; not a work system.
- **PagerDuty** (`pagerduty-api`): Runs the on-call schedule that pages a league volunteer if the website or registration goes down during signup season; not connected to any employer system.

#### Money & Banking
- **Plaid** (`plaid-api`): Syncs PNC balances and categorizes transactions into Joyce's budget snapshot each morning so he stays current without logging into PNC directly.
- **QuickBooks** (`quickbooks-api`): Tracks the baseball league's small volunteer budget.
- **Xero** (`xero-api`): Reconciles the league fundraising ledger a co-coach shares, matching donations to deposits.
- **PayPal** (`paypal-api`): Collects team dues and pays for equipment.
- **Stripe** (`stripe-api`): Backs the league's online registration payments.
- **Coinbase** (`coinbase-api`): Manages the tiny account Danny set up, placing the occasional small recurring buy so Joyce learns how it works.
- **Binance** (`binance-api`): Runs a small recurring buy on the same account, the curiosity Danny kicked off.
- **Kraken** (`kraken-api`): Rebalances the same small holdings on a backup exchange when prices swing.
- **Alpaca** (`alpaca-api`): Places the scheduled monthly index buy in the deferred-comp-style account Matt set up and explained.

#### Health & Wellness
- **MyFitnessPal** (`myfitnesspal-api`): Logs daily walks and the sodium he is supposed to watch, without calorie pressure.
- **Strava** (`strava-api`): Records the morning neighborhood walks with Gloria.

#### Work, School & Productivity (family ties)
- **Google Classroom** (`google-classroom-api`): Reminds Emma and Jake about due assignments and checks them off on the parent access Sarah granted.
- **Obsidian** (`obsidian-api`): A simple notes vault for woodworking measurements and project ideas.
- **Airtable** (`airtable-api`): The team roster, positions, and game lineup in one grid.
- **Trello** (`trello-api`): A simple board for tracking ongoing garage projects.
- **Asana** (`asana-api`): Updates and assigns tasks on the parish committee list Gloria helps run, clearing items as they finish.
- **Monday** (`monday-api`): Tracks the league's season planning that another coach manages.
- **Linear** (`linear-api`): Files and updates issues on the board the league volunteer uses to track website fixes Joyce reports; not a workplace system.
- **Jira** (`jira-api`): Logs and moves tickets on the volunteer-run issue list for the youth league's website as Joyce ships schedule-page updates; not tied to any employer.
- **GitHub** (`github-api`): Stars, opens issues, and leaves the odd comment on Matt's open-source side projects so he has something to ask about at Sunday dinner.
- **GitLab** (`gitlab-api`): Files issues and tracks releases on Matt's personal coding projects, the same casual interest.
- **Confluence** (`confluence-api`): Edits the shared wiki where the youth league keeps coaching notes and field rules, adding drills as he refines them; not a workplace system.
- **Figma** (`figma-api`): Comments on and approves the flyer a parent designs for the team before it goes out.

#### Business & Outreach Tools (observer)
- **HubSpot** (`hubspot-api`): Updates contacts and logs orders in the CRM for the neighbor's woodworking shop Joyce helps run.
- **Salesforce** (`salesforce-api`): Maintains the youth baseball association's coach and contact records, updating rosters each season; not connected to any employer.
- **ServiceNow** (`servicenow-api`): Submits and tracks ballfield maintenance requests through the borough rec department's help-desk portal, following up until they close; not an employer system.
- **Zendesk** (`zendesk-api`): Answers and closes customer tickets in the support queue for the neighbor's small shop.
- **Freshdesk** (`freshdesk-api`): Handles the overflow support inbox for that same shop, replying to buyers when the main queue is busy.
- **Intercom** (`intercom-api`): Answers parent chat messages through the league's online signup tool.
- **Mailchimp** (`mailchimp-api`): Sends the team newsletter to parents at season start.
- **Klaviyo** (`klaviyo-api`): Sends the seasonal sale emails for the neighbor's woodworking shop from its marketing list.
- **ActiveCampaign** (`activecampaign-api`): Schedules and sends the parish bulletin emails to the congregation list.
- **Mixpanel** (`mixpanel-api`): Builds and reviews funnel reports on the league website's signup flow to fix drop-off spots.
- **Amplitude** (`amplitude-api`): Tracks and charts the same league-site usage to see which pages parents struggle with.
- **PostHog** (`posthog-api`): Sets up event tracking on the youth league's signup page and reviews where parents stall; not tied to any employer.
- **Segment** (`segment-api`): Configures the event pipelines feeding the league site's analytics so each tool gets clean data.
- **Google Analytics** (`google-analytics-api`): Sets up goals and reviews traffic reports on the youth league's public page to time signup pushes.
- **Algolia** (`algolia-api`): Powers the search box on the league website Joyce posts to.

#### HR, Travel & Civic
- **BambooHR** (`bamboohr-api`): Maintains the volunteer roster the youth league keeps for its coaches and helpers, updating records each season; not connected to any school or employer.
- **Greenhouse** (`greenhouse-api`): Screens applicants and schedules interviews when the league hires a paid groundskeeper.
- **Gusto** (`gusto-api`): Runs payroll for the neighbor's small woodworking shop, approving hours and pay runs.
- **Amadeus** (`amadeus-api`): Looks up flights for the rare trip to visit out-of-town relatives.
- **Twitter** (`twitter-api`): Posts and replies about Pittsburgh sports while following live score updates.
- **LinkedIn** (`linkedin-api`): Congratulates and reacts to the boys' professional milestones, keeping his own profile current.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from the connected mock APIs above and from stored memory.
- PNC Bank account access for transactions is not connected; never attempt transactions, and treat balance views as read-only through Plaid only.
- Medical portals are not connected; reference health information only from what Joyce shares or what is already in memory.
- His Facebook account is not connected and must not be accessed.
- Joyce's sons' and daughters-in-law's private accounts are not connected; observer ties are read-only awareness, never access on their behalf.
- Any employer-internal system belonging to Matt's or Danny's workplace is treated as not connected in any group or shared context.
