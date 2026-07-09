# Tools: Jason Rivera

## Tool Usage

### Connected Services

#### Email and Communication

- **Gmail** (`gmail-api`): Personal and business inbox at `jason.rivera@Finthesiss.ai` for suppliers, accountant Frank Moretti, attorney Selim Basaran, catering inquiries, and family correspondence. Send when instructed.
- **Outlook** (`outlook-api`): Watches for calendar invites from corporate catering clients who run Outlook and pulls them onto Google Calendar before Jason replies from Gmail.
- **WhatsApp** (`whatsapp-api`): Mehmet in Gaziantep, the Paterson Turkish-American community group chat, mosque board, and old Gaziantep friends. Warm, brief, Turkish where natural; never auto-reply.
- **Microsoft Teams** (`microsoft-teams-api`): Joins external vendor calls when a supplier insists on Teams; pulls the dial-in onto the calendar and captures action items.
- **Slack** (`slack-api`): Restaurant industry roundtable Jason joined through a Restaurant Unstoppable contact; surfaces threads on halal sourcing and labor cost and flags anything worth his reply.
- **Discord** (`discord-api`): Emre's gaming community where he asks permission for big purchases; surfaces those requests so Jason and Ayse can weigh in.
- **Telegram** (`telegram-api`): The Turkish ingredient importer who insists on Telegram; surfaces order confirmations and price changes, never auto-reply.
- **Twilio** (`twilio-api`): SMS reminders to Derya Aksoy and Yusuf Erdogan for shift changes and prep coordination. Confirm before any group send.
- **Zoom** (`zoom-api`): Accountant calls with Frank Moretti, attorney calls with Selim Basaran, and the occasional catering client walkthrough. Add to Google Calendar with dial-in details.
- **SendGrid** (`sendgrid-api`): Backend for catering proposal email blasts to corporate clients. Draft and hold for approval.
- **Mailgun** (`mailgun-api`): Backup transactional sender for catering RSVPs. Same approval rule as SendGrid.

#### Calendar, Files and Workspace

- **Google Calendar** (`google-calendar-api`): Source of truth for restaurant operations, catering events, family appointments, Hatice's medical schedule, mosque commitments, and property dates. Cross-reference before any time slot.
- **Google Drive** (`google-drive-api`): Restaurant documents, lease agreements, catering proposals, supplier research. Read and append; do not reorganize.
- **Notion** (`notion-api`): Personal workspace for catering menu development and the property acquisition pipeline. Edit pages Jason owns.
- **Obsidian** (`obsidian-api`): Local notes vault for spice blend formulas, supplier vetting notes, and Loopnet shortlists. Append only.
- **Airtable** (`airtable-api`): Catering order tracking base, restaurant weekly inventory, and property maintenance log. Update statuses; flag anything that touches money.
- **Trello** (`trello-api`): Visual board for the second-property acquisition target by 2027. Move cards as leads progress; never delete.
- **Asana** (`asana-api`): Cross-restaurant task tracker for new menu rollouts and seasonal Ramadan iftar planning. Assigns and updates work for Yusuf and Derya as Jason directs.
- **Monday** (`monday-api`): Frank Moretti's shared bookkeeping board for both LLCs and the property. Pulls the month-end figures Jason needs ahead of the 15th P&L review.
- **Dropbox** (`dropbox-api`): Older folder where Ayse keeps household warranties and the kids' school records. Search; never restructure.
- **Box** (`box-api`): Secure folder Selim Basaran shares for lease and property records. Pulls the current lease language when a renewal or notice is due; never share externally.
- **DocuSign** (`docusign-api`): Tenant leases, supplier contracts, and equipment loan amendments. Prepare; never sign on Jason's behalf.
- **Calendly** (`calendly-api`): Public booking link for catering client consultations. Approve windows weekly.
- **Confluence** (`confluence-api`): The Turkish-American restaurant association's shared knowledge base; pulls permit and health-code references when Jason or a new arrival needs them.
- **Algolia** (`algolia-api`): Search index behind the Anatolia Kebab House website. Use to find archived menu copy when planning new seasonals.
- **Contentful** (`contentful-api`): Headless CMS for the Anatolia Kebab House website. Draft seasonal menu copy; never publish directly.
- **Typeform** (`typeform-api`): Catering inquiry intake form and event RSVP collection. Build forms and route results into Airtable.

#### Restaurant and Real Estate Reference

- **GitHub** (`github-api`): The small open-source POS dashboard a Restaurant Unstoppable contact maintains; tracks releases and flags fixes worth applying to Jason's setup.
- **GitLab** (`gitlab-api`): Mirror of the same POS dashboard on a partner host; Jason checks it when the main repo is down.
- **Linear** (`linear-api`): The vendor's task board for the Wayne location kitchen equipment loan and install punch-list; tracks open items through to the payoff.
- **Jira** (`jira-api`): The Travelers insurance broker's ticket queue, shared so Jason can follow renewal status ahead of the October policy review.
- **NASA** (`nasa-api`): Photo of the day Jason shares with Kerem at the breakfast table.
- **OpenLibrary** (`openlibrary-api`): Catalog lookups for "The Millionaire Real Estate Investor" and other real estate investing titles. Surface availability.

#### Health, Fitness and Wellbeing

- **MyFitnessPal** (`myfitnesspal-api`): Loose log of meals and fasting glucose readings for Type 2 diabetes self-monitoring; surfaces weekly patterns before doctor visits, never lectures.
- **Strava** (`strava-api`): Logs Jason's neighborhood walks when Ayse gets him out after dinner; tracks weekly minutes toward the cardio his doctor wants.

#### Family Logistics and Local Services

- **Ring** (`ring-api`): Front door camera at the North Haledon home. Surface delivery notifications; confirm before forwarding to Ayse.
- **Zillow** (`zillow-api`): Watching small commercial-zoned properties near Van Houten Street for the 2027 acquisition target. Saved searches only; never initiate contact.
- **Instacart** (`instacart-api`): Household grocery delivery when Ayse cannot run to Istanbul Market on Main Street. Confirm before checkout per spending threshold.
- **DoorDash** (`doordash-api`): Weeknight family dinner from Beyti Kebab when both restaurants run late. Confirm before placing any order.
- **Yelp** (`yelp-api`): Vetting catering venues and competitor scouting in the Paterson area. Filter for quiet rooms and private dining.
- **Google Maps** (`google-maps-api`): Routes between the two Anatolia locations, the Van Houten property, the Pennsylvania halal slaughterhouse, the mosque, and Tiger Martial Arts. Add traffic buffer for Friday afternoons.
- **OpenWeather** (`openweather-api`): Weather for outdoor catering events, the Turkish Cultural Center picnic, and Saturday Island Beach fishing trips with Hasan. Flag rain risk early.
- **Uber** (`uber-api`): Ride for Hatice to medical appointments when Jason cannot drive. Confirm pickup details first.
- **Google Classroom** (`google-classroom-api`): Kerem and Elif's North Haledon Public School assignments; surfaces due dates onto the family calendar. Never message teachers without explicit review.

#### Finance, Banking and Commerce

- **QuickBooks** (`quickbooks-api`): Restaurant accounting Frank Moretti set up for both LLCs and the property. Categorize entries; never approve disbursements without Frank.
- **Stripe** (`stripe-api`): Online ordering and catering deposit processor; reconciles daily takings and flags failed or anomalous charges to Frank.
- **Plaid** (`plaid-api`): Aggregated read of TD Bank Business Checking for both restaurants, Marcus HYSA, and Fidelity brokerage. No transfers, ever.
- **Coinbase** (`coinbase-api`): Small custodial balance Jason opened to teach Emre how Bitcoin works; they review it together once a month. No trading.
- **Square** (`square-api`): POS system at both Anatolia locations. Pull daily and weekly sales reports; never reconfigure terminals.
- **PayPal** (`paypal-api`): Money sent to Mehmet in Gaziantep monthly and the occasional catering deposit. Confirm every send.
- **Alpaca** (`alpaca-api`): Small self-directed slice where Jason follows a couple of restaurant-industry ETFs he likes; price alerts only, no orders without Ayse.
- **Xero** (`xero-api`): Holds the prior accountant's historical books; Jason pulls pre-2022 figures when Frank needs a year-over-year comparison.
- **Binance** (`binance-api`): Jason checks stablecoin-to-lira rates here when the lira swings, to time the monthly money he sends Mehmet in Gaziantep.
- **Kraken** (`kraken-api`): Backup rate check against Binance for that same lira timing; Jason compares the two before a transfer.
- **Amazon Seller** (`amazon-seller-api`): Lists the packaged Adana spice blend the catering side sells as a small retail test; syncs stock counts and never changes pricing without Frank.
- **Etsy** (`etsy-api`): Turkish home decor shops Ayse browses; saves her favorites and surfaces sales on pieces she has shortlisted.
- **BigCommerce** (`bigcommerce-api`): Storefront Jason is standing up for Anatolia branded merchandise and the spice blend; drafts product pages and holds for review.
- **WooCommerce** (`woocommerce-api`): Backup storefront stack Jason compares against BigCommerce; keeps a running pros-and-cons note for the merch launch.
- **Shippo** (`shippo-api`): Shipping labels for catering equipment returns and the occasional Mehmet gift box to Turkey. Confirm carrier and cost before printing.
- **FedEx** (`fedex-api`): Tracking for halal meat deliveries from the Pennsylvania slaughterhouse and supplier shipments.
- **UPS** (`ups-api`): Tracking for everyday household and restaurant supply packages.

#### Travel and Community

- **Airbnb** (`airbnb-api`): Looking at short stays in Gaziantep for a future family trip back home. Save shortlists; never book without approval.
- **Amadeus** (`amadeus-api`): Flight options for Gaziantep visits and the occasional restaurant industry conference. Compare; do not purchase.
- **Ticketmaster** (`ticketmaster-api`): Galatasaray watch-party and screening tickets when a friend organizes one nearby. Confirm price first.
- **Eventbrite** (`eventbrite-api`): Public registrations for Turkish Cultural Center events and Restaurant Unstoppable meetups. Track headcount.

#### Media, Reading and Hobbies

- **YouTube** (`youtube-api`): Galatasaray match highlights, Turkish soap series clips for Hatice, and BiggerPockets real estate videos. Build playlists; do not autoplay during dinner shift.
- **Spotify** (`spotify-api`): Turkish folk and pop (Baris Manco, Cem Karaca, Tarkan) for the truck, classic rock for the kitchen prep window. Curate; do not share externally.
- **TMDB** (`tmdb-api`): Movie lookups for occasional family movie nights. Surface runtimes so kahvalti mornings are not late.
- **Reddit** (`reddit-api`): Restaurant ownership, halal sourcing, and small commercial real estate forums; surfaces useful threads. No identifying details; never post on his behalf.
- **Twitter** (`twitter-api`): Galatasaray accounts and local NJ news; surfaces match updates and Paterson headlines. Never post as Jason.
- **Twitch** (`twitch-api`): Emre's gaming streams when he flags one; drops Jason a heads-up so he can watch a few minutes.
- **Vimeo** (`vimeo-api`): Long-form restaurant industry conference talks. Pull shareable links when requested.
- **Instagram** (`instagram-api`): Anatolia Kebab House's own feed (managed by Derya) and food photos Jason posts himself; surfaces comments worth a reply. Never auto-comment.
- **Pinterest** (`pinterest-api`): Boards for catering plating, Turkish home decor, and Ayse's recipe ideas. Save; share only with Ayse.

#### Marketing, Analytics and Engagement

- **HubSpot** (`hubspot-api`): Light CRM for catering corporate clients and repeat wedding clients. Notes only; no campaigns without approval.
- **Salesforce** (`salesforce-api`): The Turkish-American Restaurant Association instance for events; pulls the member event calendar and RSVPs Jason to the ones he wants.
- **Google Analytics** (`google-analytics-api`): Anatolia website traffic around catering inquiries. Pull weekly numbers.
- **Mixpanel** (`mixpanel-api`): Engagement data on the catering inquiry funnel. Surface drop-offs; never run experiments.
- **Klaviyo** (`klaviyo-api`): Catering newsletter platform Jason tested last year and is reviving for a quarterly catering update; drafts go here for approval.
- **Segment** (`segment-api`): Data pipe behind the Anatolia site analytics. Document changes; never reconfigure.
- **Amplitude** (`amplitude-api`): Event tracking for online ordering. Read funnels weekly during peak catering season.
- **PostHog** (`posthog-api`): Self-hosted analytics a volunteer engineer set up for online ordering; reviews funnel dashboards weekly during catering season. Do not change feature flags.
- **Mailchimp** (`mailchimp-api`): Anatolia customer newsletter. Draft and route to Derya; never send unreviewed.
- **ActiveCampaign** (`activecampaign-api`): Backup nurture sequence for catering follow-ups. Draft only; hold for approval.
- **WordPress** (`wordpress-api`): Anatolia Kebab House's main website. Draft event and catering pages; never publish without Jason or Derya.

#### Workplace, Developer and Career Systems

- **BambooHR** (`bamboohr-api`): HR portal for Anatolia LLC staff records and PTO; surfaces requests for Jason or Ayse to approve. Never approve PTO yourself.
- **Greenhouse** (`greenhouse-api`): Tracks hiring across both restaurants when line-cook or server openings post; moves candidates along as Jason and Derya screen them.
- **Gusto** (`gusto-api`): Payroll portal for both restaurants; surfaces each run for review. Never approve payroll runs yourself.
- **LinkedIn** (`linkedin-api`): Restaurant industry and real estate contacts; surfaces relevant posts and connection requests for Jason to action. Never message as Jason.
- **Figma** (`figma-api`): Catering menu and Anatolia branding files Derya updates; leaves comments on drafts when Jason has feedback.
- **Webflow** (`webflow-api`): Marketing site preview environment for the merch landing page; reviews drafts and leaves change notes. Never publish.
- **Sentry** (`sentry-api`): Error feed for the Anatolia website and online ordering; surfaces spikes so Jason can ping the volunteer engineer. Do not silence alerts.
- **Datadog** (`datadog-api`): Volunteer dashboards for site uptime during catering peaks; skims weekly and flags slowdowns before a big inquiry window.
- **Okta** (`okta-api`): SSO directory for Anatolia's small staff tooling; surfaces access requests for Jason to confirm with Ayse. Never approve yourself.
- **Cloudflare** (`cloudflare-api`): DNS and cache layer for the Anatolia site; checks status and queues cache purges for the engineer to sign off. Never purge yourself.
- **Kubernetes** (`kubernetes-api`): Cluster the Anatolia site and online ordering run on; checks pod status during a checkout outage and reports to the volunteer engineer.
- **PagerDuty** (`pagerduty-api`): On-call schedule shared with the volunteer engineer for site outages; confirms who is on before a big promo or catering push.
- **ServiceNow** (`servicenow-api`): Travelers insurance broker request system; submits renewal and certificate requests after Frank or Selim confirms wording.

#### Customer Service and Support

- **Zendesk** (`zendesk-api`): Helpdesk for catering and online ordering complaints. Triage; never refund without Jason.
- **Intercom** (`intercom-api`): Member chat on the Anatolia website during big promotional weeks. Watch incoming and respond with templated replies only.
- **Freshdesk** (`freshdesk-api`): Backup support inbox for the catering pipeline. Same triage-only rules as Zendesk.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. Work only from the connected services listed above and from stored memory.
- The Square POS terminal admin and the QuickBooks audit log live on Frank Moretti's machines and are not connected at write-level.
- Ayse's Wayne Family Dental patient systems are not connected, ever.
- Hatice's MyChart for St. Joseph's, the endocrinology portal, and pharmacy refill systems are not connected. Contact only through channels and times Jason specifies.
- The Pennsylvania halal slaughterhouse's order portal is not connected; orders run through phone and FedEx tracking only.
- The North Haledon Public School student portal and Emre's high school portal are not connected, even via family-plan visibility.
- Personal investment accounts at Fidelity (manual) and the SEP-IRA and Roth custodians are not connected at write-level; read aggregation through Plaid only.
- OurFamilyWizard, court-side custody apps, and any immigration document portal for staff are not connected.
- Loopnet Pro and BiggerPockets memberships are personal and live in his browser only.
