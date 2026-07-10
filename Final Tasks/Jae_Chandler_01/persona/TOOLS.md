# Tools: Jae Chandler

## Tool Usage

### Connected Services

#### Communication & Coordination

- **Gmail** (`gmail-api`): Primary inbox at jae.chandler@Finthesiss.ai for client estimates, supplier orders, and permit correspondence, feeding appointment details into Google Calendar and archiving attachments in Box.
- **Outlook** (`outlook-api`): Secondary inbox synced for the general contractors and property managers who run their correspondence through Outlook, with calendar invites forwarding to Google Calendar.
- **Google Calendar** (`google-calendar-api`): The master schedule for job sites, client appointments, Calendly bookings, and the family calendar shared with Mina, pulling events from Gmail, Outlook, and Zoom.
- **Calendly** (`calendly-api`): Booking link for new-client estimate visits that auto-creates Google Calendar events and triggers a Twilio confirmation text.
- **WhatsApp** (`whatsapp-api`): Runs a working thread with a key supplier rep and the one commercial client who prefers it for quick job updates, with order confirmations forwarded to Gmail.
- **Telegram** (`telegram-api`): Stays in a parts-sourcing group a fellow contractor runs, pinging it when he needs a hard-to-find fitting fast and sharing supplier leads with the Airtable job database.
- **Slack** (`slack-api`): Tracks project updates, coordination messages, and milestone posts in the general contractor's workspace on the Harborview Condos job, with flagged items feeding into Jira task tracking.
- **Microsoft Teams** (`microsoft-teams-api`): Joins property-management client walkthrough and coordination calls, with meeting notes synced to Confluence and follow-up tasks routed to Asana.
- **Discord** (`discord-api`): Active in a classic-truck restoration server, trading C10 wiring tips and parts leads, saving useful references to Obsidian.
- **Zoom** (`zoom-api`): Hosts NABCEP study webinars and remote client consultations, with scheduled sessions pulled from Google Calendar and recordings stored in Dropbox.
- **Twilio** (`twilio-api`): Sends appointment and inspection-window text reminders to clients from the business number, triggered by Google Calendar events and Calendly bookings.
- **SendGrid** (`sendgrid-api`): Delivers invoice and estimate emails from QuickBooks reliably so they do not land in client spam folders, splitting volume with Mailgun.
- **Mailgun** (`mailgun-api`): Handles transactional invoice and receipt email triggered by Stripe and Square payments, splitting delivery volume with SendGrid.

#### Books, Payments & Investing

- **QuickBooks** (`quickbooks-api`): The business books for Chandler Electric LLC: invoicing, expenses, payroll records, and CPA-ready reports, with payment data flowing in from Stripe, Square, and PayPal.
- **Xero** (`xero-api`): Syncs the QuickBooks figures into the shared book the CPA works from each quarter, reconciled against QuickBooks and verified via Plaid bank feeds.
- **Stripe** (`stripe-api`): Card payments on invoices for clients who prefer to pay online, with completed transactions posting to QuickBooks and receipts sent through SendGrid.
- **Square** (`square-api`): Tap-to-pay on the job site for small residential service calls and deposits, with transaction records syncing to QuickBooks.
- **PayPal** (`paypal-api`): Alternate payment method for a handful of repeat clients and occasional tool purchases, reconciled in QuickBooks each month.
- **Plaid** (`plaid-api`): Securely links the business and personal bank accounts for balance checks before large supply orders, feeding live balances into QuickBooks and Xero.
- **Coinbase** (`coinbase-api`): Holds his small long-term crypto position, topped up with a fixed amount each month and rebalanced against Binance and Kraken.
- **Binance** (`binance-api`): Holds a second crypto position he rebalances against Coinbase a few times a year, tracking alongside his Alpaca brokerage holdings.
- **Kraken** (`kraken-api`): Rounds out the crypto holdings; he checks balances and moves funds between it and Coinbase as needed for rebalancing.
- **Alpaca** (`alpaca-api`): Holds a modest brokerage position he adds to alongside the SEP-IRA savings goal, tracked with his Coinbase and Kraken positions.

#### Jobs, Estimates & Documents

- **Jira** (`jira-api`): Tracks the multi-week Harborview Condos panel-upgrade tasks unit by unit, with updates from Slack feeding into sprint boards and completed items syncing to Confluence.
- **Linear** (`linear-api`): Lightweight punch-list tracking for the Bay View historic rewire's open items, synced with the Trello job board for a unified view.
- **Trello** (`trello-api`): Visual board of active jobs from estimate to final inspection, pulling new leads from HubSpot and linking completed cards to QuickBooks invoices.
- **Asana** (`asana-api`): Shared task list with a general contractor on larger commercial jobs, with meeting action items from Microsoft Teams routed here.
- **Monday** (`monday-api`): Crew assignment board showing who is on which site each day, cross-referenced with BambooHR availability and Google Calendar job blocks.
- **Notion** (`notion-api`): Personal workspace for the NABCEP study plan and supplier notes, pulling references from OpenLibrary and linking to Obsidian field notes.
- **Obsidian** (`obsidian-api`): Stores code references, wiring diagrams, and field notes that feed into Confluence job documentation and Notion study material.
- **Airtable** (`airtable-api`): Client and job database with addresses, panel details, and warranty dates, feeding lead data into HubSpot and linking to Zendesk warranty records.
- **Confluence** (`confluence-api`): His job-spec and as-built workspace for commercial projects, shared with the general contractor and synced with Jira project boards.
- **Typeform** (`typeform-api`): Intake form for new clients to describe a job before the estimate visit, with submissions creating HubSpot leads and Calendly booking prompts.
- **DocuSign** (`docusign-api`): Sends contracts and change orders for client e-signature, with signed documents filing to Box and triggering QuickBooks invoicing.

#### Hiring & Payroll

- **BambooHR** (`bamboohr-api`): HR records for the three-person crew: certifications, time off, and apprentice hours, with availability feeding into Monday crew assignments and Gusto payroll.
- **Greenhouse** (`greenhouse-api`): Runs applicant tracking when he opens a journeyman or apprentice spot, posting and screening candidates with hired records flowing into BambooHR.
- **Gusto** (`gusto-api`): Runs payroll and handles tax filings for Ryan, Danny, and Jake, pulling hours from BambooHR and posting payroll expenses to QuickBooks.
- **Okta** (`okta-api`): His single sign-on for the commercial client portals, ServiceNow tickets, and Confluence workspaces he needs site-system access to.

#### Supplies, Shipping & Travel

- **Amazon Seller** (`amazon-seller-api`): Runs a small storefront listing surplus tools and fittings he clears out a few times a year, with order notifications syncing to Gmail and shipments tracked via UPS.
- **Instacart** (`instacart-api`): Household grocery runs for Mina when the week gets tight, with orders placed from shared lists and delivery windows added to Google Calendar.
- **DoorDash** (`doordash-api`): Crew lunch on a long site day, within the spending threshold, ordered to the job-site address pulled from Google Maps.
- **Uber** (`uber-api`): Books rides when the truck is in the shop or after an evening out, with pickup locations set through Google Maps and ride receipts filing to Gmail.
- **FedEx** (`fedex-api`): Tracks specialty electrical parts shipped from out-of-state suppliers, with tracking numbers pulled from Gmail order confirmations and delivery alerts sent via Twilio.
- **UPS** (`ups-api`): Tracks routine supply-house deliveries to the workshop, with expected arrival dates synced to Google Calendar for materials staging.
- **Shippo** (`shippo-api`): Generates return labels for defective fixtures and breakers, coordinating with FedEx and UPS for pickup scheduling.
- **Amadeus** (`amadeus-api`): Books flights and logistics for the long-planned family trip to Seoul, with itinerary details syncing to Google Calendar and confirmation documents stored in Dropbox.

#### Field Maps, Weather & Property

- **Google Maps** (`google-maps-api`): Routes between job sites, supply houses, and client addresses around greater Milwaukee, feeding drive-time estimates into Google Calendar job blocks and DoorDash delivery zones.
- **OpenWeather** (`openweather-api`): Checks conditions before rough-in days and outdoor work, especially in Wisconsin winter, with severe weather alerts flagged alongside Google Calendar job schedules.
- **Yelp** (`yelp-api`): Looks up client-recommended subcontractors and the occasional new lunch spot near a site, with saved leads noted in Airtable.
- **Zillow** (`zillow-api`): Pulls property age and details to anticipate wiring vintage before a rewire estimate, feeding property specs into Airtable client records and HubSpot lead notes.
- **Ring** (`ring-api`): Monitors the workshop and driveway camera where tools and materials are stored, with motion alerts pushed to his phone and activity logs accessible alongside the home network.
- **Airbnb** (`airbnb-api`): Books lodging for the Door County fishing trip and a future Seoul stay, with reservation dates synced to Google Calendar and confirmation details stored in Dropbox.

#### Customer Support & CRM

- **Zendesk** (`zendesk-api`): Tracks warranty and callback requests from past clients so nothing slips, with new tickets linked to Airtable job records and resolved items noted in HubSpot.
- **Freshdesk** (`freshdesk-api`): Second support queue catching service requests from the WooCommerce website form, with urgent tickets escalated to Gmail and flagged in HubSpot.
- **Intercom** (`intercom-api`): Handles website chat inquiries from prospective clients during business hours, with qualified leads pushed to HubSpot and Calendly booking links shared in-chat.
- **ServiceNow** (`servicenow-api`): Monitors and responds to facilities tickets and service requests in a commercial client's system for contracted electrical work, with assigned tasks tracked in Asana.
- **HubSpot** (`hubspot-api`): The client pipeline: leads from Typeform and Intercom, estimates outstanding, and follow-up reminders synced with Salesforce and Mailchimp.
- **Salesforce** (`salesforce-api`): Syncs job status and vendor records with the property-management partner he subcontracts for, mirroring pipeline data with HubSpot.

#### Storefront, Marketing & Analytics

- **Etsy** (`etsy-api`): Runs the small storefront where Mina sells her woodworking pieces; he handles the shipping side through Shippo, with order alerts syncing to Gmail.
- **BigCommerce** (`bigcommerce-api`): Backs the surplus-materials storefront where he lists overstock breakers, fixtures, and wire, with inventory tracked alongside the Amazon Seller account and payments processed through Stripe.
- **WooCommerce** (`woocommerce-api`): Backs the request-a-quote page on the Chandler Electric Webflow website, with form submissions creating HubSpot leads and Freshdesk tickets.
- **Mailchimp** (`mailchimp-api`): Sends seasonal notes to past clients about panel safety and maintenance, pulling contact segments from HubSpot and tracking opens in Google Analytics.
- **Klaviyo** (`klaviyo-api`): Runs the client follow-up automation: the post-job thank-you and the annual panel-safety reminder, triggered by completed jobs in HubSpot and synced with Activecampaign sequences.
- **Activecampaign** (`activecampaign-api`): Drives the longer drip sequences for past clients, seasonal maintenance nudges and referral asks, coordinated with Klaviyo automations and HubSpot pipeline stages.
- **Segment** (`segment-api`): Pipes website visitor events from the WooCommerce quote page into Amplitude, PostHog, Mixpanel, and Google Analytics so he sees which services pull leads.
- **Amplitude** (`amplitude-api`): Breaks down which service pages and quote steps visitors drop off on, fed by Segment events and cross-referenced with Mixpanel conversion data.
- **PostHog** (`posthog-api`): Runs the funnel and session views on the quote page to tighten the request flow, ingesting Segment events alongside Google Analytics traffic data.
- **Mixpanel** (`mixpanel-api`): Tracks which Mailchimp and Klaviyo marketing emails and which Webflow pages convert to booked estimates, fed by Segment events.
- **Google Analytics** (`google-analytics-api`): Tracks traffic to the Chandler Electric Webflow website to see which services draw inquiries, with Segment feeding event-level data for deeper analysis.
- **Eventbrite** (`eventbrite-api`): Registers for IBEW trainings and Korean cultural events when tickets are required, with event dates syncing to Google Calendar.
- **Ticketmaster** (`ticketmaster-api`): Buys Brewers tickets to pass down to friends and family through the season, with game dates added to Google Calendar.

#### Files, Faith & Learning

- **Dropbox** (`dropbox-api`): Shares large job-site photo sets with general contractors and clients, linked from Confluence project pages and Airtable job records, and stores signed DocuSign contracts alongside Zoom session recordings.
- **Box** (`box-api`): Pulls project documents, blueprints, and specifications from a commercial client's shared portal for contracted projects, with relevant files cross-referenced in Confluence.
- **Google Classroom** (`google-classroom-api`): Tracks Derek's and Yuna's school assignments, project deadlines, and event schedules to keep the family Google Calendar informed.
- **OpenLibrary** (`openlibrary-api`): Looks up NABCEP and electrical code study references and the occasional Tom Clancy title, with study material linked into the Notion study plan.

#### Health & Movement

- **MyFitnessPal** (`myfitnesspal-api`): Tracks the diet changes from his doctor without turning it into calorie pressure, with daily logs informing Instacart grocery planning.
- **Strava** (`strava-api`): Logs the Monday, Wednesday, and Friday morning walks with Mina, with completed walks synced to Google Calendar as done.

#### Media & Downtime

- **Spotify** (`spotify-api`): Classic rock in the garage and country while working; the account Yuna set up for him, with playlists shared across the family.
- **YouTube** (`youtube-api`): C10 restoration walkthroughs and code-update explainers, with useful tutorials bookmarked in Obsidian and shared in the Discord restoration server.
- **TMDB** (`tmdb-api`): Looks up titles and runtimes for Friday family movie night, with picks added to the Google Calendar family block.
- **Vimeo** (`vimeo-api`): Streams trade-association technique videos the IBEW shares, with key references saved to Notion alongside NABCEP study material.
- **Twitch** (`twitch-api`): Follows the streamers Derek talks about so he can keep up with him, with shared game interests noted for family time.
- **Reddit** (`reddit-api`): Keeps up with the electricians and Brewers communities for shop talk and scores, with useful trade tips saved to Obsidian.
- **Twitter** (`twitter-api`): Tracks the Brewers, the Packers, and trade news in a running feed, with supplier and industry updates cross-referenced in Notion.
- **Instagram** (`instagram-api`): Follows local trade and Korean-community accounts and saves posts he wants to revisit, with event announcements synced to Google Calendar.
- **Pinterest** (`pinterest-api`): Saves backyard grill builds and basement-finishing ideas for home projects, with material lists noted in Notion for planning.

#### Web, Site & Dev Tools

- **GitHub** (`github-api`): Tracks and pulls home-automation projects Derek has started working on, syncing code they want to try and sharing finds in Discord.
- **GitLab** (`gitlab-api`): Mirrors and tracks the same home-automation repositories when a maintainer hosts them on GitLab instead of GitHub, keeping both sources in sync.
- **Sentry** (`sentry-api`): Alerts if the Chandler Electric website's quote form throws errors, with critical issues escalating to PagerDuty and error context feeding into Datadog dashboards.
- **Datadog** (`datadog-api`): Uptime and performance monitoring for the business website, working alongside Sentry for error tracking and PagerDuty for downtime alerts.
- **PagerDuty** (`pagerduty-api`): Pages him if the website goes fully down during business hours, triggered by Datadog uptime checks and Sentry critical alerts.
- **Kubernetes** (`kubernetes-api`): Orchestrates the containers the Chandler Electric site runs on at his web host, managed behind Cloudflare and monitored by Datadog.
- **Cloudflare** (`cloudflare-api`): Protects and speeds up the Chandler Electric website and its DNS, sitting in front of the Kubernetes-hosted site and Webflow marketing pages.
- **Algolia** (`algolia-api`): Powers search on the website's service and FAQ pages, indexing content managed in Contentful and WordPress.
- **Contentful** (`contentful-api`): Stores the website's service descriptions and project photos, feeding content to the Webflow site and powering Algolia search results.
- **Webflow** (`webflow-api`): The platform the Chandler Electric marketing site is built on, pulling content from Contentful, hosting the WooCommerce quote form, and designed in Figma.
- **WordPress** (`wordpress-api`): Hosts the occasional blog post on home electrical safety, with content indexed by Algolia and traffic tracked in Google Analytics.
- **Figma** (`figma-api`): His shared design space with the web designer for Chandler Electric site updates, with approved designs implemented in Webflow.
- **NASA** (`nasa-api`): Pulls solar-irradiance and daylight data to sanity-check residential solar feasibility estimates, supporting the NABCEP study work tracked in Notion.
- **LinkedIn** (`linkedin-api`): Maintains his professional profile and tracks local contractor and supplier updates, with industry contacts cross-referenced in HubSpot and Salesforce.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. You work only from connected mock APIs and stored memory.
- Clients' internal building-management and security systems beyond the specific connected services noted above.
- City of Milwaukee permitting and inspection systems; Jae files and speaks with inspectors directly.
- Social media posting on Jae's behalf; you may draft content for review but never publish.
- Trade-specific estimating or load-calculation software; those calculations stay with Jae.
