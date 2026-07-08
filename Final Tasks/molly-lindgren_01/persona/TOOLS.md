# Tools: Molly Lindgren

## Tool Usage

### Connected Services

#### Family & Personal Communication

- **Gmail** (`gmail-api`): Powers the primary inbox at `molly.lindgren@voissync.ai`; receives church newsletters, Denise's long letters, clinic notices, and pharmacy refill emails, and drafts every reply for Molly to send.
- **Google Calendar** (`google-calendar-api`): Drives the "colored boxes" Molly reads daily; books medical appointments, church events, Garden Society dates, and Keith's Sunday visits with color-coded blocks.
- **WhatsApp** (`whatsapp-api`): Carries Pastor Whitfield's mission trip group; pulls the latest updates for Molly and drafts her responses on her behalf for review.
- **Slack** (`slack-api`): Tracks Keith's hospital workspace presence so Molly knows when he is mid-incident before she calls.
- **Discord** (`discord-api`): Pulls highlights from Jaylen's robotics club channel so Molly arrives at Sunday dinner with good questions about his projects.
- **Zoom** (`zoom-api`): Hosts the online Bible study Molly joins when she cannot make it in person, plus Denise's Wednesday evening video calls from Atlanta.
- **Microsoft Teams** (`microsoft-teams-api`): Hosts Denise's school counselor meetings; signals to Molly when Denise is in session so she can call after.
- **Telegram** (`telegram-api`): Carries Pastor Whitfield's parallel mission trip channel and pulls trip-day check-ins for the prayer chain.
- **Twilio** (`twilio-api`): Pushes SMS refill reminders to Molly's iPhone SE and routes outbound texts the moment Molly approves the draft.
- **Intercom** (`intercom-api`): Drives the telehealth chat at Vidalia Medical Associates and Savannah Heart; drafts Molly's question and queues it for her approval before sending.
- **Outlook** (`outlook-api`): Pulls Sweetwater Elementary substitute notifications from Molly's old district mailbox and forwards them into her main inbox.

#### Church, Faith & Community

- **Mailchimp** (`mailchimp-api`): Delivers the First Baptist Vidalia weekly newsletter to Molly's inbox and highlights the items she circles in pencil each Friday.
- **Mailgun** (`mailgun-api`): Powers delivery for the church newsletter; flags duplicate sends so Pastor Whitfield's office can correct the bulletin.
- **SendGrid** (`sendgrid-api`): Delivers pharmacy and clinic transactional emails; surfaces refill confirmations and appointment notices the moment they land.
- **Webflow** (`webflow-api`): Hosts the First Baptist Vidalia website where Pastor Whitfield posts sermon notes; pulls each new post into Molly's Sunday-prep reading.
- **WordPress** (`wordpress-api`): Hosts Pastor Whitfield's Lent and Advent reflection blog; pulls each post and queues it for Molly to read with her morning coffee.
- **Cloudflare** (`cloudflare-api`): Runs CDN and DNS behind the church website; raises uptime issues to Keith so the giving page stays up on Sunday mornings.
- **Vimeo** (`vimeo-api`): Hosts Pastor Whitfield's sermon archive; pulls the missed sermon onto Molly's iPad the week she travels with Keith to cardiology.
- **Eventbrite** (`eventbrite-api`): Books church revival tickets, the Garden Society fall tour, and Vidalia community center events; pushes confirmations to the Google Calendar.
- **Klaviyo** (`klaviyo-api`): Filters the Belk and Park Seed marketing lists and surfaces only the seasonal sales Molly would actually care about for the azalea bed.
- **HubSpot** (`hubspot-api`): Tracks the food pantry roster Pastor Whitfield's office runs; pulls Molly's every-other-Saturday shift slot into the calendar.
- **Segment** (`segment-api`): Routes church website analytics to the pastoral team dashboards; confirms Molly's tithe page sessions reach the giving funnel.
- **PostHog** (`posthog-api`): Records session behavior on the church digital giving page; verifies Molly's tithe page loads cleanly on her iPad each first-of-the-month.
- **Amplitude** (`amplitude-api`): Tracks engagement on the daily devotional email Molly subscribes to and confirms the open-rate trend stays healthy for Pastor Whitfield's office.
- **Mixpanel** (`mixpanel-api`): Tracks the church online giving funnel; pinpoints where parishioners drop off so the deacons can address it at the Wednesday meeting.
- **Google Analytics** (`google-analytics-api`): Reports church website traffic by source; surfaces the monthly summary Pastor Whitfield reviews before staff meeting.
- **Salesforce** (`salesforce-api`): Drives the First Baptist Vidalia member directory CRM; pulls Molly's profile when the deaconess board needs her contact card.
- **ActiveCampaign** (`activecampaign-api`): Drives the Vidalia Garden Society email list; pulls the monthly meeting reminder a day early so Molly can prep her azalea-bed notes.
- **Contentful** (`contentful-api`): Powers the Garden Society newsletter editor; pulls the upcoming articles into Molly's reading queue before publication day.
- **PayPal** (`paypal-api`): Processes Molly's tithe to First Baptist Vidalia building fund; confirms each contribution posted and files the receipt.
- **Stripe** (`stripe-api`): Processes Garden Society dues and online giving receipts; logs every successful payment to Molly's Drive folder.
- **Asana** (`asana-api`): Tracks the food pantry logistics board Pastor Whitfield's office runs; confirms Molly's every-other-Saturday slot and lines up substitute coverage when needed.
- **Typeform** (`typeform-api`): Pulls Garden Society interest survey responses and the church potluck signup; lines up the Sunday potluck headcount for Molly.

#### Garden, Hobbies, Reading & Music

- **Pinterest** (`pinterest-api`): Curates Molly's boards for azalea care, diabetic-friendly Southern recipes, and Maya's birthday cookie ideas.
- **YouTube** (`youtube-api`): Plays gospel playlists, Georgia gardening tutorials, and the cardiologist's patient-education clips on the iPad in the kitchen.
- **OpenLibrary** (`openlibrary-api`): Pulls catalog and metadata before Molly places a Vidalia Public Library hold; checks edition and series order.
- **Algolia** (`algolia-api`): Powers search behind the Vidalia Public Library catalog; confirms the next title in Molly's cozy mystery series is on the shelf.
- **Reddit** (`reddit-api`): Pulls posts from r/gardening and r/whatsthisplant when an unusual problem shows up in the azalea bed.
- **TMDB** (`tmdb-api`): Looks up episode metadata for the PBS documentaries and cooking competitions Molly watches in the evening.
- **Spotify** (`spotify-api`): Plays Southern Gospel and classic country (Patsy Cline, Dolly Parton) on the iPad when WVOP radio cannot tune in.
- **OpenWeather** (`openweather-api`): Powers the 7:00 AM check before the Tuesday and Thursday walks with Lorraine and triggers frost warnings for the azalea bed.
- **Airtable** (`airtable-api`): Manages the Vidalia Garden Society plant inventory and member database; Gladys gave Molly editor access for the fall-tour roster.
- **Monday** (`monday-api`): Tracks the Garden Society fall tour planning board; surfaces Molly's azalea-bed entry status for the November tour.
- **Trello** (`trello-api`): Carries the monthly meeting agenda board Gladys runs; queues Molly's comments on the agenda for review.
- **Figma** (`figma-api`): Drives the Garden Society flyer Gladys's daughter designs; confirms Molly's azalea photo lands in the layout before print.
- **BigCommerce** (`bigcommerce-api`): Powers Gladys's small online seed shop; queues Molly's seed cart for review at Sunday dinner before Keith approves the purchase.
- **WooCommerce** (`woocommerce-api`): Drives the Vidalia nursery's online catalog; builds Molly's wishlist and lines up the spring order for Keith to confirm.
- **Instagram** (`instagram-api`): Pulls Maya's baking pictures and Denise's classroom posts into Molly's morning iPad scroll with the porch coffee.
- **Twitter** (`twitter-api`): Pulls the local Vidalia news handle and the National Weather Service Charleston account so Molly sees storm watches before the walk.
- **Twitch** (`twitch-api`): Tracks Jaylen's robotics stream schedule and notifies Molly when he is live so she can drop in before Sunday's family call.

#### Health, Medication & Wellness

- **MyFitnessPal** (`myfitnesspal-api`): Logs the Tuesday and Thursday walks with Lorraine and tracks meal patterns on the bad-glucose mornings.
- **Strava** (`strava-api`): Records the Tuesday and Thursday neighborhood loop; syncs the route history with Lorraine, who is the only follower Molly has.
- **Calendly** (`calendly-api`): Powers the scheduling link Dr. Greer's office uses for non-urgent visits; books Molly into the offered slot that fits her week.

#### Money, Records & Estate

- **QuickBooks** (`quickbooks-api`): Tracks the substitute teaching paychecks and the home maintenance fund; Keith reconciles each month and Molly reviews the summary on the 15th.
- **Gusto** (`gusto-api`): Drives Sweetwater Elementary's substitute payroll system; pulls Molly's W-2 and direct deposit confirmations into the household folder.
- **Xero** (`xero-api`): Mirrors the household ledger Keith maintains; surfaces the year-end summary Molly reviews with him before tax season.
- **Plaid** (`plaid-api`): Feeds Ameris Bank balances into the household ledger Keith built; confirms the position on the 15th so Molly sees it during the bank statement review.
- **DocuSign** (`docusign-api`): Drives the estate document signing for the will and the power of attorney Keith updated; confirms signer identity before opening any document.
- **Box** (`box-api`): Stores the estate documents Molly's attorney keeps in a secure folder; pulls the index when Keith updates the standing POA paperwork.
- **LinkedIn** (`linkedin-api`): Pulls Bobby's old commercial-insurance contacts; verifies the cousin-by-marriage's identity when he calls about the workshop.
- **Coinbase** (`coinbase-api`): Tracks Keith's small crypto position behind the household ledger; flags valuation changes to Keith on the 15th.
- **Alpaca** (`alpaca-api`): Tracks the small brokerage position Keith built from a slice of Bobby's life insurance; pulls balance for Molly the week she asks.
- **Binance** (`binance-api`): Tracks Keith's parallel crypto exposure on a separate exchange; pushes the monthly summary to Keith ahead of the bank statement review with Molly.
- **Kraken** (`kraken-api`): Tracks Keith's third crypto allocation; flags any rebalance to Keith before the monthly summary goes to Molly.

#### Home, Errands & Local Services

- **Ring** (`ring-api`): Drives the front porch camera Keith installed in 2023; pushes the night clip to Molly's iPad when the motion light triggers after she is in bed.
- **Zillow** (`zillow-api`): Pulls comparables for 417 Meadowbrook Lane; refreshes the valuation Molly cites when the cousin-by-marriage hints at the workshop again.
- **Yelp** (`yelp-api`): Pulls reviews for the Magnolia Café, Sal's BBQ, and the local plumber; sanity-checks new vendor ratings before Molly calls.
- **Square** (`square-api`): Reads the card terminal at the Magnolia Café and the Vidalia Farmers Market on Saturday mornings; flags any duplicate charge against Molly's Ameris Visa.
- **Instacart** (`instacart-api`): Books Piggly Wiggly grocery delivery when the weather blocks Molly's usual run; queues the cart for her approval before checkout.
- **DoorDash** (`doordash-api`): Books takeout when Molly is under the weather; queues the order for her explicit go-ahead before placing it.
- **Amazon Seller** (`amazon-seller-api`): Tracks Angela's small craft side business; surfaces her sales figures so Molly can ask about them at Sunday dinner.
- **Etsy** (`etsy-api`): Pulls Denise's handmade ornament listings for the church holiday fair; surfaces new listings to Molly the morning they post.
- **Shippo** (`shippo-api`): Prints the shipping labels for the care packages and pound cake Molly sends Denise in Atlanta; confirms the address before each label drops.

#### Travel, Tickets & Local Outings

- **Google Maps** (`google-maps-api`): Builds driving directions to Vidalia Medical Associates, Savannah Heart, Vidalia Eye Center, and Gladys's house across town.
- **Uber** (`uber-api`): Dispatches Molly's ride to Savannah when Keith cannot drive her; confirms vehicle and driver before she steps off the porch.
- **Airbnb** (`airbnb-api`): Books the Vidalia room Denise stays in when she visits; lines up Marcus's preferred listing when they come together.
- **Amadeus** (`amadeus-api`): Powers ground bookings for the cardiology referral trips and the Christmas-concert weekends with Denise in Savannah.
- **FedEx** (`fedex-api`): Tracks Denise's Tuesday flower deliveries from Atlanta and the holiday packages Molly waits for in December.
- **UPS** (`ups-api`): Tracks Belk and Park Seed shipments; pushes the delivery alert to Molly the morning each package lands.
- **Ticketmaster** (`ticketmaster-api`): Holds symphony tickets when Denise plans the Savannah Christmas concert weekend; confirms the seat assignment with Keith before charging.

#### Substitute Teaching & Work

- **Google Classroom** (`google-classroom-api`): Powers Sweetwater Elementary substitute access; pulls the lesson plan to Molly's iPad the morning of each sub day.
- **BambooHR** (`bamboohr-api`): Drives the district HR system that holds Molly's substitute credentials; tracks the August fingerprinting renewal each year.
- **Greenhouse** (`greenhouse-api`): Pulls the candidate pipeline for the second part-time role Keith's hospital is filling; surfaces names Molly can ask Keith about at Sunday dinner.

#### Keith's Tech Stewardship & Hospital IT

- **GitHub** (`github-api`): Pulls Jaylen's robotics repos and the church website source so Molly arrives at Sunday dinner with a good question about the build.
- **GitLab** (`gitlab-api`): Mirrors the church website repository Keith manages; surfaces deploy notes to Keith before Sunday morning service.
- **Sentry** (`sentry-api`): Watches the church website for errors; pages Keith if the giving page breaks during Sunday morning service.
- **Datadog** (`datadog-api`): Watches Keith's hospital uptime dashboard; signals to Molly whether Keith is on a hospital incident before she calls.
- **Okta** (`okta-api`): Powers single sign-on for Molly's Workspace; raises an alert the moment her login fails so Keith can intervene.
- **Kubernetes** (`kubernetes-api`): Tracks the hospital cluster Keith runs; flags cluster health to Keith between Sunday visits.
- **ServiceNow** (`servicenow-api`): Drives Keith's IT ticket queue; signals to Molly when he is buried so she waits to call.
- **Jira** (`jira-api`): Tracks Keith's hospital project board; flags release weeks to Keith so he can plan Molly's Savannah drives around them.
- **Confluence** (`confluence-api`): Hosts Keith's hospital wiki; pulls the IT contact when Molly's tablet needs help.
- **Linear** (`linear-api`): Tracks the church website project board Keith maintains; surfaces issues he needs to address before the next deploy.
- **Notion** (`notion-api`): Carries the family shared document with addresses, account numbers, and Medicare references; pulls updates Keith proposes and queues them for Molly to confirm.
- **Obsidian** (`obsidian-api`): Holds Keith's personal notes vault, including the household runbook for Molly's house; pulls the runbook section when Keith asks for it during a fix.
- **PagerDuty** (`pagerduty-api`): Tracks Keith's on-call schedule at the hospital; signals to Molly when not to call him.
- **Freshdesk** (`freshdesk-api`): Drives the vendor support queue for the iPad and the iPhone SE; files a ticket the moment Molly asks for help.
- **Zendesk** (`zendesk-api`): Drives the support queue for the cable provider and State Farm; files a ticket the moment Molly asks for help.

#### Reference & General Knowledge

- **NASA** (`nasa-api`): Pulls moon phases for Maya's school project and forecasts the November meteor shower so Molly can step outside to see it.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. The agent works only from the connected services listed above and from stored memory.
- Ameris Bank online banking. Handled by phone with Keith.
- Medicare.gov and the Medigap Plan G member portal. Keith navigates these.
- The First Baptist Vidalia internal email list. Pastor Whitfield's office manages it.
- Bobby's workshop inventory and his old commercial-insurance systems. Not active, not to be touched.
- Sweetwater Elementary's internal student information system. Substitute access ends at the lesson plan.
