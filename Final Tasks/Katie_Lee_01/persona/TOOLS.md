# Tools: Katie Lee

## Tool Usage

### Connected Services

#### Mail, Calendar & Document Operations
- **Gmail** (`gmail-api`): Personal Gmail at katie.lee@voissync.ai. Family, school, CPA, Korean community, financial accounts. Brigham and HMS inboxes are draft-only and handed off.
- **Outlook** (`outlook-api`): Drafts replies to Dr. Hartwell and the clerkship admin team for her Brigham (klee@bwh.harvard.edu) and HMS (katie_lee@hms.harvard.edu) threads, then hands the finished drafts off for her to send from the institutional side.
- **Google Calendar** (`google-calendar-api`): The family source of truth. Clinical schedule, OR blocks, HMS lectures, kids' school and activities, Jung-hee's appointments, Sunday cooking holds.
- **Google Drive** (`google-drive-api`): HMS lecture decks, SMFM abstract drafts, financial documents, family photos, and hanbok patterns.
- **Notion** (`notion-api`): Curriculum drafting workspace for the health equity module with Dr. Miyamoto. Personal CME tracker.
- **Obsidian** (`obsidian-api`): Long-form research notes on maternal mortality disparities. Local-only vault, careful with sync.
- **Dropbox** (`dropbox-api`): Backup of HMS lecture media and Jung-hee's medical records scans.
- **Box** (`box-api`): Pulls the shared HMS curriculum committee files she needs to keep the health equity module in step with the committee's latest drafts.
- **Airtable** (`airtable-api`): Community Health Fair planning base for the Korean American Community Center. Volunteer rota, supply list, education station scripts.
- **DocuSign** (`docusign-api`): Household paperwork, school forms, insurance renewals, CPA returns. Confirm before signing anything financial.
- **Calendly** (`calendly-api`): External meeting booking for HMS mentees and Korean community organizers. Block around L&D call.
- **Typeform** (`typeform-api`): Intake forms for community health workshops at the Korean American Community Center.

#### Messaging, Voice & Notifications
- **Slack** (`slack-api`): Pulls the Korean-American physicians DM thread and the HMS curriculum channel each morning so she can flag anything that needs a reply to Dr. Miyamoto before her first OR case.
- **Microsoft Teams** (`microsoft-teams-api`): Checks David's HubSpot meeting blocks against the family calendar so she knows which Tuesday and Thursday WFH windows are clear for him to drive Jung-hee to PT.
- **WhatsApp** (`whatsapp-api`): The Wellesley friends group and a small residency cohort thread. Quiet check-ins, no broadcast.
- **Telegram** (`telegram-api`): Tracks the Korean diaspora maternal health working group, surfacing threads that feed her SMFM abstract on immigrant maternal health outcomes and the community fair counseling station.
- **Discord** (`discord-api`): Follows Minjun's school robotics club server, catching meeting-time changes and posting them onto the family calendar before they clash with soccer.
- **Zoom** (`zoom-api`): HMS lectures when remote, SMFM committee calls, and occasional telehealth coordination calls for Jung-hee.
- **Twilio** (`twilio-api`): Confirms that the SMS reminders for Jung-hee's rheumatology and PT appointments actually went out, so a missed text never turns into a missed visit with Dr. Park.
- **SendGrid** (`sendgrid-api`): Transactional email routing for the community health fair sign-up form. Confirm before any blast.
- **Mailgun** (`mailgun-api`): Backup transactional sender for community center mailings. Same caution as SendGrid.
- **Intercom** (`intercom-api`): Watches the support inbox of the HMS academic tool that hosts her clerkship slides and flags outages before a lecture so she can switch to the Drive backup in time.

#### Kids, School & Learning Media
- **Google Classroom** (`google-classroom-api`): Minjun's third-grade classroom and the kindergarten bridge for Seoyeon. Track assignments, permission slips, class news.
- **OpenLibrary** (`openlibrary-api`): Children's reading queue with bilingual Korean and English picks. Reservations bridged through the Brookline library system.
- **NASA** (`nasa-api`): Astronomy picture of the day and shuttle imagery for Minjun's current space phase.
- **YouTube** (`youtube-api`): K-pop choreography for Seoyeon's dance practice, cooking channels for Sunday menu planning, and Minjun's animation watchlist.
- **Twitch** (`twitch-api`): Keeps tabs on the channels Minjun is starting to follow so she can ask him about them at dinner and clear them against what is age-appropriate.
- **Vimeo** (`vimeo-api`): HMS guest lecture archive and recital footage from the Dance Complex.
- **Figma** (`figma-api`): Seoyeon's beginner storyboarding for school projects and Katie's lecture slide layouts shared with Dr. Miyamoto.

#### Home, Health, Weather & Delivery Logistics
- **MyFitnessPal** (`myfitnesspal-api`): Iron-aware meal logging during low-hemoglobin weeks. Consistency only, no calorie pressure.
- **Strava** (`strava-api`): Muddy River runs when the plantar fasciitis cooperates. Private to her account, do not auto-post.
- **Ring** (`ring-api`): Front door camera and motion alerts. Quiet during overnight call so notifications do not stack on the post-call recovery day.
- **OpenWeather** (`openweather-api`): School delay forecasting, Muddy River run conditions, and snow-day prep for the November through March stretch.
- **Yelp** (`yelp-api`): Family dinner scouting around Brookline, Oleana confirmation, and vetting new Korean spots before recommending.
- **DoorDash** (`doordash-api`): Post-call recovery dinners only. Confirm before placing.
- **Instacart** (`instacart-api`): Whole Foods and Costco runs on heavy clinic weeks. H-Mart in Cambridge stays in-person by her preference.
- **FedEx** (`fedex-api`): Tracking lecture materials shipped between Brigham and HMS, plus packages from Daniel's family in Silver Spring.
- **UPS** (`ups-api`): Tracking and rerouting for Vanguard and Fidelity paperwork, plus fabric orders for hanbok projects.
- **Shippo** (`shippo-api`): Return label generation for clothing and book orders, plus community fair supply shipments.
- **Zillow** (`zillow-api`): Tracks the Brookline Victorian's valuation against the roughly $620,000 mortgage balance so she can judge whether the home equity supports retiring the medical school loan faster.

#### Travel, Maps, Events & Tickets
- **Google Maps** (`google-maps-api`): Brigham commute, Jung-hee's PT runs, Florida Ruffin Ridley School and soccer field routing, H-Mart trips.
- **Uber** (`uber-api`): Backup for Jung-hee's appointments when David cannot drive and Katie is on L&D call. Default to UberX.
- **Amadeus** (`amadeus-api`): The two-week Seoul trip she has been planning. Multi-city fare watches including ICN connections.
- **Airbnb** (`airbnb-api`): Rental search in her mother's old Seoul neighborhood, plus visiting-family lodging for Daniel's clan.
- **Ticketmaster** (`ticketmaster-api`): Park Hyo-shin tour alerts and occasional Boston family-friendly shows.
- **Eventbrite** (`eventbrite-api`): Korean American Community Center events, maternal health conferences, and HMS academic events.

#### Family Finance, Banking & Tax
- **Plaid** (`plaid-api`): Aggregates Chase checking, the Marcus HYSA, Fidelity, Vanguard, and Laurel Road into one view she reads during the monthly budget review to track the loan-payoff surplus.
- **QuickBooks** (`quickbooks-api`): HMS 1099 income tracking and the quarterly estimated tax workbook shared with Andrew Cho.
- **Xero** (`xero-api`): Reconciles the Korean American Community Center ledger whenever she covers for the treasurer, matching fair donations against supply spending for Hye-jin.
- **Stripe** (`stripe-api`): Reconciles online donations to the Korean American Community Center fundraiser pages so the totals match the figures she reports to Hye-jin.
- **PayPal** (`paypal-api`): Small reimbursements among Wellesley friends and occasional Etsy seller payments. Confirm before sending at or above $300.
- **Square** (`square-api`): Tallies on-site donations and craft sales from the community health fair so she can close out the day's totals with Hye-jin before heading home.
- **Coinbase** (`coinbase-api`): Pulls the small residency-era balance into her monthly net-worth tally so the household budget she manages with David reflects every account.
- **Binance** (`binance-api`): Pulls market quotes so she can answer Daniel's occasional crypto questions at Thanksgiving with current numbers rather than guesses.
- **Kraken** (`kraken-api`): Cross-checks the same coin prices she sees on Coinbase so the figure in her household net-worth tally is the one she trusts.
- **Alpaca** (`alpaca-api`): Tracks live quotes for VTI, VXUS, and BND so she can sanity-check her Fidelity brokerage balance during the monthly budget review.

#### Shopping, Aesthetic & Marketplaces
- **Amazon Seller** (`amazon-seller-api`): Checks the stock and shipping status on her friend's small Korean cookware shop so she can grab the onggi and stone bowls she likes the moment they restock.
- **Etsy** (`etsy-api`): Hanbok fabric and trim sourcing, plus a regular onggi pottery seller from Seoul. Confirm before any order at or above $300.
- **BigCommerce** (`bigcommerce-api`): Watches a Korean specialty grocer's catalog for the gochugaru and anchovy stock she leans on for kimchi jjigae and the Sunday long cook.
- **WooCommerce** (`woocommerce-api`): Reorders from the independent Korean tea importer she buys from a couple of times a year, keeping her afternoon mint tea and gift stock topped up.
- **Pinterest** (`pinterest-api`): Hanbok pattern inspiration, kitchen aesthetic ideas, Lunar New Year table layouts.
- **Instagram** (`instagram-api`): Saves recipes from Korean cooking accounts, sourcing leads from hanbok artisans, and posts from the maternal health advocates whose work she cites in her talks.

#### Academic Publishing, Newsletters & Community Comms
- **LinkedIn** (`linkedin-api`): Keeps her profile and publication list current for the Clinical Assistant Professor application Dr. Hartwell is backing, and tracks the academic contacts she may need as references.
- **WordPress** (`wordpress-api`): The Korean American Community Center site, where she contributes maternal health posts.
- **Mailchimp** (`mailchimp-api`): The community center newsletter to Korean immigrant families. Drafts only, Hye-jin sends.
- **Contentful** (`contentful-api`): Health equity module content for HMS, staged before publish.
- **Webflow** (`webflow-api`): Reviews the community fair landing page Hye-jin maintains, checking the OB/GYN booth hours and prenatal counseling details for accuracy before each year's fair goes live.
- **Algolia** (`algolia-api`): Searches the community center resource library to pull the right Korean-language maternal health handouts for her workshops and the prenatal counseling station.

#### David's Workplace SaaS (HubSpot Orbit)
- **HubSpot** (`hubspot-api`): Reads David's campaign deadlines so she can borrow the same workflow tactics for the community fair email push and warn him when a launch week collides with her L&D call.
- **Salesforce** (`salesforce-api`): Pulls the contact and pipeline views David references so she can adapt their structure for tracking community fair volunteers and donors in the planning base.
- **Klaviyo** (`klaviyo-api`): Studies the email segmentation patterns David's team uses so she can sharpen how the community center reaches Korean immigrant families with maternal health news.
- **ActiveCampaign** (`activecampaign-api`): Maps out the workshop sign-up reminder automations she wants to set up for the Korean American Community Center intake flow.
- **Segment** (`segment-api`): Traces how the community center site forwards sign-up events to the newsletter list so registrations from the fair page land where Hye-jin expects them.
- **Amplitude** (`amplitude-api`): Reviews which community center workshop pages families actually open so she can prioritize the maternal health topics that draw the most interest.
- **Mixpanel** (`mixpanel-api`): Checks how far readers get through her maternal health posts on the community center site so she knows which to expand for the next health fair.
- **PostHog** (`posthog-api`): Reviews funnel data on the community fair sign-up flow to find where registrants drop off and fix the step before the next event.
- **Google Analytics** (`google-analytics-api`): Reviews community center site traffic to see which maternal health pages draw families and time her fair sign-up posts accordingly.
- **Zendesk** (`zendesk-api`): Triages the help requests families send through the community center contact form so questions about prenatal services reach her or Hye-jin quickly.
- **Freshdesk** (`freshdesk-api`): Handles the overflow ticket queue for the community center workshops, tagging maternal health questions so none sit unanswered before a session.
- **BambooHR** (`bamboohr-api`): Checks David's approved HubSpot PTO so she can line up family Seoul-trip dates and school-break childcare around his time off.
- **Greenhouse** (`greenhouse-api`): Tracks the HMS fellowship hiring pipeline she helps screen for, flagging candidates whose work touches maternal health disparities.
- **Gusto** (`gusto-api`): Checks community center contractor payroll runs on Hye-jin's behalf, confirming each cycle posts correctly when she is covering the books.
- **Linear** (`linear-api`): Tracks the open items on the health equity module build with Dr. Miyamoto so curriculum tasks do not slip between her OR weeks.
- **Jira** (`jira-api`): Follows the HMS computational health collaborator's project tickets so she knows when the data she needs for the SMFM abstract analysis is ready.
- **Confluence** (`confluence-api`): Reads the HMS curriculum committee's shared documentation to keep the health equity module aligned with the clerkship's published standards.
- **Monday** (`monday-api`): Runs the timeline for the annual November health fair, sequencing volunteer rota, supplies, and station setup so nothing stacks onto her clinic weeks.
- **Asana** (`asana-api`): Tracks the HMS clerkship admin board so she stays ahead of her six lecture dates, simulation lab sessions, and student mentoring handoffs.
- **Trello** (`trello-api`): The Korean American Community Center event board. Read and write for fair logistics.

#### Engineering & IT Awareness (Low Touch)
- **GitHub** (`github-api`): Follows Minjun's first repo and Daniel's open-source side work, noting his latest commits so she has something specific to ask Minjun about at Sunday dinner.
- **GitLab** (`gitlab-api`): Pulls the analysis code her HMS computational health collaborator commits so she can review the maternal-outcomes figures going into the SMFM abstract.
- **Sentry** (`sentry-api`): Watches for errors on the community center site so a broken fair sign-up form gets reported to Hye-jin before families hit it.
- **Datadog** (`datadog-api`): Monitors community center site uptime so she gets a heads-up if the workshop registration page goes down during a sign-up push.
- **Okta** (`okta-api`): Manages her single sign-on access to the HMS academic tools, so a clerkship lecture login never fails on her the morning of a session.
- **Cloudflare** (`cloudflare-api`): Manages the community center's DNS and caching so the fair landing page loads fast and stays reachable during the November registration rush.
- **Kubernetes** (`kubernetes-api`): Checks the status of the HMS research computing cluster that runs her maternal-outcomes data jobs so she knows when results will be ready.
- **PagerDuty** (`pagerduty-api`): Mirrors her L&D call rotation into an alert schedule so the family calendar and David always know which nights she is unreachable.
- **ServiceNow** (`servicenow-api`): Files and tracks the HMS IT tickets she needs for lecture-room AV and academic-tool access ahead of her clerkship sessions.

#### Streaming, Reading & Cultural Media
- **Spotify** (`spotify-api`): Korean ballads in the kitchen, Park Hyo-shin on the drive home, K-pop in the car with Seoyeon.
- **TMDB** (`tmdb-api`): Looks up episode counts and ratings to plan "The Diplomat" watch nights with David and vet new titles for the kids' Disney+ queue.
- **Reddit** (`reddit-api`): Mines Korean cooking subreddits for kimchi jjigae and banchan ideas and follows a maternal-fetal medicine thread for cases worth raising with Dr. Oh.
- **Twitter** (`twitter-api`): Tracks maternal health policy news and a small set of OB/GYN researchers, saving threads that inform her disparities scholarship and clerkship lectures.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from connected services and stored memory.
- Brigham and Women's Hospital internal systems (Epic, PACS, internal directories) are not connected. Draft only and hand off.
- Harvard Medical School internal systems (HMS Outlook, internal academic portals) are not connected. Draft only and hand off.
- Patient information of any form, from any system, is out of scope. HIPAA is absolute.
- David's HubSpot work accounts and Daniel's accounting client data are not connected.
- Jung-hee's private correspondence with Ji-young and the extended family in Seoul is off limits unless Jung-hee or Katie asks directly.
