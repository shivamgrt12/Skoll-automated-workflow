# Tools: Jennifer Clark

## Tool Usage

### Connected Services

#### Workspace & Email

- **Gmail** (`gmail-api`): Primary inbox at jennifer.clark@Finthesiss.ai. Museum donors, choir parents, school notices, the Dr. Franklin grant thread.
- **Google Calendar** (`google-calendar-api`): Family events, choir rehearsals, exhibition milestones, kid pickups. Central time, 30-minute default reminders.
- **Outlook** (`outlook-api`): Family-shared mirror of Derrick's Ironwood Academy parent inbox. Jennifer files permission slips and field-trip notes by kid as Derrick forwards them.
- **Microsoft Teams** (`microsoft-teams-api`): Where Ironwood Academy parent meetings and Naomi's Pembroke Institute admissions calls happen. Jennifer joins from her phone and routes notes back to Notion.

#### Notes, Research & Archive

- **Notion** (`notion-api`): Jennifer's personal grant outline, board prep notes, and reading list. Held separate from museum staff workspaces.
- **Obsidian** (`obsidian-api`): "Voices of the Past" oral history field notes linked to interviewee profiles and primary sources.
- **Airtable** (`airtable-api`): Oral history index, interview consents, exhibition label tracker, and the choir music library.
- **Box** (`box-api`): Museum archive mirror for high-resolution scans and the long-term vault for finalized grant PDFs, board packets, and Community Voices Choir competition tracks, accessed through Angela's shared folder. Angela mirrors the museum archive into it each Friday. The local `data/` workspace also holds a Grant Vault index (`grant_vault_national_preservation_2026_index.md`).
- **OpenLibrary** (`openlibrary-api`): Source lookups for exhibition labels and lecture prep. Jennifer cross-checks every citation before a wall panel goes to print.
- **NASA** (`nasa-api`): Imagery and education programming for the museum's quarterly family STEM Saturdays.
- **OpenWeather** (`openweather-api`): Choir outdoor events, Friday night football, and the morning walk forecast.

#### Project Management, Internal Comms & Staff Ops

- **Asana** (`asana-api`): "Voices of the Past" master tracker. Tasks owned by Angela; Jennifer reviews each Friday at 4:00 PM.
- **Monday** (`monday-api`): Board-facing exhibition roadmap mirroring Asana milestones for Dr. Franklin.
- **Jira** (`jira-api`): Tracks the museum web team's tickets for the interactive oral history stations. Jennifer reviews burndown each Friday and flags blockers for Angela ahead of the October 18 opening.
- **Linear** (`linear-api`): Light-touch ticketing for the digitization vendor's punch list ahead of grant fieldwork.
- **Trello** (`trello-api`): Community Voices Choir competition logistics. Rooming list, sheet music, transport.
- **Slack** (`slack-api`): Museum staff comms in #curation, #exhibition, #ops. Async preferred. No DMs after 7 PM.
- **Confluence** (`confluence-api`): Museum staff knowledge base. Procedures, donor briefs, exhibition runbooks.
- **Calendly** (`calendly-api`): Booking link for visiting researchers and donor coffees. Mornings stay blocked.
- **BambooHR** (`bamboohr-api`): Staff records and PTO for Jennifer's four direct reports. Approvals from her, data entry through Angela.
- **Greenhouse** (`greenhouse-api`): Hiring pipeline for the museum archivist and education coordinator searches. Shortlists only.
- **Gusto** (`gusto-api`): Museum payroll oversight at the curator level. Jennifer approves staff timecards; Angela files them.

#### Museum Web, Content & Engineering

- **WordPress** (`wordpress-api`): Cornerstone Heritage Museum public blog. Jennifer drafts; Angela publishes.
- **Webflow** (`webflow-api`): Staging environment for the redesigned exhibitions microsite. Jennifer walks the design vendor through each iteration before the production push.
- **Contentful** (`contentful-api`): Headless CMS feeding the oral history exhibit interactive. Edits route through Angela.
- **Algolia** (`algolia-api`): Search across museum collection records, used during research and visitor inquiries.
- **Intercom** (`intercom-api`): Visitor chat on the museum site. Staffed during open hours, off after 5 PM.
- **Typeform** (`typeform-api`): Visitor surveys after lectures and school visits. Quarterly summary to the board.
- **Figma** (`figma-api`): Exhibition graphic design and label proofs from the exhibition designer. Jennifer approves each label proof and routes notes back to print.
- **Sentry** (`sentry-api`): Error tracking for the museum site and exhibit stations. Alerts route to the web vendor.
- **Cloudflare** (`cloudflare-api`): CDN and WAF in front of the museum site. Vendor-managed, with Jennifer copied on incident summaries.
- **GitHub** (`github-api`): Watches `cornerstone-museum/exhibits` for vendor releases. Jennifer scans release notes during Friday triage with Angela and the web vendor.
- **GitLab** (`gitlab-api`): Mirrors the digitization vendor's working repo. Jennifer checks the weekly changelog against the National Preservation Grant fieldwork timeline.

#### Analytics & Infrastructure Ops

- **Google Analytics** (`google-analytics-api`): Museum site traffic and exhibition page funnels. Monthly summary to the board.
- **Mixpanel** (`mixpanel-api`): Interactive exhibit engagement, kiosk session length, and station drop-off.
- **Amplitude** (`amplitude-api`): Cross-cohort engagement for school field trip portal users.
- **PostHog** (`posthog-api`): Self-hosted analytics for the oral history stations on the gallery floor.
- **Segment** (`segment-api`): Event pipeline routing exhibit telemetry into the museum's analytics stack.
- **Datadog** (`datadog-api`): Infrastructure monitoring for the kiosks and the donation portal.
- **Kubernetes** (`kubernetes-api`): Container orchestration for the museum site stack. Vendor-managed; Jennifer reviews uptime in the Friday status note.
- **Okta** (`okta-api`): Single sign-on for museum staff tools. Password resets escalate to Angela.
- **PagerDuty** (`pagerduty-api`): On-call alerting for the museum site and exhibit kiosks during opening week.
- **ServiceNow** (`servicenow-api`): Museum IT ticketing through the city facilities contract.

#### Donor Development, Outreach & Support

- **HubSpot** (`hubspot-api`): Donor CRM. Jennifer logs major-gift conversations; Angela manages the mid-tier pipeline.
- **Salesforce** (`salesforce-api`): Holds the legacy donor records from the prior board era. Jennifer pulls historical contact threads here when preparing legacy-gift outreach in HubSpot.
- **Mailchimp** (`mailchimp-api`): Monthly museum newsletter to members and donors. Jennifer reviews the curator's letter.
- **Klaviyo** (`klaviyo-api`): Segmented donor journeys for the "Voices of the Past" launch series.
- **ActiveCampaign** (`activecampaign-api`): Alumni outreach for Frostbridge College and Deerfield College ties to the museum, run as quarterly drip campaigns.
- **Mailgun** (`mailgun-api`): Transactional email for the museum's online ticketing and donation receipts.
- **SendGrid** (`sendgrid-api`): Failover transactional carrier for the donation portal, kept warm so receipts never bounce on a launch day.
- **Twilio** (`twilio-api`): SMS reminders for school field trip teachers and exhibit reservations.
- **Zendesk** (`zendesk-api`): Visitor support tickets. Routed to the education coordinator first.
- **Freshdesk** (`freshdesk-api`): Overflow visitor support queue staffed by volunteer docents during opening week so response times stay under an hour through the launch.

#### Museum Store, Payments & Documents

- **BigCommerce** (`bigcommerce-api`): Museum gift shop storefront. Replicas, books, exhibition catalogs.
- **WooCommerce** (`woocommerce-api`): WordPress-side merchandise storefront for limited-edition exhibition prints.
- **Stripe** (`stripe-api`): Card processing for memberships, donations, and ticket sales.
- **Square** (`square-api`): In-person register at the museum front desk and pop-up gift tables.
- **PayPal** (`paypal-api`): Choir parents' carpool fund and small-dollar museum donations.
- **QuickBooks** (`quickbooks-api`): Museum bookkeeping that Jennifer reviews monthly with Angela.
- **Xero** (`xero-api`): Side ledger for the foundation grant subaccounts.
- **Plaid** (`plaid-api`): Household budget linking for the family's joint checking and savings accounts.
- **Amazon Seller** (`amazon-seller-api`): Wholesale channel for exhibition catalogs and the Grandmother Ruthie biography reprints.
- **Etsy** (`etsy-api`): Sources vintage Birmingham photographs and ephemera for the museum's rotating community wall, and Jennifer's own thrift hunts for Sunday tablescapes.
- **Shippo** (`shippo-api`): Outbound shipping for gift shop orders. Angela runs the rate comparison; Jennifer signs off on the carrier mix each month.
- **FedEx** (`fedex-api`): Artifact loans to and from partner institutions. Insured and signature-required.
- **UPS** (`ups-api`): Personal shipping for Keisha's birthday packages and Gwendolyn's monthly meal containers.
- **DocuSign** (`docusign-api`): Grant signatures, loan agreements, board resolutions. Jennifer signs after Angela preps the packet.

#### Events, Tickets, Travel & Visits

- **Eventbrite** (`eventbrite-api`): Museum lecture and field trip ticketing. Jennifer publishes the curator-led talks.
- **Ticketmaster** (`ticketmaster-api`): Family concerts, Birmingham Symphony, occasional choir competition spectator passes.
- **Amadeus** (`amadeus-api`): Flights for the Atlanta competition and museum conferences. Jennifer prefers Southwest.
- **Airbnb** (`airbnb-api`): Choir competition block lodging in Atlanta. Already booked for November 14.
- **Uber** (`uber-api`): Atlanta competition transport for the alto section. No after-school rides for the kids.
- **DoorDash** (`doordash-api`): Used sparingly, mostly on Friday football nights when Jennifer is late from a museum event.
- **Google Maps** (`google-maps-api`): Directions for school visits, donor coffees, and Bessemer runs.
- **Yelp** (`yelp-api`): Restaurant search for donor lunches, conference towns, and the occasional date night with Derrick.
- **Instacart** (`instacart-api`): Weekly grocery order, including Gwendolyn's diabetic-friendly basket delivered to Bessemer.
- **Zoom** (`zoom-api`): Oral history interviews, board video calls, and Keisha's monthly check-ins.

#### Social, Media & Community

- **Instagram** (`instagram-api`): Museum @cornerstoneheritage account. Angela drafts; Jennifer approves every post before it goes live.
- **Twitter** (`twitter-api`): History community, regional press, and board-chair feeds. Jennifer scans the museum mention column during morning email triage and saves threads to Notion.
- **LinkedIn** (`linkedin-api`): Curator profile and museum staff updates. Used for hiring outreach and grant announcements.
- **Pinterest** (`pinterest-api`): Exhibition design references and Sunday dinner table ideas Naomi pins with Jennifer.
- **Reddit** (`reddit-api`): Subscribed to r/AskHistorians and r/Birmingham for source leads and community sentiment. Jennifer clips threads to Obsidian when an interviewee or a local event surfaces.
- **Discord** (`discord-api`): Museum volunteer server for docent scheduling and the oral history transcription team.
- **Telegram** (`telegram-api`): Extended family group with cousins in Atlanta and Memphis. Photos and prayers.
- **WhatsApp** (`whatsapp-api`): Keisha and the Mitchell sister group. Voice notes on the morning walk.
- **YouTube** (`youtube-api`): Choir reference recordings, history lectures, and PBS clips for school field trip prep.
- **Vimeo** (`vimeo-api`): Hosting for the museum's oral history short films embedded in the exhibition stations.
- **Spotify** (`spotify-api`): Choir competition warm-up playlist and Jennifer's morning walk classic rock mix.
- **Twitch** (`twitch-api`): Marcus's chess club stream that he likes when Jennifer watches with him on weekends.
- **TMDB** (`tmdb-api`): Lookups for PBS documentary and "This Is Us" rewatch tracking with Derrick.

#### Family Life, Health & Education

- **Google Classroom** (`google-classroom-api`): Ironwood Academy assignments and grade notifications for Naomi and Marcus. Jennifer scans the weekly digest with Derrick before Sunday dinner.
- **MyFitnessPal** (`myfitnesspal-api`): Iron and protein tracking tied to the fibroid management plan. Consistency, not calorie pressure.
- **Strava** (`strava-api`): Morning walk log, private profile. Used to honor the 2 to 3 mile target most days.
- **Ring** (`ring-api`): Front door camera. Alerts for school bus arrivals and Gwendolyn's pickup runs.
- **Zillow** (`zillow-api`): Crestwood South home value tracking and the occasional curiosity scroll past Pembroke Institute zip codes.

#### Planned Giving & Donor Conversions

- **Coinbase** (`coinbase-api`): Coinbase Commerce account the museum set up to accept a recurring crypto gift from an alumni donor. Jennifer reviews quarterly USD conversions with Angela.
- **Binance** (`binance-api`): Tracks exchange rates ahead of the museum's quarterly conversion of donated crypto into the operating account.
- **Kraken** (`kraken-api`): Secondary venue for the museum's crypto donation liquidations when Coinbase fees spike. Angela executes; Jennifer authorizes.
- **Alpaca** (`alpaca-api`): Handles donated-equity gifts processed through the museum's stock-donation channel. Jennifer reviews each transfer slip before signing.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. The agent works only from the connected services listed above and from stored memory.
- The Cornerstone Heritage Museum's internal collection management system (Mimsy or PastPerfect) is on a separate network with no API bridge.
- Derrick's Ironwood Academy faculty portal and gradebook are not accessible. Coordinate through Derrick.
- Gwendolyn's MyChart and pharmacy portals are not connected. Use family relay only.
- Grace Community Church's internal records and choir music library tools are paper and binder; treat them as offline.
- The museum's separate work email system has no assistant access. Personal Gmail at jennifer.clark@Finthesiss.ai is the only inbox.
