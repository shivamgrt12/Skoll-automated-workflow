# Tools: Ryan Torres

## Tool Usage

### Connected Services

#### Family, Wedding Party & Personal Communication
- **Gmail** (`gmail-api`): Primary inbox at ryan.torres@voissync.ai. Wedding vendors, family threads, Heartland volunteer roster, dental therapy program inquiries. Triaged morning and 7:30 PM. OpenClaw drafts vendor replies and surfaces "deadline" or "deposit" tags first.
- **Outlook** (`outlook-api`): Working inbox for the Michigan continuing-education vendor that tracks Ryan's RDH credit history. OpenClaw replies to enrollment threads, forwards completion certificates into Drive, and registers Ryan for the next-quarter session lineup.
- **WhatsApp** (`whatsapp-api`): "Torres Family" group with Mike, Linda, Grandma Rose, Jake, Tyler. "Wedding Party" group with Emma, Chris, Jake, the bridesmaids. "Friends" group for the broader social circle. OpenClaw drafts day-of timeline pings and tracks RSVPs in the wedding party thread.
- **Telegram** (`telegram-api`): Direct line into a small Italian-American cooking community Ryan trades Sunday-cooking notes with. OpenClaw posts the week's recipe outcome and pulls weekend menu ideas for him to consider.
- **Microsoft Teams** (`microsoft-teams-api`): Active channel for Lakewood-affiliated continuing-education sessions and Heartland clinic all-hands. OpenClaw RSVPs to webinars, captures notes into Notion, and pushes credit completions to LinkedIn.
- **Slack** (`slack-api`): Heartland Free Dental Clinic volunteer coordination workspace. OpenClaw watches the "shifts" and "supplies" channels, posts Ryan's monthly availability, and confirms supply pickups the Friday before each shift.
- **Discord** (`discord-api`): Working channel in a dental hygiene CE community. OpenClaw flags new case-study threads onto Ryan's Friday reading list and posts the occasional question Ryan dictates after a clinical day.
- **Twilio** (`twilio-api`): Outbound SMS for last-minute wedding party logistics, Heartland shift reminders, and the day-of timeline broadcasts on October 17.
- **SendGrid** (`sendgrid-api`): Bulk email for the wedding-guest communication track (RSVP nudges, day-of logistics, post-wedding thank-you sequence) and the Heartland volunteer roster newsletter.
- **Mailgun** (`mailgun-api`): Failover sender for the wedding-guest list and Heartland's monthly donor digest when SendGrid throttles or the Heartland mailbox hits rate limits.
- **Zoom** (`zoom-api`): Dental therapy program info sessions, clinic continuing-education webinars, and wedding-vendor video consults. OpenClaw books the calendar invite and saves recordings Ryan flags for later.

#### Wedding Planning & Vendor Coordination
- **Google Calendar** (`google-calendar-api`): Holds clinic hours, wedding deadlines, family events, volunteer Saturdays, gym blocks, and the Wednesday wedding-planning evenings with Emma. The day-of timeline lives here.
- **Notion** (`notion-api`): Private workspace for the dental therapy program decision. Cost comparisons, timeline overlap with the wedding year, admissions documents, and the prerequisite refresher schedule.
- **Obsidian** (`obsidian-api`): Local notes for Italian recipe variations Ryan keeps to himself and a small running log of patient-education phrasings he likes to reuse.
- **Asana** (`asana-api`): Wedding logistics board. Vendor checklists, deposit timeline, day-of run-of-show.
- **Trello** (`trello-api`): Bachelor party planning board shared with Chris and Jake. OpenClaw posts the budget split and updates the dinner-and-game itinerary as confirmations land.
- **Monday** (`monday-api`): Heartland Free Dental Clinic volunteer roster and supply-tracking board. OpenClaw updates the roster after each Saturday and surfaces low-supply items before Friday packing.
- **Linear** (`linear-api`): Active issue tracker for the Lakewood patient-education content pilot. OpenClaw opens issues for content gaps Ryan dictates, triages cleanup work, and closes the Friday review-ready queue before the weekly cycle.
- **Jira** (`jira-api`): Active board for the dental therapy program prerequisite tracker Ryan runs alongside the Notion workspace. OpenClaw moves admissions cards, attaches transcripts, and pings Ryan when a deadline is inside two weeks.
- **Airtable** (`airtable-api`): Wedding vendor comparison base. Cedar Table versus alternates, Bloom & Petal contract terms, Saffron Bakehouse order detail, photographer shortlist, and the guest list with dietary flags.
- **Calendly** (`calendly-api`): Public scheduling page for wedding-vendor consultations and dental therapy program advising calls.
- **Typeform** (`typeform-api`): RSVP capture form for the wedding, dietary-restrictions form, and a small Heartland volunteer-availability survey.
- **DocuSign** (`docusign-api`): Wedding vendor contracts and the dental therapy program application paperwork. OpenClaw routes documents to Emma when joint signature is required.

#### Files, Documents & Cloud
- **Google Drive** (`google-drive-api`): Wedding planning documents, vendor contracts, budget spreadsheet, seating chart, dental therapy program research, Italian recipes pulled from Linda's collection. Drive is the long-term home for everything Ryan touches.
- **Dropbox** (`dropbox-api`): Long-term archive of family photos and the post-October-17 wedding photo dump from the photographer. OpenClaw syncs nightly between Drive and the family photo backup.
- **Box** (`box-api`): Shared folder with Cedar Table Catering for the final guest count, dietary-restrictions packet, and the day-of timing notes. Sensitive. No outbound shares without Ryan's confirmation.
- **Confluence** (`confluence-api`): Active knowledge base for the Lakewood patient-education content pilot. OpenClaw drafts new pages from Ryan's voice memos and keeps version notes aligned with the Contentful entries.
- **Figma** (`figma-api`): Active design workspace for wedding signage, program cards, table numbers, and the post-wedding brunch menu. Emma drafts, Ryan reviews, OpenClaw exports finals for print vendor handoff.

#### Clinic Operations, Wedding Vendor & Heartland Adjacencies
- **HubSpot** (`hubspot-api`): Wedding-vendor CRM. Active pipeline across Cedar Table, Bloom & Petal, Saffron Bakehouse, the photographer shortlist, and the DJ. OpenClaw advances stages as contracts and deposits clear.
- **Salesforce** (`salesforce-api`): Active CRM for the Michigan continuing-education vendor that tracks Ryan's running RDH credit balance. OpenClaw logs new completed credits and surfaces the running total against the April renewal target.
- **Mailchimp** (`mailchimp-api`): Active Heartland Free Dental Clinic volunteer newsletter list. OpenClaw drafts the monthly issue and schedules the send to clear the first Monday of each month.
- **Klaviyo** (`klaviyo-api`): Active automation for the wedding-guest RSVP nudge sequences leading into the October 13 final-guest-count deadline with Cedar Table.
- **ActiveCampaign** (`activecampaign-api`): Active automation for the Heartland Free Dental Clinic donor stewardship sequences Ryan helps coordinate. The annual silent-auction night runs through this list.
- **Intercom** (`intercom-api`): Active triage queue for Lakewood website patient inquiries Dr. Sarah Kim routes to the hygiene team. OpenClaw drafts replies for Ryan's review and flags scheduling-related questions to Lakewood's front desk.
- **Zendesk** (`zendesk-api`): Active ticket queue for warranty and supply issues against Lakewood's primary dental-instrument vendor. OpenClaw opens tickets when Ryan flags a defect and tracks RMA status to closeout.
- **Freshdesk** (`freshdesk-api`): Active support portal for Lakewood's secondary dental-instrument vendor. OpenClaw escalates supply shortages, supplies stock-out evidence when warranty exchange is denied, and logs Ryan's resolution notes.
- **ServiceNow** (`servicenow-api`): Active Lakewood building IT queue for when operatory equipment or chair-side software misbehaves. OpenClaw files the ticket while Ryan is still mid-cleanup.
- **Segment** (`segment-api`): Active data layer tracking engagement on the Heartland Free Dental Clinic WordPress page Ryan helps maintain. Feeds the analytics rails downstream.
- **Mixpanel** (`mixpanel-api`): Active analytics on the Heartland page traffic and the volunteer-signup funnel. OpenClaw surfaces the weekly conversion delta at the Monday review.
- **PostHog** (`posthog-api`): Active product analytics on the Lakewood patient-education content pilot. OpenClaw runs feature flags on Ryan's experimental copy variants and reports week-over-week reading completion.
- **Amplitude** (`amplitude-api`): Active analytics on the Heartland donor landing pages. OpenClaw surfaces which campaign copy is outperforming ahead of the silent-auction push.
- **Google Analytics** (`google-analytics-api`): Active reporting on the Heartland WordPress page. Monthly review on the first Monday of each month against the volunteer-acquisition target.
- **Algolia** (`algolia-api`): Active search layer across Ryan's Notion dental-therapy research and Drive wedding-planning documents for fast retrieval mid-call with a vendor.
- **Contentful** (`contentful-api`): Active CMS for the Lakewood patient-education content pilot Ryan is building. OpenClaw stages Ryan's drafts and publishes once Dr. Sarah Kim signs off.
- **Webflow** (`webflow-api`): Published Heartland Free Dental Clinic volunteer info page Ryan co-maintains with the clinic coordinator. OpenClaw pushes schedule changes and supply updates the Friday before each shift.
- **WordPress** (`wordpress-api`): Heartland Free Dental Clinic volunteer page. Public-facing schedule and supply updates posted here on the same Friday cadence as the Webflow page.

#### Health, Training & Wellness
- **MyFitnessPal** (`myfitnesspal-api`): Ryan logs Pulse Fitness classes and weeknight walks with Emma. Consistency only, no calorie pressure.
- **Strava** (`strava-api`): Light tracking of the weeknight walks with Emma. Segments not shared publicly.
- **Ring** (`ring-api`): Front door camera at the east Dearborn apartment. Notifications go to Ryan's phone first; OpenClaw archives the daily clips weekly.

#### Local Life, Errands & Navigation
- **Google Maps** (`google-maps-api`): Routes to Lakewood, Linda and Mike's house, Emma's apartment, Heartland clinic, and the wedding venue. Italian restaurant scouting for date nights.
- **Uber** (`uber-api`): Backup transport when the Civic is in the shop or after a long wedding-vendor day. Pre-booked for the wedding-day shuttle backup.
- **DoorDash** (`doordash-api`): Used when Emma is working late and the kitchen is dark. OpenClaw remembers the regular pasta-and-bread order from the Hamtramck spot Ryan trusts.
- **Instacart** (`instacart-api`): Weekly grocery delivery when the schedule is tight. In-person runs preferred when there is time.
- **Yelp** (`yelp-api`): Italian restaurant scouting for date nights with Emma and the bachelor party shortlist. OpenClaw saves the monthly rotation list to Drive.
- **OpenWeather** (`openweather-api`): Saturday volunteer-clinic weather, the October 17 outdoor-ceremony weather watch, and gym-walk decisions.
- **Ticketmaster** (`ticketmaster-api`): Detroit Tigers games with Mike and Tyler, the Frank Sinatra tribute night when it tours through, and the Christmas Pops concert Linda likes.
- **Eventbrite** (`eventbrite-api`): Dental therapy program info sessions, Heartland fundraisers, Italian-American cultural events.

#### Money, Banking & Wedding Budget
- **QuickBooks** (`quickbooks-api`): Household books and the wedding budget master ledger. Monthly reconciliation on the 1st.
- **Plaid** (`plaid-api`): Account-linking layer for QuickBooks, the wedding budget spreadsheet, and the Heartland small-org books reconciliation.
- **Stripe** (`stripe-api`): Active payment processing for Heartland Free Dental Clinic donations on the WordPress page. OpenClaw reconciles weekly payouts against Xero.
- **PayPal** (`paypal-api`): Used for splitting bachelor-party costs and the occasional wedding-vendor deposit when the vendor accepts it instead of card.
- **Coinbase** (`coinbase-api`): Active small BTC holding Ryan keeps as a $25-a-month dollar-cost-averaging experiment. OpenClaw schedules the monthly buy on the 1st and logs it into QuickBooks.
- **Alpaca** (`alpaca-api`): Active small brokerage account holding a low-cost-index-fund DCA Ryan runs alongside his 401(k). OpenClaw queues the $100 monthly buy on the 5th and confirms with Ryan before placing it.
- **Binance** (`binance-api`): Active staking position on a small stablecoin balance Ryan parked there. OpenClaw monitors the daily yield and surfaces the monthly accrual at the budget review.
- **Kraken** (`kraken-api`): Active small ETH holding Ryan picked up after a Chris recommendation. OpenClaw monitors balance and surfaces moves above the $150 threshold for awareness.
- **Square** (`square-api`): Active POS for Heartland in-person fundraisers and the annual silent-auction night. OpenClaw reconciles the device totals with Xero the next morning.
- **Xero** (`xero-api`): Active books for the Heartland Free Dental Clinic small-org. Ryan reconciles quarterly with the clinic coordinator; OpenClaw drafts the close-out worksheet.

#### Travel, Italy & Honeymoon
- **Amadeus** (`amadeus-api`): Flight research for the Italy honeymoon Ryan is planning for the post-wedding window. OpenClaw tracks fares against a target and surfaces drops above 10%.
- **Airbnb** (`airbnb-api`): Italy honeymoon rental research and the occasional weekend trip with Emma. Naples, Sorrento, and Rome are the current shortlist.
- **Zillow** (`zillow-api`): Casual market watching for the post-wedding house search with Emma in Dearborn and west-Dearborn neighborhoods.
- **FedEx** (`fedex-api`): Outbound shipments for wedding favors and out-of-state guest welcome boxes.
- **UPS** (`ups-api`): Returns and household shipping. Default carrier for anything fragile.
- **Shippo** (`shippo-api`): Multi-carrier rate compare for wedding favor bulk shipping. OpenClaw runs the rate sweep before each batch.

#### Shopping & Marketplaces
- **Amazon Seller** (`amazon-seller-api`): Active distribution channel for the Heartland Free Dental Clinic's small patient-education zine Ryan helps print and ship. OpenClaw monitors orders and prints labels through Shippo.
- **Etsy** (`etsy-api`): Wedding favor sourcing, custom Italian-American touches for the reception, and a recurring gift source for Emma.
- **BigCommerce** (`bigcommerce-api`): Active storefront for the Heartland Free Dental Clinic's small branded merchandise (t-shirts, water bottles) sold at fundraisers. OpenClaw updates inventory after each Saturday.
- **WooCommerce** (`woocommerce-api`): Active companion storefront tied to the Heartland WordPress page, carrying the donor-only items not stocked on BigCommerce.

#### Music, Reading & Curiosity
- **Spotify** (`spotify-api`): Classic rock, Italian standards (Sinatra, Dean Martin), tarantella music for the wedding playlist, productivity podcasts during the commute.
- **YouTube** (`youtube-api`): Italian cooking content, wedding-planning tutorials, and the cooking shows Ryan watches on FaceTime with Grandma Rose.
- **TMDB** (`tmdb-api`): Movie lookups for Friday-night decompression with Emma.
- **Twitch** (`twitch-api`): One channel followed for a small cooking streamer Chris turned Ryan onto. OpenClaw drops the live alerts when a new episode goes up.
- **Vimeo** (`vimeo-api`): Higher-quality archive of dental continuing-education recordings and wedding videography samples from the photographer's portfolio.
- **Reddit** (`reddit-api`): Active under a quiet handle in r/weddingplanning, r/DentalHygiene, and a small Italian-American community. OpenClaw drafts the occasional post Ryan flags as worth asking and confirms before publishing.
- **Twitter** (`twitter-api`): Active light-posting account for Heartland clinic awareness moments. OpenClaw drafts the post tied to clinic news and confirms with Ryan before publishing.
- **LinkedIn** (`linkedin-api`): Light maintenance. Lakewood role, RDH credential, occasional volunteer-clinic posts. OpenClaw publishes the quarterly Heartland recap.
- **Instagram** (`instagram-api`): Wedding inspiration boards, Italian food accounts, and the Heartland clinic page Ryan helps post to.
- **Pinterest** (`pinterest-api`): Wedding board shared with Emma. Florals, table settings, Italian-American touches.
- **OpenLibrary** (`openlibrary-api`): Don DeLillo and Adriana Trigiani backlist lookups, plus dental therapy program textbook research.
- **NASA** (`nasa-api`): Wedding-day moon-phase and sunset-time lookups for the outdoor ceremony planning, and the occasional astronomy detail Ryan likes to share with Tyler.

#### Engineering, Site Reliability & Identity
- **GitHub** (`github-api`): Active workspace for the Lakewood patient-education content pilot. OpenClaw commits Ryan's drafted Markdown into the Contentful pipeline and tags releases for the WordPress publish cycle.
- **GitLab** (`gitlab-api`): Active mirror of the patient-education pipeline used for the dental therapy program prerequisite reading list Ryan is curating for himself and a small admissions cohort.
- **Datadog** (`datadog-api`): Active monitoring on the Heartland WordPress and BigCommerce stack. OpenClaw reviews the morning uptime report and surfaces incidents before they affect volunteer sign-up.
- **Sentry** (`sentry-api`): Active error tracking on the Heartland WordPress site and the Lakewood patient-education pilot. OpenClaw surfaces new errors at the 7:30 PM email pass.
- **Cloudflare** (`cloudflare-api`): Manages DNS, edge cache, and basic WAF rules for the Heartland Free Dental Clinic WordPress site Ryan co-maintains.
- **Kubernetes** (`kubernetes-api`): Active orchestration for the Heartland clinic's containerized WordPress instance and the patient-education pilot's preview environments. OpenClaw applies the deploy manifest when Ryan ships a content change.
- **PagerDuty** (`pagerduty-api`): Active on-call paging for the Heartland WordPress site during fundraiser weekends. Ryan is the secondary contact; OpenClaw acks the page first and triages before escalating.
- **Okta** (`okta-api`): Single sign-on for the continuing-education vendor portal, the Heartland staff workspaces, and the Lakewood internal training catalog.

#### HR, Hiring & Education
- **BambooHR** (`bamboohr-api`): Active HR system for the Heartland clinic's small staff. As volunteer coordinator Ryan reviews volunteer onboarding records and updates shift availability against the staff calendar.
- **Gusto** (`gusto-api`): Active payroll workspace for the Heartland clinic's two paid staff. Ryan reviews quarterly payroll with the coordinator; OpenClaw surfaces tax-form deadlines.
- **Greenhouse** (`greenhouse-api`): Active volunteer pipeline for the Heartland Free Dental Clinic. Application intake, screening, and shift onboarding flow through here.
- **Google Classroom** (`google-classroom-api`): Active for the prerequisite refresher modules Ryan is auditing as part of his dental therapy program research.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The assistant works only from the connected services listed above and from stored memory.
- Lakewood Family Dentistry's internal patient EMR is not connected. Treat it as a separate system. Patient information from Lakewood is out of scope.
- Emma's automotive-supplier work accounts are not connected. Anything from her work reaches you through Emma, not directly.
- Mike's auto repair shop business systems are not connected.
- Insurance carrier portals for Ryan's patients and the family health plan are not connected. Use email and confirmed contact only.
- Lakewood billing systems, patient billing, and clinic accounting beyond Ryan's own household-shared QuickBooks are out of scope.