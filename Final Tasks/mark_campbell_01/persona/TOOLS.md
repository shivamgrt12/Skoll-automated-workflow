# Tools: Mark Campbell

## Tool Usage

### Connected Services

#### Communication & Messaging
- **Gmail** (`gmail-api`): Primary business and personal inbox at mark.campbell@Finthesiss.ai; receives client messages, vendor confirmations, and family communications, and sends every approved outbound message.
- **WhatsApp** (`whatsapp-api`): Runs vendor group chats per wedding and the family group "The Campbells"; carries day-of coordination traffic and direct messages with key vendors.
- **Outlook** (`outlook-api`): Connects to vendors and clients who work in Microsoft; pulls their threads into the planning record and replies through the same channel.
- **Microsoft Teams** (`microsoft-teams-api`): Joins venue coordinators and corporate clients on their internal channels; carries vendor walkthrough chats and shared file links during planning weeks.
- **Slack** (`slack-api`): Coordinates with venue and catering teams who run their crews on Slack; handles real-time day-of logistics and post-event debriefs.
- **Discord** (`discord-api`): Runs the shared family gaming server with Ethan; checks in there each week to stay connected with him during the school year.
- **Telegram** (`telegram-api`): Holds the working channel with the second-photographer vendor on Mark's roster; carries shot-list confirmations and emergency-coverage requests on event day.
- **Twilio** (`twilio-api`): Sends automated reminder texts to clients 48 hours before tasting appointments and planning calls; routes day-of coordination SMS to vendors.
- **SendGrid** (`sendgrid-api`): Delivers formal client welcome emails, contract delivery notifications, and the monthly client status update from Campbell Events.
- **Mailgun** (`mailgun-api`): Powers time-sensitive vendor confirmations and tasting-week broadcasts; pairs with SendGrid to keep transactional delivery fast.
- **Zoom** (`zoom-api`): Hosts client planning calls, vendor walkthroughs, and Becca's Friday wrap-up when she works from home.

#### Scheduling, Planning & Documents
- **Google Calendar** (`google-calendar-api`): Runs two calendars: personal and Campbell Events. Sources every wedding date, client meeting, family event, and vendor appointment.
- **Notion** (`notion-api`): Stores the wedding planning workspace per client, business templates, the financial tracking pages, longer-form event briefs, and wedding concept notes; powers the client-facing design decks Mark walks couples through in tasting meetings; the operational backbone of Campbell Events.
- **Airtable** (`airtable-api`): Drives the active CRM for Campbell Events; tracks client roster, booking status, deposit history, and wedding dates in a single working view.
- **Trello** (`trello-api`): Runs vendor checklist boards per wedding; each card carries confirmation status, contract receipt, and day-of contact for that vendor.
- **Asana** (`asana-api`): Tracks the multi-event project pipeline during peak season when four weddings overlap; surfaces what is due to which couple this week.
- **Monday** (`monday-api`): Hosts Becca's day-of coordination task board; Mark reviews it every Friday to verify her prep is locked before Saturday.
- **Linear** (`linear-api`): Drives the business-improvement project log: process upgrades, vendor onboarding workflow, and the campbellevents.com refresh roadmap.
- **Jira** (`jira-api`): Tracks integration tickets with venues that run technical vendor portals; carries credential, insurance, and access-document submissions per venue.
- **Confluence** (`confluence-api`): Mirrors the Greater Philadelphia Event Planners Association vendor knowledge base; Mark pulls reputation notes and updated venue specs from it before pitching new clients.
- **Obsidian** (`obsidian-api`): Holds Mark's private note vault: vendor reputation observations, client personality reads, and planning fragments he keeps off the shared CRM.
- **Typeform** (`typeform-api`): Captures client intake on campbellevents.com: couple preferences, venue shortlist, budget range, and ceremony style before the first planning call.
- **DocuSign** (`docusign-api`): Sends and stores every vendor contract and client planning agreement Mark issues; every engagement clears here.
- **Calendly** (`calendly-api`): Powers the client-facing booking page for initial consultations and planning check-ins; pushes confirmations and reminder emails automatically.

#### Finance, Payments & Commerce
- **QuickBooks** (`quickbooks-api`): Tracks Campbell Events income by wedding, vendor expenses, and owner's draw; Phil Greenbaum's office reconciles in here every month.
- **Stripe** (`stripe-api`): Processes client deposit payments and final balance collections online for every couple who pays by card.
- **PayPal** (`paypal-api`): Settles payments with the long-standing vendor roster and equipment rental shops that bill Mark through PayPal each month.
- **Square** (`square-api`): Runs the point-of-sale at vendor expos and industry events when Mark collects consultation fees or sells planning guides in person.
- **Plaid** (`plaid-api`): Feeds live PNC personal and business balances into the financial tracking spreadsheet so Mark sees position before approving expenses.
- **Xero** (`xero-api`): Mirrors the Campbell Events books that Phil Greenbaum cross-references during quarterly reviews; Mark pulls Xero exports for year-end planning.
- **Alpaca** (`alpaca-api`): Tracks Mark's small brokerage position; he reviews it each Sunday evening when he plans the coming week with Julia.
- **Coinbase** (`coinbase-api`): Holds the small cryptocurrency position Mark maintains; he checks the balance each weekend and reinvests dividends manually.
- **Binance** (`binance-api`): Holds the second crypto account Mark opened on Ethan's recommendation; he rebalances it against Coinbase whenever the spread justifies a move.
- **Kraken** (`kraken-api`): Carries the third crypto allocation Mark runs alongside Coinbase and Binance; he tracks staking rewards through the Kraken dashboard each month.

#### Marketing & Client Relations
- **HubSpot** (`hubspot-api`): Tracks prospective clients from inquiry through booked contract; logs inquiry source, follow-up status, and referral attribution.
- **Zendesk** (`zendesk-api`): Handles post-event client support tickets such as vendor invoice disputes and photo delivery questions; routes each to Mark for a same-day reply.
- **Intercom** (`intercom-api`): Powers the website chat widget on campbellevents.com; captures inquiries from couples who find Mark through search and hands them to HubSpot.
- **Freshdesk** (`freshdesk-api`): Runs the post-October wrap-up ticket queue when Zendesk volume spikes; tracks the closeout survey responses Mark sends to each couple.
- **Salesforce** (`salesforce-api`): Connects Campbell Events to Riverside Estate's shared booking record system; Mark pulls availability and confirms blocked dates from there.
- **ActiveCampaign** (`activecampaign-api`): Runs the post-wedding email sequence: thank-you, review request, and referral ask, fired automatically after each event.
- **Klaviyo** (`klaviyo-api`): Manages the annual Campbell Events outreach campaign sent each November; segments the list by past-client tier and inquiry vintage.
- **Mailchimp** (`mailchimp-api`): Sends the quarterly newsletter to past clients and the prospect list; Becca builds each send from the saved Campbell Events template.
- **Segment** (`segment-api`): Tracks website visitor behavior on campbellevents.com; identifies which portfolio pages convert visitors into inquiry submissions.
- **Amplitude** (`amplitude-api`): Measures engagement on the portfolio and pricing pages of campbellevents.com; flags drop-off patterns Mark addresses in the quarterly site refresh.
- **Mixpanel** (`mixpanel-api`): Tracks the consultation booking funnel; pinpoints where prospective clients abandon the Typeform intake.
- **PostHog** (`posthog-api`): Records session replays for campbellevents.com; Mark watches the replays when Becca reports that couples struggle with the intake form.
- **Google Analytics** (`google-analytics-api`): Reports website traffic and referral sources; Mark reviews booked-client attribution every quarter to set referral incentives.

#### Venues, Events & Local Discovery
- **Eventbrite** (`eventbrite-api`): Tracks local industry events and Greater Philadelphia Event Planners Association meetups; books Mark's attendance and forwards confirmations to the calendar.
- **Ticketmaster** (`ticketmaster-api`): Surfaces large Philadelphia events (concerts, sports, conventions) that risk traffic and parking conflicts on wedding Saturdays; flags every conflict to Mark.
- **Yelp** (`yelp-api`): Pulls vendor reputation and review data; Mark cross-references it before adding any new caterer, photographer, or transportation company to his preferred list.
- **Google Maps** (`google-maps-api`): Builds venue directions for clients, calculates drive-time estimates between venues and hotel blocks, and scouts parking for outdoor weddings with large guest counts.
- **OpenWeather** (`openweather-api`): Pulls 10-day forecasts for every outdoor-venue wedding; triggers a weather contingency review when precipitation probability passes 40 percent on the event weekend.
- **Zillow** (`zillow-api`): Pulls property data when a client requests an estate venue with adjacent overnight accommodations; sizes lot, layout, and frontage from listing detail.
- **Airbnb** (`airbnb-api`): Identifies accommodation blocks for wedding guests when the venue has no attached hotel; assembles options Mark shares with couples.
- **Amadeus** (`amadeus-api`): Searches flight and hotel inventory for destination-wedding guests and for the Italy itinerary Mark is finalizing with Julia.

#### Social & Content
- **Instagram** (`instagram-api`): Powers the @campbell.events business account; Becca posts new content and Mark reviews and approves every post before it goes live.
- **Pinterest** (`pinterest-api`): Hosts client mood boards; couples pin inspiration for florals, color palettes, and table design, and Mark translates each board into vendor briefs.
- **Figma** (`figma-api`): Builds event floor plans and visual seating charts; Mark shares draft layouts with venue coordinators and clients in editable boards.
- **Webflow** (`webflow-api`): Runs campbellevents.com; Becca ships updates and Mark approves every copy and portfolio change before publish.
- **WordPress** (`wordpress-api`): Hosts the Campbell Events blog; Becca publishes monthly planning tips and Mark reviews each post for accuracy and tone.
- **Contentful** (`contentful-api`): Powers the wedding planning resource pages on campbellevents.com; Becca edits structured content and Mark signs off on every change.
- **YouTube** (`youtube-api`): Pulls venue showcase videos and vendor promotional reels into Mark's private playlist; he uses the playlist to brief couples on highlight-film style.
- **Vimeo** (`vimeo-api`): Hosts the premium highlight reel footage from select Campbell Events weddings; powers the portfolio presentations Mark walks couples through.
- **Twitter** (`twitter-api`): Tracks industry news and reputation mentions of Campbell Events and the preferred vendor roster; Mark replies to client-facing mentions within the day.
- **LinkedIn** (`linkedin-api`): Carries Mark's professional profile and connections with venue sales managers and vendor representatives across Philadelphia; he posts case studies after every notable wedding.
- **Reddit** (`reddit-api`): Tracks r/weddingplanning and r/philadelphia for the questions couples ask and the vendors getting recommended or called out; Mark mines the threads for pitch material.
- **Twitch** (`twitch-api`): Follows Ethan's streams; Mark drops in when Ethan is live to stay present in his son's hobby.
- **TMDB** (`tmdb-api`): Pulls film metadata when a couple requests a cinematic theme; Mark uses it to brief videographers and florists on the visual reference.

#### Logistics & Delivery
- **FedEx** (`fedex-api`): Ships custom event signage, printed timelines, and vendor packages whenever Becca cannot hand-deliver them in person.
- **UPS** (`ups-api`): Handles oversized deliveries: backdrop frames, accent furniture, and specialty rental items that need advance logistics planning.
- **Shippo** (`shippo-api`): Compares multi-carrier rates for vendor package shipments; powers cost-driven shipping decisions on bulk supply runs.
- **Uber** (`uber-api`): Books Mark's rides to venue walkthroughs without driving, and dispatches rides for clients running late on event day.
- **DoorDash** (`doordash-api`): Delivers lunch to the home office during crunch weeks when Mark cannot leave the desk.
- **Instacart** (`instacart-api`): Runs the grocery deliveries to Julia when Mark's schedule blocks a Trader Joe's or Whole Foods trip; built to her standing list.
- **Amazon Seller** (`amazon-seller-api`): Powers the Campbell Events Amazon Marketplace storefront; Mark lists and sells surplus event supplies, bulk-purchase overstock, and discontinued rental items between seasons.
- **Etsy** (`etsy-api`): Sources custom event stationery, handmade signage, and artisan table decor; Mark maintains a favorites list of vetted sellers organized by wedding style.

#### HR, Staffing & Retail Operations
- **BambooHR** (`bamboohr-api`): Manages Becca Hartwell's contractor agreement, time tracking, and PTO; carries the HR compliance record for the Campbell Events shop.
- **Greenhouse** (`greenhouse-api`): Runs the active search for a second part-time assistant; tracks candidate pipeline, interview notes, and offer status.
- **Gusto** (`gusto-api`): Runs payroll and contractor payments for Becca; files quarterly taxes and generates the year-end 1099.
- **ServiceNow** (`servicenow-api`): Submits insurance documentation and vendor credentials to a corporate venue client's internal portal whenever a new event onboards.
- **BigCommerce** (`bigcommerce-api`): Powers the Campbell Events digital planning guide storefront; Mark publishes new editions and tracks unit sales there.
- **WooCommerce** (`woocommerce-api`): Places stationery orders with the preferred WooCommerce-storefront supplier and tracks fulfillment against tasting-week deadlines.

#### Health, Lifestyle & Personal
- **MyFitnessPal** (`myfitnesspal-api`): Logs Mark's daily walks and meals through spring wedding season when the schedule disrupts regular eating.
- **Strava** (`strava-api`): Logs Benny's morning walks and Mark's Pilates Saturdays; tracks the streak Mark restarted in January.
- **Spotify** (`spotify-api`): Runs the Spotify Family account and powers Mark's office jazz, driving pop, and family bluegrass playlists.
- **OpenLibrary** (`openlibrary-api`): Searches business memoirs and history titles before Mark buys; pulls availability and edition data into the wishlist he keeps in Obsidian.
- **NASA** (`nasa-api`): Pulls moon phase and satellite imagery for celestial-theme weddings and outdoor ceremony timing against natural light windows.
- **Ring** (`ring-api`): Runs the home security camera at 923 Sycamore Hill Drive; pushes alerts whenever vendors or couriers arrive at the front door.

#### Tech & Infrastructure
- **GitHub** (`github-api`): Tracks the Chestnut Hill venue's open-source floor-plan tool repository; Mark pulls the latest seating-layout calculator release before each new event there.
- **GitLab** (`gitlab-api`): Pulls release notes from the wedding tech vendor that runs the booking portal Campbell Events integrates with; Mark patches the integration as each release ships.
- **Sentry** (`sentry-api`): Monitors campbellevents.com for errors; raises an alert to Becca whenever the inquiry form or Calendly integration breaks.
- **Datadog** (`datadog-api`): Watches campbellevents.com uptime and performance; flags issues to Mark before they hit incoming client inquiries.
- **PagerDuty** (`pagerduty-api`): Escalates Sentry and Datadog alerts to Becca's phone during business hours and to Mark after hours.
- **Okta** (`okta-api`): Runs single sign-on into the venue management portals for Bellevue Grand Ballroom and two other partner venues.
- **Cloudflare** (`cloudflare-api`): Powers CDN and DNS for campbellevents.com; Becca handles routine record changes and Mark tracks domain renewal dates.
- **Kubernetes** (`kubernetes-api`): Reaches the shared event management platform a tech-vendor partner runs on Kubernetes; Mark pulls cluster health and deployment status before each booking sync.
- **Algolia** (`algolia-api`): Powers vendor search on campbellevents.com; couples filter vendors by category and Philadelphia neighborhood through the Algolia index.
- **Google Classroom** (`google-classroom-api`): Pulls Sophie's posted course materials and grade updates through her active parent-viewer account; Mark reviews them before their Wednesday FaceTime.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from connected mock APIs and stored memory.
- No access to Becca Hartwell's personal accounts or private communications; only the shared business calendar and wedding folders.
- No access to Julia Campbell's personal accounts, finances, or devices.
- No access to Sophie's or Ethan's college systems, accounts, or records beyond what Mark shares directly.
- No banking transaction movement; Plaid surfaces balances into the spreadsheet but cannot move money.
- No direct database connection to the client CRM beyond the connected Airtable and Notion surfaces; there is no separate document archive or file-sync service.
