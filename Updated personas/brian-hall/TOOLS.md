# Tools: Brian Hall

## Tool Usage

### Connected Services

#### Workspace & Daily Communication
- **Gmail** (`gmail-api`): Primary inbox at brian.hall@Greenridertech.com for clinic correspondence, insurance follow-ups, and vendor email. Checked at 5:30 AM and 7 PM.
- **Google Calendar** (`google-calendar-api`): Personal calendar holding the patient block, CrossFit classes, the twins' activities, family events, and travel.
- **Google Drive** (`google-drive-api`): Clinic buildout documents, athlete reports, and financial tracking, organized by project.
- **Outlook** (`outlook-api`): Secondary inbox for insurance company portals and BluePeak Health credentialing correspondence that routes through Outlook-based systems.
- **Microsoft Teams** (`microsoft-teams-api`): Coordinates with the Atlanta Firebirds FC athletic staff and insurance provider meetings that default to Teams.
- **Slack** (`slack-api`): The Atlanta Firebirds FC academy screening coordination channel and cross-clinic staff threads when the athletic staff prefers it.
- **WhatsApp** (`whatsapp-api`): Direct contact with the VALD rep Ryan Kimura and out-of-network vendors who prefer messaging over email.
- **Telegram** (`telegram-api`): Group chats with the Bogleheads investing community and a CrossFit programming discussion group.
- **Discord** (`discord-api`): Active in a CrossFit programming community and a sports-rehab practitioners server for clinical discussion.
- **Zoom** (`zoom-api`): Telehealth follow-ups with remote athletes and vendor demos with VALD Performance.
- **Twilio** (`twilio-api`): Powers SMS appointment reminders for clinic patients and the morning schedule-review nudge.
- **SendGrid** (`sendgrid-api`): Transactional email for clinic appointment confirmations and athlete report delivery.
- **Mailgun** (`mailgun-api`): Handles overflow transactional email for insurance notification batches and high-volume appointment weeks.

#### Clinic Operations & Practice Management
- **Calendly** (`calendly-api`): Patient self-scheduling and new-athlete consults that route into the clinic calendar.
- **DocuSign** (`docusign-api`): Patient consent forms, the SBA loan paperwork, vendor contracts, and the performance lab buildout agreements.
- **Typeform** (`typeform-api`): New-patient intake questionnaires and post-rehab outcome surveys.
- **Zendesk** (`zendesk-api`): Patient inquiry tickets for the front desk when call volume spikes.
- **Freshdesk** (`freshdesk-api`): Manages vendor support tickets and equipment warranty claims for the performance lab buildout.
- **Intercom** (`intercom-api`): Handles live chat on the Peak Performance PT website for new patient inquiries and appointment scheduling.
- **ServiceNow** (`servicenow-api`): Tracks equipment maintenance schedules and warranty service requests for the performance lab testing devices.
- **Jira** (`jira-api`): Tracks the performance lab buildout milestones and equipment install tasks.
- **Trello** (`trello-api`): Lightweight board for student rotation tasks and CE-hour tracking.
- **Asana** (`asana-api`): Manages the continuing education tracking pipeline and staff certification renewal workflows.
- **Monday** (`monday-api`): Coordinates the covered patio construction project timeline and vendor delivery schedules with Apex Build Group.
- **Linear** (`linear-api`): Tracks website feature requests and bug reports for the Peak Performance PT site.
- **Notion** (`notion-api`): Clinic operations wiki, protocol library, and the return-to-sport testing playbook.
- **Confluence** (`confluence-api`): Houses the Atlanta Firebirds FC shared screening protocols and academy partnership documentation.
- **Obsidian** (`obsidian-api`): Personal vault for CE notes, reading marginalia, and clinical reasoning notes.
- **Airtable** (`airtable-api`): Athlete caseload tracker and the equipment-quote comparison database for the lab.
- **BambooHR** (`bamboohr-api`): Staff records for the 3 PTs, 3 aides, front desk, and billing roles.
- **Gusto** (`gusto-api`): Payroll and benefits for the clinic staff.
- **Greenhouse** (`greenhouse-api`): Manages the hiring pipeline for the upcoming PT aide position as the performance lab adds capacity.

#### Athlete Performance & Wellness
- **MyFitnessPal** (`myfitnesspal-api`): Loose macro tracking around the ~200g protein target and qualifier-prep nutrition.
- **Strava** (`strava-api`): Logs conditioning runs and the occasional ruck; cross-references against WHOOP recovery.
- **OpenWeather** (`openweather-api`): Morning conditions for outdoor WODs, Ethan's Saturday soccer, and Hilton Head travel.
- **NASA** (`nasa-api`): Heat-index and UV imagery for planning summer outdoor training and family weekends.

#### Marketing, Web & Brand
- **HubSpot** (`hubspot-api`): Clinic CRM for prospective athletes and referral-source tracking.
- **Salesforce** (`salesforce-api`): Manages the Atlanta Firebirds FC academy partnership pipeline and corporate wellness program leads.
- **Mailchimp** (`mailchimp-api`): The clinic newsletter on performance tips and rehab milestones.
- **Klaviyo** (`klaviyo-api`): Powers the performance lab launch email sequence and targeted reactivation campaigns for former patients.
- **ActiveCampaign** (`activecampaign-api`): Automates the new-patient onboarding email drip and post-discharge follow-up sequences.
- **WordPress** (`wordpress-api`): The Peak Performance PT website, blog posts, and service pages.
- **Webflow** (`webflow-api`): Hosts the dedicated performance lab landing page and athlete testimonial showcase.
- **Contentful** (`contentful-api`): Manages structured content for the clinic blog, exercise video library, and patient education resources.
- **Algolia** (`algolia-api`): Powers search across the clinic blog, exercise library, and patient FAQ pages on the Peak Performance PT website.
- **Google Analytics** (`google-analytics-api`): Tracks clinic website traffic, service page conversions, and patient acquisition channels with monthly performance reviews.
- **Segment** (`segment-api`): Pipes website and email engagement events into the clinic's analytics stack for patient acquisition tracking.
- **Amplitude** (`amplitude-api`): Tracks patient journey analytics from first website visit through intake form completion and appointment booking.
- **Mixpanel** (`mixpanel-api`): Monitors conversion funnels on the clinic website and measures the effectiveness of blog content on new patient sign-ups.
- **PostHog** (`posthog-api`): Records session replays and heatmaps on the Peak Performance PT website to improve the patient scheduling flow.
- **Figma** (`figma-api`): Reviews and comments on brand and signage drafts for the new performance lab.

#### Finance, Investing & Payments
- **Plaid** (`plaid-api`): Links the household and clinic accounts into the budget view he tracks with Karen.
- **Stripe** (`stripe-api`): Processes patient card payments and program package purchases at the clinic.
- **Square** (`square-api`): Handles point-of-sale payments for in-person clinic visits, retail rehab products, and performance lab session packages.
- **PayPal** (`paypal-api`): Processes vendor deposits, reimbursements for cookout and team supplies, and patient refunds when needed.
- **QuickBooks** (`quickbooks-api`): Clinic bookkeeping, revenue tracking, and the monthly financial review.
- **Xero** (`xero-api`): Handles the performance lab's separate expense tracking and project-based accounting for the SBA loan reconciliation.
- **Alpaca** (`alpaca-api`): Manages a self-directed index fund sleeve for the household portfolio alongside the core Vanguard VTSAX holdings.
- **Coinbase** (`coinbase-api`): Monitors cryptocurrency market trends for financial literacy and comparison notes against Vanguard VTSAX index performance.
- **Kraken** (`kraken-api`): Provides alternative asset price feeds used in Brian's Bogleheads community discussions about portfolio diversification.
- **Binance** (`binance-api`): Supplies global cryptocurrency exchange data for the household investment research dashboard.

#### Family, Home & Smart Devices
- **Google Classroom** (`google-classroom-api`): Atlanta Global Academy first-grade updates for Ethan and Lily.
- **Ring** (`ring-api`): Doorbell and backyard camera in Kirkwood; package alerts and playset monitoring.
- **Zillow** (`zillow-api`): Neighborhood market tracking and Kirkwood property comps for the household financial picture.
- **Pinterest** (`pinterest-api`): Shared boards with Karen for patio design, backyard landscaping, and party planning ideas.
- **Dropbox** (`dropbox-api`): Photo backup for family events, cookouts, and the twins' school milestones.
- **Box** (`box-api`): Stores shared clinic training videos and large equipment specification files from vendors.

#### Travel & Local
- **Google Maps** (`google-maps-api`): Routes to clinic, the Midtown YMCA, Piedmont Park games, and the Houston and Hilton Head drives.
- **Amadeus** (`amadeus-api`): Flights to Houston for Dad's birthday and family travel planning.
- **Airbnb** (`airbnb-api`): Lodging for the Hilton Head trip and family stays when hotels do not fit.
- **Uber** (`uber-api`): Rides after late basketball games or when both vehicles are tied up with the twins.
- **Yelp** (`yelp-api`): Recon on BBQ and family-friendly spots, in Atlanta and when traveling.

#### Commerce, Shipping & Errands
- **Amazon Seller** (`amazon-seller-api`): Publishes the clinic's curated rehab equipment list on Amazon for patient convenience and affiliate referrals.
- **Etsy** (`etsy-api`): Sources custom clinic signage, personalized staff gifts, and handmade items for the performance lab decor.
- **BigCommerce** (`bigcommerce-api`): Runs the Peak Performance PT online store for branded merchandise and performance lab program packages.
- **WooCommerce** (`woocommerce-api`): Integrates with the WordPress clinic site to handle online booking payments and rehab product purchases.
- **Instacart** (`instacart-api`): Grocery delivery runs when the Saturday farmers market trip is missed.
- **DoorDash** (`doordash-api`): Family dinner delivery on heavy clinic days.
- **Shippo** (`shippo-api`): Labels for returning or transferring clinic equipment and warranty items.
- **FedEx** (`fedex-api`): Shipping athlete reports and signed documents when overnight delivery is needed.
- **UPS** (`ups-api`): Ships clinic equipment parts, vendor returns, and performance lab supply deliveries.

#### Sports, Media & Reading
- **YouTube** (`youtube-api`): Rehab technique videos, CrossFit movement breakdowns, and BBQ method clips.
- **Spotify** (`spotify-api`): Training playlists, classic rock, and the podcast rotation during the commute.
- **TMDB** (`tmdb-api`): Tracks family movie nights and the twins' Disney watchlist.
- **Vimeo** (`vimeo-api`): Stores clinic exercise demo videos used for patient education.
- **Twitch** (`twitch-api`): Streams CrossFit competition broadcasts and live sports rehab educational sessions.
- **Ticketmaster** (`ticketmaster-api`): Hawks games and concert outings with Karen.
- **Eventbrite** (`eventbrite-api`): CrossFit competitions, qualifier registration, and continuing-education workshops.
- **OpenLibrary** (`openlibrary-api`): Tracks his reading queue across longevity, performance, and business titles.

#### Social & Professional Networks
- **Instagram** (`instagram-api`): Clinic highlights, athlete wins (with consent), and BBQ posts.
- **Twitter** (`twitter-api`): Follows sports medicine researchers and Arsenal accounts; shares clinic milestones and rehab tips.
- **LinkedIn** (`linkedin-api`): Professional profile, clinic updates, and connections with referral providers.
- **Reddit** (`reddit-api`): Engages in sports physical therapy, CrossFit, and Bogleheads communities for clinical and investing signal.

#### Dev, Infrastructure & Monitoring
- **GitHub** (`github-api`): Stores CrossFit programming spreadsheets, clinic protocol templates, and data analysis scripts.
- **GitLab** (`gitlab-api`): Hosts version-controlled clinic protocol documents and the return-to-sport testing playbook for staff collaboration.
- **Sentry** (`sentry-api`): Monitors the Peak Performance PT website for errors and broken patient scheduling flows.
- **Datadog** (`datadog-api`): Tracks clinic website uptime, page load performance, and patient portal availability.
- **Cloudflare** (`cloudflare-api`): DNS and caching for the Peak Performance PT domain.
- **Kubernetes** (`kubernetes-api`): Manages the container infrastructure underlying the clinic's hosted web services and scheduling platform.
- **PagerDuty** (`pagerduty-api`): Sends alerts when the clinic website or patient scheduling system experiences downtime outside business hours.
- **Okta** (`okta-api`): Manages single sign-on and role-based access for clinic staff across the practice management tools.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from connected mock APIs and stored memory.
- The clinic EMR (WebPT) is separate and not connected to the assistant. Treat patient charting and treatment records as off-system.
- Karen's MedPlus Pharmacy work accounts and any patient or pharmacy systems are private to her and not connected.
- Personal banking and brokerage portals are not directly connected; budget visibility comes only through Plaid.
- In group or shared contexts, treat any institutional internal system as not connected, and work from what Brian tells you and stored memory only.
