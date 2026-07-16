# Tools: Andrew Morales

## Tool Usage

### Connected Services

#### Email, Calendar & Workspace
- **Gmail** (`gmail-api`): Primary inbox for andrew.morales@Greenridertech.co. Session bookings, publishing correspondence, and industry networking that needs a paper trail.
- **Outlook** (`outlook-api`): Secondary inbox for the labels and studios that route through Microsoft. Andrew pulls corporate session leads from here and forwards the confirmed ones into Gmail to keep one paper trail.
- **Google Calendar** (`google-calendar-api`): Master calendar for sessions, co-writes, church choir, medical appointments, and protected solo-EP time. Defaults to Central Time.
- **Google Drive** (`google-drive-api`): Lyric sheets, demo files, voice-memo backups, contract copies, and session notes, organized by date and status (pitched, held, recorded, personal).
- **Dropbox** (`dropbox-api`): Shared folder where DT and Terrell drop rough mixes and stems from Copperline EP sessions for Andrew to review and mark up.
- **Box** (`box-api`): Secure store for his signed publishing paperwork and the timestamped authorship records he keeps to prove he wrote a hook.
- **DocuSign** (`docusign-api`): Drafts envelopes for co-write split sheets and session agreements for Andrew's signature; never signs on his behalf.
- **Calendly** (`calendly-api`): Booking link he shares with producers and co-writers who want to grab a studio block or writing slot.
- **Google Classroom** (`google-classroom-api`): Hosts the vocal-technique and songwriting masterclasses he is enrolled in between projects. Tracks assignment due dates and feedback from his instructors.

#### Songwriting, Notes & Reference
- **Notion** (`notion-api`): Song catalog, EP production tracker, pitch status board, and the running list of hooks and titles he is sitting on.
- **Obsidian** (`obsidian-api`): Local lyric notebook mirroring his pocket-notebook scraps, melodic-fragment index, and private drafts not yet ready to share.
- **Airtable** (`airtable-api`): Session-income log, the 400-plus voice-memo fragment library tagged by mood and key, and co-write contact tracking.
- **OpenLibrary** (`openlibrary-api`): Tracks his music-biography and Southern-fiction reading list. Currently surfacing the Lydia Mendoza biography and the next Sandra Cisneros essay collection.
- **Algolia** (`algolia-api`): Powers fast search across his own lyric and session-note archive in Drive when he is hunting an old line.
- **NASA** (`nasa-api`): Pulls the astronomy photo of the day for imagery when a lyric needs a sky, a border night, or a desert metaphor.
- **Contentful** (`contentful-api`): Structured content store behind his artist site, holding bio copy, show listings, and EP release notes he updates each cycle.
- **Figma** (`figma-api`): Working files for EP cover art, lyric-video frames, and merch mockups he iterates on with a designer friend.

#### Music, Audio & Video
- **Spotify** (`spotify-api`): Market study, playlist curation, and reference tracks. Studies what is cutting through in country and Tejano and pulls comps for pitches.
- **YouTube** (`youtube-api`): Pulls live performances, vocal tutorials, and reference clips of the artists he is preparing pitches for.
- **Vimeo** (`vimeo-api`): Higher-quality session and performance videos DT shares privately before they are public; Andrew leaves time-coded notes back.
- **Twitch** (`twitch-api`): Drops him into live songwriter rounds and producer streams he keeps up with for community, gear talk, and tracking technique.
- **TMDB** (`tmdb-api`): Powers fast lookups when a music supervisor asks about a sync placement or when he is confirming a soundtrack credit before a co-write.

#### Messaging & Communication
- **WhatsApp** (`whatsapp-api`): The "Morales Family Reunion" group, the San Antonio cousins group, and the Nashville session-singer group.
- **Telegram** (`telegram-api`): A backchannel a few touring session players use to swap last-minute gig and booking openings.
- **Slack** (`slack-api`): The Copperline Studios workspace for scheduling sessions and trading mix notes with DT and Terrell.
- **Discord** (`discord-api`): A Nashville songwriters' server and a Tejano-music community where he trades feedback and references.
- **Microsoft Teams** (`microsoft-teams-api`): Silverbell Music Group's writer calls and quarterly pitch-review meetings with Vanessa.
- **Zoom** (`zoom-api`): Remote co-writes with out-of-town writers and telehealth follow-ups with Dr. Hicks when a fasting visit is not needed.
- **Twilio** (`twilio-api`): Outbound SMS reminders he sets for himself, such as vocal warmups, leave-by pings for yoga, and the nightly call to Mamá.
- **SendGrid** (`sendgrid-api`): Outbound sender for the session confirmations and Silverbell statements Andrew issues to producers and co-writers from his Gmail address.
- **Mailgun** (`mailgun-api`): Fallback sender that takes over studio and continuing-education confirmations the moment the primary queue throttles before a heavy session week.
- **Intercom** (`intercom-api`): Support widget on his distribution and studio-booking platforms; he opens a ticket the moment a payment posts wrong or an upload stalls.

#### Social, Promotion & Audience
- **Instagram** (`instagram-api`): His most active platform, where he posts songwriting clips, studio behind-the-scenes, and Nashville life. He runs every post himself; the agent surfaces DM activity and engagement summaries when he asks.
- **Twitter** (`twitter-api`): Pulses the Nashville and Tejano industry feed, surfacing cut news, label moves, and tour announcements for artists he might pitch.
- **LinkedIn** (`linkedin-api`): Professional profile kept current for publishing, sync, and label-relationship networking, with weekly direct outreach to pluggers and supervisors.
- **Reddit** (`reddit-api`): Pulls daily threads from r/songwriting, r/Nashville, and r/WeAreTheMusicMakers for craft and business sanity checks, with the occasional answer back.
- **Pinterest** (`pinterest-api`): Boards for stage looks, vintage Western wear, and EP visual direction he sources from with his designer friend.
- **WordPress** (`wordpress-api`): His artist-site blog where he drafts and publishes the occasional behind-the-song post around release windows.
- **Webflow** (`webflow-api`): Marketing front end of his artist site, where he publishes show dates and updates the EP landing page each release cycle.
- **Mailchimp** (`mailchimp-api`): His fan newsletter, sent before songwriter rounds and ahead of the EP release.
- **Klaviyo** (`klaviyo-api`): Promotional flows for merch and EP pre-saves he turns on around release windows and off again afterward.
- **ActiveCampaign** (`activecampaign-api`): Drip sequences he subscribes to from the gear and vocal-training brands he follows for deals and clinic announcements.
- **Segment** (`segment-api`): Event pipeline behind his artist site that confirms signup and pre-save events are firing cleanly after every Webflow update.
- **HubSpot** (`hubspot-api`): Silverbell's writer-relations CRM, pushed down to him, tracking which songs are out on pitch and to whom.

#### Travel, Events & Tickets
- **Amadeus** (`amadeus-api`): Saved flight searches for Nashville to San Antonio, pinging him when fares drop ahead of Abuelita's birthday or the holidays.
- **Airbnb** (`airbnb-api`): Lodging for out-of-town writing retreats and family stays in San Antonio when Mamá's place is full.
- **Zillow** (`zillow-api`): East Nashville saved searches that surface when a "what if I bought instead of rented" listing matches his price and walkability filters.
- **Eventbrite** (`eventbrite-api`): Songwriter rounds, showcases, and the industry mixers he registers for around the EP push.
- **Ticketmaster** (`ticketmaster-api`): Holds for concerts he studies for the live craft, and Tejano shows when an artist comes through Texas or the Midwest.
- **Typeform** (`typeform-api`): Intake forms for co-write requests and the feedback survey he sends after songwriter rounds.

#### Food, Local, Getting Around & Shopping
- **Instacart** (`instacart-api`): Sunday meal-prep grocery delivery for pozole and the week's cooking, with his standing Tex-Mex staples on file.
- **DoorDash** (`doordash-api`): Nashville hot chicken and late-night orders after a session runs past midnight.
- **Uber** (`uber-api`): His default ride since selling the car, to and from studios, church, and songwriter rounds.
- **Yelp** (`yelp-api`): Scouts venues, dinner spots for industry meetings, and the hot-chicken joints he keeps ranking.
- **Google Maps** (`google-maps-api`): Drive times to Copperline, Magnolia Sound, Bluebird Track, and Sunrise Flow, plus route planning for San Antonio trips.
- **OpenWeather** (`openweather-api`): Pulls forecasts before walks, Radnor Lake hikes, rooftop shows, and travel days to Texas.
- **Ring** (`ring-api`): The walk-up's front-door doorbell that pings his iPhone when gear or a Mamá care package arrives.
- **Amazon Seller** (`amazon-seller-api`): Storefront for the small batch of EP merch (signed lyric prints, hat patches, tour tees) Andrew sells alongside songwriter-round dates, with inventory and orders piped through to Square.
- **Etsy** (`etsy-api`): Sources vintage Western wear, statement buckles, and small handmade gifts for Diego and Sofia.
- **BigCommerce** (`bigcommerce-api`): The boutique cowboy-boot storefront where he sets restock alerts for 1970s Western styles and buys the moment a pair in his size drops.
- **WooCommerce** (`woocommerce-api`): The small Latino-owned Nashville shop where he reorders his sandalwood-and-cedar cologne and Cafe Bustelo.
- **Shippo** (`shippo-api`): Return labels for stage clothes and gear that did not fit or work out.
- **FedEx** (`fedex-api`): Inbound tracking for recording gear, vinyl, and the boots he wins at online estate sales.
- **UPS** (`ups-api`): Tracking for the monthly book and gift packages he ships to Diego and Sofia and the care packages from Mamá.

#### Money, Royalties & Crypto
- **Plaid** (`plaid-api`): Connector linking his Heartland Credit Union checking and savings into his budget tracker.
- **Stripe** (`stripe-api`): Captures studio-time and co-write receipts so EP spending stays inside the $8,000 budget.
- **Square** (`square-api`): Logs merch and tip sales at songwriter rounds where he runs a reader, and reconciles Amazon Seller merch revenue back to the same ledger.
- **PayPal** (`paypal-api`): Splits with co-writers and the conduit for the $300 he sends Mamá each month.
- **QuickBooks** (`quickbooks-api`): Tracks session income, the Silverbell advance, and royalties for his self-employed taxes.
- **Xero** (`xero-api`): Secondary ledger his accountant uses at tax time to reconcile 1099 session work against QuickBooks.
- **Alpaca** (`alpaca-api`): A small starter brokerage account he is finally opening as the first step toward retirement saving, set to dollar-cost the publishing advance once a month.
- **Coinbase** (`coinbase-api`): A tiny BTC position from a 2024 curiosity, kept on a quarterly tax-lot tally so his bookkeeper has clean records at filing.
- **Binance** (`binance-api`): A small ETH position from the same 2024 curiosity, tracked alongside Coinbase on the quarterly tally.
- **Kraken** (`kraken-api`): A minor position kept active so he can compare staking rates against his savings APY, a focus-keeper that reminds him the EP gets the discretionary money first.

#### Health & Fitness
- **MyFitnessPal** (`myfitnesspal-api`): Loose tracking around reflux triggers and the doctor's nudge toward more vegetables, consistency only, no calorie pressure.
- **Strava** (`strava-api`): Neighborhood songwriting walks and the occasional Radnor Lake hike on weekends.

#### Industry Ops, CRM & Project Tracking
- **Salesforce** (`salesforce-api`): Silverbell's pitch CRM where Andrew works his catalog, holds, and cut history with Vanessa each quarter.
- **Monday** (`monday-api`): The EP production board shared with DT, tracking tracking days, mixes, and masters toward the mid-September target.
- **Jira** (`jira-api`): The ticket queue his web developer uses for artist-site fixes; he files here when a page breaks before a show.
- **Trello** (`trello-api`): Personal board for the five EP songs, each card moving from written to demoed to tracked to mixed.
- **Asana** (`asana-api`): Co-write scheduling board shared with Vanessa, holding writer pairings and deadlines.
- **Linear** (`linear-api`): Tracks the public roadmap of his distribution platform so he knows which release-tooling features land before the EP drops.
- **Confluence** (`confluence-api`): Silverbell's writer handbook and pitch-process docs. He pulls the submission-format cheat-sheet before quarterly reviews with Vanessa.
- **ServiceNow** (`servicenow-api`): Studio IT ticketing he files into when a Copperline session is blocked by an equipment issue.
- **Greenhouse** (`greenhouse-api`): Silverbell's hiring pipeline. Andrew flags it when a new plugger is hired, so he knows which contact will start carrying his songs into A&R rooms.
- **Gusto** (`gusto-api`): Payroll for the part-time bookkeeper who helps with his session-income filings.
- **BambooHR** (`bamboohr-api`): Silverbell's writer-roster portal where his deal terms and statements live.
- **Freshdesk** (`freshdesk-api`): Support queue for his music-distribution vendor when a royalty allocation goes sideways.
- **Zendesk** (`zendesk-api`): Support tickets with his digital-distribution platform when a release upload stalls.

#### Web, Dev & Observability
- **GitHub** (`github-api`): Contributes lyric-and-chord pattern patches to the open-source teaching tool his cousin Reggie runs in his San Antonio music classroom.
- **GitLab** (`gitlab-api`): Mirror of his artist-site repo. Andrew pushes content updates here when his developer is travelling and the primary repo is locked.
- **Sentry** (`sentry-api`): Monitors errors on his artist site and pages him the moment the EP landing page misbehaves before a release.
- **Datadog** (`datadog-api`): Tracks uptime on his artist site so he knows the host is solid before a tour-date or EP announcement spikes traffic.
- **PagerDuty** (`pagerduty-api`): On-call routing for his artist site so he can tell at a glance whether an outage belongs to his developer or the host before he reaches out.
- **Okta** (`okta-api`): SSO across the Silverbell corporate tooling stack, where Andrew handles his own logins and lockouts.
- **Cloudflare** (`cloudflare-api`): DNS and caching for his artist site, where he flushes the cache after a tour-date or EP content update.
- **Kubernetes** (`kubernetes-api`): The cluster his developer's agency runs his site on; he confirms deploy status here before a release goes live.
- **PostHog** (`posthog-api`): Funnel analytics on EP pre-saves and newsletter signups from his site.
- **Mixpanel** (`mixpanel-api`): Engagement dashboards on which songs, clips, and reels drive the most plays and follows, surfaced before he plans the next batch of socials.
- **Amplitude** (`amplitude-api`): Audience-growth dashboards he reviews before deciding which markets to push the EP into.
- **Google Analytics** (`google-analytics-api`): Artist-site traffic and where listeners come from, summarized weekly into a one-screen brief.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from the connected services listed above and from stored memory.
- Venmo and his Heartland Credit Union mobile banking are not connected. Andrew handles those on his iPhone.
- Ridgecrest Health Insurance and the medical-provider portals are not connected. The agent drafts messages for Andrew to send through them himself.
- His Instagram posting is run by Andrew personally; the assistant surfaces engagement and DM activity but never composes or posts.
- Label-internal and Silverbell-internal systems beyond his own writer access are off-limits. In group or shared contexts, treat them as not connected and work from what Andrew tells you and stored memory.
- Private accounts belonging to his family, Keisha, DT, Terrell, and Vanessa are not connected and are off-limits.
