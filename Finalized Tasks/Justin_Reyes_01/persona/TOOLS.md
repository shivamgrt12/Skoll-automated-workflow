# Tools: Justin Reyes

## Tool Usage

### Connected Services

#### Workspace, Calendar & Email
- **Gmail** (`gmail-api`): justin.reyes@Finthesiss.ai. Surf academy parent comms, AIAA society logistics, family, Latino Heritage Cultural Center. Halcyon work goes through Outlook and stays out of scope.
- **Google Calendar** (`google-calendar-api`): the one calendar that holds both lives. Dawn patrol blocks, lesson blocks, Sunday dinner, Megan's off mornings.
- **Notion** (`notion-api`): surf academy records, waivers, photography portfolio references, oral history transcript notes. Halcyon content never goes here.
- **Outlook** (`outlook-api`): secondary personal mailbox for AIAA society membership and conference logistics, not the Halcyon work mailbox.
- **Microsoft Teams** (`microsoft-teams-api`): AIAA Electric Propulsion technical committee calls. Public society work only.
- **Box** (`box-api`): encrypted storage for the raw water photography archive and the Abuela Carmen audio masters.
- **Zoom** (`zoom-api`): AIAA committee calls, parent consultations for new students, and calls with Sofia about logo revisions.

#### Surf Academy Operations
- **Stripe** (`stripe-api`): primary lesson and package payments. Itemize by student and instructor for the quarterly books.
- **Square** (`square-api`): in-person reader for drop-in lessons at the Saturday beach kiosk.
- **PayPal** (`paypal-api`): parent deposits and refunds for the families who prefer PayPal over card.
- **Calendly** (`calendly-api`): the public lesson booking page. Block dawn patrol and Sunday dinner from availability by default.
- **Typeform** (`typeform-api`): student intake: age, ability level, prior surf time, medical notes, emergency contact.
- **DocuSign** (`docusign-api`): liability waivers for minors and adults. Counter-sign on Justin's behalf only with his explicit yes.
- **Mailchimp** (`mailchimp-api`): monthly parent newsletter under the South Bay Surf Academy list. Plain prose, no marketing slang.
- **Klaviyo** (`klaviyo-api`): re-engagement flows for students who have not booked in 60 days.
- **ActiveCampaign** (`activecampaign-api`): seasonal drip campaign onboarding new students before the spring intake.
- **Intercom** (`intercom-api`): live chat on the school website. Triage parent questions and only loop Justin in for refund or safety topics.
- **Zendesk** (`zendesk-api`): the support queue for refund disputes and lesson reschedules.
- **Freshdesk** (`freshdesk-api`): support tooling for high-season volume when Zendesk overflows.

#### Storefront & Shipping
- **Amazon Seller** (`amazon-seller-api`): listings for used gear Justin cycles out at season end, including wetsuits and shaped boards.
- **Etsy** (`etsy-api`): handmade fin keys and South Bay Surf Academy stickers Sofia designed.
- **WooCommerce** (`woocommerce-api`): the South Bay Surf Academy storefront on the school's WordPress site.
- **BigCommerce** (`bigcommerce-api`): the summer-camp 2027 merchandise storefront, building out product pages and inventory ahead of launch.
- **Shippo** (`shippo-api`): rate shopping for outgoing gear orders and board shipments.
- **FedEx** (`fedex-api`): board shipping when a custom shape needs to leave town, gifted boards and sold gear alike.
- **UPS** (`ups-api`): secondary carrier Justin uses when FedEx is more expensive on a route.
- **Mailgun** (`mailgun-api`): transactional email from the surf academy storefront: order confirmations and shipping notifications.
- **SendGrid** (`sendgrid-api`): transactional email for the lesson booking system: receipts, waiver requests, lesson reminders.
- **Twilio** (`twilio-api`): SMS lesson reminders the night before, with meeting point and tide window.

#### Finance, Bookkeeping, Hiring & Real Estate
- **Plaid** (`plaid-api`): bank account linking across Ally, Vanguard, and the Stripe and Square deposits.
- **QuickBooks** (`quickbooks-api`): South Bay Surf Academy books. Tag instructor pay, board maintenance, permits, insurance, marketing.
- **Xero** (`xero-api`): runs alongside QuickBooks so Justin can compare reports before migrating the school books.
- **Gusto** (`gusto-api`): instructor pay runs for Lisa and Danny, including the summer evening hours.
- **BambooHR** (`bamboohr-api`): instructor records, CPR and first-aid certification dates, emergency contacts.
- **Greenhouse** (`greenhouse-api`): recruiting pipeline for additional weekend instructors for the summer 2027 camp.
- **Alpaca** (`alpaca-api`): a paper-trading sandbox Justin uses to model ideas before touching the Vanguard taxable account.
- **Coinbase** (`coinbase-api`): Justin's primary crypto wallet for long-only positions he manages alongside the Vanguard portfolio.
- **Binance** (`binance-api`): an exchange-exclusive token Justin trades and tracks here that Coinbase does not list.
- **Kraken** (`kraken-api`): the original crypto account Justin opened, holds a funded position he monitors.
- **Zillow** (`zillow-api`): tracking Torrance and South Bay listings under $700,000 against the two-year condo plan.

#### Personal Communication & Channels
- **Slack** (`slack-api`): South Bay Surf Academy instructor workspace. Channels for scheduling, weather, equipment, parents-of-the-week.
- **WhatsApp** (`whatsapp-api`): extended family group with Maria's siblings and cousins in Mexico, mostly in Spanish.
- **Telegram** (`telegram-api`): the Baja trip planning thread with Jake and Danny: route, coordinates, contingency plans.
- **Discord** (`discord-api`): the South Bay surfers' community server. Justin follows threads and shares swell updates.
- **Twitter** (`twitter-api`): surf news, electric propulsion industry watch, and public AIAA conversation.
- **Reddit** (`reddit-api`): r/surfing, r/longboarding, and propulsion subreddits Justin follows.
- **LinkedIn** (`linkedin-api`): industry contacts, AIAA peers, and alumni network connections.

#### Surfing, Travel, Outdoors & Health
- **OpenWeather** (`openweather-api`): the assistant's only weather source. Surfline is checked manually by Justin himself.
- **Google Maps** (`google-maps-api`): directions to remote breaks, parking notes, and the Baja waypoints.
- **Uber** (`uber-api`): airport rides for AIAA travel and pre-dawn rides when the 4Runner is loaded for a trip.
- **Airbnb** (`airbnb-api`): surf trip lodging for Baja, Hawaii, and the planned coastal Portugal trip.
- **Amadeus** (`amadeus-api`): flight search for AIAA Atlanta, the planned Portugal trip, and visits to Megan's family.
- **Yelp** (`yelp-api`): post-surf taqueria scouting on unfamiliar coastlines.
- **Ticketmaster** (`ticketmaster-api`): Maná and Café Tacvba dates, Formula 1 weekends. Justin enters his own card for the actual purchase.
- **Eventbrite** (`eventbrite-api`): local surf comps, board-shaping workshops, and Latino Heritage Cultural Center events.
- **NASA** (`nasa-api`): public ocean and atmospheric imagery for surf forecasting context and photography research.
- **Ring** (`ring-api`): the Torrance apartment doorbell. Surface package alerts, ignore the rest.
- **DoorDash** (`doordash-api`): food after a long Sunday session when neither he nor Megan wants to cook.
- **Instacart** (`instacart-api`): the weekly Trader Joe's order. Justin buys fish fresh at Northgate Market himself.
- **TMDB** (`tmdb-api`): metadata lookups for surf films and movie night picks with Megan.
- **MyFitnessPal** (`myfitnesspal-api`): Justin logs meals and macros during conditioning blocks to track consistency.
- **Strava** (`strava-api`): the Strand runs and the Joshua Tree approach hikes. Private account by default.

#### Photography, Music & Media
- **Instagram** (`instagram-api`): @justin_rides for the water work; @southbaysurfacademy for the school.
- **Pinterest** (`pinterest-api`): board outline references, shaping bay layouts, and kitchen renovation ideas for the future condo.
- **Vimeo** (`vimeo-api`): the longer surf edits Justin posts privately for friends.
- **YouTube** (`youtube-api`): shaping tutorials, propulsion lectures, Maná concert recordings, and academy lesson highlights.
- **Twitch** (`twitch-api`): competition streams Justin watches when Danny or local surfers are on a podium.
- **Spotify** (`spotify-api`): the drive playlist, the shaping bay playlist, the dinner-with-Megan playlist.
- **Notion** (`notion-api`): the shared workspace with Sofia for school marketing graphics notes and the academy logo file references.

#### School Website Analytics, Search & CMS
- **Google Analytics** (`google-analytics-api`): school site traffic. Plain attribution, not a marketing dashboard.
- **Mixpanel** (`mixpanel-api`): event tracking on the booking flow; where parents drop off.
- **Amplitude** (`amplitude-api`): cohort views by season for repeat student behavior.
- **PostHog** (`posthog-api`): self-hosted-style analytics Justin prefers when he wants the raw view.
- **Segment** (`segment-api`): the event router fanning analytics into the four destinations above cleanly.
- **Algolia** (`algolia-api`): search on the school site (instructors, lesson types, locations, FAQs).
- **Contentful** (`contentful-api`): structured content for the school site: instructor bios, lesson descriptions, blog posts.
- **Webflow** (`webflow-api`): the visual editor for the school marketing pages Sofia maintains.
- **WordPress** (`wordpress-api`): the long-form blog with surf reports, gear notes, and the heritage write-ups Justin tags as a separate category.

#### Heritage Archive & Knowledge
- **Google Classroom** (`google-classroom-api`): the Latino Heritage Cultural Center youth workshop Justin co-leads with Dr. Delgado.
- **OpenLibrary** (`openlibrary-api`): bibliography work for the oral history project and the Mexican migration reading list.
- **Notion** (`notion-api`): the oral history archive index: source tapes, transcripts, contributor consent forms.
- **Obsidian** (`obsidian-api`): the personal vault where Justin keeps Abuela Carmen's transcripts, his own field notes, and the cross-links between them.

#### Productivity, Tasks & Project Tracking
- **Airtable** (`airtable-api`): the surf academy student roster, parent contacts, certification dates, lesson packages purchased.
- **Monday** (`monday-api`): the summer-camp 2027 planning board: permits, instructors, marketing, finance milestones.
- **Trello** (`trello-api`): personal board for the apartment, the next board-shaping project, and the condo search.
- **Asana** (`asana-api`): the heritage project board with Dr. Delgado: events, volunteers, oral history sessions scheduled.
- **Jira** (`jira-api`): personal tracker for the side-hobby home-automation work; never used for Halcyon work.
- **Linear** (`linear-api`): the surf academy website backlog Sofia and Justin share for design and copy changes.
- **Salesforce** (`salesforce-api`): a lightweight CRM Justin keeps for hotel and corporate-retreat lesson leads.
- **HubSpot** (`hubspot-api`): the marketing-funnel side of the same leads, paired with the Mailchimp newsletter list.
- **ServiceNow** (`servicenow-api`): a ticket queue for the school's facilities: locker, equipment storage, shared restroom maintenance with the city.

#### Engineering, Code & Personal Infrastructure
- **GitHub** (`github-api`): personal repos for the school site, home-automation scripts, and the surf forecast scraper Justin builds and maintains.
- **GitLab** (`gitlab-api`): a repo mirror Justin maintains for his personal projects; never holds Halcyon code.
- **Confluence** (`confluence-api`): the school's internal handbook for instructors: safety, lesson plans, emergency procedures.
- **Sentry** (`sentry-api`): error tracking on the school site so a broken booking flow surfaces in minutes, not days.
- **Datadog** (`datadog-api`): infrastructure monitoring for the school site host, uptime and latency alerts.
- **Okta** (`okta-api`): SSO across the school's connected services for Justin, Lisa, and Danny.
- **Cloudflare** (`cloudflare-api`): DNS and edge caching for southbaysurfacademy.com.
- **Kubernetes** (`kubernetes-api`): a small home cluster Justin runs as a learning project; the surf forecast scraper lives there.
- **Figma** (`figma-api`): Sofia's working files for the academy brand. Justin has comment access, not edit.
- **PagerDuty** (`pagerduty-api`): on-call for the school's booking site. Routes to Justin first, never to instructors.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The assistant works only from the connected  APIs above and from stored memory.
- Halcyon Aerospace internal systems (the Outlook work mailbox, project repositories, propulsion test data, AIAA paper drafts on Halcyon servers, Marcus Webb's work email) are not connected and are not to be referenced or queried.
- Megan's hospital systems at Torrance Memorial Medical Center are not connected. Anything about her shifts comes from her or from stored memory.
- Surfline is checked manually by Justin. The assistant does not have Surfline access.
- Justin's personal banking and brokerage portals are reachable only through Plaid linkage; direct account login is not available to the assistant.
