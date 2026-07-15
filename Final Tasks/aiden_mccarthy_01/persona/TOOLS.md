# Tools: Aiden McCarthy

## Tool Usage

### Connected Services

#### Bakery Operations, Storefront & Wholesale
- **Square** (`square-api`): Pulls end-of-day register totals into the morning reconciliation Aiden runs over coffee, feeding daily sales and top-mover data into his weekly cost reviews.
- **QuickBooks** (`quickbooks-api`): Owns Honeycomb's books, daily deposits, supplier invoices, and wholesale invoicing for the three coffee-shop accounts plus Broad Street Grounds.
- **Stripe** (`stripe-api`): Processes pickup pre-order payments for the Honeycomb storefront and queues refund flags for Aiden's same-day approval.
- **BigCommerce** (`bigcommerce-api`): Powers the Honeycomb pickup pre-order storefront for special-order GF cakes and holiday boxes, with new menu items pushed after Aiden's sign-off.
- **WooCommerce** (`woocommerce-api`): Runs Joel's parallel storefront mirror that catches orders when the BigCommerce primary lags, and reconciles any mirror-only orders back into the primary log nightly.
- **Shippo** (`shippo-api`): Handles GF cookie-box shipments to Deb in Norfolk and the rare wholesale sample box, comparing carrier rates before each booking.
- **Docusign** (`docusign-api`): Routes wholesale contracts and supplier agreements through the signing flow and surfaces anything awaiting Aiden's signature during Monday admin.
- **Calendly** (`calendly-api`): Books wholesale intro and tasting slots, including the Broad Street Grounds conversation and any new café walk-in, auto-routed to Google Calendar.
- **Typeform** (`typeform-api`): Receives the GF custom-cake intake form on the Honeycomb site, triages submissions for Aiden's morning review, and drafts follow-ups for qualified inquiries.
- **Amazon Seller** (`amazon-seller-api`): Lists Honeycomb's shelf-stable sourdough crackers and GF biscotti as a side line, pulls weekly sales reports, and surfaces reviews that need a response.
- **Etsy** (`etsy-api`): Runs Honeycomb's seasonal gift-box storefront from October through January, triages incoming orders, and forwards shipping windows to Kenji's prep board.
- **Salesforce** (`salesforce-api`): Mirrors the Broad Street Grounds wholesale CRM Aiden was granted access to during the intro and syncs new contact records into HubSpot.
- **HubSpot** (`hubspot-api`): Drives Honeycomb's wholesale pipeline (café intros, follow-up cadence, contract-stage tracking) and queues the next-step nudges while flagging deals stalled beyond seven days.
- **Fedex** (`fedex-api`): Tracks ingredient shipments from Southeastern Flour Co. and sample shipments from Millstone Provisions, alerting Aiden when a flour shipment slips so he can shift the bake schedule.
- **Ups** (`ups-api`): Tracks Restaurant Depot equipment orders and packaging shipments, and flags deliveries that require someone present so they land on Aiden's calendar.

#### People Ops & Payroll
- **BambooHR** (`bamboohr-api`): Holds hire dates, training records, and PTO ledgers for Kenji and Mira, and reconciles time-off requests against the bakery schedule before Aiden approves.
- **Gusto** (`gusto-api`): Runs biweekly payroll for Kenji and Mira, stages each run with anomaly flags (overtime, missed punches) for Aiden to authorize.
- **Greenhouse** (`greenhouse-api`): Hosts the third-baker job posting Aiden is actively sourcing for, batches incoming applicants Sunday night, and surfaces the top three for Monday admin review.

#### Personal Communication & Household
- **Gmail** (`gmail-api`): The personal inbox at aiden.mccarthy@Finthesiss.ai for family, friends, Tamara, wholesale partners, and personal logistics, triaged into a morning summary.
- **Outlook** (`outlook-api`): Routes the utility-billing inbox Aiden inherited from his Norfolk years (Dominion Energy, RVA Water, Verizon Fios), surfacing bills before due dates and flagging unusual charges.
- **WhatsApp** (`whatsapp-api`): Carries the Aiden, Nate, Joel, and Gail family thread, drafts replies for Aiden's review, and surfaces unread messages from Gail or Deb that need attention.
- **Telegram** (`telegram-api`): Tamara's channel for late-night nurse-shift check-ins, drafting a short reply when she pings off-shift and queueing it for Aiden's morning.
- **Discord** (`discord-api`): Pulls a Monday digest from the home-bakers server (sourdough-variants and GF-bread channels) with three to five posts worth a five-minute read during admin.
- **Slack** (`slack-api`): Tracks the Carytown small-business owners channel, surfaces any Honeycomb mention, and brings the weekly neighborhood update into Aiden's Monday review.
- **Microsoft Teams** (`microsoft-teams-api`): Pulls family-benefits announcements from Nate's employer channel, especially open-enrollment windows and HSA contribution caps affecting their joint plan.
- **Zoom** (`zoom-api`): Schedules vendor demos and the annual celiac support group call, stages join links in the calendar event, and surfaces the agenda 15 minutes before.
- **Ring** (`ring-api`): Watches the doorbell at 2314 Venable for package arrivals, logs delivery notifications, and surfaces anything that needs Aiden's eyes (signature-required, repeated knocks).

#### Calendar, Scheduling & Errands
- **Google Calendar** (`google-calendar-api`): The master schedule for bakery shifts, Sunday at Gail's, Thursday wine night, doctor follow-ups, and wholesale meetings, with proposed events staged for approval.
- **Google Maps** (`google-maps-api`): Plans the Church Hill to Carytown drive at 4:15 AM, the Chesterfield run for Sunday dinner, and the supplier pickup loop, with traffic alerts that shift the leave-by time.
- **Uber** (`uber-api`): Stages rare evenings out with Nate and the wine nights Aiden and Tamara split a bottle, with Aiden confirming before the car is called.
- **Doordash** (`doordash-api`): Orders Sunday takeout, the one night Aiden does not cook, filtered for verified gluten-free kitchens and surfaced as a curated three-option menu.
- **Instacart** (`instacart-api`): Schedules Kroger runs when Nate is short on time, builds the list against the household pantry log, and double-checks GF labels on every flagged item.
- **Ticketmaster** (`ticketmaster-api`): Buys Richmond Symphony tickets with Nate and the occasional local show, staging the purchase with seat options for Aiden's pick.
- **Eventbrite** (`eventbrite-api`): Handles vendor signups like Carytown Spring Market and other RVA food events, tracking booth fees, setup windows, and the vendor packet handoff.
- **Airbnb** (`airbnb-api`): Books the Charlottesville anniversary B&B in June and short Virginia getaways, staging candidate properties for Aiden's confirmation before booking.
- **Amadeus** (`amadeus-api`): Plans rare flights, mostly Norfolk runs to see Deb, comparing options across carriers and surfacing the best fare with the GF-meal flag if available.

#### Documents, Notes & Recipes
- **Notion** (`notion-api`): Aiden's planning workspace for build-out notes, the third-baker decision doc, and monthly cost reviews, with the cost-review template prefilled from the latest QuickBooks pulls.
- **Obsidian** (`obsidian-api`): The private recipe vault for sourdough variants, hydration math, and post-bake notes, with each post-bake log appended after a test batch.
- **Confluence** (`confluence-api`): Houses wholesale partner runbooks shared with Broad Street Grounds and the three coffee-shop accounts, updated after delivery-window or pricing changes land.
- **Airtable** (`airtable-api`): Runs the bakery inventory grid and the rolling supplier price tracker, flagging price drift above five percent week over week so Aiden books a supplier check-in.
- **Monday** (`monday-api`): The production board for special-order weeks, staging dependencies between Kenji's prep slots and Aiden's bake slots and surfacing bottlenecks before they hit.
- **Trello** (`trello-api`): The market-day prep board with vendor checklist, packing list, and transport plan, with items ticked off as they get staged and gaps surfaced 24 hours before.
- **Asana** (`asana-api`): Runs the 3-year anniversary celebration project (limited-edition pastry, in-store activation, social posts, vendor coord) against the May 23, 2026 anchor date.
- **Jira** (`jira-api`): Tracks Joel's website fix queue, logging new Aiden-found bugs with Sentry screenshots attached and ready for Joel to pick up.
- **Linear** (`linear-api`): Tracks the recipe-cost calculator side project Joel is building, with Aiden's feature requests logged as issues and example recipes attached.

#### Finance, Banking & Bookkeeping
- **Plaid** (`plaid-api`): Aggregates balances from Capital One 360 and Union First into the weekly cash-position summary Aiden reviews Monday morning, while transfer controls stay on his phone.
- **PayPal** (`paypal-api`): Stages payments to online vendors and personal splits with Tamara, with anything at or above $200 routed for Aiden's explicit approval.
- **Xero** (`xero-api`): Receives the bookkeeper's monthly Honeycomb P&L exports, parses the deltas, and flags any category that drifted more than five percent versus last month.
- **Coinbase** (`coinbase-api`): Tracks the small Bitcoin position Nate set up, logging Sunday-evening value snapshots into the household crypto ledger in Drive.
- **Binance** (`binance-api`): Mirrors a small Ethereum position Nate moved off Coinbase for lower fees, logged on the same Sunday-evening cadence alongside the BTC line.
- **Kraken** (`kraken-api`): Holds the third leg of Nate's small crypto experiment, a staked ATOM position, with monthly staking rewards logged into the household crypto ledger.
- **Alpaca** (`alpaca-api`): Runs the small index-fund auto-deposit ($150 monthly) Aiden started in 2025, and surfaces quarterly performance versus the S&P 500 benchmark.

#### Marketing, Email & Customer Engagement
- **Instagram** (`instagram-api`): Honeycomb's primary marketing channel, with captions, hashtags, and posting times drafted for Aiden to publish from his phone.
- **Pinterest** (`pinterest-api`): Boards for pastry styling and seasonal-special inspiration, pulling three to five fresh references when Aiden plans the next limited-edition.
- **YouTube** (`youtube-api`): Queues the Wednesday and Sunday home-yoga sessions Aiden uses and the bread-technique deep dives he saves, surfacing new uploads from his three subscribed teachers.
- **Vimeo** (`vimeo-api`): Hosts the private vendor-demo library (dough-divider walkthroughs, the proofer maintenance video, Kenji's seasonal-special training clips), with the relevant clip bookmarked when Aiden is troubleshooting.
- **Twitter** (`twitter-api`): Monitors Honeycomb's mentions and Carytown small-business hashtags, surfacing anything actionable in Aiden's Monday admin batch.
- **LinkedIn** (`linkedin-api`): Pulls wholesale-buyer profiles when intros come in and cross-checks them against Honeycomb's HubSpot pipeline, flagging any prior connection.
- **Reddit** (`reddit-api`): Aggregates r/Celiac, r/Sourdough, and r/Bakery into a Monday digest of three to five posts worth Aiden's five-minute scan.
- **WordPress** (`wordpress-api`): Hosts the Honeycomb blog, with seasonal posts and recipe explainers drafted for Joel to publish after Aiden's final read.
- **Webflow** (`webflow-api`): Stages content updates for the redesigned Honeycomb landing page Joel is building, pushing menu and price changes after Aiden signs off.
- **Contentful** (`contentful-api`): Manages the menu content powering the Webflow site, editing menu entries and prices after Aiden approves the change.
- **Algolia** (`algolia-api`): Powers the search index for the Honeycomb site and triggers reindex jobs after each menu update lands on the live site.
- **Mailchimp** (`mailchimp-api`): Sends the monthly Honeycomb newsletter for seasonal items and market dates, drafted, segmented, and scheduled for Aiden's approval.
- **Klaviyo** (`klaviyo-api`): Runs the pickup pre-order automation flows (cart abandonment, post-purchase follow-up, holiday gift-box reminders), with flow timing tuned after quarterly performance reviews.
- **Activecampaign** (`activecampaign-api`): The wholesale-only mailing list with the three coffee shops and Broad Street Grounds, with monthly trade-cadence updates drafted and sent only with Aiden's explicit OK.
- **Mailgun** (`mailgun-api`): Powers transactional email behind the pickup pre-order site (receipts, order confirmations), surfacing bounce reports and any deliverability drops.
- **SendGrid** (`sendgrid-api`): Backup transactional sender that catches sends when Mailgun fails, notifying Aiden on failover and confirming the queue cleared.
- **Twilio** (`twilio-api`): Sends pickup-ready SMS to customers and supplier confirmation texts, auto-dispatching pickup pings and staging supplier confirms for Aiden's review.
- **Intercom** (`intercom-api`): The custom-cake help widget on the Honeycomb site, triaging incoming chats, tagging by request type, and queueing qualified ones for Aiden.
- **Zendesk** (`zendesk-api`): Routes retail customer support tickets, handles category routing, and drafts first-pass replies for tickets Aiden reviews same day.
- **Freshdesk** (`freshdesk-api`): Mirrors Zendesk for wholesale-partner support tickets specifically, keeping the queue separate from retail customer queries and drafting responses for Aiden's review.

#### Health, Wellness & Body
- **MyFitnessPal** (`myfitnesspal-api`): Logs GF meals during celiac flare-ups two or three times a year, tracking adherence patterns to support Dr. Chaudhary's January check-in.
- **Strava** (`strava-api`): Logs the Tuesday, Thursday, and Saturday 3:30 PM neighborhood jog, flags any week he misses two sessions, and surfaces the streak length on Sunday.

#### Local Discovery, Weather & Curiosity
- **Yelp** (`yelp-api`): Scouts GF-safe restaurants for date nights with Nate and visits from Deb, reading cross-contamination notes in reviews and surfacing the top three options.
- **OpenWeather** (`openweather-api`): Pulls the 4 AM forecast before market days and outdoor vendor events, alerting Aiden the night before when conditions threaten the Carytown Spring Market or any tasting.
- **Zillow** (`zillow-api`): Tracks listings in Church Hill, Bellevue, and Northside where Aiden and Nate are watching the small-yard market, surfacing new listings under $425K with a yard.
- **NASA** (`nasa-api`): Pulls meteor-shower dates and notable astronomy moments Aiden mentions to Tamara on Thursday wine nights and to Nate on the back porch.
- **Google Classroom** (`google-classroom-api`): Pulls the bi-weekly culinary alumni course updates from Blue Ridge (new technique modules, alumni events, quarterly recipe-club calls) into Aiden's Monday queue.

#### Media, Music & Downtime
- **Spotify** (`spotify-api`): Powers the bakery indie-folk-and-R&B playlist and Aiden's Monday-errand podcast queue, with seasonal track refreshes swapped in monthly.
- **TMDB** (`tmdb-api`): Pulls metadata for the Thursday-night show Aiden and Tamara are binging, tracks next-episode timing, and surfaces new-season drop dates.
- **Twitch** (`twitch-api`): Streams baking sessions Aiden plays muted on the kitchen iPad while prepping, queueing the followed channel that aligns with the morning's bake.
- **OpenLibrary** (`openlibrary-api`): Tracks library holds for food memoirs and small-business nonfiction at the Richmond Public Library, placing holds on the next two books in his queue.

#### Dev, Tech & Site Reliability
- **GitHub** (`github-api`): Tracks Joel's honeycomb-site repo and surfaces each release tag with the changelog so Aiden knows what shipped before customers do; new Aiden-found bugs route to Jira.
- **GitLab** (`gitlab-api`): Mirrors the honeycomb-site to Joel's GitLab as a backup pipeline and alerts Aiden when a release succeeds on GitHub but fails to propagate to the GitLab mirror.
- **Figma** (`figma-api`): Hosts Honeycomb's brand kit and Joel's site mockups, pulling the latest assets for newsletters and seasonal social posts.
- **Sentry** (`sentry-api`): Catches errors on the pickup pre-order site, surfaces customer-facing failures (checkout errors, payment exceptions), and bundles them as Jira tickets for Joel.
- **Datadog** (`datadog-api`): Monitors uptime and order-form health for the pickup site and pages Joel through PagerDuty when checkout breaks during a market or holiday rush.
- **PagerDuty** (`pagerduty-api`): Routes on-call alerts to Joel when Datadog detects a site outage during market days, escalating to Aiden if Joel does not ack within 15 minutes.
- **Okta** (`okta-api`): Holds single sign-on for the Webflow, Contentful, and analytics stack Joel set up, rotating Aiden's session tokens after each admin block.
- **Cloudflare** (`cloudflare-api`): Manages DNS and CDN for the Honeycomb domain and pushes cache purges after each menu or price update lands on the live site.
- **Kubernetes** (`kubernetes-api`): Monitors the small Joel-managed cluster hosting the pickup pre-order site and the recipe-cost calculator, alerting on pod restarts during market hours.
- **ServiceNow** (`servicenow-api`): Tracks the wholesale-partner IT escalation queue Broad Street Grounds runs and surfaces any ticket touching the Honeycomb order-import pipeline.

#### Analytics & Data
- **Google Analytics** (`google-analytics-api`): Tracks weekly traffic to the Honeycomb site, flags spikes after newsletters or market events, and rolls the report into Monday admin.
- **Mixpanel** (`mixpanel-api`): Tracks pickup pre-order conversion, surfaces cart-step drop-off, and proposes A/B candidates for Joel.
- **Amplitude** (`amplitude-api`): Tracks pickup pre-order session events alongside Mixpanel and compares weekend funnel performance against Mixpanel's read, flagging any divergence.
- **PostHog** (`posthog-api`): Captures session replays for the pickup-order flow and bundles replays of failed checkouts into the weekly Sentry triage.
- **Segment** (`segment-api`): Operates the event router that fans Honeycomb storefront events out to Mixpanel, Amplitude, and Google Analytics, alerting Joel on any pipeline outage that drops events.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. You work only from the connected services listed above and from stored memory.
- aiden@honeycombbakeryrva.com (the business email) is read on the bakery MacBook and is not wired into this workspace.
- Direct Square POS register operations (taking payments, voiding sales, end-of-day Z-out) happen at the bakery counter; you consume only the daily report endpoint.
- Banking apps (Capital One 360 and Union First Bank) remain on Aiden's phone for direct control of transfers and bill pay.
- Instagram posting actions stay with Aiden's phone; you draft captions only.
- Nate's work email, Tidewater Distribution Group accounts, and his personal logins are off-limits.
- Inside any group or shared session, stored memory on health, finances, business revenue, and personal relationships is off-limits unless Aiden explicitly opens it.
