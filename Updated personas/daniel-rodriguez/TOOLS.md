# Tools: Daniel Rodriguez

## Tool Usage

### Connected Services

#### Email, Calendar & Scheduling

- **Gmail** (`gmail-api`): His inbox at daniel.rodriguez@greenridertech.com for personal notes, supplier inquiries, and appointment confirmations, synced with Google Calendar for event creation from email threads.
- **Google Calendar** (`google-calendar-api`): The master calendar for his work schedule, personal appointments, family calls, and date plans, fed by Calendly bookings and Gmail confirmations.
- **Outlook** (`outlook-api`): A secondary address that catches culinary supplier newsletters and vendor receipts, forwarding key items to Gmail for unified tracking.
- **Calendly** (`calendly-api`): Booking link he uses to schedule tasting slots and commissary-kitchen walkthroughs, with confirmed slots pushed to Google Calendar automatically.
- **Mailchimp** (`mailchimp-api`): Runs the early interest list for the future taco and torta truck, with subscriber data synced to HubSpot for lead tracking.
- **Mailgun** (`mailgun-api`): Delivers the order confirmations he sends produce suppliers, triggered from his Airtable ordering sheet.
- **SendGrid** (`sendgrid-api`): Sends appointment and supplier reminders he sets for himself, coordinated with Google Calendar event times.
- **Twilio** (`twilio-api`): Sends himself prep-deadline and inhaler-refill text reminders, triggered by Google Calendar events and monthly recurring schedules.

#### Messaging & Calls

- **WhatsApp** (`whatsapp-api`): How Carlos Vega and suppliers send quick produce updates and photos, with price changes flagged against Airtable cost tables.
- **Telegram** (`telegram-api`): The culinary-school group chat with Danny and old classmates trading technique and recipe ideas that feed into his Obsidian vault.
- **Microsoft Teams** (`microsoft-teams-api`): Joins the food festival organizer's vendor coordination calls, with meeting notes synced to Monday for event logistics tracking.
- **Zoom** (`zoom-api`): Joins supplier calls and remote food truck consultant sessions, with follow-up action items pushed to Jira.
- **Slack** (`slack-api`): Coordinates the Charleston pop-up vendor collective, with event updates cross-posted to the Monday logistics board.
- **Discord** (`discord-api`): Active in a fermentation and home-cook community for technique threads that inform his Confluence recipe procedures.
- **Twitch** (`twitch-api`): Follows cooking streamers and live restaurant build-outs, saving build-out ideas to his Pinterest boards for truck design inspiration.

#### Recipes, Reading & Media

- **OpenLibrary** (`openlibrary-api`): Looks up cookbooks and food writing to track down, with titles saved to a reading list in Notion.
- **Spotify** (`spotify-api`): The kitchen prep playlist and his running mixes of rock, hip-hop, indie, and jazz, synced with Strava running sessions.
- **YouTube** (`youtube-api`): Technique tutorials, knife skills, and food truck build-out videos he saves, with key takeaways bookmarked to Obsidian notes.
- **TMDB** (`tmdb-api`): Looks up cooking competition shows and Bourdain episodes he watches on off nights, tracking what he has seen.
- **Vimeo** (`vimeo-api`): Watches chef talks and technique shorts, with inspiration clips saved alongside Pinterest boards.
- **Pinterest** (`pinterest-api`): Saves plating ideas, taco and torta concepts, and food truck design inspiration, feeding into Figma mockups for the truck.
- **Reddit** (`reddit-api`): Reads cheftalk, food truck, and fermentation communities when researching a problem, with useful threads bookmarked to Obsidian.
- **NASA** (`nasa-api`): Looks up moon phases and night-sky photos to swap with his sister Elena via WhatsApp.

#### Maps, Weather & Local

- **Google Maps** (`google-maps-api`): Directions to suppliers, the commissary kitchen, festival sites, and family trips, with travel time estimates fed into Google Calendar event scheduling.
- **OpenWeather** (`openweather-api`): Morning weather before runs, pollen-heavy days that trigger his asthma alerts via Twilio, and outdoor festival planning coordinated with Eventbrite events.
- **Yelp** (`yelp-api`): Hours and reviews for Leon's, The Rusty Anchor, Millers All Day, and scouting truck spots, with promising locations pinned in Google Maps.
- **Uber** (`uber-api`): Backup ride when the Vespa is in the shop and he needs to reach work or an appointment, with ride receipts tracked against his monthly budget.
- **DoorDash** (`doordash-api`): Late-night order after a brutal close when he does not want to cook, with spending tracked in his monthly expense review.
- **Instacart** (`instacart-api`): Backup grocery delivery on a week too slammed for a Trader Joe's run, with orders synced against his grocery budget line.

#### Banking, Money & Shipping

- **Plaid** (`plaid-api`): Pulls balance snapshots from Charleston Area FCU to confirm the food truck fund before a larger purchase.
- **PayPal** (`paypal-api`): Splits a tab with Danny and receives event tip-outs, with transactions reflected in his monthly budget tracking.
- **QuickBooks** (`quickbooks-api`): Models startup costs and margins for the food truck business plan, pulling supplier costs from Airtable.
- **Xero** (`xero-api`): Keeps an alternate cost view he compares against QuickBooks for the plan, ensuring the Google Drive business plan stays accurate.
- **Square** (`square-api`): The point-of-sale he is configuring for pop-ups and the future truck, with sales data feeding into QuickBooks revenue tracking.
- **Stripe** (`stripe-api`): Sets up online ordering and deposit handling for pop-up preorders through WooCommerce, with transaction data synced to QuickBooks.
- **Coinbase** (`coinbase-api`): Holds a small starter crypto position he set up to learn the basics, tracked alongside his Alpaca brokerage view.
- **Binance** (`binance-api`): A second small crypto wallet he checks against Coinbase and Kraken price feeds.
- **Kraken** (`kraken-api`): Pulls crypto price feeds he occasionally checks against his Coinbase and Binance positions.
- **Alpaca** (`alpaca-api`): A tiny brokerage position he opened to start a retirement habit, with portfolio value checked alongside his Plaid balance snapshots.
- **UPS** (`ups-api`): Tracks care packages of dried chiles and spices from his mother and equipment orders, with delivery dates pushed to Google Calendar.
- **FedEx** (`fedex-api`): Tracks specialty ingredients and kitchen tools for menu development, with expected arrival dates synced to his prep schedule.
- **Shippo** (`shippo-api`): Generates return labels when a piece of gear does not work out, coordinating pickup scheduling with Google Calendar.
- **Amazon Seller** (`amazon-seller-api`): Lists branded merch and surplus kitchen gear he sells ahead of the truck launch, with revenue tracked in QuickBooks.

#### Events, Sourcing, Work & Fitness

- **Eventbrite** (`eventbrite-api`): Registers for food and wine festivals, pop-ups, and industry tastings around Charleston, with confirmed events pushed to Google Calendar and logistics tracked in Monday.
- **Ticketmaster** (`ticketmaster-api`): Buys concert and show tickets on a rare night off, with event dates added to Google Calendar to avoid shift conflicts.
- **Typeform** (`typeform-api`): His vendor application and intake forms for festival booths and pop-ups, with responses feeding into Asana task tracking.
- **Greenhouse** (`greenhouse-api`): Tracks kitchen openings he scouts for potential prep-team hires, coordinated with his BambooHR staffing view.
- **BambooHR** (`bamboohr-api`): Views his schedule, pay stubs, and PTO in the restaurant's HR portal, cross-referenced with Google Calendar for shift planning.
- **Gusto** (`gusto-api`): Reviews his pay records the restaurant runs through Gusto, with pay dates reflected in his monthly budget cycle.
- **MyFitnessPal** (`myfitnesspal-api`): Loosely tracks running and recovery without turning food into a number, synced with Strava run data.
- **Strava** (`strava-api`): Logs the Battery waterfront runs two to three mornings a week, with run data shared to MyFitnessPal and playlists pulled from Spotify.

#### Files, Photos & Design

- **Google Drive** (`google-drive-api`): Stores the food truck business plan, recipe notes, supplier lists, and menu drafts, serving as the central document hub linked from Notion, Asana, and Trello.
- **Dropbox** (`dropbox-api`): A shared folder where festival organizers drop vendor packets and floor plans, with key documents cross-referenced in Monday event logistics.
- **Box** (`box-api`): Where Linden & Rye keeps recipe standards and allergen sheets he references during Confluence procedure updates.
- **Figma** (`figma-api`): Reviews and comments on the food truck logo and menu board a designer friend mocked up, with final assets linked to the Webflow landing page.
- **DocuSign** (`docusign-api`): E-signs leases, insurance, and supplier forms, with signed documents archived to Google Drive.
- **Google Classroom** (`google-classroom-api`): Follows a small-food-operations business course he enrolled in, with key takeaways applied to his Asana food truck launch milestones.

#### Productivity & Planning

- **Notion** (`notion-api`): The shared food truck brainstorm space he and Danny build out, linking to Google Drive docs and Asana milestones.
- **Obsidian** (`obsidian-api`): A linked vault of recipe ideas and fermentation notes, with technique threads saved from Reddit, YouTube, and Discord.
- **Asana** (`asana-api`): His food truck launch-milestone task board, with milestones cross-referenced to Jira permitting steps and Google Drive deliverables.
- **Trello** (`trello-api`): The menu-development board for seasonal dishes like the smoked duck taco, with cost data pulled from Airtable ingredient tables.
- **Monday** (`monday-api`): Tracks pop-up event logistics with the vendor collective, synced with Eventbrite registrations and Slack coordination.
- **Linear** (`linear-api`): A lightweight punch list for food truck website tasks, coordinated with the GitLab codebase and Webflow landing page.
- **Jira** (`jira-api`): Tracks build-out and permitting steps with the truck consultant, with follow-up actions from Zoom calls logged here.
- **Confluence** (`confluence-api`): Documents his prep standards and recipe procedures, drawing from Box allergen sheets and Obsidian recipe experiments.
- **Airtable** (`airtable-api`): The supplier and ingredient cost table for menu and truck planning, feeding cost data into QuickBooks and Trello menu boards.

#### Storefront, Marketing & Analytics

- **WordPress** (`wordpress-api`): Runs his recipe and food truck progress blog, with traffic tracked by Google Analytics and PostHog.
- **Webflow** (`webflow-api`): Builds the landing page for the future food truck, with content managed through Contentful and search powered by Algolia.
- **Contentful** (`contentful-api`): Manages the content blocks for the truck site's menu pages, deployed to the Webflow landing page.
- **BigCommerce** (`bigcommerce-api`): Sets up the merch store for branded truck goods, with inventory synced from Amazon Seller listings.
- **WooCommerce** (`woocommerce-api`): Powers a ticketed pop-up dinner page he sells through, with payments processed via Stripe.
- **Etsy** (`etsy-api`): Sources handmade aprons, knife rolls, and signage, and lists his own designs with shipments tracked through Shippo.
- **Klaviyo** (`klaviyo-api`): Sends segmented updates to his pop-up dinner subscribers, with engagement data flowing into Mixpanel funnel tracking.
- **ActiveCampaign** (`activecampaign-api`): Automates the food truck interest-list follow-ups, working alongside Mailchimp subscriber data.
- **HubSpot** (`hubspot-api`): Tracks supplier and catering-lead relationships for the truck, fed by Mailchimp subscriber imports and Salesforce pipeline data.
- **Salesforce** (`salesforce-api`): Manages the catering inquiry pipeline he is building, with leads synced to HubSpot for relationship tracking.
- **Segment** (`segment-api`): Routes truck-site events from Webflow into Amplitude, Mixpanel, and Google Analytics.
- **Amplitude** (`amplitude-api`): Reviews engagement on the truck preorder page, with event data routed through Segment.
- **PostHog** (`posthog-api`): Watches self-hosted usage data on his WordPress recipe blog, providing an independent analytics view.
- **Mixpanel** (`mixpanel-api`): Tracks the pop-up signup funnel, with events flowing from Segment and subscriber actions from Klaviyo.
- **Google Analytics** (`google-analytics-api`): Watches traffic to the food truck site and blog, with events routed through Segment alongside Amplitude.

#### Web Infrastructure & Support

- **GitHub** (`github-api`): Pulls open-source menu and ordering templates a developer friend points him to, feeding into the GitLab truck-site codebase.
- **GitLab** (`gitlab-api`): Hosts the truck-site code a developer friend maintains, with deployments served through Cloudflare and monitored by Datadog.
- **Cloudflare** (`cloudflare-api`): Manages DNS and caching for the food truck domain, serving the Webflow landing page and WordPress blog.
- **Algolia** (`algolia-api`): Powers menu and recipe search on the truck site, indexing content managed in Contentful.
- **Okta** (`okta-api`): Single sign-on across the tools the vendor collective shares, including Slack, Monday, and Dropbox.
- **ServiceNow** (`servicenow-api`): Files facility requests through the commissary kitchen's portal, with request status tracked in Jira.
- **PagerDuty** (`pagerduty-api`): Alerts him via Twilio if the truck preorder site goes down during a pop-up, triggered by Datadog monitors.
- **Datadog** (`datadog-api`): Monitors uptime on the truck site and blog, feeding alerts into PagerDuty and error data into Sentry.
- **Sentry** (`sentry-api`): Catches errors on the preorder and menu pages, with issues linked to the GitLab codebase for the developer friend to fix.
- **Kubernetes** (`kubernetes-api`): Monitors the cluster where the developer friend hosts the food truck site, with health data feeding into Datadog dashboards.
- **Zendesk** (`zendesk-api`): Files support tickets with his phone and software providers, tracking resolution alongside his ServiceNow requests.
- **Freshdesk** (`freshdesk-api`): Submits warranty claims for appliances and kitchen gear, with claim status tracked to completion.
- **Intercom** (`intercom-api`): Uses website chat for help on supplier and equipment sites, with conversation history accessible for follow-up.

#### Travel, Home & Social

- **Airbnb** (`airbnb-api`): Books the occasional weekend away with Willa on a rare double day off, with trip dates synced to Google Calendar.
- **Amadeus** (`amadeus-api`): Looks up flights for trips to see family in Houston and Austin, with booking confirmations pushed to Google Calendar and Gmail.
- **Zillow** (`zillow-api`): Eyes Charleston commercial and commissary spaces for the truck, with promising listings saved to the Notion food truck brainstorm.
- **Ring** (`ring-api`): Watches the building's shared entry camera at the studio, with motion alerts coordinated around his work schedule.
- **Instagram** (`instagram-api`): Drafts captions and food photos for @daniel.cooks; he reviews before posting, with content ideas drawn from Pinterest boards.
- **Twitter** (`twitter-api`): Follows Charleston food media; the agent drafts posts for review, coordinated with Instagram content for consistent messaging.
- **LinkedIn** (`linkedin-api`): A lean profile he checks when an industry contact reaches out, with connection requests cross-referenced against his Greenhouse scouting.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. The agent works only from connected services and stored memory.
- The 7shifts restaurant scheduling app is a phone app he uses separately; the agent helps him plan around shifts but cannot read or change them.
- Charleston Area FCU banking is handled on his phone only; the agent never moves money or logs in on his behalf.
- The Discover card app is on his phone and outside the agent's reach.
- His physical mail, in-person kitchen work, and anything on the line are outside the agent's reach.
