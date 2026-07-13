# Tools: Kim Russell

## Tool Usage

### Connected Services

#### Crestline Consulting Workspace & Documents
- **Gmail** (`gmail-api`): Kim's primary inbox at kim.russell@Finthesiss.ai. Wholesale cafe threads, parent emails, vendor orders, and personal correspondence.
- **Google Calendar** (`google-calendar-api`): The master calendar. Mon/Wed/Fri baking blocks, weekday studio classes, Saturday rehearsals, wholesale deliveries, and Sunday lunch at Irene's.
- **Google Drive** (`google-drive-api`): Recipes organized by category, choreography notebooks, recital planning documents, bakery financials, and student records.
- **Outlook** (`outlook-api`): Forwards inbound messages from the Brownstone Bookshop Cafe wholesale contact into Gmail for unified inbox management.
- **Dropbox** (`dropbox-api`): Stores recital video files and choreography reference recordings shared with guest choreographers who do not use Drive.
- **Box** (`box-api`): Used by the bakery's accountant to deposit quarterly tax packets. Kim downloads only; nothing sensitive is uploaded here.
- **Notion** (`notion-api`): Kim's personal teaching workspace. Class lesson plans, level-by-level technique notes, and the running list of choreography ideas.
- **Obsidian** (`obsidian-api`): Local vault for recipe development notes, including grandmother's pie variations and Della's pound cake notebook annotations. Stays offline for security.
- **Airtable** (`airtable-api`): Wholesale order tracker (cafe, day, quantity, status) and the custom-order pipeline with delivery dates and dietary flags.
- **Confluence** (`confluence-api`): References the Brighton Beach Community Center wiki for stage dimensions, lighting rigs, and dressing room access during recital planning.
- **DocuSign** (`docusign-api`): Parent enrollment agreements, wholesale contracts with new cafes, and the bakery's home-kitchen license renewal. Confirm with Kim before sending anything for her signature.
- **Typeform** (`typeform-api`): The custom-order intake form on the bakery's Instagram link in bio. New submissions land in Gmail; route triage entries to Airtable.

#### Communication Channels
- **Slack** (`slack-api`): Brighton Ballet Academy team channel with Marina, the two part-time instructors, and the accompanist. Operational only.
- **WhatsApp** (`whatsapp-api`): Extended Russell-Petrov family group and the long-running thread with Brighton Academy of Dance classmates. Voice notes are normal here.
- **Microsoft Teams** (`microsoft-teams-api`): One standing call per month with the Brooklyn ballet schools network for shared casting and master class coordination.
- **Telegram** (`telegram-api`): Connects Kim to a Black pastry chefs collective where she shares recipes and discusses technique.
- **Discord** (`discord-api`): Monitors the advanced students' recital announcements server so Kim can gauge anxiety levels before performances.
- **Zoom** (`zoom-api`): Parent meetings, virtual recital previews for out-of-town family, and wholesale tasting calls. Studio teaching is in person, not here.
- **Twilio** (`twilio-api`): Class reminder SMS for the parent list. Confirm any template change with Kim before sending.
- **SendGrid** (`sendgrid-api`): Transactional email for the bakery's order confirmations and the studio's recital ticket receipts.
- **Mailgun** (`mailgun-api`): Sends transactional emails when the bakery's website host requires a secondary delivery channel. Keep credentials in `$MAILGUN_API_KEY`.
- **Calendly** (`calendly-api`): Custom-order consultations for wedding dessert tables and large-format cakes. Studio scheduling does not run here.

#### Bakery Finance, Payments & Investing
- **Stripe** (`stripe-api`): Online custom-order payments through the bakery website. Reconciles into QuickBooks weekly.
- **Plaid** (`plaid-api`): Syncs personal budgeting data across Chase checking, savings, and the Roth IRA for financial tracking.
- **QuickBooks** (`quickbooks-api`): Russell's Pastries books. Wholesale invoicing, custom-order revenue, ingredient cost tracking, monthly P&L. Kim reviews on the 1st of each month.
- **Xero** (`xero-api`): Reads the monthly statement from one ingredient supplier who exports in Xero format.
- **Square** (`square-api`): POS card reader for in-person custom-order pickups and bakery pop-up events. Wholesale cafes are invoiced through Stripe.
- **PayPal** (`paypal-api`): Personal account for church fundraising, Brighton Beach community potlucks, and small family transactions.
- **Coinbase** (`coinbase-api`): Tracks a crypto watchlist David recommended so Kim can join investment conversations at his holiday office gathering.
- **Alpaca** (`alpaca-api`): Demonstrates recurring buy patterns in a sandbox David configured for Kim's investment education.
- **Binance** (`binance-api`): Provides market data for the investment conversations Kim shares with David at social gatherings.
- **Kraken** (`kraken-api`): Maintains a crypto watchlist Kim reviews before conversations with David about market trends.

#### Ballet School & Parent Outreach
- **Google Classroom** (`google-classroom-api`): Brighton Ballet Academy resource site. Recital music links, costume guides, technique videos, and the parent handbook.
- **Salesforce** (`salesforce-api`): Parent and student CRM. Class history, family relationships, recital roles, alumni contacts.
- **HubSpot** (`hubspot-api`): Marketing automation for the bakery's seasonal-menu newsletter. Quarterly cadence, opt-in only.
- **Zendesk** (`zendesk-api`): Vendor support tickets for the studio's sound system, the bakery POS, and the website host.
- **Freshdesk** (`freshdesk-api`): Handles support tickets from the bakery website vendor for site maintenance and issue resolution.
- **Intercom** (`intercom-api`): Live chat on the bakery site. Auto-replies route custom-order inquiries to Calendly.
- **ServiceNow** (`servicenow-api`): IT ticketing for the Brighton Beach Community Center's box-office system that the studio uses for recital ticket sales.
- **Mailchimp** (`mailchimp-api`): Quarterly newsletter to roughly 900 parents and alumni families. Kim approves every send.
- **Klaviyo** (`klaviyo-api`): Holiday-specific drip campaigns for the bakery when Thanksgiving and Christmas pre-orders open.
- **ActiveCampaign** (`activecampaign-api`): Archives email campaign history from the bakery's first three years for seasonal strategy reference.

#### Operations, HR & Project Tracking
- **BambooHR** (`bamboohr-api`): Light HR records for the two part-time studio instructors and the Saturday accompanist. Onboarding documents and W-2 contractor agreements.
- **Greenhouse** (`greenhouse-api`): Manages the assistant teacher search Kim and Marina are running for the fall term, from job post drafting through candidate review.
- **Gusto** (`gusto-api`): Studio payroll. Marina runs it; Kim approves on the 15th and the last day of each month.
- **Linear** (`linear-api`): Kim's personal project board. Spring gala milestones, fall semester syllabus, commercial-kitchen lease research, and the holiday wholesale rollout.
- **Jira** (`jira-api`): Tracks the Brooklyn ballet schools network's joint master class planning board for scheduling coordination.
- **Trello** (`trello-api`): Family board shared with Natasha for nieces' birthdays, Thanksgiving and Christmas hosting, and Irene's apartment maintenance items.
- **Asana** (`asana-api`): Recital production logistics per show, including costumes, lighting, music edits, program printing, and parent volunteer assignments.
- **Monday** (`monday-api`): Bakery operations board with wholesale account renewals, vendor reviews, and the home-kitchen license cycle.

#### Teaching, Research & Reference
- **OpenLibrary** (`openlibrary-api`): Citation lookup for the ballet history reading list Kim sends advanced students and for cookbook references.
- **NASA** (`nasa-api`): Coastal weather and atmospheric pressure data for the boardwalk forecast and the dough proofing variables on the most humid summer days.
- **WordPress** (`wordpress-api`): The bakery site at russellspastries.com. Menu, pre-order windows, custom-order intake.
- **Contentful** (`contentful-api`): Staging copy for the studio website rebuild Marina is steering. Editorial only.

#### Storefront, Wholesale & Shipping
- **Amazon Seller** (`amazon-seller-api`): Holds the account Kim used for pecan praline tin sales in 2022, available for future direct-to-consumer launches.
- **Etsy** (`etsy-api`): Sources cake toppers, ceramic plates for tasting boxes, and handmade items Kim gifts the nieces.
- **BigCommerce** (`bigcommerce-api`): Stands ready for direct-to-consumer holiday pastry box sales when Kim expands beyond wholesale.
- **WooCommerce** (`woocommerce-api`): The bakery site's storefront plugin for seasonal pre-order windows. Enabled only during Thanksgiving and Christmas weeks.
- **Shippo** (`shippo-api`): Ships pecan pralines and pound cakes to extended family in Atlanta and Charleston.
- **FedEx** (`fedex-api`): Tracking for ingredient shipments, specialty French butter, and Madagascar vanilla bean orders.
- **UPS** (`ups-api`): Tracking for studio costume orders, recital backdrop deliveries, and barre equipment.

#### Travel, Events & Local Life
- **Amadeus** (`amadeus-api`): Searches flights and hotels when Kim plans travel, including the Paris trip with Irene booked in 2017.
- **Airbnb** (`airbnb-api`): Weekend rentals in Charleston with Elena, and the long-promised New Orleans trip when she finally takes it.
- **Uber** (`uber-api`): Airport transfers only. In Brighton Beach and Brooklyn she walks or takes the B/Q.
- **Eventbrite** (`eventbrite-api`): Recital ticket sales for the Brighton Ballet Academy winter showcase and spring gala.
- **Ticketmaster** (`ticketmaster-api`): Books NYC Ballet performance tickets three to four times per season and Lincoln Center jazz or Dance Theatre of Harlem events.
- **Google Maps** (`google-maps-api`): Drive times for wholesale delivery routes between the apartment, Cafe Nostalgia, Brownstone Bookshop Cafe, and Heritage Deli. Subway routes for Manhattan trips.
- **Yelp** (`yelp-api`): Restaurant intel for Thursday dinners with Elena. Caribbean in Crown Heights, Japanese in the East Village, Italian in the West Village, French in Cobble Hill.
- **OpenWeather** (`openweather-api`): Daily forecast for the boardwalk walk, the dough's behavior in summer humidity, and recital-week weather for the community center venue.
- **DoorDash** (`doordash-api`): Orders dinner delivery when a late wholesale production day leaves no time to cook.
- **Instacart** (`instacart-api`): Weekly grocery run for household basics that do not require the Nostrand Avenue trip. Soul food and Caribbean markets she walks to in person.
- **Ring** (`ring-api`): One doorbell camera at the apartment door for wholesale pickup confirmations. Motion alerts muted between 9:30 PM and 4:00 AM.
- **Zillow** (`zillow-api`): Watching commercial kitchen lease listings in Sheepshead Bay and Coney Island as a 2027 daydream.

#### Media, Social & Decompression
- **Spotify** (`spotify-api`): Three saved playlists. Chopin for morning barre, Aretha and Nina for the kitchen, Tchaikovsky for choreography.
- **YouTube** (`youtube-api`): Saved playlists of classical ballet performances, lamination technique videos, and Dance Theatre of Harlem archival footage.
- **Vimeo** (`vimeo-api`): Recital videos from previous years, hosted privately and shared with parents on request.
- **TMDB** (`tmdb-api`): Watchlist for the bedroom projector. Spike Lee, Barry Jenkins, French New Wave, and a slow Criterion working list.
- **Twitch** (`twitch-api`): Follows two pastry streamers Della recommended for lamination and decoration technique reference.
- **Instagram** (`instagram-api`): @russells_pastries. Business account, around 2,400 followers, three to four posts per week. Kim posts from her phone; draft captions only when asked.
- **Pinterest** (`pinterest-api`): Boards for plating ideas, recital costume references, and bookshelf inspiration for the apartment.
- **Twitter** (`twitter-api`): Follows Black food writers, ballet critics, and a group of Brooklyn restaurateurs for industry awareness.
- **LinkedIn** (`linkedin-api`): Professional bio for the studio. Kim approves connection requests herself, slowly.
- **Reddit** (`reddit-api`): Follows r/Baking, r/Pastry, and a dance-pedagogy subreddit for technique trends and community discussion.

#### Health & Movement
- **MyFitnessPal** (`myfitnesspal-api`): Daily barre work, yoga twice a week, boardwalk walks. Consistency log only, never calories. Her body has been a dancer for thirty-six years and does not need scrutiny.
- **Strava** (`strava-api`): Tracks Elena's running activity so Kim knows when to check in after a long Manhattan loop.

#### Web, Engineering & Analytics Observer
- **GitHub** (`github-api`): Follows a notation tool repo maintained by a former advanced student, giving Kim conversation topics for alumni dinners.
- **GitLab** (`gitlab-api`): Monitors the Brighton Beach Community Center's volunteer scheduling repo to catch recital slot changes early.
- **Sentry** (`sentry-api`): Error monitoring on the bakery website. Page Kim only if the order form is fully down.
- **Datadog** (`datadog-api`): Monitors uptime and infrastructure health for the bakery site and the studio site through dashboard alerts.
- **PagerDuty** (`pagerduty-api`): On-call alerts for the bakery site go to the website vendor first; Kim is paged only on total outage during a pre-order window.
- **Okta** (`okta-api`): SSO for the Crestline Consulting workspace and the studio's vendor portals.
- **Cloudflare** (`cloudflare-api`): DNS, CDN, and DDoS protection for the bakery site. No changes without Kim's confirmation.
- **Kubernetes** (`kubernetes-api`): Checks the website host's cluster status for diagnostics when site issues surface during pre-order windows.
- **Figma** (`figma-api`): Reviews recital program mockups and bakery seasonal menu cards David designs, with Kim adding feedback and comments.
- **Webflow** (`webflow-api`): Staging environment for the studio website rebuild. Publish requires Kim's approval.
- **Algolia** (`algolia-api`): Search index for the bakery site menu. Re-index after each seasonal menu update.
- **Google Analytics** (`google-analytics-api`): Bakery site traffic before, during, and after each holiday pre-order window.
- **Mixpanel** (`mixpanel-api`): Event tracking on the custom-order inquiry form, including opens, partial submissions, and completions.
- **Amplitude** (`amplitude-api`): Funnel analysis for the holiday pre-order flow.
- **PostHog** (`posthog-api`): Heatmaps and anonymized session replays on the bakery site.
- **Segment** (`segment-api`): Single source of truth that routes events into Mixpanel, Amplitude, and PostHog.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from connected APIs and stored memory.
- **Brighton Beach Medical patient portal** (Dr. Vera Orlova's office) is not connected. Kim accesses it directly for her own records.
- **Natasha's dental practice records** and the family-discount account are not connected. Family scheduling happens by text.
- **Della Mason's personal accounts and communications** are not connected. Della is phone-only.
- **Marina Katz's personal accounts** and the side ledger Marina runs in her own QuickBooks instance are not connected. The shared bakery and school books are; her personal books are not.
- **Insurance carrier portals** (renters, bakery commercial liability, studio liability) are not connected. Kim or Marina log in directly for renewals.
- **Brighton Ballet Academy parent banking and student family financial information** is not connected and is never sought.
