# Tools: Angela Pham

## Tool Usage

### Connected Services

#### Google Workspace & Personal Productivity
- **Gmail** (`gmail-api`): Personal correspondence on `angela.pham@Finthesiss.ai`. Medical scheduling, school, CPA, golf club, D&D and BBQ groups.
- **Google Calendar** (`google-calendar-api`): Family calendar, Saturday tee times, D&D, medical appointments, BBQ cooks. Default time-block tool.
- **Google Drive** (`google-drive-api`): D&D campaign binder, household docs, coffee inventory, BBQ logs. Personal account only.
- **Google Maps** (`google-maps-api`): Drive time to Prestonwood, soccer fields, UNC Healthcare, and the parents' house in Cary.
- **Google Classroom** (`google-classroom-api`): Read-only view of Minh's 2nd grade assignments at Underwood Elementary. No write actions on Angela's behalf.
- **Calendly** (`calendly-api`): Booking link Angela shares with mentees and occasional Unreal community contacts. Holds reserved focus windows.
- **DocuSign** (`docusign-api`): Insurance forms, school paperwork, CPA returns, and Raj's practice documents she co-signs.
- **Dropbox** (`dropbox-api`): Read-only legacy archive from grad school and earlier Epic work.
- **Box** (`box-api`): Read-only Northwestern Mutual policy docs and a few inherited family files.
- **Notion** (`notion-api`): Personal planning, Vietnam trip itinerary draft, and the D&D worldbuilding wiki.
- **Obsidian** (`obsidian-api`): Local vault for engineering notes, brisket cook logs, and migraine pattern tracking.

#### Messaging & Voice
- **WhatsApp** (`whatsapp-api`): Vietnam-side family, the Buon Ma Thuot coffee estate, and Raj's parents on travel weeks.
- **Discord** (`discord-api`): D&D group server, the Saturday foursome occasional channel, and two Hanoi FC supporters servers.
- **Slack** (`slack-api`): Reference-only mirror. Epic Slack lives on the work device and stays there.
- **Microsoft Teams** (`microsoft-teams-api`): Reference-only. Epic also runs Teams, also on the work device.
- **Telegram** (`telegram-api`): Read-only on two BBQ competition organizers' channels.
- **Outlook** (`outlook-api`): Reference-only. `angela.pham@epicgames.com` is the work device. Never relay.
- **Zoom** (`zoom-api`): Telehealth with Dr. Rachel Kim and occasional family video with Hanoi cousins.
- **Twilio** (`twilio-api`): SMS relays for delivery notices, school auto-texts, and golf foursome timing pings.
- **SendGrid** (`sendgrid-api`): Outbound transactional mail for the D&D group when she invites a guest player.
- **Mailgun** (`mailgun-api`): Backup transactional relay for the coffee collection spreadsheet alerts.

#### Engineering, DevOps & Architecture Reference
- **GitHub** (`github-api`): Personal account. Side scripts for the coffee tasting spreadsheet, D&D dice helpers, and BBQ thermometer parsing.
- **GitLab** (`gitlab-api`): Read-only. Watches indie Unreal community plugins her engineers contribute to.
- **Jira** (`jira-api`): Reference-only. Epic Jira lives on the work device.
- **Linear** (`linear-api`): Personal project tracker for the UE-adjacent reading list, household projects, and one open-source side project.
- **Confluence** (`confluence-api`): Reference-only. Epic Confluence lives on the work device.
- **Figma** (`figma-api`): D&D map layouts, brisket cook timeline diagrams, and one mentee's portfolio review.
- **Sentry** (`sentry-api`): Reference-only. Watches errors on her coffee inventory web app.
- **Datadog** (`datadog-api`): Reference-only. Personal Raspberry Pi metrics for the smoker temperature rig.
- **PagerDuty** (`pagerduty-api`): Wakes her if the smoker rig drops below 200F mid-cook. No on-call rotation.
- **Kubernetes** (`kubernetes-api`): Read-only on the tiny home cluster running family photo backup and the D&D map server.
- **Cloudflare** (`cloudflare-api`): DNS and edge for `pham-family.net`. The kids' family photo site sits behind it.
- **Okta** (`okta-api`): Reference-only. Personal SSO for a few side service logins.
- **ServiceNow** (`servicenow-api`): Reference-only. Pediatric dentistry vendors Raj evaluates run on it.
- **Algolia** (`algolia-api`): Search index over the Vietnamese coffee tasting journal.
- **Contentful** (`contentful-api`): Drafting CMS for the homebrew D&D campaign wiki.

#### Coordination, Forms & Customer Inboxes
- **Asana** (`asana-api`): Vietnam trip planning board shared with Hung and the kitchen renovation backlog.
- **Trello** (`trello-api`): Saturday golf foursome rotation board and a brisket competition tracker.
- **Monday.com** (`monday-api`): Household project board for the basement build-out planned next year.
- **Airtable** (`airtable-api`): Coffee collection inventory, BBQ competition log, and D&D NPC roster.
- **Typeform** (`typeform-api`): D&D group session feedback forms and mentee intake forms when she takes a new one.
- **Intercom** (`intercom-api`): Inbox for the small coffee tasting blog she barely maintains.
- **Freshdesk** (`freshdesk-api`): Backup support inbox for the same blog, mostly auto-route.
- **Zendesk** (`zendesk-api`): Read-only tickets for two specialty vendors she buys smoker accessories from.

#### Product Analytics & Telemetry
- **Google Analytics** (`google-analytics-api`): Traffic on the coffee tasting blog. Quarterly skim.
- **Amplitude** (`amplitude-api`): Reference-only. A mentee asked her to spot-check a funnel last quarter.
- **PostHog** (`posthog-api`): Self-hosted funnel data for the coffee blog.
- **Mixpanel** (`mixpanel-api`): Reference-only. One side-project mobile app she advises on.
- **Segment** (`segment-api`): Routes the coffee blog events to PostHog and GA. Set and forget.

#### Marketing, CRM & Outreach
- **Salesforce** (`salesforce-api`): Reference-only. Raj's practice vendor relationships sit here.
- **HubSpot** (`hubspot-api`): Reference-only. The coffee importer she buys from runs HubSpot lifecycle.
- **Mailchimp** (`mailchimp-api`): Quarterly D&D player newsletter and Tet party invites for the wider family list.
- **Klaviyo** (`klaviyo-api`): Reference-only. Two retailers she buys from send flow emails she silences.
- **ActiveCampaign** (`activecampaign-api`): Reference-only. Another retailer flow she keeps muted.

#### Finance, Banking & Markets
- **Plaid** (`plaid-api`): Read-only aggregator across Chase checking, Ally HYSA, Fidelity, Schwab, and the BMW loan.
- **Stripe** (`stripe-api`): Coffee blog tip jar. Quarterly statement review.
- **QuickBooks** (`quickbooks-api`): Reference-only. Andrew Tillman files the joint return out of QuickBooks.
- **Xero** (`xero-api`): Reference-only. Raj's practice runs Xero. Off-limits without his explicit ask.
- **PayPal** (`paypal-api`): Coffee estate transfers and occasional D&D supplies. Two-factor on.
- **Square** (`square-api`): Reference-only. BBQ vendors at NC competitions take Square.
- **Alpaca** (`alpaca-api`): Reference-only. Watching one paper-trading bot a mentee wrote.
- **Coinbase** (`coinbase-api`): Read-only on a small experimental position. No active trading.
- **Binance** (`binance-api`): Reference-only. Off-limits for transactions.
- **Kraken** (`kraken-api`): Reference-only. Off-limits for transactions.

#### Hobbies, Sport, Media & Culture
- **OpenWeather** (`openweather-api`): Pre-cook forecast for Sunday brisket, Saturday tee-time wind read, and run window check.
- **Spotify** (`spotify-api`): Family playlists. Arctic Monkeys, The National, Ngot, Vu, A Tribe Called Quest, De La Soul.
- **TMDB** (`tmdb-api`): Movie night picks with Raj and occasional kid film vetting.
- **Vimeo** (`vimeo-api`): Indie Unreal community shorts and a few D&D actual-play clips.
- **YouTube** (`youtube-api`): Brisket reference cooks, golf swing breakdowns, and Hanoi FC match recaps. YouTube Premium account.
- **Twitch** (`twitch-api`): Hanoi FC fan streams in V-League off hours and a couple of D&D streamers she watches.
- **Reddit** (`reddit-api`): r/BBQ, r/golf, r/DnD, r/HanoiFC, r/UnrealEngine. Lurker.
- **Twitter** (`twitter-api`): Read-only. Following Unreal engineers, BBQ pitmasters, and Hanoi FC journalists.
- **Instagram** (`instagram-api`): Personal account. Coffee setups, brisket shots, kid photos shared only with grandparents.
- **Pinterest** (`pinterest-api`): D&D map inspiration, kitchen ideas, and kid party planning.
- **LinkedIn** (`linkedin-api`): Light touch on connections she actually knows. No content posting on her behalf.
- **NASA** (`nasa-api`): Solar weather and air quality for outdoor cooks, plus one Hanoi FC away-day flight path lookup.
- **OpenLibrary** (`openlibrary-api`): Reading list lookups, currently Andy Weir and Tanya Reilly titles.
- **Eventbrite** (`eventbrite-api`): BBQ qualifier registration and the occasional Raleigh tech meetup.
- **Ticketmaster** (`ticketmaster-api`): Hanoi FC US-tour matches and occasional concert tickets for date night.
- **Strava** (`strava-api`): Tuesday and Thursday Umstead runs and Saturday morning route logs.
- **MyFitnessPal** (`myfitnesspal-api`): Crohn's safe-foods tracker during flares; stays quiet between flares.

#### Food, Home & Local Errands
- **Yelp** (`yelp-api`): Bida Manda, Vidrio, Longleaf Swine, Brewery Bhavana. Reservation and hours lookup.
- **DoorDash** (`doordash-api`): Friday D&D pizza order and late evening crunch dinners.
- **Instacart** (`instacart-api`): Weekly grocery for the Vietnamese-Indian-American kitchen rotation. Raj owns the list.
- **Uber** (`uber-api`): Airport runs for Unreal Fest, Vietnam trip, and the occasional late ride home.
- **Airbnb** (`airbnb-api`): BBQ competition weekends, Hilton Head family rentals, and Vietnam logistics.
- **Zillow** (`zillow-api`): Casual watch on Falls of Neuse comps. No transactions.
- **Ring** (`ring-api`): Doorbell and exterior cameras. Notify on package and on Linh's pickup arrival.

#### Travel, Shipping & Logistics
- **Amadeus** (`amadeus-api`): Flights for Unreal Fest, the Vietnam trip with Hung, and BBQ travel.
- **FedEx** (`fedex-api`): Humira specialty pharmacy shipments. Track aggressively.
- **UPS** (`ups-api`): D&D miniature orders and coffee bean shipments from Nguyen Coffee Supply.
- **Shippo** (`shippo-api`): Return labels for BBQ accessory misorders.

#### Storefronts, Web & E-Commerce Reference
- **Amazon Seller** (`amazon-seller-api`): Reference-only. A friend's small Hanoi FC merch shop she advises on.
- **Etsy** (`etsy-api`): Reference-only. The Vietnamese coffee artisan she buys from sells here.
- **BigCommerce** (`bigcommerce-api`): Reference-only. One BBQ rub vendor she likes.
- **WooCommerce** (`woocommerce-api`): Reference-only. Stands by for the coffee blog merch store if she ever turns it back on.
- **Webflow** (`webflow-api`): Coffee tasting blog frontend.
- **WordPress** (`wordpress-api`): Reference-only archive of early blog posts before Webflow.

#### HR & People Operations Reference
- **BambooHR** (`bamboohr-api`): Reference-only. Raj's practice runs BambooHR for office staff.
- **Greenhouse** (`greenhouse-api`): Reference-only. Used once to evaluate two Unreal hiring funnel candidates as a favor.
- **Gusto** (`gusto-api`): Reference-only. Raj's practice payroll. Off-limits without his explicit ask.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from connected mock APIs and stored memory.
- Epic Games internal systems (work Outlook on `angela.pham@epicgames.com`, work Slack, work Jira, work Confluence, work Teams, Perforce, and any UE proprietary tooling) live on the work MacBook and are not connected.
- Raj's Triangle Kids Dental clinical systems and patient records are kept separate by design.
- Personal banking apps (Chase, Ally, Fidelity, Schwab) and brokerage transaction surfaces are phone-and-web only, not connected for actions.
- The kids' Primrose and Underwood school portals are not connected; Raj and Angela log in directly.
- Angela's parents' and in-laws' personal accounts are not connected.
