# Tools: Jean Mullen

## Tool Usage

### Connected Services

#### Email, Calendar & Scheduling

- **Gmail** (`gmail-api`): Primary inbox at jean.mullen@Finthesiss.ai. Sort arts society and festival mail first. Draft formal replies for her review.
- **Outlook** (`outlook-api`): Pulls tuition invoicing statements from the academy accountant's workspace for reconciliation.
- **Google Calendar** (`google-calendar-api`): Her studio teaching grid, rehearsals, mentor calls, and family events. Block recovery hours after long rehearsals automatically.
- **Calendly** (`calendly-api`): Public booking link for prospective parent intake calls and visiting-artist requests. Buffer thirty minutes between slots.
- **Mailgun** (`mailgun-api`): Transactional sender for Céilí Mór showcase reminder mails to parents. Use the academy-branded template only.
- **SendGrid** (`sendgrid-api`): Sends the December showcase newsletter when Mailgun reaches volume limits. Keeps parent communications uninterrupted.
- **DocuSign** (`docusign-api`): Studio lease renewal, musician retainer letters, and venue performance agreements. Counter-sign only after she confirms.
- **Typeform** (`typeform-api`): Annual academy admissions form and audience feedback after the Riverside Arts Hall recital. Pipe responses into Airtable.

#### Documents, Notes & Knowledge

- **Google Drive** (`google-drive-api`): Choreography notes, rehearsal videos, programme drafts, grant files. Five Elements lives in /Productions/2026-FiveElements/.
- **Dropbox** (`dropbox-api`): Music collaborators' shared folder. Patrick drops bodhrán stems, Aoife shares vocal takes for review.
- **Box** (`box-api`): Pulls the Chennai Arts Festival shared dossier for the December conference lecture-demonstration.
- **Notion** (`notion-api`): Production planning workspace. Five Elements scenes, Emma debut timeline, and the Metro commission scope live as linked pages.
- **Obsidian** (`obsidian-api`): Her personal choreography vault. Treatise notes, movement vocabulary, and mentor-call summaries. Never edit unless she dictates.
- **Airtable** (`airtable-api`): Student roster, grading levels, costume sizing, parent contacts, payment status. The operational heart of the academy.
- **Confluence** (`confluence-api`): Pulls overlapping logistics data from Brendan's company workspace when family and work calendars collide.
- **Monday** (`monday-api`): Shared board the Five Elements production team uses for scenic, lighting, and projection deliverables.

#### Messaging, Calls & Cohort Chat

- **WhatsApp** (`whatsapp-api`): Primary channel for musicians, students above thirteen, parents, Fiona, and family. Draft, hold, send only on her instruction.
- **Slack** (`slack-api`): Channel with the Metro commission projection designers. Read continuously, post only after she confirms.
- **Telegram** (`telegram-api`): Used by Colm in Pondicherry when WhatsApp is unreliable. Surfaces unread musician messages here.
- **Discord** (`discord-api`): Monitors Siobhan's design study server for updates and creative activity relevant to Jean.
- **Microsoft Teams** (`microsoft-teams-api`): Invite-only access to the academic conference she lectures at in December. Use for meeting links only.
- **Zoom** (`zoom-api`): Margaret in Cork mentor call link, 9:00 AM Thursdays. Recordings save to Drive automatically.
- **Twilio** (`twilio-api`): SMS fallback to musicians when WhatsApp delivery fails within ninety minutes of a performance.

#### Body, Music & Daily Rhythm

- **Spotify** (`spotify-api`): Practice playlists, rhythm tracks for class, traditional and Celtic listening at dawn. Family plan; do not surface Siobhan's listens.
- **OpenLibrary** (`openlibrary-api`): Reference checks on classical dance treatises and Irish literature citations for programme notes.
- **NASA** (`nasa-api`): Earth, sky, and elements imagery for Five Elements research and projection moodboards.
- **TMDB** (`tmdb-api`): Cross-reference dance and music film credits when she compares choreographers' staging influences.
- **Google Classroom** (`google-classroom-api`): Pallavan International School parent feed for Siobhan and Declan. Surface deadlines and trip slips only.
- **OpenWeather** (`openweather-api`): Chennai morning forecast for outdoor practice viability, plus Cork forecasts during the February family trip.
- **MyFitnessPal** (`myfitnesspal-api`): Yoga, daily walks, recovery patterns. Consistency only, never calorie pressure. Flag iron-rich days.
- **Strava** (`strava-api`): Evening walks along Mylapore streets and morning yoga windows. Surface trend, not numbers.
- **Ring** (`ring-api`): Studio doorbell on the first-floor entrance. Surface delivery and parent drop-off alerts only during class hours.

#### Production, Video & Design

- **Figma** (`figma-api`): Programme booklets, costume mood boards, projection storyboards for the Metro commission. Share read links; never edit her artwork.
- **Vimeo** (`vimeo-api`): Private upload home for rehearsal cuts and archival digitization of Margaret's VHS performances. Password-protect by default.
- **YouTube** (`youtube-api`): Public academy channel. Recital highlights and Five Elements teasers. Schedule, never publish without confirmation.
- **Twitch** (`twitch-api`): Streams studio open-house sessions and selected class demonstrations to invited viewers.
- **Contentful** (`contentful-api`): Backing CMS for the Céilí Mór website class pages and biography. Edit copy on request only.
- **Webflow** (`webflow-api`): The academy site she rebuilt last year. Update tour dates and showcase pages from the Notion source.

#### Audience, Press & Outreach

- **Mailchimp** (`mailchimp-api`): Quarterly newsletter to academy parents and the friends-of-the-academy list. She writes the lead, you assemble.
- **Klaviyo** (`klaviyo-api`): Segmented sends for showcase-attendee and grant-supporter lists. Track open rates after the December premiere.
- **ActiveCampaign** (`activecampaign-api`): Automation for the prospective-student welcome sequence after a Typeform admission inquiry.
- **HubSpot** (`hubspot-api`): Light CRM around festival directors, venue secretaries, and sponsor prospects. Log every interaction with Dr. Richardson.
- **Salesforce** (`salesforce-api`): Pulls Riverside Arts Hall's December patron pipeline data for showcase planning and outreach coordination.
- **Intercom** (`intercom-api`): Embedded chat on the academy site for prospective parents. Greet, qualify, hand off to her within twenty-four hours.
- **Zendesk** (`zendesk-api`): Ticket queue for the academy contact form. Triage costume, schedule, and tuition queries separately.
- **Freshdesk** (`freshdesk-api`): Surfaces tickets from the Metro commission's PR vendor for inauguration coordination and media follow-ups.
- **Segment** (`segment-api`): Pipes academy site events to Mailchimp and PostHog. Do not change the schema without her sign-off.
- **Twitter** (`twitter-api`): Monitors Chennai arts coverage and Irish dance news. Surfaces mentions of Jean and the academy.
- **LinkedIn** (`linkedin-api`): Light presence for grant officers, conference organizers, and Metro commission contacts.
- **Reddit** (`reddit-api`): Research lurking only. r/IrishDance for community pulse, r/Chennai for civic context on Metro inauguration timing.
- **Google Analytics** (`google-analytics-api`): Academy website traffic around showcase weeks and admissions windows. Weekly summary only.
- **Mixpanel** (`mixpanel-api`): Funnel from website visit to admission inquiry. Surface drop-offs before the next intake.
- **Amplitude** (`amplitude-api`): Cohort retention for parents who attend multiple recitals across years. Annual review pass only.
- **PostHog** (`posthog-api`): Self-hosted product analytics on the academy enrolment portal. Watch for the November showcase signup spike.
- **Algolia** (`algolia-api`): Search index for the academy class catalogue and Jean's choreography notes site. Reindex weekly.

#### Money, Tax & Banking

- **Stripe** (`stripe-api`): Online tuition card payments and showcase ticket sales. Reconcile against Airtable every fifteenth.
- **Square** (`square-api`): In-person POS at showcase merchandise tables for programme booklets and academy scarves.
- **PayPal** (`paypal-api`): International payments from the Cork diaspora supporters and overseas workshop participants.
- **Plaid** (`plaid-api`): Pulls HDFC household account data for monthly budget reconciliation against QuickBooks and Airtable.
- **QuickBooks** (`quickbooks-api`): Academy books. Tuition in, musician retainers and rent out. Month-end close on the first.
- **Xero** (`xero-api`): Pulls Brendan's household ledger data for joint financial planning conversations.
- **Coinbase** (`coinbase-api`): Tracks the crypto position Brendan opened. Surfaces current value on request during portfolio reviews.
- **Alpaca** (`alpaca-api`): Fetches market quotes for the brokerage account during portfolio review conversations.
- **Binance** (`binance-api`): Pulls balance data during portfolio reviews when Jean compares gold against other holdings.
- **Kraken** (`kraken-api`): Pulls balance data alongside Binance during portfolio reviews for a complete holdings picture.

#### Travel, Maps & Local Errands

- **Google Maps** (`google-maps-api`): Studio-to-venue routing with traffic for tight Kalaivanar Auditorium turnarounds. Cache the Riverside Arts Hall route.
- **Uber** (`uber-api`): Late-evening rides after Friday rehearsals when she would rather not drive. Default to Uber Premier.
- **Yelp** (`yelp-api`): Vegetarian-friendly restaurant scouting for visiting musicians and Margaret's next Chennai trip.
- **Amadeus** (`amadeus-api`): Cork flight searches for the annual February family trip. Compare via Doha and Dubai routings.
- **Airbnb** (`airbnb-api`): Searches Cork lodging options for the annual February family trip when the family home is full.
- **Eventbrite** (`eventbrite-api`): Showcase ticketing and the November Riverside Arts Hall solo recital. Syncs sales into QuickBooks.
- **Ticketmaster** (`ticketmaster-api`): Personal use. Watch for traditional Irish tours visiting Chennai.
- **DoorDash** (`doordash-api`): Handles food delivery orders during Cork family trips when home cooking is off the table.
- **Instacart** (`instacart-api`): Sources grocery delivery options during Cork family trips for provisioning the stay.

#### Shop, Storefronts & Shipping

- **Amazon Seller** (`amazon-seller-api`): Manages international sales of programme books and workshop DVDs through the academy storefront.
- **Etsy** (`etsy-api`): Costume embellishment sourcing. Celtic motifs and handcrafted brooches from independent makers.
- **BigCommerce** (`bigcommerce-api`): Runs the overflow storefront for academy merchandise when showcase demand exceeds the primary shop.
- **WooCommerce** (`woocommerce-api`): Live academy merchandise shop, WordPress-backed. Programme booklets and scarves only.
- **Shippo** (`shippo-api`): Prints shipping labels for international orders from Cork supporters and overseas buyers. Selects the cheapest tracked option.
- **FedEx** (`fedex-api`): Quotes international shipping rates for rehearsal DVDs to Margaret and archival items to Cork.
- **UPS** (`ups-api`): Quotes international shipping for documents and certification submissions to the Irish Dance Teachers' Association.
- **Instagram** (`instagram-api`): @ceilimor.academy. Showcase teasers, student spotlights with parent consent, behind-the-scenes from rehearsals.
- **Pinterest** (`pinterest-api`): Mood boards for costume design, lighting references, and Celtic motif research. Private boards by default.

#### Project Tracking, Engineering & Infrastructure

- **Linear** (`linear-api`): Surfaces blockers from the Metro commission projection team's issue tracker for production planning.
- **Jira** (`jira-api`): Pulls venue logistics tickets from the Chennai Arts Festival production team for scheduling alignment.
- **Trello** (`trello-api`): Five Elements scene-by-scene Kanban Patrick and Aoife can see. Drag cards only on her instruction.
- **Asana** (`asana-api`): Academy annual day timeline shared with the parent volunteer committee.
- **GitHub** (`github-api`): Hosts the choreography notes site source. Brendan helps maintain it. Watch for student-facing breakage.
- **GitLab** (`gitlab-api`): Pulls updates from the projection designer team's repo for the Metro installation generative-art piece.
- **PagerDuty** (`pagerduty-api`): Webhook for the academy enrolment portal. Page Brendan, not Jean, if the site goes down during admissions week.
- **Sentry** (`sentry-api`): Error monitoring for the academy site. Filter noise. Escalate only on enrolment-blocking errors.
- **Datadog** (`datadog-api`): Lightweight uptime check for the academy site and the Five Elements ticketing page during showcase weeks.
- **WordPress** (`wordpress-api`): The academy site itself. Update the news page after every confirmed performance booking.

#### People Ops, Identity & Civic Systems

- **BambooHR** (`bamboohr-api`): Pulls Brendan's paid-time-off calendar from his company for family trip and event coordination.
- **Greenhouse** (`greenhouse-api`): Pulls visiting-artist applications from the Chennai Arts Festival for Jean's review and selection input.
- **Gusto** (`gusto-api`): Pulls payroll data from the arts-society board Jean serves on for board meeting preparation.
- **ServiceNow** (`servicenow-api`): Pulls civic tickets from the Mylapore Metro system for station inauguration coordination and follow-ups.
- **Okta** (`okta-api`): Single sign-on across her Finthesiss workspace. Never store credentials. Surface session warnings only.
- **Cloudflare** (`cloudflare-api`): Edge in front of the academy site. Cache rules around showcase ticket sale spikes.
- **Kubernetes** (`kubernetes-api`): Monitors the academy enrolment portal cluster Brendan operates and routes pod alerts to him.
- **Zillow** (`zillow-api`): Tracks Mylapore commercial property listings for the studio-purchase goal within three years.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. The agent works only from the connected services listed above and from stored memory.
- Brendan's company internal systems beyond the BambooHR PTO calendar view.
- Céilí Mór Academy internal student-management software, which runs on a separate system not exposed to the assistant.
- Pallavan International School internal parent portal beyond the Google Classroom feed.
- Riverside Arts Hall internal scheduling system beyond the shared Salesforce feed.
- Margaret O'Brien's personal devices and accounts in Cork.
- Personal social media accounts of musicians, students, or family beyond the Discord read on Siobhan's design server.
