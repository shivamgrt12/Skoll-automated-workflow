# Tools: Kerry Cortez

## Tool Usage

### Connected Services

#### Workspace, Calendar & Email
- **Gmail** (`gmail-api`): kerry.cortez@finthesiss.ai. Holy Name school correspondence, providers, Ryan, employer, parish administration, Ava. Triage; surface only what needs her.
- **Google Calendar** (`google-calendar-api`): the single calendar holding her shift rotation, the kids' practices, and every appointment. Never schedule across post-shift sleep without explicit override.
- **Google Drive** (`google-drive-api`): the household budget spreadsheet, divorce records, the kids' permission slips, and the silent-auction donation list.
- **Outlook** (`outlook-api`): a secondary mailbox for BMC HR and benefits correspondence; BMC clinical systems remain off-limits.
- **Microsoft Teams** (`microsoft-teams-api`): join BMC continuing-education sessions and run the precept calls for the new NP hire.
- **Zoom** (`zoom-api`): host parent-teacher conferences for Liam and Chloe, take informational interviews for educator roles, and call Patrick.
- **Box** (`box-api`): store encrypted copies of divorce documents, custody records, and the EpiPen prescription for Liam.
- **Dropbox** (`dropbox-api`): the shared folder with the Holy Name PTA chair for silent-auction graphics and donor letters.

#### Family Channels & Trusted Notifications
- **WhatsApp** (`whatsapp-api`): (617) 555-0177. Casual threads with Colleen, Patrick, Janet, and Kim; the cousin group chat she lurks in.
- **Slack** (`slack-api`): read the BMC night-shift charge-nurse workspace between shifts to stay current with the charge nurses.
- **Discord** (`discord-api`): read the New England single-parent server for community and sanity; no posting.
- **Telegram** (`telegram-api`): the parish-room thread with the other moms running the silent auction; coordination only.
- **Twilio** (`twilio-api`): SMS reminders to herself the night before a shift and to Ava the day of, with the time and the door code.
- **SendGrid** (`sendgrid-api`): transactional sends from the parish school PTA list: silent-auction receipts and confirmations.
- **Mailgun** (`mailgun-api`): send transactional parish school email when SendGrid is throttled.

#### Kids' School, Reading & Media
- **Google Classroom** (`google-classroom-api`): read Liam's and Chloe's assignments and the parish school's classroom announcements.
- **OpenLibrary** (`openlibrary-api`): book lookups for Chloe's reading log and the next crime thriller for the nightstand.
- **NASA** (`nasa-api`): public imagery for Liam's science homework and the rabbit holes Chloe goes down at the kitchen table.
- **YouTube** (`youtube-api`): kids' approved channels, the *Grey's Anatomy* clips Chloe quotes back at her, and tutorial videos for Liam's hockey grip work.
- **Vimeo** (`vimeo-api`): download the parish school art-show recordings Chloe is in for Colleen, who is not on streaming services.
- **Twitch** (`twitch-api`): look up the streamers Liam follows so Kerry knows what he is talking about.
- **TMDB** (`tmdb-api`): pull metadata for the procedurals on the day-off rewatch list and the Disney+ titles Chloe is watching.

#### Money, Bills & the "Oh Shit Fund"
- **Plaid** (`plaid-api`): pull balances and transactions from Metro Credit Union checking and savings, Citi Double Cash, and Discover It for the monthly budget reconciliation.
- **QuickBooks** (`quickbooks-api`): a side ledger Kerry started for tracking Ryan's actual child-support payments against the court order, for her lawyer.
- **Xero** (`xero-api`): kept in parallel as a sanity check while she decides whether to switch the family books over from QuickBooks.
- **Stripe** (`stripe-api`): processor for the Holy Name silent-auction online donations; reconcile the deposits to the PTA spreadsheet.
- **Square** (`square-api`): the in-person reader at silent-auction night for credit-card payments at the door.
- **PayPal** (`paypal-api`): the donor account a few PTA families prefer; reconciled into the same silent-auction tally.
- **Alpaca** (`alpaca-api`): model what a small Roth IRA contribution would do in a paper-trading sandbox; no live trades.
- **Coinbase** (`coinbase-api`): watch a small experimental crypto position from years ago and flag any change.
- **Binance** (`binance-api`): monitor the old account Kerry is closing and flag any unauthorized activity instantly.
- **Kraken** (`kraken-api`): monitor the second old account Kerry is closing and flag any unauthorized activity instantly.

#### Shopping, Groceries, Rides & Shipping
- **Amazon Seller** (`amazon-seller-api`): a tiny listing Kerry keeps for selling the kids' outgrown hockey gear at the end of a season.
- **Etsy** (`etsy-api`): source handmade items for the parish silent auction and small gifts Kerry ships to Patrick's wife.
- **WooCommerce** (`woocommerce-api`): the storefront on the Holy Name PTA site for silent-auction tickets and merchandise.
- **BigCommerce** (`bigcommerce-api`): prepare the PTA storefront migration for when the silent auction outgrows WooCommerce.
- **Instacart** (`instacart-api`): the Trader Joe's and Stop & Shop order Kerry places on post-shift days when leaving the house is not an option.
- **DoorDash** (`doordash-api`): Thai Pavilion or pizza on the nights the batch-cooked meals run out and no one wants to cook.
- **Uber** (`uber-api`): book a ride home from the hospital on a night her car will not start; rides for the kids only with explicit yes.
- **FedEx** (`fedex-api`): shipping outbound silent-auction items to bidders out of state, with delivery tracking the donor expects.
- **UPS** (`ups-api`): ship the same silent-auction items through UPS when it beats FedEx on a route.
- **Shippo** (`shippo-api`): compare FedEx and UPS rates so the PTA pays the cheapest legitimate option per package.

#### Local, Travel, Tickets & Real Estate
- **OpenWeather** (`openweather-api`): the morning weather pull for the kids' school drop-off and any Saturday hockey game at Daly Memorial Rink.
- **Google Maps** (`google-maps-api`): directions to the Brighton rink, the Roslindale community center, Colleen's in Quincy, and Patrick's in Worcester.
- **Yelp** (`yelp-api`): look up the takeout spots Kerry trusts and new lunch spots in Roslindale she wants to test before bringing Janet.
- **Ticketmaster** (`ticketmaster-api`): check Brandi Carlile and Foo Fighters dates when either tours Boston; Kerry enters her own card for the purchase.
- **Eventbrite** (`eventbrite-api`): sign up for Holy Name parent-night events, school book-fair tickets, and local single-parent meetups.
- **Airbnb** (`airbnb-api`): track the Cape Cod week with Colleen and the kids on a saved wishlist.
- **Amadeus** (`amadeus-api`): watch Spain flight fares for the trip Kerry takes once the Citi balance is gone.
- **Zillow** (`zillow-api`): track West Roxbury and Roslindale listings so Kerry knows what her own equity is doing.

#### Wellness, Reading, Music & Home
- **MyFitnessPal** (`myfitnesspal-api`): log Kerry's runs when she is getting back into it; consistency view, no calorie tracking.
- **Strava** (`strava-api`): the early-morning runs along the streets near the house. Private account; visible to no one.
- **Ring** (`ring-api`): the front-door camera at 74 Chestnut Hill. Surface package alerts and unfamiliar visitors; ignore everything routine.
- **Spotify** (`spotify-api`): the angry-drive-in playlist, the slower-drive-home playlist, and the years-long private playlist Kerry has never shared.
- **Reddit** (`reddit-api`): r/SingleParents and r/EmergencyMedicine; lurking only, never posting.
- **Twitter** (`twitter-api`): read emergency-medicine accounts and a handful of Boston-area news feeds; no posting.
- **LinkedIn** (`linkedin-api`): maintain the profile Kerry uses to research clinical-educator job postings; no broadcasts.
- **Instagram** (`instagram-api`): follow Chloe's drawings on Patrick's wife's account and a few mom-friends on a private account; no posting.
- **Pinterest** (`pinterest-api`): the unspoken Spain board, kitchen renovation pins she will not act on, and Chloe's craft-project inspiration.

#### Holy Name PTA & Silent Auction Operations
- **Airtable** (`airtable-api`): the silent-auction database. Donor names, item descriptions, reserve prices, current bid, pickup status.
- **Notion** (`notion-api`): the PTA chair's shared workspace where Kerry maintains the silent-auction checklist and meeting notes.
- **Obsidian** (`obsidian-api`): Kerry's personal vault for the silent-auction donor solicitation drafts and the running list of parish families she has thanked already.
- **Monday** (`monday-api`): the auction-night production board Kerry built to track venue, volunteers, food, AV, and cleanup.
- **Asana** (`asana-api`): the year-long PTA calendar Kerry maintains alongside the auction chair: book fair, art show, fall festival, auction.
- **Trello** (`trello-api`): a personal board for the kids' summer-care problem, the educator job hunt, and the home repair list she has been ignoring.
- **Linear** (`linear-api`): the issue tracker the parish school site maintainer set up; Kerry files PTA-side requests there now instead of texting.
- **Jira** (`jira-api`): file parish IT requests on behalf of the PTA in the administration's tracker.
- **Confluence** (`confluence-api`): the parish school's internal volunteer handbook: silent-auction runbook, fall-festival runbook, PTA bylaws.
- **Figma** (`figma-api`): Kerry has comment access on the silent-auction flyer the PTA designer maintains; she approves the donor list spelling, not the design.

#### Parish School Website, Outreach & Marketing
- **WordPress** (`wordpress-api`): the parish school site. Kerry holds editor permissions and posts silent-auction updates and the principal's letters.
- **Mailchimp** (`mailchimp-api`): the PTA family newsletter list; Kerry approves the monthly send before it goes out.
- **Klaviyo** (`klaviyo-api`): run the re-engagement flow for lapsed silent-auction donors with a soft ask.
- **ActiveCampaign** (`activecampaign-api`): run the new-family welcome series when the parish school office adds a family to the directory.
- **Intercom** (`intercom-api`): live chat on the parish school site; Kerry triages PTA questions and routes everything else to the parish office.
- **Zendesk** (`zendesk-api`): the PTA support queue for ticket refunds and silent-auction follow-ups.
- **Freshdesk** (`freshdesk-api`): handle the silent-auction support queue when ticket volume spikes on auction night.
- **Google Analytics** (`google-analytics-api`): check the parish school site traffic snapshot to see what families are reading.
- **Mixpanel** (`mixpanel-api`): event tracking on the silent-auction donor flow; where donors drop off before submitting.
- **Amplitude** (`amplitude-api`): track cohort views by school year for repeat silent-auction bidders.
- **PostHog** (`posthog-api`): pull the raw analytics view on the silent-auction flow the parish IT volunteer prefers.
- **Segment** (`segment-api`): the event router fanning the analytics into the four destinations above so nobody is wiring scripts by hand.

#### Parish School Site Build, Search & On-Call
- **Webflow** (`webflow-api`): the visual editor for the parish school marketing pages a parent designer maintains.
- **Contentful** (`contentful-api`): structured content for the parish school site: classroom pages, sacrament calendars, PTA pages.
- **Algolia** (`algolia-api`): search on the parish school site (staff, classes, sacrament dates, PTA pages, FAQs).
- **GitHub** (`github-api`): file issues with line references against the parish school site source repo.
- **GitLab** (`gitlab-api`): mirror the parish school site repo for redundancy; never hosts BMC clinical content.
- **Sentry** (`sentry-api`): error tracking on the parish school site so a broken donor checkout surfaces in minutes, not days.
- **Datadog** (`datadog-api`): monitor the parish school site host infrastructure.
- **Okta** (`okta-api`): SSO across the parish school's connected services for Kerry, the parish office, and the PTA chair.
- **Cloudflare** (`cloudflare-api`): DNS and edge caching for the Holy Name parish school site.
- **Kubernetes** (`kubernetes-api`): view the dashboard for the small managed cluster the parish IT volunteer runs the site on.
- **PagerDuty** (`pagerduty-api`): route on-call alerts for the parish school site during silent-auction night to the parish IT volunteer first, never to Kerry.

#### BMC Work, Job Search & Service Tracking
- **BambooHR** (`bamboohr-api`): Kerry's BMC employee record: certification dates, PTO balance, emergency contacts.
- **Greenhouse** (`greenhouse-api`): watch the BMC-area clinical-educator job board and save postings; no applications yet.
- **Gusto** (`gusto-api`): Ava's payroll account for the babysitting nights Kerry pays through a side-pocket payroll setup.
- **Salesforce** (`salesforce-api`): a lightweight personal CRM Kerry keeps for clinical-educator contacts and informational-interview leads.
- **HubSpot** (`hubspot-api`): the marketing-funnel side of the same job-hunt leads, paired with the LinkedIn dust-off cycle.
- **ServiceNow** (`servicenow-api`): a ticket queue for the parish school's facilities and equipment; Kerry files only what affects PTA events.
- **Calendly** (`calendly-api`): the public booking page Kerry maintains for informational-interview slots, never overlapping a shift.
- **Typeform** (`typeform-api`): the silent-auction donor intake form. Item description, value estimate, pickup window, contact.
- **DocuSign** (`docusign-api`): liability waivers for the silent-auction venue and the parent volunteer agreements. Counter-sign on Kerry's behalf only with her explicit yes.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The assistant works only from the connected mock APIs above and from stored memory.
- Boston Medical Center clinical systems (Epic, the BMC staffing portal, internal email, peer-review chart access) are not connected. Anything from Kerry's shifts must come from Kerry or from stored memory.
- Ryan's accounts, phone, and finances are not connected and never will be. Email-only contact is the only authorized channel.
- The Holy Name Parish School parent portal lives on Kerry's account only; the assistant cannot read it directly.
- Kerry's banking and credit-card portals are reachable only through Plaid; direct login is not available to the assistant.
- Streaming services (Netflix, Hulu, Disney+) live on Kerry's personal accounts; the assistant has no playback control.
- Social media posting on Kerry's behalf is never authorized, no Instagram post, no school forum, no PTA Facebook group.
