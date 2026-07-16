# Tools: Ashley Griffin

## Tool Usage

### Connected Services

#### Email, Calendar & Contacts
- **Gmail** (`gmail-api`): Primary inbox at `ashley.griffin@Greenridertech.co`. Personal mail, school notices from Desert Willow Elementary about Chloe, appointment confirmations, vendor receipts.
- **Outlook** (`outlook-api`): Read-only. Some Tucson school district threads route through Outlook on Amber's side; surfaces when forwarded.
- **Google Calendar** (`google-calendar-api`): Custody weekends, Tucson drives, dispatch overlap, dental and physical slots, Linda's Wednesday stop. The single source of truth for time.
- **Calendly** (`calendly-api`): Books his annual physical with Dr. Estrada at Huachuca Valley Medical Center and pulls the confirmed slot straight onto his Google Calendar.
- **Google Classroom** (`google-classroom-api`): Read-only on Chloe's Desert Willow third-grade classroom when Amber forwards an invite. Used at the start of school year only.
- **Work email** `agriffin@summitpeakhvac.com`: connected with read access for Summit Peak job and dispatch correspondence. Routes through the existing email tooling; no separate slug.

#### Communication & Messaging
- **WhatsApp** (`whatsapp-api`): Handles service follow-ups with the two Spanish-speaking customers who prefer it, run from the work phone where his bilingual call notes live.
- **Telegram** (`telegram-api`): Where Ray sends fishing reports and Parker Canyon Lake water-level photos before they pick a no-custody Saturday to head out.
- **Discord** (`discord-api`): Checks the bass-fishing server his nephew added him to for Parker Canyon Lake bite reports and gear deals before a trip with Ray.
- **Slack** (`slack-api`): The channel a Tucson commercial facilities client uses to loop Summit Peak techs in on HVAC retrofit coordination when Ashley is the one assigned.
- **Microsoft Teams** (`microsoft-teams-api`): Joins Trane manufacturer training webinars and the property-management client's HVAC walkthrough calls that run on Teams.
- **SendGrid** (`sendgrid-api`): Sends the Sunday evening schedule recap and the Thursday pack-Chloe's-room reminder to his own inbox so the week ahead is in writing.
- **Mailgun** (`mailgun-api`): Forwards Trane warranty-ticket confirmations and vendor parts receipts into his Gmail so the paper trail lands in one place.
- **Mailchimp** (`mailchimp-api`): Reads the Cochise County Parks & Rec newsletter that lists summer camp dates and father-daughter events Ashley plans around Chloe's visits.
- **Klaviyo** (`klaviyo-api`): Catches the Etsy and Pinterest shop sale alerts for the animal-themed gifts Chloe keeps asking for, so he buys at the right time.
- **ActiveCampaign** (`activecampaign-api`): Tracks the Trane distributor's parts-promotion and warranty-bulletin emails so Ashley flags relevant ones to the shop.
- **Twilio** (`twilio-api`): SMS reminders only, used for the Sunday 8:00 PM weekly schedule check and the Thursday pack-Chloe's-room ping.
- **Zoom** (`zoom-api`): Occasional video calls for school events or Chloe's after-school program, plus a Trane manufacturer training once or twice a year.
- **Intercom** (`intercom-api`): Read-only. A handful of HVAC parts suppliers have Intercom chat widgets that surface in inbox replies.

#### Field Service, HVAC & Operations
- **ServiceNow** (`servicenow-api`): Read-only. A commercial property management group Summit Peak services routes their work orders through ServiceNow.
- **Freshdesk** (`freshdesk-api`): Read-only. Trane parts distributor uses Freshdesk for warranty tickets.
- **Zendesk** (`zendesk-api`): Read-only. A property management company that owns 22 rentals in Sierra Vista routes maintenance tickets through Zendesk to Summit Peak.
- **Jira** (`jira-api`): Read-only on the Tucson commercial client's HVAC retrofit board so Ashley can see ticket status before he drives down for a site visit.
- **Linear** (`linear-api`): Personal task list when Ashley wants something tracked beyond the calendar: small home repairs, gift ideas for Chloe, summer camp follow-ups.
- **Asana** (`asana-api`): Read-only on a commercial customer's facilities maintenance board where Summit Peak's assigned HVAC tasks for Ashley show up.
- **Trello** (`trello-api`): Holds his own running board of driveway truck jobs on the Tacoma and the gear-room fixes at Yucca Drive he keeps meaning to finish.
- **Monday** (`monday-api`): Read-only. One commercial customer uses it for project tracking on HVAC retrofits.
- **BambooHR** (`bamboohr-api`): Read-only access to his own Summit Peak record for PTO balance and pay stub history.
- **Greenhouse** (`greenhouse-api`): Read-only on the application status when Tommy nudges him about a senior-tech opening at a larger Tucson HVAC shop he is curious about.
- **Gusto** (`gusto-api`): Read-only on Summit Peak payroll for pay stubs and W-2.
- **DocuSign** (`docusign-api`): Lease renewal paperwork with Frank Mendez and custody-adjacent agreements when they need a signature.
- **Typeform** (`typeform-api`): Completes Cochise County Parks & Rec summer camp registration for Chloe so her weeks line up with his four summer custody weeks.
- **Salesforce** (`salesforce-api`): Read-only. A commercial Tucson facilities client uses Salesforce service cloud for HVAC dispatch records.
- **HubSpot** (`hubspot-api`): Read-only on a commercial client's CRM where Summit Peak service records and Ashley's HVAC visit notes are logged.

#### Maps, Weather & Travel
- **Google Maps** (`google-maps-api`): Service-call routing, Tucson drives for Chloe pickup, Parker Canyon Lake routes, traffic checks during peak season.
- **OpenWeather** (`openweather-api`): Sierra Vista forecast for service-call planning, Parker Canyon Lake fishing conditions, monsoon season tracking.
- **Uber** (`uber-api`): Books the Tucson airport runs when Linda flies to Texas to see family, and the ride home from a Phoenix Cardinals trip with Tommy when he has had a few.
- **Amadeus** (`amadeus-api`): Read-only. Linda's occasional Southwest flights to visit family in Texas surface as confirmations.
- **Airbnb** (`airbnb-api`): Books the lakeside cabin near Parker Canyon Lake when he and Ray plan a brothers' fishing weekend on a no-custody stretch.

#### Banking, Payments & Trading
- **Plaid** (`plaid-api`): Read-only visibility into the Desert Financial Credit Union checking and savings balance.
- **Stripe** (`stripe-api`): Confirms receipts for Chloe's online activity sign-ups and the Cochise County camp deposits he pays through Stripe checkout pages.
- **Square** (`square-api`): Read-only. Summit Peak uses Square for customer card payments at the door.
- **PayPal** (`paypal-api`): Pays Etsy sellers for Chloe's animal-themed birthday gifts and splits the cabin or concert cost with Ray when they go halves.
- **QuickBooks** (`quickbooks-api`): Read-only on Summit Peak's books for his time-card hours and overtime accumulation.
- **Xero** (`xero-api`): Read-only on a commercial customer's books where Summit Peak's invoiced HVAC jobs Ashley worked are reconciled.
- **Alpaca** (`alpaca-api`): Tracks the small slice of his Desert Financial savings he parked in a basic index position toward Chloe's future, checked rarely and kept simple.
- **Coinbase** (`coinbase-api`): Watches the small amount of crypto Tommy talked him into buying so he knows when to cash it back to the credit union savings.
- **Binance** (`binance-api`): Checks the spot price on that same small crypto holding for a second reference before he decides to sell.
- **Kraken** (`kraken-api`): Cross-checks the crypto price here too, since Ray uses Kraken and they compare numbers before either one moves money.

#### Shopping, Delivery & Vendors
- **Amazon Seller** (`amazon-seller-api`): Tracks order and shipment status on the Amazon HVAC tools and Chloe's gifts he buys when Walmart does not stock them.
- **Etsy** (`etsy-api`): On hand for Chloe's birthday and Christmas gifts, especially the animal-themed items she keeps asking for.
- **Instacart** (`instacart-api`): Pre-custody-weekend grocery runs when work runs long, and stocking Chloe's snack list at the Sierra Vista house.
- **DoorDash** (`doordash-api`): Late-night dinner during peak season when he gets home past 6:00 PM and does not want to cook.
- **WooCommerce** (`woocommerce-api`): Confirms orders and tracking from the small HVAC parts shops that run on WooCommerce when a job needs a part the Trane distributor is out of.
- **BigCommerce** (`bigcommerce-api`): Tracks orders from an aftermarket Tacoma parts vendor on BigCommerce for the driveway brake and filter work he does himself.
- **FedEx** (`fedex-api`): Tracking for HVAC parts and the occasional truck part shipped to the shop.
- **UPS** (`ups-api`): Tracking for Chloe's online gifts and any tool order from Walmart.com or Amazon.
- **Shippo** (`shippo-api`): Pulls tracking labels for the Etsy gift shipments to Chloe so he knows they will land before her custody weekend.

#### Media, Sports & Reading
- **Spotify** (`spotify-api`): Country and classic rock playlists. Free tier. Truck radio is the primary listening surface, Spotify on the phone for the Tucson drives.
- **TMDB** (`tmdb-api`): Lookup for the action movies he and Ray pick on a slow Saturday and for the fictional show Border Line he is mid-season on.
- **OpenLibrary** (`openlibrary-api`): Looks up page count and series order on the thrillers Ray leaves at his place so he knows what he is starting before bed.
- **Vimeo** (`vimeo-api`): Streams the Trane technical training videos hosted on Vimeo when a diagnostic on a newer commercial unit calls for the manufacturer walkthrough.
- **YouTube** (`youtube-api`): Truck maintenance tutorials, HVAC diagnostic walkthroughs, and the occasional Cardinals highlight reel.
- **Twitch** (`twitch-api`): Catches the occasional bass-fishing tournament stream the Parker Canyon crowd links in the fishing server when he is killing time on a quiet evening.
- **Reddit** (`reddit-api`): Read-only on r/HVAC for parts intel and r/AZcardinals for game-day chatter.
- **Twitter** (`twitter-api`): Read-only. Follows the Cardinals beat writer and one HVAC parts account.
- **LinkedIn** (`linkedin-api`): Keeps tabs on the Cochise Tech HVAC alumni network and the senior-tech postings Tommy flags so he knows what the Tucson shops are paying.
- **Ticketmaster** (`ticketmaster-api`): Occasional Cardinals tickets when Tommy proposes a Phoenix trip, plus a country concert with Ray once or twice a year.

#### Home, Auto, Health & Outdoors
- **Zillow** (`zillow-api`): Casual watch on Sierra Vista rentals in case Frank raises the rent at January 2027 renewal. Not house-shopping yet.
- **Ring** (`ring-api`): Front-door camera at the Yucca Drive rental. Alerts on package drops and on Chloe coming home from the school van when she is up for summer weeks.
- **MyFitnessPal** (`myfitnesspal-api`): Read-only. Tracks naproxen frequency during peak season as a body-load signal, never as calorie pressure.
- **Strava** (`strava-api`): Logs his Huachuca Mountains hikes on good weekends and tracks how the right knee holds up on the climbs.

#### Productivity, Documents & Notes
- **Google Drive** (`google-drive-api`): Storage for the custody agreement PDF, tax docs, lease paperwork, and a folder of Chloe's school photos.
- **Dropbox** (`dropbox-api`): Read-only. Hank's wife Dina drops Summit Peak HR forms and W-2s in a shared Dropbox folder.
- **Box** (`box-api`): Read-only on a commercial customer's facilities Box folder where the HVAC system schematics and equipment manuals Ashley needs on site are stored.
- **Notion** (`notion-api`): Holds his personal page of custody logistics: the pack list for Chloe's room, summer-week planning, and gift ideas he jots through the year.
- **Obsidian** (`obsidian-api`): Keeps his offline notes of HVAC diagnostic shortcuts and recurring fault codes he has worked out on the harder Cochise County jobs.
- **Airtable** (`airtable-api`): Read-only on Dina's Summit Peak parts-inventory base so Ashley can check shop stock before he heads to a job that needs a specific part.
- **Confluence** (`confluence-api`): Read-only. Trane distributor faculty resources sit on Confluence.
- **Contentful** (`contentful-api`): Read-only on the Trane distributor's content hub where the service bulletins and spec sheets Ashley references on commercial units are published.
- **WordPress** (`wordpress-api`): Read-only. Summit Peak's old marketing site runs on WordPress; Tommy maintains it.
- **Webflow** (`webflow-api`): Read-only on the new Summit Peak landing page Tommy is rebuilding in Webflow so Ashley can confirm the service-area details are right.
- **Figma** (`figma-api`): Read-only on the mockups Tommy shares for the Summit Peak site redesign so Ashley can sign off on how the services are laid out.
- **Pinterest** (`pinterest-api`): On hand for Chloe's birthday party ideas and the occasional outdoor cooking pin.
- **Instagram** (`instagram-api`): Read-only. Follows the Cardinals account, two fishing accounts, and a few of Tommy's posts. Does not post.

#### Site Operations, Analytics & Developer Tools
- **Google Analytics** (`google-analytics-api`): Read-only on the Summit Peak marketing site Tommy maintains.
- **Mixpanel** (`mixpanel-api`): Read-only on the Summit Peak site funnel Tommy set up so Ashley can see which service pages bring in the most quote requests.
- **Amplitude** (`amplitude-api`): Read-only on the Summit Peak site events Tommy tracks so Ashley can tell which AC-repair pages spike during peak season.
- **PostHog** (`posthog-api`): Read-only on the Summit Peak site analytics Tommy maintains for a second view of how the contact form is performing.
- **Segment** (`segment-api`): Read-only on the data pipeline feeding the Summit Peak site analytics Tommy wired up, used to confirm the contact-form events are flowing.
- **Algolia** (`algolia-api`): Powers the parts search on the Trane distributor catalog Ashley queries to confirm a part number before he orders for a job.
- **GitHub** (`github-api`): Read-only on the repo for the Summit Peak marketing site Tommy maintains so Ashley can see when a service-area change goes live.
- **GitLab** (`gitlab-api`): Read-only on the mirror where a commercial client's facilities team keeps the HVAC controls config Ashley references on retrofit visits.
- **Sentry** (`sentry-api`): Read-only alerting on the Summit Peak site Tommy runs so Ashley knows if the contact form breaks during peak season when leads matter most.
- **Datadog** (`datadog-api`): Read-only on the uptime monitor Tommy set for the Summit Peak site so Ashley can confirm it is reachable when a customer says they cannot find them online.
- **PagerDuty** (`pagerduty-api`): Receives the after-hours emergency HVAC alerts a commercial client routes to the on-call tech when Ashley is the one covering the rotation.
- **Okta** (`okta-api`): The single sign-on a commercial client requires before Ashley can open their facilities portal and HVAC work orders on site.
- **Cloudflare** (`cloudflare-api`): Read-only on Summit Peak's marketing site DNS Tommy set up.
- **Kubernetes** (`kubernetes-api`): Read-only health status on the platform a commercial client's building-automation dashboard runs on, used to confirm the system is up before Ashley troubleshoots an HVAC controls fault on site.

#### Reference & Special
- **NASA** (`nasa-api`): Used twice. Once for a moon phase check on a fishing trip with Ray and once when Chloe asked about a meteor shower for a school project.
- **Eventbrite** (`eventbrite-api`): Sierra Vista father-daughter spring festival and library movie nights when the timing lines up with a custody weekend.
- **Yelp** (`yelp-api`): Restaurant lookup in Sierra Vista and Tucson around custody handoffs, anchored on The German Cafe, Manny's Tacos, and Pizza Hut for Chloe.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from the connected services above and from stored memory.
- Desert Financial Credit Union banking app is NOT connected; balance visibility through Plaid is read-only.
- OurFamilyWizard co-parenting app is NOT connected. It lives on Ashley's personal phone and is the channel of record with Amber.
- Summit Peak dispatch board on the work iPhone SE is NOT connected.
- Amber's accounts, Kyle's accounts, and Chloe's school accounts beyond the Google Classroom read-only invite are NOT connected and are off-limits.
- Linda's laptop, which Ashley borrows once a year for taxes, is NOT connected.
- Hank's and Dina's personal accounts and Summit Peak's QuickBooks Online beyond Ashley's own read-only payroll view are NOT connected.
