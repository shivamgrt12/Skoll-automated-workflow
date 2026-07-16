# Tools: Darren Cash

## Tool Usage

### Connected Services

#### Email, Messaging & Voice

- **Gmail** (`gmail-api`): Personal account at `darren.cash@Greenridertech.co`. Academic email from Oakridge, research threads with Professor Whitfield, dive shop scheduling, and family logistics flow here.
- **Outlook** (`outlook-api`): Secondary mailbox for graduate school applications, since several programs default to Outlook for admissions correspondence.
- **WhatsApp** (`whatsapp-api`): Dive crew group chat with Cole and the Atlantic Reef instructors, plus the family thread. Drafts replies and triages incoming messages for his approval before anything sends.
- **Telegram** (`telegram-api`): Underwater photography group chat with a small ring of international shooters who trade location tips and rig builds. Drafts responses to gear-build questions and forwards location-tip threads worth saving.
- **Discord** (`discord-api`): Active in the marine bio undergrad server, the Carolina surf forecast community, and an underwater photography critique channel. Threads new study group posts and surfaces critique requests on his own photos.
- **Slack** (`slack-api`): Whitfield research group channel for daily lab logistics, sample handoffs, and weekend dive plans. Surfaces sample-handoff threads and dive-plan confirmations the morning of.
- **Microsoft Teams** (`microsoft-teams-api`): Ichthyology office hours and Oakridge marine sciences guest-lecture sessions. Joins on his calendar invite and captures lecture chat for later notes.
- **Twilio** (`twilio-api`): SMS scaffolding for portfolio print order confirmations and shift-swap nudges to Brett. Drafts queue for his per-message approval before going out.
- **SendGrid** (`sendgrid-api`): Transactional sender behind the portfolio mailing-list signup confirmations and the monthly underwater photo dispatch.
- **Mailgun** (`mailgun-api`): Backup transactional sender for portfolio print order receipts and password resets when SendGrid throttles.

#### Calendar, Meetings & Events

- **Google Calendar** (`google-calendar-api`): Personal calendar for classes, lab sessions, dive shop shifts, family visits, and research dives. Default timezone Eastern Time (Wilmington).
- **Calendly** (`calendly-api`): Booking link for tourists who want a private dive briefing and for print buyers picking up at the studio corner. Blocks class hours and ocean windows automatically.
- **Zoom** (`zoom-api`): Office hours with Professor Whitfield when she is off campus, grad school info sessions, and family check-ins when Brooke wants to show off a new art piece.
- **Eventbrite** (`eventbrite-api`): Carolina marine conservation talks, dive trade nights, and local art markets where he sells prints. Holds his RSVPs and ticket QR codes.

#### Documents, Notes & Drives

- **Notion** (`notion-api`): Personal workspace for the fish ID log (187 species), reading list, and graduate program comparison table.
- **Obsidian** (`obsidian-api`): Local thesis vault for daily research notes, observations from each survey dive, and protocol drafts.
- **Confluence** (`confluence-api`): Oakridge marine sciences lab protocols he contributes to and references before every survey dive.
- **Airtable** (`airtable-api`): Research dive base tracking site, depth, visibility, transect counts, and photo references for Wrightsville Sound surveys.
- **Typeform** (`typeform-api`): PADI student intake forms for Atlantic Reef Dive Co., portfolio print order forms, and research participant surveys.
- **DocuSign** (`docusign-api`): Dive shop liability waivers, lease renewal, student loan paperwork, and portfolio print licensing agreements.
- **WordPress** (`wordpress-api`): Underwater photography portfolio site with photo galleries, dive log entries, and the print storefront.

#### Research, Science & Learning

- **NASA** (`nasa-api`): Sea surface temperature data and ocean color imagery for the Carolina coast. Feeds context for coral stress windows.
- **OpenWeather** (`openweather-api`): Marine forecast, swell, wind, and barometric pressure. Cross-check against Surfline before any morning call.
- **OpenLibrary** (`openlibrary-api`): Marine biology textbooks, ocean essays, and the steady drip of pop science he reads between exams.
- **Google Classroom** (`google-classroom-api`): Oakridge course pages for Marine Ecology, Organic Chemistry, and upcoming Ichthyology and Biostatistics. Surface assignment due dates.

#### Code, Dev, Web & Cloud

- **GitHub** (`github-api`): Repository for R scripts and Python notebooks supporting the coral recovery analysis. Shared with Professor Whitfield. Keep commit messages plain English.
- **GitLab** (`gitlab-api`): Oakridge-hosted instance for the lab's CS-adjacent class projects and the portfolio site's deploy pipeline.
- **Linear** (`linear-api`): Dive shop tooling tickets, equipment maintenance, gear orders, and shift swap requests.
- **Jira** (`jira-api`): Oakridge research IT ticket system for lab equipment requests and software access.
- **Asana** (`asana-api`): Wrightsville Sound research project board tracking seasonal milestones with Professor Whitfield.
- **Monday** (`monday-api`): Brett's dive shop scheduling board where Darren picks up shift swaps and gear maintenance assignments.
- **Trello** (`trello-api`): Honors thesis sub-tasks and grad school application checklist.
- **Sentry** (`sentry-api`): Error monitoring on the portfolio site so broken galleries surface before customers see them.
- **Datadog** (`datadog-api`): Uptime and latency monitoring for the portfolio site and the print storefront.
- **Kubernetes** (`kubernetes-api`): Oakridge research compute cluster runs marine ecology image-processing jobs (coral cover segmentation) on the lab's shared pod.
- **Cloudflare** (`cloudflare-api`): CDN and edge protection in front of the portfolio site and the print storefront.
- **Figma** (`figma-api`): Poster layouts for the undergrad research symposium and portfolio print mockups.
- **Webflow** (`webflow-api`): Frontend for the portfolio landing page and the print store, kept in sync with the WordPress galleries.
- **Contentful** (`contentful-api`): CMS holding portfolio photo entries, captions, dive metadata, and species tags.
- **Algolia** (`algolia-api`): On-site search across the portfolio photo library by species, location, and depth.
- **Google Analytics** (`google-analytics-api`): Portfolio site traffic, referrers, and which print pages are converting.
- **PostHog** (`posthog-api`): Behavior analytics on portfolio engagement and session replay on the print checkout flow.

#### Operations, HR & Identity

- **Zendesk** (`zendesk-api`): Vendor tickets for Surfline, GoPro, and the credit union.
- **Freshdesk** (`freshdesk-api`): Customer support inbox for portfolio print buyers when there is a shipping or licensing question.
- **Intercom** (`intercom-api`): Live chat widget on the portfolio site for incoming print inquiries and student-dive booking questions.
- **ServiceNow** (`servicenow-api`): Oakridge campus ticket system for building access, key cards, and lab safety incident reports.
- **PagerDuty** (`pagerduty-api`): Storm and swell threshold alerts wired through the OpenWeather integration when conditions cross an unsafe-dive line.
- **Okta** (`okta-api`): SSO for personal subscriptions and the Oakridge research portal. Surface password rotation prompts the day they appear.
- **BambooHR** (`bamboohr-api`): Atlantic Reef Dive Co. HR records: W-4, dive instructor certification copies, and emergency contact info.
- **Greenhouse** (`greenhouse-api`): Tracker for pending graduate program applications and assistantship interview steps. Holds candidate-side responses and stage transitions.
- **Gusto** (`gusto-api`): Pay stubs and W-2s from Atlantic Reef Dive Co., plus the year-end tip summary.

#### Finance, Payments & Investing

- **Stripe** (`stripe-api`): Payment processor for portfolio print orders and the occasional licensing fee.
- **Plaid** (`plaid-api`): Bridge for monthly budget views across the credit union checking and savings accounts.
- **PayPal** (`paypal-api`): Splitting bills with Cole and gear group buys with the dive crew.
- **Square** (`square-api`): In-person POS at the art markets where he sells prints alongside the dive shop booth.
- **Alpaca** (`alpaca-api`): Micro Roth IRA contributions from print sale fees and seasonal tip earnings, quarterly buys of a low-cost index ETF.
- **Coinbase** (`coinbase-api`): Primary crypto wallet. Holds USDC and a small BTC stack from print sale fees, with $25 monthly DCA buys he runs as a long-horizon hedge against the off-peak income dip.
- **Binance** (`binance-api`): Active position in a small ocean-cleanup token Cole flagged from a marine conservation Reddit thread. Reviews weekly, takes profit into the print-gig revenue account.
- **Kraken** (`kraken-api`): Where USDC from international print buyers lands before he transfers to the credit union, since the conversion beats the bank's foreign-transfer fees.
- **QuickBooks** (`quickbooks-api`): Bookkeeping for the underwater photography print side gig: income, expenses, and mileage to art markets.
- **Xero** (`xero-api`): Quarter-by-quarter 1099 prep workbook for the print gig, so the spring self-employment tax filing window is a one-day job instead of a one-week scramble.

#### Marketing, Sales & Audience

- **HubSpot** (`hubspot-api`): CRM-lite tracking prospective graduate school program contacts, admissions officers, and current research collaborators.
- **Salesforce** (`salesforce-api`): Oakridge career center alumni network outreach for grad school informational interviews.
- **Mailchimp** (`mailchimp-api`): Sends the monthly underwater photo dispatch newsletter to the portfolio mailing list.
- **Klaviyo** (`klaviyo-api`): Automated sequences for print buyers: order confirmation, shipping update, post-purchase review ask.
- **Segment** (`segment-api`): Routes portfolio site visitor events into Mixpanel, Amplitude, and Google Analytics.
- **Mixpanel** (`mixpanel-api`): Funnel analytics on the portfolio site from gallery view to print purchase.
- **Amplitude** (`amplitude-api`): Retention analysis on returning portfolio visitors and newsletter subscribers.
- **ActiveCampaign** (`activecampaign-api`): Drip campaign nurturing grad school program contacts toward an info interview.

#### Commerce, Travel & Local Life

- **Amazon Seller** (`amazon-seller-api`): Underwater prints listed on Amazon Handmade, primarily smaller framed pieces.
- **Etsy** (`etsy-api`): Storefront for limited-run underwater prints and pottery collaborations with a Wilmington ceramics maker, and a buyer account for gifts to Mom, Grandma Dorothy, and Brooke.
- **BigCommerce** (`bigcommerce-api`): Alternative storefront for higher-margin large-format prints.
- **WooCommerce** (`woocommerce-api`): WordPress-integrated print checkout on the main portfolio site.
- **Instacart** (`instacart-api`): Grocery runs during big swell windows when the surf is too good to leave.
- **DoorDash** (`doordash-api`): Late-night study orders during finals. Default to local seafood shacks over chains.
- **Airbnb** (`airbnb-api`): Camp-style stays for field trips and grad school visit weekends. Filter for parking that fits the 4Runner.
- **Uber** (`uber-api`): Rides home from Front Street Brewery when he and Cole are out. Keep cars at the apartment.
- **Amadeus** (`amadeus-api`): Flight research for graduate school campus visits. Aisle seats and morning arrivals.
- **FedEx** (`fedex-api`): Personal shipping and print orders going to out-of-state buyers.
- **UPS** (`ups-api`): Personal returns and overflow print shipments.
- **Shippo** (`shippo-api`): Multi-carrier label printing for portfolio print orders, rate-shops UPS, FedEx, and USPS.
- **Zillow** (`zillow-api`): Scanning rentals near short-list grad programs as he narrows the list.
- **Google Maps** (`google-maps-api`): Routes to remote dive sites, Croatan trailheads, and the drive down to Southport. Avoid traffic into Wilmington on summer weekends.
- **Yelp** (`yelp-api`): Sweet tea spots, local seafood shacks, and coffee on the way to early shifts. Skip tourist traps.

#### Health, Fitness & Home Monitoring

- **MyFitnessPal** (`myfitnesspal-api`): Hydration and protein tracking around long dive days. No calorie pressure.
- **Strava** (`strava-api`): Ocean swim sessions and beach run mileage, synced from his iPhone to keep cardio baseline visible during exam weeks.
- **Ring** (`ring-api`): Doorbell at Grandma Dorothy's place in Southport so he can check on porch deliveries when he is not there.

#### Media, Social & Discovery

- **YouTube** (`youtube-api`): Surf forecast videos, marine biology lectures, John Mayer acoustic sessions, and dive technique breakdowns.
- **Vimeo** (`vimeo-api`): Hosts his longer underwater dive video edits for portfolio embeds.
- **Spotify** (`spotify-api`): Premium account. Southern rock, Americana, John Mayer, lo-fi for studying, acoustic guitar playlists when he is homesick.
- **Twitch** (`twitch-api`): Occasional dive prep and gear setup streams for the underwater photography community.
- **TMDB** (`tmdb-api`): Movie lookups before a rare night in with Cole.
- **Twitter** (`twitter-api`): Active marine bio account sharing dive findings, NOAA reposts, and Carolina conservation news.
- **LinkedIn** (`linkedin-api`): Current profile maintained for graduate school applications and conservation job leads.
- **Reddit** (`reddit-api`): Active poster in r/marinebiology, r/scuba, and r/Wilmington for local notes.
- **Pinterest** (`pinterest-api`): Composition inspiration board for underwater photography: light angles, kelp shapes, color grading.
- **Instagram** (`instagram-api`): Underwater photography posts at `@darren.cash.underwater`, about 800 followers. Drafts captions, schedules timing, and tags species; final approval and the post action stay with him.
- **Ticketmaster** (`ticketmaster-api`): Tyler Childers, Jason Isbell, and Allman Brothers tribute tour alerts when they come through North Carolina.

#### Not Connected

- Cloud file drives (Google Drive, Dropbox, Box) are not available to this agent. Deliverables are written to the local `data/` workspace, not to a cloud drive.
- Live web search, web browsing, and deep internet research are not available. The agent works only from the connected services listed above and from stored memory.
- Banking apps at the local credit union and Venmo. Phone only.
- Surfline Premium and the Tides Near Me app. Phone only. Pull conditions through OpenWeather here.
- His parents' and Grandma Dorothy's private accounts. Coordinate through Darren or through the family WhatsApp thread.
- Atlantic Reef Dive Co. internal booking system. Brett owns the master, Darren works from his weekly schedule and the Asana view.
- Oakridge University course management portal beyond the Google Classroom feed. Final grades and tuition flow through the registrar, not this agent.
