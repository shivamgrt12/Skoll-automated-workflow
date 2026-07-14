# Tools: Eric Lambert

## Tool Usage

### Connected Services

#### Communication & Messaging

- **Discord** (`discord-api`): CS study group coordination and assignment Q&A with classmates.
- **Intercom** (`intercom-api`): In-app help widget on the budget tracker. Eric reads alpha-tester conversations to spot rough edges in onboarding.
- **Microsoft Teams** (`microsoft-teams-api`): Lakeview University IT department internal channel for shift scheduling and escalations.
- **Slack** (`slack-api`): CS department workspace for project collaboration and TA office hours.
- **Telegram** (`telegram-api`): Messaging with Mateo for sharing articles and political discussion threads.
- **Twilio** (`twilio-api`): SMS reminders for medication, deadlines, and appointment alerts.
- **WhatsApp** (`whatsapp-api`): Primary family channel for Elena, Roberto, and Diego. Recipe voice notes from Mom.
- **Zoom** (`zoom-api`): Virtual office hours with Prof. Kim and remote tutoring sessions.

#### Email, Calendar & Cloud Storage

- **Gmail** (`gmail-api`): Primary email at eric.lambert@Finthesiss.ai for correspondence, job applications, and appointment confirmations.
- **Outlook** (`outlook-api`): Receives Lakeview IT department communications forwarded from university systems.
- **Google Calendar** (`google-calendar-api`): Classes, IT shifts, tutoring, therapy, exams, and social plans. Central scheduling hub.
- **Calendly** (`calendly-api`): Tutoring session booking for CS 101/102 students through the Learning Center.
- **Notion** (`notion-api`): Course notes and study guides organized by semester and subject.
- **Obsidian** (`obsidian-api`): Personal knowledge vault for CS concepts, interview prep notes, and side project documentation.
- **Google Drive** (`google-drive-api`): Class notes, project files, resume drafts, and cover letters.
- **Dropbox** (`dropbox-api`): Shared folder with Priya for apartment documents, lease copies, and grocery lists.
- **Box** (`box-api`): Shared storage at the IT help desk for shift handoffs, loaner-laptop agreements, and Eric's scan archive of textbooks he has resold.
- **SendGrid** (`sendgrid-api`): Sends the budget tracker's monthly summary email to Eric and a small alpha-test list (Priya and Mateo).
- **Mailgun** (`mailgun-api`): Transactional email backbone for the budget tracker's password-reset and verification flows during alpha testing.

#### Code, Development & Infrastructure

- **GitHub** (`github-api`): Coursework repos and the Python budget tracker project. Free student account.
- **GitLab** (`gitlab-api`): Lakeview CS department lab assignments hosted on a self-hosted instance.
- **Sentry** (`sentry-api`): Error tracking on the budget tracker, surfaces the stack traces Eric used to chase by hand.
- **Datadog** (`datadog-api`): Infrastructure monitoring dashboards accessed through the IT help desk for troubleshooting.
- **PagerDuty** (`pagerduty-api`): IT help desk escalation alerts during shifts, routing urgent tickets to senior staff.
- **Kubernetes** (`kubernetes-api`): Container orchestration for Intro to Systems coursework labs and homework deployments.
- **Cloudflare** (`cloudflare-api`): DNS and domain management for the personal portfolio site.
- **Okta** (`okta-api`): Single sign-on access for Lakeview university services through the IT help desk.
- **WordPress** (`wordpress-api`): Personal portfolio and blog for internship applications.
- **Webflow** (`webflow-api`): CS Club's recruiting microsite. Eric pushes copy updates before each new-member week.
- **Contentful** (`contentful-api`): Headless CMS backing the CS Club event page Eric helps maintain alongside the Webflow shell.
- **Algolia** (`algolia-api`): Powers the transaction-search bar on the budget tracker. Lets Eric filter by merchant, category, or amount.

#### Project Tracking & Collaboration

- **Linear** (`linear-api`): Personal task tracking for the budget tracker project and assignment deadlines.
- **Jira** (`jira-api`): IT department help desk ticketing for submitting, tracking, and resolving support requests.
- **Trello** (`trello-api`): Shared board with Mateo for planning dates and shared to-do items.
- **Asana** (`asana-api`): CS group project coordination for Intro to Systems team assignments.
- **Monday** (`monday-api`): Tutoring center schedule and session tracking through the Learning Center.
- **Airtable** (`airtable-api`): Course planning spreadsheet for requirements, electives, and graduation timeline.
- **Confluence** (`confluence-api`): IT department knowledge base for troubleshooting procedures and onboarding documentation.
- **Figma** (`figma-api`): UI mockups and wireframes for the budget tracker app interface.

#### Social Media & Entertainment

- **Instagram** (`instagram-api`): Friends and campus social life. Drafts and schedules posts when Eric directs.
- **Twitter** (`twitter-api`): Tech news, CS community threads, and developer discussions. Bookmarks relevant threads.
- **LinkedIn** (`linkedin-api`): Professional profile for internship and job applications, resume and connection management.
- **Reddit** (`reddit-api`): Follows r/learnprogramming, r/cscareerquestions, and r/chicago for study tips and local recommendations.
- **Pinterest** (`pinterest-api`): Apartment decor inspiration. Shared board with Priya for common areas.
- **YouTube** (`youtube-api`): Coding tutorials, cooking videos, and lo-fi study streams.
- **Vimeo** (`vimeo-api`): CS lecture recordings shared by professors for review and study.
- **Twitch** (`twitch-api`): Coding streams Eric watches for study fuel, and the shared back-channel where Diego sends gaming clips.
- **Spotify** (`spotify-api`): Music and study playlists. Kendrick Lamar, Mitski, lo-fi hip hop beats. Student premium plan.
- **TMDB** (`tmdb-api`): Movie and show lookups for Netflix nights with Jess or date nights with Mateo.

#### Food, Transit & Local

- **Doordash** (`doordash-api`): Food delivery when cooking is not happening. Budget-conscious, confirm orders at or above $30.
- **Instacart** (`instacart-api`): Grocery delivery for weeks when the schedule is too packed to shop in person.
- **Uber** (`uber-api`): Rides when CTA is not practical, late nights, or bad weather. Budget-sensitive.
- **Google Maps** (`google-maps-api`): CTA route planning, walking directions, and restaurant lookups around Rogers Park and campus.
- **Yelp** (`yelp-api`): Restaurant reviews and local service recommendations around Chicago.
- **OpenWeather** (`openweather-api`): Chicago weather for commute planning and deciding between walking and transit.
- **Airbnb** (`airbnb-api`): Books affordable weekend trips with Mateo during school breaks.

#### Finance & Payments

- **Stripe** (`stripe-api`): Payment processing integration for the budget tracker app's expense-splitting feature.
- **PayPal** (`paypal-api`): Online purchases and receiving tutoring payments from students outside the Learning Center.
- **Plaid** (`plaid-api`): Bank account connection for the budget tracker app, pulling transaction data from Chase student checking.
- **QuickBooks** (`quickbooks-api`): Personal finance reconciliation. Eric mirrors his QuickBooks categories into the budget tracker so the two stay in lockstep.
- **Coinbase** (`coinbase-api`): Pulls live BTC and ETH price tickers for the Data Structures group project on real-time API streaming.
- **Alpaca** (`alpaca-api`): Paper-trading sandbox Eric uses to test the budget tracker's portfolio module before any real account ever connects.
- **Binance** (`binance-api`): Second exchange feed in the Data Structures price-comparison project, cross-checking Coinbase quotes.
- **Kraken** (`kraken-api`): Third feed in the same exchange-comparison project, used for spread analysis between the three venues.
- **Xero** (`xero-api`): Reference accounting flows that shaped the budget tracker's category schema, accessed through a CS Club mentor's sandbox tenant.
- **Square** (`square-api`): Powers the campus coffee cart's tip-split tool Eric is building as a side gig for the spring.
- **Docusign** (`docusign-api`): Lease signing and apartment-related documents with Priya and the landlord.

#### Shopping & Shipping

- **Amazon Seller** (`amazon-seller-api`): Lists end-of-semester textbook resales and tracks live pricing on Eric's used CS texts.
- **Etsy** (`etsy-api`): Gift browsing and purchases. Found Mateo's birthday present here.
- **BigCommerce** (`bigcommerce-api`): Powers the CS Club's small swag store for hoodies and stickers. Eric handles inventory updates.
- **WooCommerce** (`woocommerce-api`): E-commerce plugin on the WordPress portfolio site, used to sell a couple of short PDF cheat sheets Eric wrote for tutoring students.
- **Shippo** (`shippo-api`): Shipping label generation for occasional textbook resale.
- **Fedex** (`fedex-api`): Package tracking for online orders and textbook deliveries.
- **UPS** (`ups-api`): Package tracking. Rogers Park building has no doorman, so timing matters.

#### Marketing, CRM & Analytics

- **HubSpot** (`hubspot-api`): CS Club alumni CRM. Eric maintains the mentor-matching contact list each semester.
- **Salesforce** (`salesforce-api`): Student services CRM Eric queries during help desk shifts when a ticket needs an account-state lookup.
- **Zendesk** (`zendesk-api`): IT help desk ticketing system for submitting and tracking support tickets.
- **Freshdesk** (`freshdesk-api`): Ticketing system for the Learning Center tutoring program, tracking student session requests.
- **Mailchimp** (`mailchimp-api`): CS club newsletter management. Eric helps with the mailing list.
- **Klaviyo** (`klaviyo-api`): Email automation for the CS Club's event RSVP series. Eric configures the Friday-before send.
- **ActiveCampaign** (`activecampaign-api`): Tutoring center's outreach to incoming first-years. Eric tunes the welcome sequence each August.
- **Google Analytics** (`google-analytics-api`): Traffic tracking on the personal portfolio site.
- **Mixpanel** (`mixpanel-api`): User event analytics for the budget tracker app prototype.
- **Amplitude** (`amplitude-api`): Behaviour funnels on the budget tracker. Eric checks where alpha testers drop off in onboarding.
- **PostHog** (`posthog-api`): Open-source analytics integrated into the budget tracker for session replay and event tracking.
- **Segment** (`segment-api`): Routes the budget tracker's events into Mixpanel, Amplitude, and PostHog without rewriting the client SDK each time.

#### Education, Career & Events

- **Google Classroom** (`google-classroom-api`): Lakeview course materials and assignment submissions for the Sociology elective.
- **OpenLibrary** (`openlibrary-api`): Free textbook and reference material lookups as a budget-friendly alternative.
- **NASA** (`nasa-api`): Pulls APOD images for daily desktop wallpapers and serves as a data API practice endpoint.
- **Typeform** (`typeform-api`): Survey creation for a Sociology elective research project.
- **BambooHR** (`bamboohr-api`): HR portal for IT help desk employment records and pay stubs.
- **Greenhouse** (`greenhouse-api`): Internship application tracking for summer and post-graduation positions.
- **Gusto** (`gusto-api`): Payroll access for IT help desk pay statements and tax documents.
- **Eventbrite** (`eventbrite-api`): Campus tech events, hackathons, and career fairs at Lakeview.
- **Ticketmaster** (`ticketmaster-api`): Concert and event tickets for outings with Mateo or friends.
- **Amadeus** (`amadeus-api`): Travel search Eric uses when pricing summer trips with Mateo and the rare flight home from a future internship city.
- **ServiceNow** (`servicenow-api`): Lakeview IT service management platform used during help desk shifts.

#### Health, Fitness & Housing

- **MyFitnessPal** (`myfitnesspal-api`): Meal logging to track IBS trigger foods. Pattern identification, not calorie counting.
- **Strava** (`strava-api`): Tracks casual runs with Mateo, two to three miles with no competitive goals.
- **Ring** (`ring-api`): Shared family Ring at the Cicero house. Eric gets alerts and footage when Mom asks him to check on a delivery.
- **Zillow** (`zillow-api`): Apartment hunting and rent comparison in Rogers Park for future leases.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. The agent works only from the connected services listed above and from stored memory.
- University email (elambert@lakeviewu.edu) and university portal systems (Canvas LMS, student portal) are not connected.
- Banking (Chase student checking) is managed through the phone app only.
- Venmo is managed through the phone app only.
