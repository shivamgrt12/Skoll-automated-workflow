# Tools: Ryan Mitchell

## Tool Usage

### Connected Services

#### Family & Personal Communication
- **Gmail** (`gmail-api`): Primary inbox at ryan.mitchell@Finthesiss.ai. Ryan triages at 6:30 AM, lunch, and 9:00 PM, with cohort administration, pediatric scheduling, and book club at the top of the pile.
- **Outlook** (`outlook-api`): Personal Outlook holds the NASW Maryland chapter newsletter, the continuing-education vendor mail Ryan needs for license renewals, and the foster-care training peer network digests. It sits separate from the BCDSS Outlook he uses on the work side.
- **WhatsApp** (`whatsapp-api`): "Mitchell Family" thread with Uncle Oscar in Silver Spring and cousins in Dakar. Voice notes from Oscar arrive weekly, recipes monthly, and the Senegal trip planning thread surfaces every spring.
- **Telegram** (`telegram-api`): Thread with two MSW classmates now in Nairobi and Berlin. Cross-time-zone updates twice a month and Senegal logistics from the Berlin friend who has been twice.
- **Microsoft Teams** (`microsoft-teams-api`): Active in the monthly inter-agency child welfare working group that meets when a case crosses county or state lines. Ryan keeps notifications muted off-meeting and drafts the agenda the Sunday before.
- **Slack** (`slack-api`): Foster care training peer network workspace. Ryan posts in the "curriculum" and "case-studies" channels after each cohort wraps and pulls shared materials from the "library" channel before the next.
- **Discord** (`discord-api`): Child welfare social worker community server. Ryan posts de-identified case-discussion questions to peers monthly and answers newer caseworkers' onboarding questions in the #welcome channel.
- **Twilio** (`twilio-api`): Outbound SMS for last-minute cohort cancellations to the participant list and book club host-change blasts.
- **SendGrid** (`sendgrid-api`): Bulk email for the foster cohort welcome packet, the weekly cohort recap email, and the end-of-cohort participant evaluation requests.
- **Mailgun** (`mailgun-api`): Backup sender for the cohort distribution list when SendGrid throttles around enrollment week. Same template library, identical sender identity.
- **Zoom** (`zoom-api`): Biweekly Monday 7 PM Telehealth with Dr. Felicia Grant, foster cohort guest speaker sessions when an out-of-state speaker can join remotely, and the rare remote co-teaching session when his back keeps him home.

#### Calendar, Planning & Productivity
- **Google Calendar** (`google-calendar-api`): Family calendar holds BCDSS court dates, cohort sessions, kids' school and pediatric appointments, choir, book club, and Wednesday mom-dinner. Monday therapy and Wednesday dinner sit on the calendar in red as immovable.
- **Notion** (`notion-api`): Private workspace for Ryan's slow-burn book project on the child welfare system. Chapter outlines, source notes, and the running "what cannot be said in a case file" notebook.
- **Obsidian** (`obsidian-api`): Local notes for cohort observations and de-identified patterns from his caseload. Daily notes after court testimony or a hard home visit.
- **Asana** (`asana-api`): Foster cohort operations board. Session checklists, materials prep, participant follow-up, and the monthly cohort-end debrief tasks.
- **Trello** (`trello-api`): Personal "house and life" board for repairs, renewals, and the HVAC replacement that is coming.
- **Monday** (`monday-api`): Joint tracker with Marcus for kids' school logistics, AYSO season operations, and the basement-to-bedroom remodel that is two years out.
- **Linear** (`linear-api`): Ryan's own issue tracker for the book project. Chapters as issues, source quotes as comments, and the cross-references between case-study patterns and the policy chapters.
- **Jira** (`jira-api`): Tracker for cohort logistics tickets. Participant follow-ups, workbook reprints, room-booking issues Ryan flags to BCDSS facilities, and the post-cohort evaluations triage.
- **Airtable** (`airtable-api`): Cohort participant database across past graduates. Names, certifications, placement outcomes, and the continuing-education touchpoints Ryan owes the network.
- **Calendly** (`calendly-api`): Public scheduling page for prospective foster parent intake conversations and the occasional speaking inquiry from a regional child welfare conference.
- **Typeform** (`typeform-api`): End-of-cohort participant evaluation form and the mid-cohort check-in pulse survey. Results flow to Airtable on submit.
- **DocuSign** (`docusign-api`): Cohort participant agreements, BCDSS contract paperwork for the 1099 cohort income, and the eventual home equity line paperwork when the HVAC replacement happens.

#### Files, Documents & Cloud
- **Google Drive** (`google-drive-api`): Personal Drive holds the adapted PRIDE curriculum, case studies, handouts, family documents, household records, and the unfinished essay drafts.
- **Dropbox** (`dropbox-api`): Long-term archive of cohort materials and recordings, family photos, and Robert Sr.'s scanned recipe cards. Ryan adds new recordings after each cohort wrap and pulls a recipe card most Sunday mornings.
- **Box** (`box-api`): Shared folder with the family accountant for tax records and the 1099 cohort income. The accountant prefers Box for the quarterly handoff, and Ryan drops the QuickBooks export on the 1st.
- **Confluence** (`confluence-api`): Ryan's personal knowledge base for the PRIDE curriculum adaptations, court testimony templates, and the case-study patterns he reuses across cohorts.
- **Figma** (`figma-api`): Cohort handout layouts. Ryan sketches the structure; a designer friend from book club polishes the typography between cohorts.

#### Foster Cohort, Outreach & Site
- **HubSpot** (`hubspot-api`): CRM for prospective foster parents Ryan meets through church and community events. Tagged for the next cohort opening so the welcome email lands on day one.
- **Salesforce** (`salesforce-api`): Pipeline CRM for the wider prospective-foster-parent funnel that comes in through the cohort landing page. Ryan logs each inquiry, screens by phone, and routes them to the next cohort window.
- **Mailchimp** (`mailchimp-api`): Quarterly newsletter to past cohort graduates with continuing-education tips, recertification reminders, and the resource library links.
- **Klaviyo** (`klaviyo-api`): Sends the foster cohort welcome sequence across the ten weeks of each cohort. Intake confirmation, prerequisites, day-one logistics, mid-cohort check-in, and the certificate dispatch.
- **ActiveCampaign** (`activecampaign-api`): Drip campaign for cohort graduates between cohorts. Quarterly continuing-education tips, recertification window reminders, and the call for guest case studies before the next cycle.
- **Intercom** (`intercom-api`): Live chat on the cohort landing page. Ryan answers prospective-parent intake questions in the 9:00 PM window after the kids are down.
- **Zendesk** (`zendesk-api`): Help desk for cohort participants. Logistics questions, certificate replacements, and post-cohort tech issues with the workbook PDFs.
- **Freshdesk** (`freshdesk-api`): Second queue for the Grace Community Church choir's logistical inquiries. Rehearsal swaps, music assignments, and seasonal program rotation. Pastor Walker asked Ryan to hold the queue when the previous volunteer moved.
- **ServiceNow** (`servicenow-api`): Facilities queue for the BCDSS training room. Ryan files HVAC and projector tickets the morning after a bad cohort night and chases them to close.
- **Segment** (`segment-api`): Event router that pushes cohort signup and workbook-storefront activity to QuickBooks for the 1099 ledger and to Mailchimp for the graduate newsletter list.
- **Mixpanel** (`mixpanel-api`): Funnel tracking on the cohort landing page. Ryan reviews drop-off in the prospective-foster-parent intake form before each cohort cycle and trims the questions that lose people.
- **PostHog** (`posthog-api`): Session replays on the intake form. Ryan watches three or four a cohort to see where prospective parents stall, then rewrites the form copy that confused them.
- **Amplitude** (`amplitude-api`): Engagement tracking for the cohort resource library. Tells Ryan which case studies and handouts past graduates download most, which feeds the next cohort's pre-read.
- **Google Analytics** (`google-analytics-api`): Monthly reporting on the cohort landing page hosted on WordPress. Ryan reviews on the 1st with the household budget.
- **Algolia** (`algolia-api`): Powers search across the cohort resource library on WordPress. Participants type "trauma-informed visit" and the right handout surfaces in two keystrokes.
- **Contentful** (`contentful-api`): Holds the cohort resource library content. Case studies, discussion prompts, take-home reflections, published cohort-by-cohort as Ryan writes them.
- **Webflow** (`webflow-api`): Small Sunday-pot-roast blog Ryan posts to when a recipe lands. Audience is family, church friends, and a few cohort graduates who asked for the mafe.
- **WordPress** (`wordpress-api`): The cohort landing page. Session schedules and prerequisites posted before each cohort, archived after the cohort wraps.

#### Health, Wellness & Home Security
- **MyFitnessPal** (`myfitnesspal-api`): Ryan logs yoga sessions and the anti-inflammatory eating pattern that helps the back. Consistency only, no calorie pressure.
- **Strava** (`strava-api`): Walks around the Greenfield neighborhood when the back is at a 3 instead of a 6. Private account, route shared with Marcus on evening loops.
- **Ring** (`ring-api`): Front door camera at the Greenfield rowhouse. Notifications go to Marcus's phone first because Ryan's is often in the office without service.

#### Home, Errands & Local Life
- **Google Maps** (`google-maps-api`): Home visit routes, BCDSS to court to school pickup paths, Silver Spring run for Uncle Oscar's, parking tactics for downtown.
- **Uber** (`uber-api`): Backup when the Accord is in the shop or after a late evening court date when driving home is not safe.
- **DoorDash** (`doordash-api`): Rare. Only on a particularly bad back day or a court evening that ran long.
- **Instacart** (`instacart-api`): Weekly grocery delivery during cohort season, when the Tuesday and Thursday evenings are gone. Off-cohort, Ryan shops in person.
- **Yelp** (`yelp-api`): New restaurant scouting for date nights with Marcus and family-friendly spots when Uncle Oscar visits Baltimore.
- **OpenWeather** (`openweather-api`): Morning weather call for the kids' clothes, soccer Saturday call, and home visit planning if a route is exposed.
- **Ticketmaster** (`ticketmaster-api`): Occasional Ravens game with Marcus, the kids' first big-venue events when they are old enough.
- **Eventbrite** (`eventbrite-api`): Local continuing education events, Grace Community Church functions, book club author talks.

#### Money, Banking & Investing
- **QuickBooks** (`quickbooks-api`): Household books and the 1099 cohort ledger. Monthly reconciliation on the 1st with Marcus, 529 contribution log alongside.
- **Plaid** (`plaid-api`): Live link between PNC, Ally, and QuickBooks. Powers daily transaction categorization and the monthly budget reconciliation. Read scope by Plaid's design, write scope by Ryan's choice.
- **Stripe** (`stripe-api`): Processes the cohort workbook orders for prospective foster parents who cannot access the BCDSS-issued copies. Five to ten orders a month at $40 a copy.
- **PayPal** (`paypal-api`): Book club host reimbursements, occasional Etsy purchases, and the gift collection for Tami after a hard year.
- **Coinbase** (`coinbase-api`): Tracks the small holding Ryan bought in 2021 to understand the wallet UX a few of his caseload families had fallen for. Research lane for the book project's chapter on financial coercion.
- **Alpaca** (`alpaca-api`): Paper-trading account where Ryan models 529 allocation changes before he and Marcus discuss them at the monthly budget review.
- **Binance** (`binance-api`): Same research lane as Coinbase. Ryan watches predatory order-book patterns parents in his caseload describe and pulls screenshots for the book.
- **Kraken** (`kraken-api`): The withdrawal-flow tester. A cohort participant lost $400 to a fake "withdrawal fee" prompt in 2024, and Ryan keeps a foothold here to keep the muscle memory current for the cohort warnings.
- **Square** (`square-api`): Point-of-sale for in-person cohort workbook orders at the BCDSS training room. Ryan runs $40 paperback transactions on his phone when a participant asks for a second copy.
- **Xero** (`xero-api`): Mirror of the cohort 1099 ledger the family accountant prefers when she imports for tax season. Ryan exports a quarterly snapshot from QuickBooks and uploads.

#### Travel, Shipping & Real Estate
- **Amadeus** (`amadeus-api`): Flight research for the long-promised Dakar trip and occasional weekend research for Rehoboth or the western Maryland cabin.
- **Airbnb** (`airbnb-api`): Family weekend rentals, the western Maryland cabin booking, eventually the Dakar trip lodging.
- **Zillow** (`zillow-api`): Casual market watching. They will not move from the Greenfield rowhouse, but Ryan likes knowing the comps.
- **FedEx** (`fedex-api`): Outbound shipments for cohort workbook reprints and the occasional Etsy gift to family in Dakar.
- **UPS** (`ups-api`): Default carrier for returns and the gift packages to Sarasota relatives. Tracking watch on the holiday surge.
- **Shippo** (`shippo-api`): Multi-carrier rate compare for the annual cohort workbook bulk order and the cookbook print-run shipments.

#### Shopping & Marketplaces
- **Amazon Seller** (`amazon-seller-api`): Live softcover listing for the cohort workbook. Five to ten copies a month to former cohort graduates and a few academic libraries that catalogue the PRIDE adaptations.
- **Etsy** (`etsy-api`): Recurring purchases for kids' birthday gifts, handmade items from Senegalese-American makers, and the occasional anniversary gift for Marcus.
- **BigCommerce** (`bigcommerce-api`): Direct-sale storefront for the recipe cookbook Ryan is quietly assembling from his father's cards. Small print runs sold to church and family at cost plus shipping.
- **WooCommerce** (`woocommerce-api`): Digital case-study PDFs at $5 each, tied to the WordPress cohort landing page. Direct sales bypass Amazon's cut and fund the workbook reprints.

#### Media, Reading & Curiosity
- **Spotify** (`spotify-api`): Family shared plan. Hazelnut-coffee gospel on Sunday mornings, neo-soul on the porch, the private "Reset" playlist for hard nights.
- **YouTube** (`youtube-api`): Cooking videos for Senegalese dishes from Uncle Oscar's repertoire, kids' content with household filters on, occasional sermon archives.
- **TMDB** (`tmdb-api`): Movie lookups for Friday family movie night, vetting documentary picks about food and social policy.
- **Twitch** (`twitch-api`): One channel followed for a chef who streams Senegalese cooking. No subscriptions.
- **Vimeo** (`vimeo-api`): Higher-quality archive of cohort guest-speaker sessions and continuing education recordings Ryan re-watches before recertification.
- **Reddit** (`reddit-api`): r/socialwork and a couple of foster-parent subreddits. Ryan posts twice a year answering newer caseworkers' onboarding questions and scans cohort-relevant threads before each cycle.
- **Twitter** (`twitter-api`): Follows child welfare policy researchers and a few Baltimore journalists. Posts when a cohort wraps, short photo and three lines about what landed.
- **LinkedIn** (`linkedin-api`): MSW connections, post when a cohort cycle wraps, and the steady DMs from regional conference organizers asking him to speak.
- **Instagram** (`instagram-api`): Quiet presence. Andrew's school updates and the Grace Community Church choir account.
- **Pinterest** (`pinterest-api`): Shared board with Marcus for the basement bedroom remodel and Senegal trip ideas.
- **OpenLibrary** (`openlibrary-api`): Book club queue lookups and child welfare backlist titles.
- **NASA** (`nasa-api`): Andrew's space phase. Ryan pulls images for the dinosaur-and-rockets bedroom wall.

#### Engineering, Identity & Ops
- **GitHub** (`github-api`): Hosts the open-source PRIDE curriculum adaptations Ryan publishes for the wider child welfare community. A former cohort graduate watches the repo and contributes pull requests.
- **GitLab** (`gitlab-api`): Mirror of the same curriculum repo for social workers in programs that prefer GitLab over GitHub. Ryan pushes to both on cohort wrap.
- **Datadog** (`datadog-api`): Monitors the cohort landing page's uptime around enrollment windows. The graduate-built tooling emits to it, and Ryan checks the dashboard before each cohort opens.
- **Sentry** (`sentry-api`): Catches errors on the cohort intake form and the workbook storefront. Ryan triages reports the morning after a session when a participant flags that the form broke.
- **Cloudflare** (`cloudflare-api`): Holds DNS and bot protection for the cohort landing page and the cookbook storefront.
- **Kubernetes** (`kubernetes-api`): Runs the small VPS cluster that hosts the cohort landing page, the cookbook storefront, and the resource library. Ryan checks pod health Sunday afternoons after church.
- **PagerDuty** (`pagerduty-api`): On-call rotation for the cohort landing page during enrollment windows. Ryan takes the page if signups break Tuesday or Thursday evening; otherwise the rotation is quiet.
- **Okta** (`okta-api`): Single sign-on Ryan uses for the continuing-education vendor portal and the NASW Maryland chapter member area.

#### HR, Hiring & Education
- **BambooHR** (`bamboohr-api`): Personal HR file. BCDSS paystubs scanned for the home mortgage refi, cohort 1099 records, MSW licensure renewals, and the CEU certificates.
- **Gusto** (`gusto-api`): Runs the small honoraria for the two cohort guest speakers ($200 each, twice a year) and the designer friend's typography work on the cohort handouts.
- **Greenhouse** (`greenhouse-api`): Holds the prospective-foster-parent intake pipeline as a hiring funnel. Intake call, screening, cohort acceptance, cohort completion. Same workflow logic, repurposed for foster parent vetting.
- **Google Classroom** (`google-classroom-api`): Parent shadow account Ryan uses to follow Andrew's Rosemont Elementary assignments and parent updates.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from the connected services listed above and from stored memory.
- BCDSS internal systems (MD CHESSIE, BCDSS Outlook, BCDSS-issued laptop) are not connected. They sit on the work side and never appear here.
- Baltimore City Juvenile Court case management is not connected.
- Marcus's Dunbar HS Google Workspace is not connected. Anything from the school side reaches the assistant through Marcus.
- Rosemont Elementary and Little Explorers Daycare parent portals are not connected. Ryan and Marcus check those themselves.
- Insurance carrier portals for the family Maryland state health plan are not connected. The confirmed phone contact is the channel.
- Live brokerage trading authority is not granted. Alpaca stays in paper-trade mode and the crypto holdings are research only.
- Jackie's, Denise's, and Uncle Oscar's private accounts are not connected. Communication happens by phone, text, or WhatsApp.
