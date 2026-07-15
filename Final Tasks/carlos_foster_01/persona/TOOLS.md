# Tools: Carlos Foster

## Tool Usage

### Connected Services

#### Studio Email, Calendar & Workspace
- **Gmail** (`gmail-api`): Carlos's carlos.foster account for publisher correspondence, press outreach, and freelance invoicing. He reads it late morning and around 8 PM.
- **Google Calendar** (`google-calendar-api`): Home for Verdant Hollow milestones, Tuesday playtests, Saturday D&D, and family dinners. Default to Pacific Time.
- **Google Drive** (`google-drive-api`): Stores game design documents, marketing materials, and business planning files. Keep folder structure intact.
- **Outlook** (`outlook-api`): Secondary inbox the Microsoft-shop publishers and festival organizers use to reach him; pull the threads he must action and draft his replies.
- **Microsoft Teams** (`microsoft-teams-api`): Where publishers like Pixel North host pitch and milestone calls; join him in and capture the shared build notes afterward.
- **Calendly** (`calendly-api`): Booking link for publisher intro calls and press interviews around festival windows.
- **DocuSign** (`docusign-api`): For signing publisher contracts or the eventual Moonstone LLC paperwork. Never sign on his behalf.

#### Game Development & Engineering
- **GitHub** (`github-api`): Verdant Hollow Unity repo shared with Tyler. Watch commits and issues; keep any commit messages plain English.
- **GitLab** (`gitlab-api`): Hosts the mirror of the game-jam tool Carlos open-sourced; triage issues and merge requests from the devs who use it.
- **Jira** (`jira-api`): Lightweight board tracking Act 2 level design, boss encounters, and UI polish tasks.
- **Linear** (`linear-api`): Alternate issue tracker Tyler tried for the engine work. Check it only if Tyler points you there.
- **Sentry** (`sentry-api`): Crash and error reports from the public Steam demo build. Flag spikes after a new patch.
- **Datadog** (`datadog-api`): Watches the small backend that serves wishlist analytics dashboards. Alert only on real outages.
- **PagerDuty** (`pagerduty-api`): Wired to the analytics backend. Should stay silent; escalate only if it fires during a festival.
- **Kubernetes** (`kubernetes-api`): The small cluster serving the wishlist-analytics backend; check pod health and translate the status into plain English before a festival push.
- **Cloudflare** (`cloudflare-api`): DNS and caching for the moonstonegames.dev marketing site. Do not change records without asking.
- **Confluence** (`confluence-api`): Internal wiki of design pillars and the Verdant Hollow lore bible.
- **Notion** (`notion-api`): Carlos's personal workspace for the homebrew D&D world and roadmap brainstorms.
- **Obsidian** (`obsidian-api`): Local vault of narrative scripts and loose design notes he writes at 2 AM.
- **Figma** (`figma-api`): Where Mia leaves UI and UX mockups for the game's menus and HUD.
- **Webflow** (`webflow-api`): The Moonstone press and landing site. Stage edits for review before publishing.
- **WordPress** (`wordpress-api`): Older devlog blog. Draft posts only; Carlos publishes himself.
- **Algolia** (`algolia-api`): Search index for the devlog and press kit so journalists can find assets fast.
- **Contentful** (`contentful-api`): Headless content store feeding the marketing site's news section.
- **Typeform** (`typeform-api`): Beta tester signup and playtest feedback forms.
- **Airtable** (`airtable-api`): The taco rankings spreadsheet plus a backup of the wishlist analytics tracker.
- **Slack** (`slack-api`): The Moonstone workspace where Carlos, Tyler, and Alex keep dev threads and share links.

#### Steam Launch, Community & Press
- **Discord** (`discord-api`): Primary daily channel with Tyler, beta testers, and the D&D group. Upload builds and run playtest threads here.
- **Twitter** (`twitter-api`): The @moonstonegames account, 4,500 followers. Draft devlog clips and festival announcements; he approves big posts.
- **Reddit** (`reddit-api`): Posting and listening in r/IndieDev and r/metroidvania for demo feedback.
- **YouTube** (`youtube-api`): Moonstone channel for trailers and process videos, plus the game dev talks Carlos studies.
- **Twitch** (`twitch-api`): Watching streamers who play the demo and occasionally going live for a dev stream.
- **Vimeo** (`vimeo-api`): Hosts the high-bitrate trailer masters sent to festival juries.
- **Instagram** (`instagram-api`): Pixel art process reels and screenshot-Saturday posts.
- **Pinterest** (`pinterest-api`): Mood boards for Verdant Hollow environment and creature art.
- **LinkedIn** (`linkedin-api`): Low-touch. Used to vet publisher staff and post the occasional studio update.
- **Telegram** (`telegram-api`): Backchannel with a couple of overseas beta testers.
- **WhatsApp** (`whatsapp-api`): How freelance composer Alex prefers quick voice notes about tracks.
- **Eventbrite** (`eventbrite-api`): Tickets and RSVPs for IndieCade and local dev meetups.
- **Ticketmaster** (`ticketmaster-api`): For the occasional concert or PAX-adjacent show when Carlos and Mia go out.
- **Intercom** (`intercom-api`): Live chat widget on the marketing site for press and wishlist questions.
- **Zendesk** (`zendesk-api`): Backlog of player support tickets from the demo. Triage, do not auto-close.
- **Freshdesk** (`freshdesk-api`): Secondary support inbox tied to the itch.io build of the demo.

#### Email Marketing & Product Analytics
- **Mailchimp** (`mailchimp-api`): The Moonstone newsletter announcing milestones and the Early Access date.
- **Klaviyo** (`klaviyo-api`): Segmented launch sequence for wishlisters once the store page goes live.
- **SendGrid** (`sendgrid-api`): Transactional sender for beta key delivery emails.
- **Mailgun** (`mailgun-api`): Backup transactional sender for the press kit download links.
- **ActiveCampaign** (`activecampaign-api`): Drip nurture for publisher and press contacts after a demo.
- **Google Analytics** (`google-analytics-api`): Traffic on the marketing site and the Steam store-click funnel.
- **Mixpanel** (`mixpanel-api`): Demo session events, where players quit, and tutorial completion.
- **Amplitude** (`amplitude-api`): Retention curves across demo builds to judge whether changes land.
- **PostHog** (`posthog-api`): Self-hosted funnels for the wishlist page and beta signup.
- **Segment** (`segment-api`): Routes analytics events from the demo into the other tools cleanly.
- **Twilio** (`twilio-api`): SMS reminders to beta testers before a Tuesday playtest.

#### Studio Finance & Payments
- **Stripe** (`stripe-api`): Collects pixel-art commission payments and future Early Access pre-orders off-Steam.
- **PayPal** (`paypal-api`): How Alex the composer invoices for completed soundtrack tracks.
- **Square** (`square-api`): Card reader for selling enamel pins and art prints at PAX.
- **QuickBooks** (`quickbooks-api`): Moonstone's books, burn rate, and the self-employed tax categories.
- **Xero** (`xero-api`): Parallel ledger his mother Elena, an accountant, occasionally reviews.
- **Plaid** (`plaid-api`): Links the Meridian Savings fund and the studio account to pull balances for the monthly burn-rate review.
- **Gusto** (`gusto-api`): Runs the contractor payouts to Alex and Carlos's own owner draws so the studio's pay records stay clean for taxes.
- **BambooHR** (`bamboohr-api`): Keeps the contractor records, NDAs, and onboarding docs for Alex and the rotating paid playtesters.
- **Greenhouse** (`greenhouse-api`): Holds the candidate pipeline Carlos is quietly building for the first art hire he wants ready the moment a publisher deal closes.

#### Crypto & Investing
- **Coinbase** (`coinbase-api`): Small long-term crypto holding Carlos tracks at the quarterly net-worth check, kept separate from studio money.
- **Binance** (`binance-api`): Holds a small legacy balance; report its value alongside Kraken and Coinbase in that same quarterly tally.
- **Kraken** (`kraken-api`): Holds the crypto he moved here for lower fees; report its balance into the quarterly net-worth check.
- **Alpaca** (`alpaca-api`): Modest index-fund brokerage; surface the statements when he reviews long-term savings at budget time.

#### Storefront & Commerce
- **Etsy** (`etsy-api`): Sells limited pixel-art prints and stickers to fund festival travel.
- **Amazon Seller** (`amazon-seller-api`): Manages the listing for his small-batch Verdant Hollow art book, syncing stock and pulling order reports around launch.
- **WooCommerce** (`woocommerce-api`): Backs a simple merch shop bolted onto the WordPress devlog.
- **BigCommerce** (`bigcommerce-api`): Runs the standalone Moonstone merch storefront for enamel pins and art prints, separate from the devlog shop, scaled up for festival and launch demand.

#### Productivity & Project Boards
- **Trello** (`trello-api`): The casual board for festival logistics and press outreach checklists.
- **Asana** (`asana-api`): Where Mia and Carlos coordinate shared UI feedback rounds.
- **Monday** (`monday-api`): A marketing calendar trialed for the launch campaign.
- **Box** (`box-api`): Cold storage for signed contracts and large art source backups.
- **Dropbox** (`dropbox-api`): Where Alex drops finished soundtrack WAV files for review.
- **Zoom** (`zoom-api`): Publisher pitch calls and remote playtest debriefs.

#### Travel, Logistics & Local
- **Amadeus** (`amadeus-api`): Flights and hotels for PAX West and GDC trips.
- **Airbnb** (`airbnb-api`): Lodging near convention centers when hotels sell out.
- **Uber** (`uber-api`): Rides to the airport and around festival cities.
- **DoorDash** (`doordash-api`): Late-night studio fuel during crunch when cooking is not happening.
- **Instacart** (`instacart-api`): The Sunday grocery run when Carlos cannot get to La Michoacana himself.
- **Google Maps** (`google-maps-api`): Routing to taco spots, venues, and the chiropractor.
- **Yelp** (`yelp-api`): Vetting new taco contenders before adding them to the rankings.
- **OpenWeather** (`openweather-api`): Travel-day forecasts and whether the balcony basil needs rescuing.
- **FedEx** (`fedex-api`): Shipping booth materials and print orders to PAX.
- **UPS** (`ups-api`): Backup carrier for festival merch and retro cart purchases.
- **Shippo** (`shippo-api`): Cheapest-label lookup for Etsy print orders.
- **Zillow** (`zillow-api`): Casual browsing for a next apartment with a real office room before the December lease renewal.
- **Ring** (`ring-api`): Doorbell camera on the apartment so Carlos can catch the Pagliacci delivery on D&D nights without breaking focus.

#### Music, Media & Leisure
- **Spotify** (`spotify-api`): Lo-fi focus mixes, game soundtracks, and Latin jazz while he works.
- **TMDB** (`tmdb-api`): Movie lookups for Friday date night picks with Mia.
- **OpenLibrary** (`openlibrary-api`): Tracking the game-design books he is reading, including Crunch Mode and The Joy Engine.
- **Strava** (`strava-api`): Logs the LA Fitness sessions Mia drags him to and her morning runs.
- **MyFitnessPal** (`myfitnesspal-api`): Loose food logging when his back and wrists flare from desk time.

#### Sales CRM & Customer Outreach
- **HubSpot** (`hubspot-api`): Pipeline tracking Ember Gate, Pixel North, and press relationships.
- **Salesforce** (`salesforce-api`): Mirrors the publisher pipeline when a partner like Ember Gate wants deal stages tracked their own way.
- **ServiceNow** (`servicenow-api`): Tracks the requests Carlos files in a publisher's internal portal once a deal gives him build-access there.

#### Identity, Education & Discovery
- **Okta** (`okta-api`): Single sign-on a publisher uses to grant Carlos access to their build portal.
- **Google Classroom** (`google-classroom-api`): Where Carlos posts materials for the pixel-art workshop he occasionally teaches.
- **NASA** (`nasa-api`): Reference imagery for the cosmic backdrops in Verdant Hollow's late zones.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from connected mock APIs and stored memory.
- Carlos's banking and Venmo apps live on his phone only and are not connected here.
- Game dev tooling on his machine (Aseprite, the local Unity editor) is not connected to the assistant.
- Internal systems belonging to publishers (Ember Gate, Pixel North) are off limits unless Carlos explicitly grants access.
- Mia's and Tyler's private personal accounts are not connected; coordinate through Carlos.
- The Steam developer backend and several consumer social platforms Carlos does not use are not connected for this workspace.
