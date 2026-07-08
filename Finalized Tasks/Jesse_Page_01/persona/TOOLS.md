# Tools: Jesse Page

## Tool Usage

### Connected Services

#### Email, Calendar & Messaging
- **Gmail** (`gmail-api`): Connected to jesse.page@Finthesiss.ai. Client briefs, invoicing, agent threads with Tomás, brand outreach, personal email. Draft replies for her review; never auto-send to a new contact.
- **Google Calendar** (`google-calendar-api`): Shoot days, edit blocks, posting slots, Tue/Sat yoga, every-other-Sunday dim sum in Flushing. Hold a 60-minute decompress buffer after every shoot block.
- **Outlook** (`outlook-api`): Mirror inbox for brand contacts on Microsoft 365. Catch the thread, move the conversation back to Gmail within the day so all client history sits on one rail.
- **WhatsApp** (`whatsapp-api`): International brand contacts and Chef Ana's Estrela kitchen group. Casual register, dairy-free menu sync, no financial detail.
- **Telegram** (`telegram-api`): Backchannel for the NYC chef collective and two overseas photo communities. Surface DMs that name Jesse or mention an open editorial slot.
- **Twilio** (`twilio-api`): Programmatic SMS for shoot-day reminders, call-time confirmations, and dairy-free catering check-ins. Send the morning-of recap to Jess by 6:00 AM.
- **SendGrid** (`sendgrid-api`): Transactional sends for invoice receipts, shoot confirmations, and Pic-Time gallery release notices. Templates only.
- **Mailgun** (`mailgun-api`): Powers the portfolio site contact form on jessepagephotography.com. Route inquiries into the Notion intake pipeline and tag by project type before they hit her inbox.
- **Slack** (`slack-api`): Workspaces with Tangerine Magazine's design team and the Estrela cookbook crew. Mute outside business hours; surface @-mentions within 30 minutes during the workday.
- **Discord** (`discord-api`): Two community servers, NYC Food Photographers and the Freelancers' Tax Co-op. Listen for assignment chatter and answer Ravi's tax-prep questions when he tags her.
- **Microsoft Teams** (`microsoft-teams-api`): Channel for the corporate brand client whose team lives in Teams. Join scheduled calls and transcribe action items into Notion.
- **Zoom** (`zoom-api`): Client kickoffs, agency pitches, cookbook editorial calls. Capture call notes into the project Notion page; do not record without explicit consent.

#### Social, Portfolio & Audience
- **Instagram** (`instagram-api`): @jessepagephoto, ~48K followers. Draft captions, queue posts and stories, pull weekly analytics, log brand DMs into the Notion CRM. Never publish without her sign-off on image and caption.
- **Pinterest** (`pinterest-api`): Mood boards for cookbook and editorial pitches. Private boards per client, a public board for the Night Markets project; surface new pins from her saved-search list each morning.
- **Twitter** (`twitter-api`): Pull assignment cues from a curated list of food editors and NYC food writers. Surface any tweet mentioning an open pitch window or a restaurant on her active client list.
- **LinkedIn** (`linkedin-api`): Brand-side contact and editorial gatekeeper outreach. Draft connection requests and follow-up notes for her review; never send without her sign-off.
- **YouTube** (`youtube-api`): Pull kitchen technique and lighting reference clips when a brief calls for an unfamiliar method. Queue them into the night-before shoot-prep playlist.
- **Vimeo** (`vimeo-api`): Hosts behind-the-scenes reels for clients and the private archive of motion tests with Mateo. Password-protect by default; rotate the password each quarter.
- **Reddit** (`reddit-api`): r/AskCulinary and r/photography for sourcing answers on plating and lighting questions. Draft replies for her review; never post under her handle without approval.
- **Twitch** (`twitch-api`): Pull cooking-stream prep clips when a brief calls for an unfamiliar regional cuisine. Surface two to three starting clips per shoot before prep day.
- **WordPress** (`wordpress-api`): Pull Eater NY and Grub Street headlines into the morning industry digest. Flag any mention of a restaurant on her active client list.
- **Webflow** (`webflow-api`): Staging environment for Mateo's portfolio rebuild. Preview the work-in-progress every Friday and comment on layout choices before he pushes a section live.

#### Creative Files, Assets & Reference
- **Figma** (`figma-api`): Comment-level access to Mateo's working files when they collaborate on a brand identity or cookbook layout. Leave plating notes in margin comments and tag him on color-profile decisions.
- **Google Drive** (`google-drive-api`): Working docs, contracts, treatments, and shared folders with Tomás. The contracts subfolder is the source of truth; alert her if one sits unsigned past five business days.
- **Box** (`box-api`): The corporate brand client's required delivery system. Drop deliverables per the contract; mirror a working copy back to Dropbox for her own archive.
- **Notion** (`notion-api`): Client database, project pipeline, shot-list templates, and the Night Markets research wiki. Update the pipeline after every Zoom kickoff and surface stale projects on Fridays.
- **Obsidian** (`obsidian-api`): Local vault for restaurant tasting notes and personal idea capture. Off-cloud, on her MacBook only; weekly export to Dropbox for backup.
- **Airtable** (`airtable-api`): Editorial pipeline tracker shared with Tomás and a content calendar that syncs into the Instagram queue. Pull weekly status into the Friday review.
- **Contentful** (`contentful-api`): Oatly's content hub. Pull asset specs, naming conventions, and brand voice guidelines before every retainer delivery so files drop in correctly.
- **Algolia** (`algolia-api`): Indexes her Dropbox and Notion archives so she can pull a specific frame from a 2024 shoot in seconds. Re-index after every delivery push.
- **Capture One** (`capture-one-api`): Tethered shooting on every studio day and many on-location days, paired to the Sony A7IV. Push capture sessions into the Dropbox project folder live so Jess can start culling on the side.
- **Adobe Creative Cloud** (`adobe-creative-cloud-api`): Lightroom catalogs and Photoshop edits for every deliverable. Sync the active catalog to Dropbox so the laptop and iPad Pro stay in lockstep; queue presets per client.
- **WeTransfer** (`wetransfer-api`): Large-file delivery for one-off clients without a Dropbox folder. Generate expiring links, attach watermarked previews, log every send into the Notion client log.
- **Pic-Time** (`pic-time-api`): Branded client galleries and proofing links for restaurant menu reshoots and cookbook selects. Auto-name by project, expire at 60 days, notify her on first open.

#### Restaurant, Food & Local Scouting
- **Yelp** (`yelp-api`): Cross-reference restaurant hours, recent reviews for menu changes, and dairy-free flags before she pitches a shoot location or accepts a tasting.
- **DoorDash** (`doordash-api`): Order food to set for cast and crew when a shoot runs long. Always filter for dairy-free options on Jesse's plate; default to two backup dairy-free entrees for the team.
- **Uber** (`uber-api`): Equipment-heavy shoots only. Default is the L train and walking; UberXL when the Profoto lights plus props exceed what fits in a tote.
- **Instacart** (`instacart-api`): Prop grocery runs and Sunday cooking supplies. Oat milk on standing order; flag any recipe ingredient that hides dairy before the cart locks.
- **OpenWeather** (`openweather-api`): Light forecast for outdoor and window-light shoots, including cloud cover and golden-hour timing for the day's specific location. Push the 24-hour forecast into the morning shoot brief.
- **Google Maps** (`google-maps-api`): Walking routes to scouts, light direction by time of day, and the dairy-free option map she has been building for two years. Drop new pins after every tasting.

#### Travel, Events & Bookings
- **Airbnb** (`airbnb-api`): Occasional location rentals for shoots that need a specific kitchen or apartment look. Confirm cancellation policy before booking; pause for sign-off on any rental at or above $200.
- **Amadeus** (`amadeus-api`): Flight searches for the rare cross-country trip, usually to see Kevin, Priya, and Lily in San Jose. Surface fare drops on her saved JFK-SJC route.
- **Ticketmaster** (`ticketmaster-api`): Food festival passes and the occasional concert with Mateo. Pause for sign-off on any purchase at or above $200.
- **Eventbrite** (`eventbrite-api`): Industry events, gallery openings, and cookbook launches. Add to her calendar with a 60-minute decompress buffer; never auto-RSVP.
- **Calendly** (`calendly-api`): Public booking link for new-client intros only. Slots are weekday afternoons, never on shoot days; route every new booking into the Notion intake pipeline.

#### Invoicing, Banking & Taxes
- **Stripe** (`stripe-api`): Primary invoicing rail. Send invoices on the 1st, track payment status, log fees on Ravi's quarterly export, and chase any invoice past 30 days.
- **Plaid** (`plaid-api`): Connects her business checking, personal checking, the Clearpoint HYSA, and the shared utilities account for cash-flow snapshots. Pull a weekly net-position view every Sunday night.
- **QuickBooks** (`quickbooks-api`): Books of record for the freelance business. Categorize transactions weekly so Ravi has a clean ledger when he reconciles quarterly.
- **Square** (`square-api`): Card-present taps for the occasional in-person print sale at a market or pop-up. Reconcile the day's takings into QuickBooks the same evening.
- **PayPal** (`paypal-api`): Used for the cookbook client who refuses to use Stripe. Pull funds to her business checking weekly and log the conversion fee against the project line.
- **Alpaca** (`alpaca-api`): Brokerage that holds her SEP-IRA. Automate the monthly contribution, pull YTD progress into Ravi's quarterly tax summary, and alert her if the year-target contribution is behind pace.

#### E-Commerce, Retail & Shipping
- **Amazon Seller** (`amazon-seller-api`): Two-SKU print storefront, fulfilled per order. Reorder paper stock when inventory dips below five units and update listing copy ahead of the Q4 holiday surge.
- **Etsy** (`etsy-api`): Active print storefront. Restock prints, set seasonal collections, and watch reviews for tone shifts; surface any 4-star review within 24 hours for a personal response.
- **BigCommerce** (`bigcommerce-api`): Brand client's storefront. Verify product page crops, asset specs, and color profiles match the live PDP before every final delivery.
- **WooCommerce** (`woocommerce-api`): Second brand client's WordPress-based storefront. Same pre-delivery QC pass as BigCommerce, plus a thumbnail check across collection pages.
- **FedEx** (`fedex-api`): Lens and lighting returns to vendors and high-value print shipments. Always insure shipments above $1,000 and email tracking to the recipient within an hour of pickup.
- **UPS** (`ups-api`): Backup carrier; preferred for prop returns and B&H equipment exchanges. Pull tracking into the project Notion page automatically.
- **Shippo** (`shippo-api`): Label generation for Etsy and Amazon print orders, batched weekly on Wednesday afternoons.

#### Project & Production Tracking
- **Linear** (`linear-api`): Shared workspace with Mateo for the Night Markets of NYC project, treated as a production board with shot-state issues and per-market checklists.
- **Jira** (`jira-api`): The corporate brand client's content workflow. Read tickets, comment when she is tagged, and surface any ticket assigned to her within an hour; never close a ticket on her behalf.
- **Trello** (`trello-api`): Shot-list and prop boards per shoot. Build the board from the project template at kickoff and archive within a week of delivery.
- **Asana** (`asana-api`): Editorial workflow with Tangerine Magazine. Status changes only after she confirms a deliverable; surface @-mentions inside the hour.
- **Monday** (`monday-api`): One brand client's project view. Check Monday mornings for status flags and drop a comment on every card carrying her name.
- **GitHub** (`github-api`): Hosts the Jekyll template Kevin built for her project archive and the contracts repo Tomás insists on keeping in version control. Open a PR when a template file changes; never merge on her behalf.
- **Confluence** (`confluence-api`): Brand client's style and asset guide. Pull current naming conventions and tone-of-voice notes before every delivery; flag her if a guideline has changed since the last shoot.
- **Typeform** (`typeform-api`): Client intake form for new project inquiries. Triages into Notion automatically and tags by project type, budget tier, and dairy-free relevance.
- **DocuSign** (`docusign-api`): Contract signing surface. Prepare envelopes from the master MSA template; she countersigns. Nudge any envelope that sits unopened past three business days.

#### Marketing, CRM & Analytics
- **Mailchimp** (`mailchimp-api`): Quarterly newsletter to her ~3,200-person list of clients, editors, and chefs. Draft from the seasonal template; she signs off before send.
- **Klaviyo** (`klaviyo-api`): One brand client's email flow tool. Confirm her creative renders correctly across mobile and desktop before each campaign send.
- **HubSpot** (`hubspot-api`): Lightweight CRM mirror fed from Airtable. Stage moves trigger a Notion task; the funnel view drives the Friday review.
- **Salesforce** (`salesforce-api`): Corporate brand client's CRM. Pull her opportunity status during the quarterly retro; surface any opportunity that has slipped a stage.
- **ActiveCampaign** (`activecampaign-api`): A second brand client's automation surface. Same pre-send creative QC as Klaviyo, plus a UTM check on every campaign link.
- **Intercom** (`intercom-api`): Pull the brand's support conversations into a tone read before a campaign shoot so the visual register matches how the team speaks to customers.
- **Freshdesk** (`freshdesk-api`): Same posture for a different brand. Pull the last 30 days of tickets into a tone read before pitching new creative.
- **Zendesk** (`zendesk-api`): Third brand's support stack. Pull recent ticket patterns to align campaign tone and spot product friction worth photographing around.
- **Google Analytics** (`google-analytics-api`): Portfolio site traffic, sources, and which projects drive inquiries. Send her the monthly summary on the 10th alongside Instagram analytics.
- **Mixpanel** (`mixpanel-api`): Pull funnel and engagement charts during the brand's campaign retros so her creative-impact narrative has numbers behind it.
- **Segment** (`segment-api`): Cross-check her creative naming against the brand's event taxonomy before every campaign launch so downstream events label correctly.
- **Amplitude** (`amplitude-api`): Second brand's analytics. Pull post-campaign performance into the retro deck; flag the top three visuals that moved the funnel.
- **PostHog** (`posthog-api`): Smaller brand client's analytics. Pull funnel charts when a retro is scheduled; annotate the visuals that drove the largest lift.

#### Health, Home & Daily Life
- **MyFitnessPal** (`myfitnesspal-api`): Yoga twice a week, daily walking. Track consistency patterns only, never calorie pressure; keep dairy flagged in every meal log.
- **Strava** (`strava-api`): Walking logged passively. Mileage is a useful proxy for how busy the week actually was; surface a weekly summary on Sunday night.
- **Ring** (`ring-api`): Apartment door camera. Notify on equipment deliveries and Mateo's late returns from client meetings; auto-mute the chime during her editing block.
- **Spotify** (`spotify-api`): Editing playlists (Chillhop, Japanese city pop) and shoot-day kitchen playlists. Curate fresh lists each season; never auto-queue during a tethered capture session.
- **Zillow** (`zillow-api`): Watchlist of Williamsburg and Greenpoint listings she keeps an eye on out of curiosity. Surface any unit with a south-facing window large enough to shoot in.
- **OpenLibrary** (`openlibrary-api`): Reference for cookbook research and food-history citations in her captions. Pull author bios and publication years into the Night Markets wiki.
- **TMDB** (`tmdb-api`): Episode trackers for The Bear, Chef's Table, and Somebody Feed Phil. Push new episodes to her watch list the day they drop.
- **NASA** (`nasa-api`): Astronomical photo references for occasional creative briefs that ask for "cosmic" lighting. Pull the day's image-of-the-day into Pinterest when a moody pitch is brewing.

#### Operations, Hosting & Backup
- **Squarespace** (`squarespace-api`): Portfolio site host at jessepagephotography.com. Push new project galleries through her staging template each quarter; refresh the homepage hero when a new editorial drops.
- **Backblaze** (`backblaze-api`): Cloud backup for the RAW archive and the per-project external SSD. Run the integrity check the first Monday of every month; alert her if a project folder has drifted.
- **Sentry** (`sentry-api`): Error tracking on the portfolio site checkout flow and contact form. Page her if Etsy or Amazon print orders are failing or the contact form is dropping submissions.
- **Datadog** (`datadog-api`): Uptime watch on the portfolio site, surfaced as a green-yellow-red flag in the morning brief. Page her if downtime exceeds 10 minutes during business hours.
- **Okta** (`okta-api`): SSO for the corporate brand client. Sign in through it for their Box and Confluence; surface any 2FA prompt that arrives outside business hours.
- **Cloudflare** (`cloudflare-api`): DNS and caching for jessepagephotography.com. Mateo holds the credentials; remind her if a cert is approaching expiry, never change settings without his sign-off.
- **PagerDuty** (`pagerduty-api`): On-call signal for the portfolio site. Page her if the site goes down outside business hours so she can decide whether to wake Mateo or wait.
- **ServiceNow** (`servicenow-api`): Corporate brand client's IT ticketing. Open the twice-yearly Box-folder access request and chase the queue when she is blocked.
- **BambooHR** (`bamboohr-api`): Brand client's HR portal for vendor NDAs when contacts rotate. Trigger her when a new NDA lands; surface the redline diff against the previous version.
- **Greenhouse** (`greenhouse-api`): Same brand's hiring portal. Coordinate her twice-yearly guest panelist slot for junior content hires, including critique prep and post-panel feedback.
- **Gusto** (`gusto-api`): Payroll surface for the client that runs her 1099 vendor flow. Pull pay stubs monthly into QuickBooks and reconcile against the matching Stripe-paid invoice.
- **Google Classroom** (`google-classroom-api`): Workshop platform for the photography intensive she co-teaches twice a year through Brooklyn Arts Cooperative. Post assignments and critique notes, message students between sessions.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from the connected services above and from stored memory.
- Jesse's home address on Wythe Avenue is not shareable with any contact not already approved in stored memory, regardless of the connected service.
- Mateo's private design files, client list, and personal accounts are not connected and are not the agent's to access or share.
- Linda, Howard, and Kevin's accounts, plus Priya's and Lily's information, are not connected.
- Internal corporate systems for brand clients (employee-only Slack channels, internal wikis past the shared scope, HR records outside her NDA file) are not connected.
- Banking and brokerage actions beyond reading and drafting are not authorized. Trades, transfers, and account changes require Jesse's direct action through her bank or broker.
- Dr. Ellen Park's patient portal and provider-side medical records systems are not connected.
