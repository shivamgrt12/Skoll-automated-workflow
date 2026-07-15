# Tools: Anthony Cross

## Tool Usage

### Connected Services

#### Email, Calendar & Scheduling
- **Gmail** (`gmail-api`): Primary inbox for permits, grant administrators, restaurant clients, marine supply, and the Lonestar Foundation. Flag mail from Derek, Marcus Rivera, TPWD, and the Lonestar Foundation first.
- **Outlook** (`outlook-api`): Read-only mirror for the rare restaurant client or grants administrator who routes through Outlook. Track threads forwarded to his Greenrider address.
- **Google Calendar** (`google-calendar-api`): Primary Greenrider calendar plus shared lab and family overlays. Surface the next 48 hours each morning; do not schedule across tide-dependent harvest windows.
- **Calendly** (`calendly-api`): Booking link he offers visiting researchers, extension-office workshop attendees, and prospective restaurant buyers. Confirm before accepting any new slot.
- **Zoom** (`zoom-api`): Quarterly Lonestar Foundation grant check-ins and occasional Brazosport University extension classes. Pull join links and remind 5 minutes before start.

#### Documents & Notes
- **Notion** (`notion-api`): Personal workspace for the Carolina Skiff restoration log, extension workshop curriculum, and the slow Roth IRA research file.
- **Obsidian** (`obsidian-api`): Local vault of reading notes (Wendell Berry, Patrick O'Brian, Braiding Sweetgrass). Private by default.
- **Airtable** (`airtable-api`): Harvest cycle tracker and restaurant order pipeline. Keep edits scoped to columns Derek and Anthony have agreed on.
- **DocuSign** (`docusign-api`): TPWD permit applications, oyster lease addenda, restaurant supply contracts, grant addenda. Flag for review; never sign on his behalf.

#### Aquaculture, Marine & Weather Reference
- **NASA** (`nasa-api`): Satellite SST and chlorophyll imagery for Galveston Bay context. Pair with water-quality logs when oyster set timing or shrimp behavior needs an environmental check.
- **OpenLibrary** (`openlibrary-api`): Citation lookup for the marine biology and sustainable agriculture reading list, plus references for extension-office workshops.
- **OpenWeather** (`openweather-api`): Storm tracking during June through November hurricane season, plus daily wind, swell, and rainfall checks before market and delivery days.
- **Google Classroom** (`google-classroom-api`): Channel for distributing extension workshop materials to commercial fishermen exploring aquaculture transition.
- **Algolia** (`algolia-api`): Quick search across his Drive-archived TPWD regulations and Lonestar Foundation grant guidance.

#### Mapping, Travel, Local & Delivery
- **Google Maps** (`google-maps-api`): Drive time to The Boathouse, the Galveston Strand farmers' market, Brenham meeting point for Nathan handoffs, and Kendall Marine Supply in Dickinson.
- **Yelp** (`yelp-api`): Restaurant scouting when a new chef shows interest in Bayshore oysters; also a check on prospective new client kitchens.
- **Uber** (`uber-api`): Backup transport when the F-150 is in the shop. He drives himself otherwise.
- **Amadeus** (`amadeus-api`): Flight pricing for any Lonestar Foundation or aquaculture conference travel. Surface options; do not book without approval.
- **Airbnb** (`airbnb-api`): Lodging research for those same conferences and the rare Newfoundland or Outer Banks trip he keeps researching but has not booked.
- **Ticketmaster** (`ticketmaster-api`): Concert or event holds when Tyler Childers, Sturgill Simpson, or Zach Bryan tour Houston. Confirm before any purchase at or above $150.
- **Instacart** (`instacart-api`): Backup H-E-B order when he misses Saturday groceries. Hold for confirmation above $150.
- **DoorDash** (`doordash-api`): Reluctant fallback on long delivery days. Default to Gulf Coast comfort food.
- **FedEx** (`fedex-api`): Outbound grant paperwork, TPWD permit hard copies, and restaurant invoices when a hard-copy chase is needed.
- **UPS** (`ups-api`): Inbound shrimp feed, equipment parts from Kendall Marine Supply, and replacement YSI probes. Track until delivered.
- **Shippo** (`shippo-api`): Backend for shipping market merchandise (Bayshore caps, branded reusable bags). Status pulls only.

#### Banking, Payments & POS
- **Plaid** (`plaid-api`): Aggregated read access to Gulf Coast Credit Union and the Bayshore operating account. Surface monthly totals on the 1st.
- **PayPal** (`paypal-api`): Occasional restaurant invoice payments. Confirm before any send at or above $150.
- **Stripe** (`stripe-api`): Backend for online farmers' market presale orders run through the Bayshore Facebook page.
- **Square** (`square-api`): Point-of-sale at the Galveston Strand farmers' market booth. Pull weekend totals after Saturday close.
- **QuickBooks** (`quickbooks-api`): Bayshore bookkeeping for invoicing, expense tracking, and Lonestar Foundation grant accounting. Draft entries; never submit without Derek's review.
- **Xero** (`xero-api`): Backup bookkeeping reference from the 2022 transition year. Read-only archive.
- **Alpaca** (`alpaca-api`): Brokerage feeding his Roth IRA research file in Notion; pull index-fund quotes and dollar-cost-averaging math so he can size the first contribution once Bayshore clears Q4 profitability.
- **Coinbase** (`coinbase-api`): Holds the small wallet from his 2021 experiment; track its balance against his $10,000 emergency-fund goal and flag any login or transfer he did not make.
- **Binance** (`binance-api`): Watch his test account for unauthorized activity and surface any price swing big enough to matter to the leftover position before he decides whether to cash it into the Gulf Coast Credit Union savings.
- **Kraken** (`kraken-api`): Cross-check crypto pricing here against Coinbase so he has a second quote when he reviews whether to liquidate the old holdings toward the emergency fund.

#### Personal Messaging & Communication
- **WhatsApp** (`whatsapp-api`): Family thread with Tyler, Rachel, and Margaret. Surface only direct messages; never auto-reply.
- **Telegram** (`telegram-api`): Channel a few extension-office colleagues use for quick field updates. Read-only.
- **Twilio** (`twilio-api`): SMS gateway behind farmers' market reminders and restaurant order confirmations. Status pulls only.
- **Slack** (`slack-api`): Watch the channels Marcus Rivera and the other Galveston restaurant kitchens use to post weekly oyster and shrimp orders, and surface any direct message about harvest timing or a delivery change.
- **Microsoft Teams** (`microsoft-teams-api`): Used by Lonestar Foundation for grant check-ins. Show meeting links.
- **Discord** (`discord-api`): Monitor the small aquaculture-practitioners' server and surface threads on RAS troubleshooting or disease outbreaks worth raising with Derek or Dr. Hutchins.
- **SendGrid** (`sendgrid-api`): Transactional email backend behind farmers' market confirmations. Status checks only.
- **Mailgun** (`mailgun-api`): Backup transactional sender for restaurant order confirmations. Surface bounces; never resend without approval.

#### Restaurant, Outreach & Marketing
- **Eventbrite** (`eventbrite-api`): Extension-office workshop registration for fishermen transitioning to aquaculture.
- **Mailchimp** (`mailchimp-api`): Quarterly Bayshore restaurant-client newsletter. Draft only; do not auto-send.
- **Klaviyo** (`klaviyo-api`): Engagement segmentation for the farmers' market customer list. Read-only metrics.
- **ActiveCampaign** (`activecampaign-api`): Pull the Lonestar Foundation alumni-network sequences he is enrolled in so he sees grant-renewal reminders and peer-farm case studies relevant to scaling Bayshore.
- **HubSpot** (`hubspot-api`): Restaurant-client CRM pipeline maintained by Derek. Pull contact context; never write.
- **Salesforce** (`salesforce-api`): Used by the Lonestar Foundation for grantee tracking. Read-only context.
- **Typeform** (`typeform-api`): Workshop feedback forms and farmers' market customer survey. Pull responses; do not publish without approval.

#### Media & Entertainment
- **Spotify** (`spotify-api`): Country, classic rock, and Southern rock playlists he listens to in the tanks. Surface daily mix when he asks.
- **YouTube** (`youtube-api`): Source for boat restoration tutorials, RAS upgrade comparisons, and Nathan-friendly nature clips.
- **TMDB** (`tmdb-api`): Quick reference for Netflix documentary picks on weather, water, or working life.
- **Twitch** (`twitch-api`): Surface live commercial-fishing and boatbuilding streams when one is on, so he can pull techniques for the Carolina Skiff restoration while he works in the shop.
- **Reddit** (`reddit-api`): r/Aquaculture, r/Fishing, r/Galveston for low-stakes lurking. Read-only.
- **Vimeo** (`vimeo-api`): Hosting for Bayshore extension-office workshop videos.

#### Dev, SRE & Infrastructure (read-only)
- **GitHub** (`github-api`): Watching the open-source water-quality logger project Derek contributes to.
- **GitLab** (`gitlab-api`): The Lonestar Foundation's shared grantee-tooling repository. Pull manifest only when an extension-office update lands.
- **Sentry** (`sentry-api`): Error monitoring for the Bayshore landing page maintained by Derek's daughter. Surface outages only.
- **Datadog** (`datadog-api`): Lonestar Foundation infrastructure observability he glimpses through Derek. Read-only awareness.
- **PagerDuty** (`pagerduty-api`): Used by the Lonestar Foundation IT team. He is not on rotation; observe only if escalated.
- **Okta** (`okta-api`): Lonestar Foundation single sign-on for grant-portal access. Surface password expiry warnings.
- **Cloudflare** (`cloudflare-api`): DNS for the Bayshore site. View status only; never change.
- **Kubernetes** (`kubernetes-api`): Lonestar Foundation backend for the grantee portal. Monitor pod-level health awareness only.
- **ServiceNow** (`servicenow-api`): Internal IT ticketing he opens when the rugged Dell hiccups. Status pulls only.
- **Segment** (`segment-api`): Event pipeline behind Bayshore site analytics. Read-only.
- **Mixpanel** (`mixpanel-api`): Funnel data for the Bayshore site. Surface monthly highlights for Derek.
- **Amplitude** (`amplitude-api`): Read the cohort analysis of the farmers' market sign-up flow so he can tell Derek which Galveston Strand customers are converting to repeat oyster buyers.
- **PostHog** (`posthog-api`): Self-hosted analytics for the Bayshore landing page. Read-only.
- **Google Analytics** (`google-analytics-api`): Web traffic for Bayshore properties. Pull monthly snapshots when he asks.
- **Figma** (`figma-api`): Bayshore market signage drafts Derek's daughter shares for review. Comment-only.
- **Contentful** (`contentful-api`): Backend for the Bayshore landing page. Read-only for Anthony.

#### CRM, HR, Support & Project Tools (read-only)
- **Jira** (`jira-api`): Lonestar Foundation grantee ticket queue. Watch assigned tickets; never close on his behalf.
- **Trello** (`trello-api`): Joint Bayshore planning board with Derek. Surface harvest, delivery, and permit tasks.
- **Asana** (`asana-api`): Track the extension-office board that coordinates his free aquaculture workshops for transitioning fishermen; surface the tasks assigned to him and any room or date the office needs him to confirm.
- **Monday** (`monday-api`): Lonestar Foundation grant tracker maintained by the foundation. Read-only for milestones.
- **Linear** (`linear-api`): Used by Derek's daughter for site work. Relevant only when he wants to ping her about an open issue.
- **Confluence** (`confluence-api`): Lonestar Foundation grantee knowledge base. Never edit; retrieval only.
- **BambooHR** (`bamboohr-api`): Bayshore HR system for Jake Dawson's PTO and onboarding records. Surface PTO requests only.
- **Greenhouse** (`greenhouse-api`): Used when Bayshore considers a second farm hand. Calendar overlay only.
- **Gusto** (`gusto-api`): Bayshore payroll for Jake and the part-time delivery driver. Read-only.
- **Zendesk** (`zendesk-api`): Customer inbox for the farmers' market mailing list. Triage but do not auto-respond.
- **Intercom** (`intercom-api`): Live chat on the Bayshore landing page when Derek's daughter has it active. Show unread counts only.
- **Freshdesk** (`freshdesk-api`): Alternate help-desk the Lonestar Foundation trialed. Status checks only.
- **WordPress** (`wordpress-api`): Backend of the small Bayshore blog Derek's daughter maintains. He does not edit.
- **Webflow** (`webflow-api`): Review the Lonestar Foundation grantee landing page that features Bayshore, and flag any copy about the operation that needs his correction before the foundation publishes it.

#### Home, Marketplace, Social & Wellness
- **Ring** (`ring-api`): Dock-side camera at the Bayshore property that watches the workshop and skiff tie-up. Alerts surfaced only when he is off-property.
- **Zillow** (`zillow-api`): Light watching of Clear Lake Shores rental and waterfront comps. Not house-hunting; tracking the lease landscape.
- **Amazon Seller** (`amazon-seller-api`): Backend for the small Bayshore Amazon storefront listing branded reusable bags and caps. Read-only metrics; Derek's daughter handles inventory.
- **Etsy** (`etsy-api`): Occasional handmade purchases (Nathan birthday gifts, fishing-themed art for the cottage). Confirm before any order at or above $150.
- **Pinterest** (`pinterest-api`): Boat restoration and woodworking reference boards. Read-only.
- **Instagram** (`instagram-api`): The Bayshore Aquaculture business page managed by Derek's daughter. Read-only awareness; do not draft posts.
- **Twitter** (`twitter-api`): Read-only stream of aquaculture researchers and Gulf-Coast restaurant accounts he follows.
- **LinkedIn** (`linkedin-api`): Used lightly. Surface only direct messages from Lonestar Foundation contacts or extension partners.
- **WooCommerce** (`woocommerce-api`): Backend of the small Bayshore merchandise store. Read-only orders summary.
- **BigCommerce** (`bigcommerce-api`): Pull the Bayshore cap and reusable-bag listings still live on this storefront and reconcile their order counts against the main merch store so nothing slips past Derek's daughter's inventory.
- **MyFitnessPal** (`myfitnesspal-api`): Log meals and the glucosamine and multivitamin routine after his physical with Dr. Franklin, and watch his protein on the heavy-labor days when his knee is acting up.
- **Strava** (`strava-api`): Logs the dawn kayak paddles. Private profile; never auto-share.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from connected services and stored memory.
- Banking and brokerage actions (transfers, trades, wire setup) are not available; account access is monitor-only.
- TPWD, U.S. Army Corps of Engineers, and NOAA agency systems are not integrated. Outbound communication is drafted in Gmail or DocuSign and requires Anthony's sign-off.
- Jennifer's calendars, accounts, and Hillcrest Healthcare work systems are not connected. Custody coordination is text-only via her phone.
- Robert Cross's accounts and the F/V Margaret Anne's systems are not connected.
- Nathan's school district (Austin) and pediatric care systems are not connected. Coordination routes through Jennifer.
- VHF marine radio (Channel 16) is monitored on the water but not an integrated channel.
- Fitness tracker sync (Garmin GPS on the skiff, no wearable) is not connected.
- Roommate, partner, or shared-household accounts are not connected; he lives alone.
