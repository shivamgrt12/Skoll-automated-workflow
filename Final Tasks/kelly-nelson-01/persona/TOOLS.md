# Tools: Kelly Nelson

## Tool Usage

### Connected Services

#### Communication & Messaging
- **Gmail** (`gmail-api`): Crestline Consulting inbox at kelly.nelson@voissync.ai. Personal, HFF, family coordination.
- **Outlook** (`outlook-api`): Read-only window when a foster parent or attorney writes from a Microsoft 365 mailbox. Reply via Gmail.
- **Slack** (`slack-api`): Hartford Foster Futures workspace with Derek, Sarah, and two volunteer leads. Channels: #gala, #case-for-kids, #youth-group.
- **Microsoft Teams** (`microsoft-teams-api`): Used only for CT Coalition of Children's Services coalition meetings.
- **WhatsApp** (`whatsapp-api`): International thread with cousins in Ireland that Aunt Nancy introduced her to.
- **Discord** (`discord-api`): Read-only on Sarah's classroom community server, used for substitute coverage swaps when Sarah asks Kelly to keep an eye out.
- **Telegram** (`telegram-api`): Read-only on a national foster-care advocates channel where state legislation news lands first.
- **Twilio** (`twilio-api`): HFF support-group SMS reminders for opt-in attendees. Send only, no reply storage beyond opt-out flags.
- **SendGrid** (`sendgrid-api`): HFF gala invitations and the 1,200-contact newsletter. Always test-send to Derek before pushing live.
- **Mailgun** (`mailgun-api`): Transactional backup for HFF event registration if SendGrid is rate limited.
- **Zoom** (`zoom-api`): Court prep with attorneys, remote testimony when permitted, and the quarterly state coalition call.

#### Calendar, Scheduling & Events
- **Google Calendar** (`google-calendar-api`): Primary calendar on kelly.nelson@voissync.ai. Personal, therapy, running, family, HFF, court reminders.
- **Calendly** (`calendly-api`): Public booking link for HFF press inquiries and foster-parent intake conversations.
- **Eventbrite** (`eventbrite-api`): HFF gala ticketing ($50 each, $15K goal) and quarterly community forums.
- **Typeform** (`typeform-api`): Pre-event surveys for the youth support group and post-gala feedback forms.
- **DocuSign** (`docusign-api`): HFF sponsor agreements, vendor contracts for the gala, board affirmations.
- **Ticketmaster** (`ticketmaster-api`): Occasional concert or theater booking with Camille. The Adele tour was the last one.

#### Documents, Notes & Casework Prep
- **Notion** (`notion-api`): HFF operations workspace. Gala planning binder, board notes, "Case for Kids" research pages.
- **Obsidian** (`obsidian-api`): Local vault for LCSW exam prep and her own clinical reflections. Never sync casework.
- **Google Drive** (`google-drive-api`): HFF documents, LCSW prep folder, personal writing. Lives under kelly.nelson@voissync.ai.
- **Dropbox** (`dropbox-api`): Shared folder with Derek for HFF financial backups and grant reports.
- **Box** (`box-api`): Read-only on the CT Coalition of Children's Services shared resource library.
- **Airtable** (`airtable-api`): HFF contact database, gala attendee tracking, fundraising progress dashboard.
- **Figma** (`figma-api`): HFF gala invitations and Instagram graphics. Sarah designs, Kelly approves.

#### Advocacy CRM & Outreach
- **HubSpot** (`hubspot-api`): HFF donor and contact CRM, 1,200 records. Tag by donor tier and last-touch date.
- **Salesforce** (`salesforce-api`): Read-only access to the CT Coalition of Children's Services partner CRM.
- **Mailchimp** (`mailchimp-api`): Backup newsletter list kept in case the SendGrid templates break before a gala send.
- **Klaviyo** (`klaviyo-api`): Tested once for HFF event flows. Kept as a fallback automation tool.
- **ActiveCampaign** (`activecampaign-api`): Cold-outreach pipeline for legislative contacts among undecided CT House members.
- **Segment** (`segment-api`): Routes HFF signups from Eventbrite, Typeform, and the website into HubSpot.
- **Intercom** (`intercom-api`): Chat widget on the HFF website. Sarah handles, Kelly reviews escalations only.
- **Zendesk** (`zendesk-api`): Read-only ticket queue at a partner youth-services nonprofit Kelly consults for.
- **Freshdesk** (`freshdesk-api`): Read-only support queue at another partner where HFF runs a referral pipeline.

#### Project & Task Management
- **Monday** (`monday-api`): "Case for Kids" campaign board. Each policy stage tracked with owner and deadline.
- **Asana** (`asana-api`): HFF gala project plan. Tasks assigned to Derek, Sarah, and two volunteer leads.
- **Trello** (`trello-api`): Kelly's personal Kanban for LCSW exam prep chapters and study deadlines.
- **Jira** (`jira-api`): Read-only on the HFF website rebuild board run by a pro bono dev shop.
- **Linear** (`linear-api`): Read-only on the same dev shop's product issues for the HFF intake tool.
- **Confluence** (`confluence-api`): CT Coalition shared documentation. Bills, hearing dates, advocacy talking points.

#### Research, Knowledge & Learning
- **OpenLibrary** (`openlibrary-api`): Background reading and citations for the "Case for Kids" position paper.
- **NASA** (`nasa-api`): Image of the day for the HFF Instagram on slow news weeks. Free, public, beautiful.
- **Google Classroom** (`google-classroom-api`): Coordination space for HFF volunteer training modules, run on Sarah's educator account.
- **WordPress** (`wordpress-api`): hartfordfosterfutures.org blog. Drafts go to Derek for review before publish.
- **Contentful** (`contentful-api`): Headless CMS for the HFF site rebuild. Read-only until the migration ships.
- **Webflow** (`webflow-api`): Landing pages for the gala and the "Case for Kids" launch. Sarah builds, Kelly proofs.

#### Maps, Errands, Local Hartford & Movement
- **Google Maps** (`google-maps-api`): Home visit routing across Hartford County, with traffic checks for court mornings.
- **Yelp** (`yelp-api`): Restaurant lookups for the dinners she actually books with Camille. Max Downtown, ON20.
- **OpenWeather** (`openweather-api`): Run-day forecast, gala day forecast, snow planning for the home-visit calendar.
- **DoorDash** (`doordash-api`): Late-night order after a hard court day when cooking is not happening. Used sparingly.
- **Instacart** (`instacart-api`): Stop & Shop pickup on weeks the home-visit schedule eats Saturday.
- **Uber** (`uber-api`): Rides home from gala night and the rare evening with wine. Not used for daily commute.
- **Airbnb** (`airbnb-api`): Boston weekends with Aunt Nancy and Steve, and the New York trips with Camille.
- **Zillow** (`zillow-api`): Browsing only. She is not buying soon, but she likes to know West End prices.
- **Ring** (`ring-api`): Front-door camera on the brownstone. Motion-clip review only.
- **MyFitnessPal** (`myfitnesspal-api`): Loose tracking around marathon training weeks. Patterns only, no calorie pressure.
- **Strava** (`strava-api`): Running log on the CT River trail. Mon, Wed, Sat mornings. Half marathon 2025, full marathon 2027 in training.

#### Money & Finance
- **Stripe** (`stripe-api`): HFF gala ticket processing and online donations on the website.
- **Plaid** (`plaid-api`): Reads her Ally HYSA, Webster checking, and the HFF Webster account into the budget spreadsheet.
- **PayPal** (`paypal-api`): Smaller HFF donations and the occasional reimbursement to a foster parent who covered intake costs.
- **Square** (`square-api`): In-person card reader at the gala silent auction.
- **QuickBooks** (`quickbooks-api`): HFF books, co-managed with Derek. Quarterly review with the CPA.
- **Xero** (`xero-api`): Read-only at the CPA's office for HFF year-end reconciliation.
- **Coinbase** (`coinbase-api`): Small ETH position from a 2021 paycheck experiment. She keeps it as a curiosity.
- **Binance** (`binance-api`): Watch-only on a public market view. Not a trading account.
- **Kraken** (`kraken-api`): Watch-only second venue for the same. She does not move money here.
- **Alpaca** (`alpaca-api`): Tax-loss harvesting on the Roth IRA she opened the year she earned her LMSW. Touched annually.

#### Travel & Shipping
- **Amadeus** (`amadeus-api`): Train and flight searches for Boston and the occasional New York or Vermont trip.
- **FedEx** (`fedex-api`): HFF grant report shipments to funders who still want hard copies.
- **UPS** (`ups-api`): Sponsor packets to corporate gala donors. Tracking and pickup scheduling.
- **Shippo** (`shippo-api`): Bulk label printing for gala thank-you boxes to top donors.

#### Social Media & Entertainment
- **Instagram** (`instagram-api`): @hartfordfosterfutures (1,100 followers). Sarah manages, Kelly approves anything legislative.
- **Pinterest** (`pinterest-api`): Gala decor boards and recipe ideas for Sunday dinner specials.
- **YouTube** (`youtube-api`): Saved playlists for marathon long-run audio and trauma-informed practice CE talks.
- **Spotify** (`spotify-api`): Run mixes, the evening Norah Jones rotation, the Adele playlist she would deny.
- **TMDB** (`tmdb-api`): Movie lookups when Camille suggests something. Quick check before she commits.
- **Vimeo** (`vimeo-api`): HFF gala video host. The 2024 highlight reel and Derek's testimony clip live here.
- **Twitch** (`twitch-api`): Read-only on a streamer Sarah likes, used for birthday gift research.
- **Reddit** (`reddit-api`): r/socialwork lurker. She reads, she does not post.
- **Twitter** (`twitter-api`): HFF account read-only. Sarah posts, Kelly reviews anything legislative.
- **LinkedIn** (`linkedin-api`): Professional profile updates and occasional connections with CT Coalition members.
- **Etsy** (`etsy-api`): Small independent gifts for birthdays and the HFF volunteer thank-you boxes.

#### Vendor, HR, DevOps & Infrastructure
- **Amazon Seller** (`amazon-seller-api`): Read-only view at a friend's small business where Kelly volunteers as an advisor.
- **WooCommerce** (`woocommerce-api`): HFF merch shop (t-shirts, totes). Low volume, Sarah ships.
- **BigCommerce** (`bigcommerce-api`): Read-only at a partner nonprofit's gift shop for cross-promotion planning.
- **BambooHR** (`bamboohr-api`): Read-only at the CT Coalition partner where Kelly contracts trainings. Onboarding records only.
- **Greenhouse** (`greenhouse-api`): Read-only at the same coalition partner for HFF candidate referrals.
- **Gusto** (`gusto-api`): Personal pay-stub view for the upcoming HFF first-paid-role planning conversation.
- **GitHub** (`github-api`): Read-only. Watching the pro bono dev shop's HFF site repo so she can flag content needs.
- **GitLab** (`gitlab-api`): Read-only at the dev shop's mirror, used only when GitHub is down.
- **Kubernetes** (`kubernetes-api`): No direct use. Listed because the HFF site stack runs on a managed cluster the dev shop maintains.
- **Cloudflare** (`cloudflare-api`): DNS and DDoS view for hartfordfosterfutures.org. Sarah holds the actual keys.
- **Datadog** (`datadog-api`): Site uptime dashboard for hartfordfosterfutures.org. Kelly checks before press events.
- **Sentry** (`sentry-api`): Error monitoring for the HFF intake tool. Alerts route to Sarah first, then Kelly.
- **PagerDuty** (`pagerduty-api`): Off-hours alerts for the HFF site. Sarah is the on-call name; Kelly is only paged when Sarah is unreachable during gala week.
- **Okta** (`okta-api`): SSO into the CT Coalition partner systems Kelly has read-only access to.
- **ServiceNow** (`servicenow-api`): Coalition partner IT ticketing. Used only when access to a shared system breaks.
- **Mixpanel** (`mixpanel-api`): HFF site funnel analytics. Shows where donors drop off in the gala flow.
- **PostHog** (`posthog-api`): Backup product analytics on the intake tool. Sarah owns the dashboards.
- **Amplitude** (`amplitude-api`): A/B test data on subject lines from the SendGrid newsletter sends.
- **Algolia** (`algolia-api`): Search on the HFF resource library. Foster parents look up training and forms.
- **Google Analytics** (`google-analytics-api`): hartfordfosterfutures.org traffic. Weekly review on Mondays.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from connected services and stored memory.
- Connecticut DCF internal systems, the kelly.nelson.work@gmail.com inbox, and any state child-welfare database. Treat as out of reach.
- Any private account belonging to a family member, a former partner, a friend, or a colleague.
- Any client, foster family, court system, or attorney working on an active DCF case.
- Real-time access to court filings or sealed records.
