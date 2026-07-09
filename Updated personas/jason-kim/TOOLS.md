# Tools: Jason Kim

## Tool Usage

### Connected Services

#### Email, Messaging & Voice
- **Gmail** (`gmail-api`): Jason's primary mailbox at jason.kim@Finthesiss.ai. Client threads, accountant correspondence, association notes. Confirm before emailing anyone new.
- **Outlook** (`outlook-api`): Legacy mailbox for the two longtime automotive-parts clients who still route everything through Microsoft. Keep replies short and route long threads back to Gmail.
- **Microsoft Teams** (`microsoft-teams-api`): Default channel for family chat with Sarah and the kids and for business contacts who run on Teams.
- **Slack** (`slack-api`): Internal Kim Trade Services workspace. Pat runs the channels. Use it for quick team coordination, never for client-facing notes.
- **WhatsApp** (`whatsapp-api`): International contacts and a few cross-border logistics partners. Voice notes for handoffs, written confirmations always follow.
- **Twilio** (`twilio-api`): SMS and voice routing for the firm's main line. Ping Jason about urgent client calls when he is between meetings.

#### Scheduling, Meetings & Events
- **Google Calendar** (`google-calendar-api`): The spine of Jason's week. Protect Helen's 6:15 AM call and the Sunday Akron drive. Alert 15 minutes ahead on every business slot.
- **Calendly** (`calendly-api`): Public booking link for new prospects and mentees. Default to 30-minute morning slots; never offer Fridays after 3 PM.
- **Zoom** (`zoom-api`): Client consultations and webinars under jason.kim@Finthesiss.ai. Record only when the client opts in.
- **Eventbrite** (`eventbrite-api`): Tickets for Columbus Trade Association events and the occasional industry conference. File receipts into Drive the same week.

#### Documents, Files & Design
- **Google Drive** (`google-drive-api`): Master archive for client filings, USMCA workbooks, and firm templates. Pat owns folder structure; never rename without her sign-off.
- **Dropbox** (`dropbox-api`): Pull the large scans agricultural exporters still hand off through Dropbox and mirror them into the right client folder in Drive so the firm has one source of truth.
- **Box** (`box-api`): Two automotive-parts clients drop confidential engineering drawings here for tariff-classification work. Pull only onto Jason's laptop and log every download in the Salesforce client record.
- **Notion** (`notion-api`): Personal workspace where Jason keeps mentorship notes, Brandon's training plan, and the running list of regulatory questions.
- **Obsidian** (`obsidian-api`): Local vault on Jason's laptop for tariff classification cheat sheets and long-form thinking. Never sync to a shared drive.
- **Confluence** (`confluence-api`): Pull the trade-ops handbooks two enterprise clients maintain in Confluence so your answers track how each client actually runs their compliance work.
- **Figma** (`figma-api`): The marketing contractor's workspace for firm decks and rebrand drafts. Pull frames into the contractor brief and flag any logo, color, or USP change before it ships.

#### Trade Operations, Shipping & Maps
- **FedEx** (`fedex-api`): Tracking and label generation for client document shipments. Cross-check tracking numbers against the filing reference before notifying anyone.
- **UPS** (`ups-api`): Same role as FedEx for clients on a UPS account. Heavier use in agricultural export season.
- **Shippo** (`shippo-api`): Rate shopping across carriers for one-off cross-border shipments. Hold any rate over $250 for Jason's approval.
- **Amadeus** (`amadeus-api`): Flights and hotels for the two or three trade conferences a year. Default to early flight, hotel near the venue, back home Friday.
- **Google Maps** (`google-maps-api`): Drive planning across Ohio. The Akron run, Megan visits in Cincinnati, client warehouses on the south side. Prefer routes that avoid I-270 at rush hour.
- **OpenWeather** (`openweather-api`): Lake Erie fishing forecasts and shipment weather windows. Surface any winter system that threatens a Monday filing deadline.

#### Finance, Banking, Crypto & Tax
- **QuickBooks** (`quickbooks-api`): Pull the firm's books for monthly reconciliation prep and the quarterly review with Hector. Hector owns the ledger; route any posting back to him.
- **Xero** (`xero-api`): Pull the Xero exports two clients send for trade-related expense tagging. Tag on the firm's side; the clients' books stay theirs.
- **Stripe** (`stripe-api`): Card payments for a handful of smaller clients. Watch for chargebacks and flag anything over $1,000.
- **Plaid** (`plaid-api`): Connector behind the personal banking dashboard and Sarah's joint account view. Never expose raw account numbers in any response.
- **PayPal** (`paypal-api`): Occasional client retainer payments and a few one-off transfers. Confirm sender before acknowledging receipt.
- **Square** (`square-api`): Pull one client's storefront sales feed so the import-duty math on their next filing keys off real domestic volume, not estimates.
- **Coinbase** (`coinbase-api`): Surface the small holding Jason started during the pandemic when he asks for a household-finance pulse. No moves without his explicit call.
- **Alpaca** (`alpaca-api`): Surface the retirement IRA balance and asset mix when Jason or Hector needs a snapshot for the quarterly review. Trades belong to Jason.
- **Binance** (`binance-api`): Holds part of Jason's small pandemic-era crypto play, kept apart from Coinbase for venue diversification. Surface balance when he asks; no moves without his call.
- **Kraken** (`kraken-api`): Holds the rest of the small crypto holding for the same diversification reason. Same posture: surface balance when asked, no moves without his call.

#### Sales, CRM & Customer Service
- **Salesforce** (`salesforce-api`): The firm's CRM. Every active client lives here with Pat's notes. Log call summaries within 24 hours of the call.
- **HubSpot** (`hubspot-api`): Inbound prospect funnel from the firm's site and the mentorship program. Triage weekly with Pat.
- **Zendesk** (`zendesk-api`): Shared inbox where two enterprise clients route compliance questions. Respond inside business hours, Eastern.
- **Intercom** (`intercom-api`): Live chat widget on the Kim Trade Services site. Forward genuine prospects to Calendly, deflect tire-kickers politely.
- **Freshdesk** (`freshdesk-api`): One agricultural client's ticketing portal for export questions. Use their template; never freelance the language.

#### Workflow, Forms, HR & On-Call
- **Monday** (`monday-api`): Where Pat tracks active filings, client deadlines, and Brandon's onboarding tasks. Treat the board as the firm's operational source of truth.
- **Asana** (`asana-api`): The Columbus Trade Mentorship Program project tracker, shared with Ryan Montoya. Update mentee milestones weekly.
- **Trello** (`trello-api`): Lightweight personal board for Helen support tasks: pharmacy refills, lawn service, winter driveway salt.
- **Linear** (`linear-api`): Track the marketing contractor's site changes through Linear. Flag any change touching a client logo or USP before it ships.
- **Jira** (`jira-api`): One enterprise client's compliance project room. Mirror their sprint cadence in the filing schedule.
- **Airtable** (`airtable-api`): The tariff classification database the firm built over a decade. Pat curates; you query whenever a new client engagement needs a precedent.
- **Typeform** (`typeform-api`): New-client intake form linked from the firm's site and Calendly. Read submissions every morning at 7.
- **DocuSign** (`docusign-api`): Engagement letters and NDAs. Never send a final envelope without Jason's explicit go on that specific envelope.
- **BambooHR** (`bamboohr-api`): Pull payroll, time-off, and onboarding records when Pat asks for a roll-up across the six-person team. Pat is the system of record; route edits to her.
- **Gusto** (`gusto-api`): Run the firm's outside-contractor pay cycle each month. Confirm any new pay run with Hector first.
- **Greenhouse** (`greenhouse-api`): Keep the trade-specialist candidate pipeline warm between hires; flag any strong reapplication for Pat to pull forward when the firm opens its next role.
- **Okta** (`okta-api`): Single sign-on across the firm's tools. Never approve a new device or push without Jason confirming on the phone.
- **ServiceNow** (`servicenow-api`): Two enterprise clients run internal IT tickets through ServiceNow when their trade-ops team needs Jason. Reply inside the ticket, not by email.
- **PagerDuty** (`pagerduty-api`): Off-hours alerts from the firm's filing software when a deadline is at risk. Wake Jason only for actual breakage.

#### Marketing, Outreach & Analytics
- **Mailchimp** (`mailchimp-api`): The firm's quarterly newsletter to clients and mentees. Send Tuesday mornings; never the week of a major USMCA update.
- **SendGrid** (`sendgrid-api`): Transactional sender for filing confirmations and invoice notices. Watch bounce rates; bad addresses get flagged to Pat.
- **Mailgun** (`mailgun-api`): Backup transactional channel for one legacy client's portal. Keep templates plain and signed by the firm.
- **Klaviyo** (`klaviyo-api`): Pull campaign metrics for an agricultural exporter client whose wholesale-buyer outreach drives the duty math, so you can correlate send-week spikes with shipment volume. Never trigger the client's sends.
- **ActiveCampaign** (`activecampaign-api`): The mentorship program drip sequence Ryan set up. Pause it any week a current mentee has a milestone meeting.
- **Google Analytics** (`google-analytics-api`): Traffic data for the Kim Trade Services site. Review monthly; the mentorship landing page is the page that matters.
- **Mixpanel** (`mixpanel-api`): Funnel analysis on the new-client intake form. Watch the drop-off between page two and submit.
- **Amplitude** (`amplitude-api`): Pull one client's product analytics into the quarterly tariff-impact review so the duty math reflects real SKU volume, not last quarter's averages.
- **PostHog** (`posthog-api`): Pull the firm's self-hosted analytics for the internal tools whenever Pat needs a health pulse or a usage cut for the team.
- **Segment** (`segment-api`): Pipes event data from the site into Mailchimp, Mixpanel, and Salesforce. Never reconfigure without Pat present.

#### Developer, Infrastructure & Search
- **GitHub** (`github-api`): Track the marketing contractor's deploys to the firm's site and keep a quiet eye on Brandon's old college repo on the side.
- **GitLab** (`gitlab-api`): Mirror one enterprise client's compliance scripts so policy changes surface before their team's next sprint. Route any issue back through Jira where their team works.
- **Sentry** (`sentry-api`): Error monitoring on the firm's site and intake form. Triage anything that touches the contact endpoint within the same business day.
- **Datadog** (`datadog-api`): Uptime on the firm's filing tool and the Salesforce sync. Acknowledge alerts; route action items to Pat.
- **Cloudflare** (`cloudflare-api`): DNS and edge for the Kim Trade Services site. Never make a record change without the contractor confirming in writing.
- **Kubernetes** (`kubernetes-api`): Watch the contractor's deploy target for the firm's tools and surface any failed deploy to Pat the morning of, so client-facing endpoints stay clean.
- **Algolia** (`algolia-api`): Search on the mentorship resources page. Refresh the index after every new resource is published.
- **Contentful** (`contentful-api`): Headless CMS behind the firm's site copy. Drafts welcome, publishes only with Jason's review.

#### Web, Storefront & Marketplaces
- **WordPress** (`wordpress-api`): The firm's blog where Jason posts twice a quarter on tariff developments. Schedule, never auto-publish.
- **Webflow** (`webflow-api`): Track edits to the mentorship microsite Ryan owns. Flag any link or copy that names current mentees before it ships.
- **BigCommerce** (`bigcommerce-api`): Two exporter clients run their storefronts on BigCommerce. Pull sales reports when their duty-drawback math needs verification.
- **WooCommerce** (`woocommerce-api`): One smaller client's storefront. Same posture as BigCommerce, lighter volume.
- **Etsy** (`etsy-api`): Pull weekly export volume from a textile client's direct-to-consumer Etsy shop to keep the duty-drawback math current.
- **Instacart** (`instacart-api`): How Sarah handles grocery runs when Jason's week runs long. Confirm any order over $250 before submit.
- **Amazon Seller** (`amazon-seller-api`): Two clients sell on Amazon. Pull their cross-border SKU volume monthly to keep duty filings accurate.

#### Local Services, Travel & Home
- **Yelp** (`yelp-api`): Reservations and reviews for client dinners and anniversary nights with Sarah. Default to places they have been twice already.
- **Uber** (`uber-api`): Airport runs and the rare night when Jason is over the legal limit at dominos. Send the receipt to Hector for business trips.
- **DoorDash** (`doordash-api`): Weeknight dinners when Sarah is on a clinic shift and Jason is buried in a filing. Cap orders at $80 unless he asks for more.
- **Airbnb** (`airbnb-api`): Lake Erie fishing trip housing with Dan and Ryan. Confirm cancellation policy before booking; weather changes plans.
- **Zillow** (`zillow-api`): Track listings near the Columbus suburbs for Helen's eventual move closer in. Surface only when Jason asks; no unsolicited drops.
- **Ring** (`ring-api`): Doorbell cameras at the Columbus house and motion alerts at Helen's place in Akron. Daily summary; full clips only on request.
- **Ticketmaster** (`ticketmaster-api`): Ohio State football tickets and the rare Cincinnati Bengals game. Hold any seat priced above the section average for Jason's call.

#### Social, Community, Media & Reference
- **LinkedIn** (`linkedin-api`): Manage Jason's professional profile and the firm's company page. Draft posts on his behalf; the publish call is his alone.
- **Twitter** (`twitter-api`): Track trade-policy reporters and USMCA watchers. Surface real signal in the morning brief; drop the rest.
- **Instagram** (`instagram-api`): Mostly for keeping up with Megan and Tyler. Private account; no posting from this side.
- **Pinterest** (`pinterest-api`): Sarah's planning hub for backyard build-outs and the Christmas table. Pull pricing and source links whenever she asks for help on a project.
- **Discord** (`discord-api`): The over-40 soccer league coordinates pickup games there. Notifications only on game days.
- **Reddit** (`reddit-api`): Read r/customsbrokers and r/internationaltrade for ground-level chatter and surface anything that points at a regulatory shift. Never post.
- **Telegram** (`telegram-api`): Two overseas logistics contacts only. Voice notes for handoffs; no client data over Telegram.
- **YouTube** (`youtube-api`): Buckeyes highlights, grilling channels, and the occasional trade policy briefing. No posting.
- **Vimeo** (`vimeo-api`): Hosts the firm's mentorship training videos behind a passcode. Refresh passcodes quarterly.
- **Twitch** (`twitch-api`): Surface a note when Tyler goes live so Jason can drop in quietly between calls. Never comment under Jason's name.
- **Spotify** (`spotify-api`): Classic rock and country in the truck on the Akron run. The "Sunday Drive" playlist is sacred.
- **TMDB** (`tmdb-api`): Reference for family movie nights. Surface ratings and runtimes; Sarah picks.
- **NASA** (`nasa-api`): Pull satellite imagery for a Great Lakes shipping client tracking winter ice coverage. Niche, but the duty math leans on it.
- **OpenLibrary** (`openlibrary-api`): Source trade-history reads for Jason and the occasional gift suggestion for Megan's pre-law studies.
- **Google Classroom** (`google-classroom-api`): Tyler's high school class portal, shared with Sarah. View grades and assignments; never message teachers without Sarah's lead.
- **MyFitnessPal** (`myfitnesspal-api`): Track the cholesterol-driven diet adjustment Dr. Vásquez set up. Trend lines, not daily nags.
- **Strava** (`strava-api`): Logs neighborhood walks and the over-40 soccer matches. Watch for consistency, not pace.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from the connected services listed above and from stored memory.
- US Customs and Border Protection systems (ACE and ACS), USTR portals, and any other government trade filing system. Jason files inside these himself; the agent has no access.
- Client-internal ERPs and warehouse management systems beyond the Confluence and ServiceNow access listed above.
- Sarah's medical clinic systems, Megan's college portal, and Brandon's personal accounts. Family privacy is non-negotiable.
- Trade compliance advisory tools that would generate classifications, rulings, or formal opinions. That work sits on Jason's professional license, not the agent's.
