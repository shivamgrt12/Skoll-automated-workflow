# Tools: Darius Barker

## Tool Usage

### Connected Services

#### Restaurant POS, Bookkeeping & Payments
- **Square** (`square-api`): Runs the mobile POS terminal Darius takes to catering events the Clover terminal cannot leave the restaurant for. Settles each event's tab the next morning.
- **PayPal** (`paypal-api`): Collects catering deposits from corporate clients who insist on PayPal over Venmo. Two or three deposits a month during catering peak.
- **Stripe** (`stripe-api`): Charges ticketed New Year's Eve prix fixe and anniversary event seats. Refunds require Darius's approval; otherwise auto-captures.
- **Plaid** (`plaid-api`): Aggregates restaurant checking and personal accounts at River City Community Credit Union. Pulls daily balances and transaction data for the Sunday inventory and Monday bookkeeping.
- **QuickBooks** (`quickbooks-api`): Memphis Soul Kitchen's books. Categorizes vendor expenses and surfaces the monthly P&L for the last-Monday review with Megan and Devon.
- **Xero** (`xero-api`): Exports quarterly tax-prep files in Xero format for the accountant working the small business loan refinance.
- **Coinbase** (`coinbase-api`): Runs a $25 monthly Bitcoin auto-buy Tanya talked Darius into trying. He reviews the position at year-end with his tax prep.
- **Alpaca** (`alpaca-api`): Holds a small Memphis-area REIT plus an S&P index ETF. Darius rebalances quarterly and sweeps catering bonuses into it.
- **Binance** (`binance-api`): Sends small crypto gifts to a Memphis cousin who insists on it for birthdays. Two or three transactions a year.
- **Kraken** (`kraken-api`): Holds a USDC stablecoin balance for the one specialty-spice vendor who only accepts USDC. Darius converts on demand each order.

#### Vendors, Logistics & Contracts
- **Amazon Seller** (`amazon-seller-api`): Memphis Soul Kitchen branded hot sauce and dry rub listings. Restocks each spring before the festival circuit and pushes seasonal price updates.
- **Etsy** (`etsy-api`): Orders decor and gift bags for the Mother's Day brunch and the anniversary dinner. Two or three orders per major event.
- **FedEx** (`fedex-api`): Tracking for specialty ingredient shipments from out-of-state suppliers. Surfaces delivery delays before the prep window.
- **UPS** (`ups-api`): Schedules vendor shipments and the monthly care package Darius sends to Earl in Memphis.
- **Shippo** (`shippo-api`): Prints labels for the monthly hot-sauce and dry-rub fulfillment batch and for branded merchandise gifts.
- **DocuSign** (`docusign-api`): Vendor agreements, catering contracts, and the eventual 2027 lease renewal with Frank Donovan. Drafts the package; Darius signs personally.

#### Catering, Events & Ticketing
- **Eventbrite** (`eventbrite-api`): Ticket sales for the New Year's Eve four-course dinner and seated anniversary events.
- **Calendly** (`calendly-api`): Catering consult bookings. Blocks the Tuesday-through-Sunday lunch rushes and the Thursday band rehearsal.
- **Typeform** (`typeform-api`): Intake form for catering inquiries on the Memphis Soul Kitchen site. Routes responses to Megan and surfaces big-ticket leads to Darius.
- **Ticketmaster** (`ticketmaster-api`): Books Riverside Groove Collective festival passes when promoters reference dates and buys Grizzlies tickets for the annual Memphis trip.

#### Marketing, CRM & Customer Support
- **HubSpot** (`hubspot-api`): Catering CRM. Tracks Dominion Financial Group and other corporate leads from first inquiry through delivery and follow-up.
- **Salesforce** (`salesforce-api`): Pushes new corporate catering leads to clients that require Salesforce vendor records. Updates contact properties every two weeks.
- **Mailchimp** (`mailchimp-api`): Monthly Memphis Soul Kitchen newsletter. Seasonal menu drops, catering availability, anniversary invites.
- **Klaviyo** (`klaviyo-api`): Segmented sends for repeat catering clients. Anniversary outreach uses this segment, not the general newsletter.
- **ActiveCampaign** (`activecampaign-api`): Automated thank-you sequence after each catering event. Tags the client with the menu so the next pitch lands warm.
- **Mailgun** (`mailgun-api`): Transactional email behind reservation confirmations. Surfaces bounce rates before they touch deliverability.
- **SendGrid** (`sendgrid-api`): Sends catering confirmations and signed-contract delivery emails. Two or three batches per active event week.
- **Twilio** (`twilio-api`): SMS notifications for catering pickup windows and large-party reservation reminders.
- **Intercom** (`intercom-api`): Watches website chat threads on memphissoulkitchen.com and escalates any inquiry naming a budget over $1,500 to Megan and Darius.
- **Zendesk** (`zendesk-api`): Logs catering complaint tickets and the resolution thread. Darius reads every ticket before calling the customer back personally.
- **Freshdesk** (`freshdesk-api`): Vendor support inbox for issues with food suppliers and the Clover POS vendor. Darius opens a ticket whenever a delivery is short or wrong.

#### Website, Storefront & Analytics
- **WordPress** (`wordpress-api`): memphissoulkitchen.com. Menu pages, catering page, anniversary event posts. Drafts the copy; Megan publishes.
- **Webflow** (`webflow-api`): The Riverside Groove Collective band site. Pushes a tour-date update after every gig confirmation.
- **BigCommerce** (`bigcommerce-api`): The Memphis Soul Kitchen merch storefront for branded hot sauce, dry rubs, and t-shirts. Updates inventory monthly and pushes anniversary specials.
- **WooCommerce** (`woocommerce-api`): Runs the holiday gift-card storefront on memphissoulkitchen.com. Darius ships a fresh batch every November and audits redemption monthly.
- **Contentful** (`contentful-api`): Headless store for menu photos and the press kit. Refreshes after every menu change.
- **Algolia** (`algolia-api`): Powers the menu search and catering FAQ on the site. Reindexes after every menu change.
- **Google Analytics** (`google-analytics-api`): Catering page traffic, anniversary RSVP funnel, holiday menu page views. Surfaces the weekly spike, not the noise.
- **Mixpanel** (`mixpanel-api`): Reservation funnel events. Cross-checks against Google Analytics for the holiday push.
- **Segment** (`segment-api`): Pipes web events into Mailchimp, HubSpot, and Mixpanel. Do not change destinations without Darius's sign-off.
- **Amplitude** (`amplitude-api`): Cohort view of repeat catering clients. Pulls before pitching a renewal package.
- **PostHog** (`posthog-api`): Tracks the catering quote tool's session recordings and form funnels. Darius reviews it weekly when GA misses the funnel detail he wants.
- **Figma** (`figma-api`): Menu mockups, anniversary event flyers, and the hot sauce label. Exports each revision for Darius to hand-approve.

#### Social, Reviews & Press
- **Instagram** (`instagram-api`): Posts to @memphissoulkitchen feed. Plate photos, the kitchen wall with Dorothy's framed photo, band tour stops. Megan reviews drafts before publishing.
- **Pinterest** (`pinterest-api`): Builds private boards for the seasonal Virginia-Southern fusion menu experiments. Pins weekly during menu R&D weeks.
- **Twitter** (`twitter-api`): Posts band gig announcements, Grizzlies reactions, and Memphis Soul Kitchen anniversary teasers. Two or three posts a week.
- **Reddit** (`reddit-api`): Comments in r/restaurateur about supply tips and replies in r/rva when locals ask about Southern restaurants. A handful of comments a week.
- **LinkedIn** (`linkedin-api`): Posts catering case studies after big corporate jobs and reaches out monthly to two or three warm corporate-catering leads.
- **Yelp** (`yelp-api`): Restaurant review monitor. Surfaces new reviews daily; Darius personally responds to anything below four stars within 48 hours.
- **TMDB** (`tmdb-api`): Family movie-night lookups. The kids pick; you fact-check ratings and runtime.

#### Music, Band & Video
- **Spotify** (`spotify-api`): Restaurant dinner-service playlist (Marvin Gaye is the anchor). Also Riverside Groove Collective artist page and monthly listener counts.
- **YouTube** (`youtube-api`): Band performance uploads and the bass tutorials Jaylen saves. Schedules premieres for after-school hours.
- **Twitch** (`twitch-api`): Livestreams band rehearsals when a festival promoter asks for a preview clip. Two or three streams a year, plus Grizzlies playoff watches with the kids.
- **Vimeo** (`vimeo-api`): Hosts the Riverside Groove Collective's high-quality festival recordings. Darius uploads after every paid gig and sends promoter download links.
- **Discord** (`discord-api`): Riverside Groove Collective server. Setlist files, rehearsal notes, gig logistics.

#### Family, School & Daily Messaging
- **Gmail** (`gmail-api`): darius.barker@Greenridertech.co. Vendor correspondence, licensing, community organization emails. Drafts for Darius's approval on new contacts.
- **Google Calendar** (`google-calendar-api`): Restaurant shifts, band rehearsals, basketball coaching, church, family events. The master schedule.
- **Google Drive** (`google-drive-api`): Restaurant financial records, menu planning docs, catering proposals, vendor agreements. Confirms before sharing folders externally.
- **Google Classroom** (`google-classroom-api`): Jaylen at Westbrook Preparatory and Zaria at Oakwood Elementary. Surfaces upcoming due dates so Monique knows by Monday evening.
- **WhatsApp** (`whatsapp-api`): Posts and replies in the Barker Family group, Church Hill Community Association, and Riverside Groove Collective group.
- **Telegram** (`telegram-api`): Memphis cousin group thread. Darius drops birthday wishes and Grizzlies reactions; checks it most evenings.
- **Microsoft Teams** (`microsoft-teams-api`): Reads Westbrook Preparatory parent updates and forwards signal items to Monique.
- **Outlook** (`outlook-api`): Pulls Westbrook Preparatory and Oakwood Elementary parent calendars and mirrors them into Google Calendar each evening so Monique sees one view.
- **Slack** (`slack-api`): Catering coordination workspace shared with Devon and Megan during big events. Posts the prep checklist the night before each event.
- **Zoom** (`zoom-api`): Pastor Hayes's men's ministry calls when Darius cannot make it in person. Also corporate catering kickoff calls.

#### Travel, Maps, Weather & Local Errands
- **Google Maps** (`google-maps-api`): Delivery routing for catering, vendor pickup directions for Devon, drive time to Byrd Park for Saturday coaching.
- **OpenWeather** (`openweather-api`): Outdoor catering weather calls and Saturday basketball-day forecasts. Surfaces threats 72 hours out so Devon and Megan can prep covers.
- **Amadeus** (`amadeus-api`): Searches Memphis trip itineraries to see Earl. Books a flight when the fare drops below the Richmond-to-Memphis threshold Darius keeps.
- **Airbnb** (`airbnb-api`): Books cabins and stays for family weekend trips and Memphis visits to see Earl when hotels are tight.
- **Uber** (`uber-api`): Books rides home after late catering nights and for staff after the kitchen closes past 10 PM. A handful of trips a month.
- **DoorDash** (`doordash-api`): Memphis Soul Kitchen storefront on DoorDash for delivery orders. Monitors daily; pauses when the kitchen is slammed.
- **Instacart** (`instacart-api`): Emergency ingredient runs when Southside Wholesale is closed and the kitchen is mid-service.
- **Zillow** (`zillow-api`): Tracks the building Frank Donovan owns and comparable Church Hill commercial properties. Darius checks comps monthly while working toward the 2027 buy.
- **Ring** (`ring-api`): Restaurant back-door camera. Surfaces motion alerts after close; ignores daytime delivery noise.

#### Health, Reading & Curiosity
- **MyFitnessPal** (`myfitnesspal-api`): Daily walk and salt-intake tracking per Dr. Rhodes's blood pressure plan. Consistency only, no calorie pressure.
- **Strava** (`strava-api`): Logs the 15-minute walk to the restaurant and Saturday basketball mornings. Private profile; Monique is the only follower.
- **OpenLibrary** (`openlibrary-api`): The Sankofa Chronicles series Jaylen put him onto, plus restaurant industry references and Black history for the kids' bedtime stories.
- **NASA** (`nasa-api`): Zaria's school science questions. Surfaces clean images and the next visible-from-Richmond event.

#### Notes, Staff, Tasks & Engineering Tools
- **Notion** (`notion-api`): Catering proposal templates, menu R&D notes, anniversary event planning page.
- **Obsidian** (`obsidian-api`): Darius's private recipe notebook digitized. Cross-linked by ingredient and by which of Dorothy's originals it builds on.
- **Airtable** (`airtable-api`): Vendor list, band booking tracker, catering pipeline, basketball roster. The connective tissue of the operation.
- **Trello** (`trello-api`): Lightweight prep board the kitchen line uses on Friday and Saturday shifts.
- **Asana** (`asana-api`): Anniversary event task board with assignees for Megan, Devon, and the part-time servers.
- **Monday** (`monday-api`): Catering pipeline view shared with Devon when Asana is the wrong shape for a quick read.
- **Jira** (`jira-api`): Files bug reports for the memphissoulkitchen.com refresh when Darius spots something during a service. Drops issues with screenshots; the web developer works the queue.
- **Linear** (`linear-api`): Tracks the band-site refactor milestones with the developer. Darius drops feature requests as comments when something on tour-date pages needs to change.
- **Confluence** (`confluence-api`): Staff handbook, food-safety procedures, opening and closing checklists. Drafts updates for Darius to approve before publishing.
- **Dropbox** (`dropbox-api`): Band performance audio archives and high-res restaurant photos. Shared with Riverside Groove Collective.
- **Box** (`box-api`): Uploads signed catering contracts and compliance documents to the folders corporate clients require. Drops a new file after every contract close.
- **GitHub** (`github-api`): Watches Jaylen's bass-tab repo and leaves an issue or comment when a tab needs a fingering note. Father-son code review.
- **GitLab** (`gitlab-api`): Hosts the band site source. Tags releases when the tour calendar updates and pings the developer when copy needs a refresh.
- **Kubernetes** (`kubernetes-api`): Restarts the catering quote tool's web pod when the form locks up during an inquiry rush. Darius runs the restart command from his phone.
- **Sentry** (`sentry-api`): Errors on the catering form and ticket checkout. Alerts Megan first and Darius second if the issue persists.
- **Datadog** (`datadog-api`): Tracks site performance during the December and holiday-season traffic spikes. Darius opens the pinned dashboard before every major promotion.
- **PagerDuty** (`pagerduty-api`): Routes catering-site incidents to the developer's on-call. Darius is the secondary escalation when the site is down during a paid event window.
- **Cloudflare** (`cloudflare-api`): Manages DNS and rate limiting for both the restaurant and band sites. Darius rotates the cache after every menu update and reviews the security log weekly.
- **Okta** (`okta-api`): Single sign-on for corporate catering clients who require SSO before granting a vendor login.
- **BambooHR** (`bamboohr-api`): Staff records for Devon, Megan, Terrence, Marcus Jr., DeShawn, and the part-time servers. Updates time-off requests weekly and W-2s every January.
- **Gusto** (`gusto-api`): Restaurant payroll. Runs every other Friday with Darius's explicit approval.
- **Greenhouse** (`greenhouse-api`): Runs hiring funnels when Memphis Soul Kitchen needs a new line cook or server. Darius opens a role two or three times a year and reviews applications nightly.
- **ServiceNow** (`servicenow-api`): The Dominion Financial Group vendor portal. Submits catering invoices through their workflow.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. You work from the connected services listed above and from stored memory only.
- Venmo on Darius's phone (@Darius-Barker). You can prompt him to settle in Venmo but cannot act inside it.
- Zelle through River City Community Credit Union. Drafted on Darius's phone, not the agent.
- Clover POS on-site at the restaurant. Sales, orders, and inventory live there; you read summaries only when Darius exports them.
- Personal banking inside the River City Community Credit Union app on Darius's phone.
- Monique's personal accounts, group chats, and finances.
- Riverside Baptist Church internal systems, congregation records, and Pastor Hayes's private correspondence.
- Earl's medical records and his providers in Memphis.
- Jaylen's, Zaria's, and Caleb's personal devices and school logins beyond the parent-facing Classroom, Teams, and Outlook views.
- Facebook (business page and personal account). Megan manages the Memphis Soul Kitchen page directly inside the Facebook app; no Facebook API is available to the agent.
- RichmondEats merchant portal for the local-delivery storefront. Megan operates it directly inside the merchant app; the agent reads exported reports only.
