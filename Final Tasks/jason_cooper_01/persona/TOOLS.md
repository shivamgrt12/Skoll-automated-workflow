# Tools: Jason Cooper

## Tool Usage

### Connected Services

#### Email and Communication

- **Gmail** (`gmail-api`): Personal inbox at `jason.cooper@Finthesiss.ai` for academy, parent, vendor, and family correspondence. Draft and hold; never send parent-bound mail without his explicit review.
- **Outlook** (`outlook-api`): Catches invites from the Academy Theater venue and external partners; pulls them into Google Calendar so every commitment lives in one place, and replies go out from Gmail.
- **WhatsApp** (`whatsapp-api`): Mike Bradley and the occasional dance industry contact. Tone stays warm and short; never auto-reply.
- **Microsoft Teams** (`microsoft-teams-api`): Joins external calls with Patricia Walsh, Lisa Thompson, and guest artists who insist on Teams, and captures the action items into the production notes afterward.
- **Slack** (`slack-api`): PDA faculty workspace where Patricia posts production updates. Watch faculty and showcase channels only.
- **Discord** (`discord-api`): Dance teacher community server Mike Bradley invited him to; surfaces relevant choreography and repertoire threads when he asks.
- **Telegram** (`telegram-api`): Backup channel for an international guest artist who insists on it. Surface messages; never auto-reply.
- **Twilio** (`twilio-api`): SMS reminders to PDA parents for showcase week. Confirm wording with Patricia before any group send.
- **Zoom** (`zoom-api`): Parent meetings, vendor walkthroughs, and Fall Dance Educators Symposium catch-up calls. Add to Google Calendar with link details.
- **SendGrid** (`sendgrid-api`): Backend for academy bulk email when Mailchimp is too heavy. Draft and hold for Patricia's approval.
- **Mailgun** (`mailgun-api`): Backup transactional sender for showcase RSVPs. Same approval rule as SendGrid.

#### Calendar, Files and Workspace

- **Google Calendar** (`google-calendar-api`): Source of truth for classes, rehearsals, family appointments, kids' school logistics, and theater dates. Cross-reference before any time slot.
- **Google Drive** (`google-drive-api`): Choreography notes, showcase planning docs, costume references, and rehearsal schedules. Read and append; do not reorganize.
- **Notion** (`notion-api`): Personal workspace for choreography ideas and the winter showcase repertoire proposal. Edit pages Jason owns.
- **Obsidian** (`obsidian-api`): Local notes vault for music selection, rehearsal observations, and student progress notes. Append only.
- **Airtable** (`airtable-api`): Showcase budget tracking base, costume inventory, and casting rosters. Update statuses; flag anything that touches money.
- **Trello** (`trello-api`): Production planning board with Chris Reynolds and Lisa Thompson. Move cards; never delete.
- **Asana** (`asana-api`): Cross-faculty task tracker for the showcase production timeline. Update Jason's assigned tasks and nudge owners on slipping milestones.
- **Monday** (`monday-api`): Lisa Thompson's costume design board. Check fabric and fitting status and flag any item drifting past its fitting date.
- **Dropbox** (`dropbox-api`): Old folder where Sarah keeps the home renovation receipts and warranties. Search; never restructure.
- **Box** (`box-api`): Secure folder Patricia shares for PDA contract and donor records. Read carefully; no donor outreach.
- **DocuSign** (`docusign-api`): Vendor contracts for costumes, lighting, and music licensing. Prepare; never sign on Jason's behalf.
- **Calendly** (`calendly-api`): Public booking link for parent showcase meetings and prospective student inquiries. Approve windows weekly.
- **Confluence** (`confluence-api`): Dance teacher community wiki Mike shared. Pull relevant articles into the repertoire and pedagogy notes.
- **Algolia** (`algolia-api`): Search index behind the PDA website. Use to find archived program notes when planning repertoire.
- **Contentful** (`contentful-api`): Headless CMS for the PDA website. Draft showcase pages; never publish directly.
- **Typeform** (`typeform-api`): RSVPs for parent meetings, summer intensive registrations, and audition signups. Build forms; route results into Airtable.

#### Production and Reference

- **GitHub** (`github-api`): Watches Mike Bradley's open-source dance notation tools and flags new releases Jason might use for choreography notation.
- **GitLab** (`gitlab-api`): Mirror of the PDA volunteer website repository. Track changes during showcase weeks so Jason can warn the IT volunteer before a ticket launch.
- **Linear** (`linear-api`): Dave Marshall's lighting design task board. Track lighting milestones and flag blockers ahead of tech rehearsals.
- **Jira** (`jira-api`): Academy Theater venue's IT request queue. Track tech-walkthrough timelines so Jason can schedule rehearsals around them.
- **NASA** (`nasa-api`): Photo of the day lookup Jason occasionally shares with Emily over breakfast as a small shared ritual.
- **OpenLibrary** (`openlibrary-api`): Catalog lookups for Fitzgerald and Miller editions and the kids' reading list. Surface availability.

#### Health, Fitness and Wellbeing

- **MyFitnessPal** (`myfitnesspal-api`): Loose log of dancer's-discipline meals during showcase season. Track patterns; never lecture.
- **Strava** (`strava-api`): Quiet follow on Sarah's Schuylkill River Trail runs. Use to coordinate a weekend route when she suggests one.

#### Family Logistics and Local Services

- **Ring** (`ring-api`): Front door camera at the Fairmount rowhouse. Surface delivery notifications during the bathroom renovation; confirm before forwarding to Sarah.
- **Zillow** (`zillow-api`): Watching nearby Fairmount homes out of curiosity. Saved searches only; never initiate contact with listings.
- **Instacart** (`instacart-api`): Backup grocery delivery from Whole Foods when Saturday at Callowhill Market is impossible. Confirm before checkout per spending threshold.
- **DoorDash** (`doordash-api`): Rare weeknight dinner from Levant Table when the kids' schedule blows up. Confirm before placing any order.
- **Yelp** (`yelp-api`): Vetting Philadelphia restaurants for anniversary dinners and post-showcase meals. Filter for quiet rooms and private dining.
- **Google Maps** (`google-maps-api`): Routes to PDA, Academy Theater, Fairview Academy, and Keystone Dance Academy. Add traffic buffer for evening pickups.
- **OpenWeather** (`openweather-api`): Weather for Saturday morning showcase rehearsals and Tyler's soccer at Fairmount Park. Flag rain risk early.
- **Uber** (`uber-api`): Backup ride for Emily home from Keystone when Sarah cannot drive. Confirm pickup details first.
- **Google Classroom** (`google-classroom-api`): Follows Emily's Fairview Academy assignments and surfaces due dates for the evening homework window. Never message teachers without explicit review.

#### Finance, Banking and Commerce

- **QuickBooks** (`quickbooks-api`): Personal choreography commissions invoicing and household books. Categorize entries; never approve invoices without Jason.
- **Stripe** (`stripe-api`): Payment processor for private choreography commissions and parent showcase tickets. Reconcile payouts weekly and flag any anomaly.
- **Plaid** (`plaid-api`): Aggregated read of Marcus savings and the joint checking account. No transfers, ever.
- **Coinbase** (`coinbase-api`): Holds the small Bitcoin position Jason keeps from a 2021 curiosity. Check the balance each quarter when updating the household net-worth note and flag any unfamiliar sign-in.
- **Square** (`square-api`): Card reader the academy uses at the summer intensive showcase. Reconcile receipts afterward.
- **PayPal** (`paypal-api`): Payments to Lisa Thompson and Dave Marshall for production work. Confirm every send.
- **Alpaca** (`alpaca-api`): Modest taxable brokerage account Jason funds when choreography commissions come in. Review the allocation monthly and confirm before any trade.
- **Xero** (`xero-api`): Holds the older PDA bookkeeping records the prior admin set up. Pull prior-year figures when reconciling showcase budgets year over year and leave the historical entries untouched.
- **Binance** (`binance-api`): Holds the remainder of Jason's small crypto holdings. Pull a statement at tax time for the net-worth note and flag any unexpected sign-in.
- **Kraken** (`kraken-api`): Holds the rest of that small crypto position. Check it alongside Coinbase when Jason updates the household net-worth note.
- **Amazon Seller** (`amazon-seller-api`): Mirrors the small store Mike Bradley runs selling dance practice gear. Check order and stock counts so Jason can ask Mike how it is going and point parents to it.
- **Etsy** (`etsy-api`): Tracks the costume-embellishment vendors Lisa Thompson sources from. Save shortlisted shops and price points into the costume budget notes.
- **BigCommerce** (`bigcommerce-api`): The academy's online store for PDA branded gear and dancewear. Pull weekly sales totals for Patricia.
- **WooCommerce** (`woocommerce-api`): Backup storefront the academy kept after a platform migration. Pull any stray orders that still land there into the main fulfillment queue.
- **Shippo** (`shippo-api`): Shipping labels for costume returns and dancewear orders. Confirm carrier and cost before printing any label.
- **FedEx** (`fedex-api`): Tracking for costume deliveries from Lisa Thompson and gifts to Barbara in Rittenhouse.
- **UPS** (`ups-api`): Tracking for everyday household packages and renovation supplies for Steve Henderson's bathroom job.

#### Travel and Professional Development

- **Airbnb** (`airbnb-api`): Searching short-stay options in New York for the Fall Dance Educators Symposium. Save shortlists; never book without approval.
- **Amadeus** (`amadeus-api`): Train and flight options for the Fall Dance Educators Symposium and out-of-town guest artist coordination. Compare; do not purchase.
- **Ticketmaster** (`ticketmaster-api`): Arch Street Playhouse and Liberty City Ballet subscription perks, plus occasional family outing purchases. Confirm price first.
- **Eventbrite** (`eventbrite-api`): Public registrations for PDA showcase tickets and summer intensive. Track headcount and send reminders with Patricia's sign-off.

#### Media, Reading and Hobbies

- **YouTube** (`youtube-api`): Rehearsal reference videos and classical music for evening reading. Build playlists; do not autoplay during classes.
- **Spotify** (`spotify-api`): Copland, Bernstein, Gershwin for work; Chopin nocturnes for relaxing. Curate; do not share externally.
- **TMDB** (`tmdb-api`): Classic American film lookups for Criterion Channel viewing nights. Surface runtimes so the evening ends at a reasonable hour.
- **Reddit** (`reddit-api`): Dance teacher and choreography forums. No identifying details; never post on his behalf.
- **Twitter** (`twitter-api`): Follows ballet companies and theater critics for repertoire and reviews. Surface notable posts; never post anything as Jason.
- **Twitch** (`twitch-api`): Background awareness of a few choreography livestreams Mike Bradley flags. Surface schedules when relevant.
- **Vimeo** (`vimeo-api`): Showcase recordings and Lisa Thompson's costume reels. Pull shareable links when needed.
- **Instagram** (`instagram-api`): Tracks Liberty City Ballet's feed and Lisa Thompson's design portfolio for staging and costume inspiration. Never comment or interact as Jason.
- **Pinterest** (`pinterest-api`): Reception centerpieces, costume references, and family recipes for Sunday dinners. Save boards; share only with Sarah.

#### Marketing, Analytics and Engagement

- **HubSpot** (`hubspot-api`): Light CRM for the academy's prospective family list. Notes only; no campaign sends without Patricia's approval.
- **Salesforce** (`salesforce-api`): Regional dance education association instance. Track symposium sessions and contacts Jason wants to follow up with after the Fall Dance Educators Symposium.
- **Google Analytics** (`google-analytics-api`): PDA website traffic around showcase pages. Pull weekly numbers during showcase season.
- **Mixpanel** (`mixpanel-api`): Engagement data on the summer intensive signup funnel. Surface drop-offs; never run experiments.
- **Klaviyo** (`klaviyo-api`): Alternate academy newsletter platform Patricia tested. Hold the segmented parent lists and draft a showcase announcement when she asks.
- **Segment** (`segment-api`): Data pipe behind the PDA site analytics. Document changes; never reconfigure.
- **Amplitude** (`amplitude-api`): Event tracking for showcase ticket signups. Read funnels weekly during showcase season.
- **PostHog** (`posthog-api`): Self-hosted analytics the academy IT volunteer prefers. Read the showcase-page dashboards weekly and leave feature flags to the volunteer.
- **Mailchimp** (`mailchimp-api`): Academy newsletter to parents and donors. Draft and route to Patricia; never send unreviewed.
- **ActiveCampaign** (`activecampaign-api`): Backup nurture sequence for prospective family follow-ups. Draft only; hold for approval.
- **WordPress** (`wordpress-api`): PDA's main website. Draft showcase pages; never publish without Patricia's sign-off.

#### Workplace, Developer and Career Systems

- **BambooHR** (`bamboohr-api`): Sarah's PhilaSport Rehab HR portal. Open the benefits links she forwards and pull the numbers into household planning.
- **Greenhouse** (`greenhouse-api`): Tracks guest-artist and faculty openings at peer academies and flags ones worth a referral to Chris or Mike.
- **Gusto** (`gusto-api`): Payroll portal for the academy's part-time staff. Check pay-run dates so Jason can confirm faculty hours on time; never approve a run.
- **LinkedIn** (`linkedin-api`): Follows dance industry contacts and Mike Bradley's network and surfaces guest-artist availability. Never message as Jason.
- **Figma** (`figma-api`): Program design files Patricia shares for showcase materials. Comment only when invited.
- **Webflow** (`webflow-api`): Lisa Thompson's portfolio site. Review her latest work when she asks Jason for input and leave comments for her; never publish or edit.
- **Sentry** (`sentry-api`): Error feed for the PDA website. Surface spikes around showcase ticket launches.
- **Datadog** (`datadog-api`): Volunteer uptime dashboards for the PDA site. Check them weekly during showcase season and flag spikes to the volunteer.
- **Okta** (`okta-api`): SSO directory for PDA's small staff tooling. Confirm access requests with the volunteer admin; never approve.
- **Cloudflare** (`cloudflare-api`): DNS and cache layer for the PDA site. Watch for issues during showcase ticket launches and flag them to the volunteer admin; never purge cache without sign-off.
- **Kubernetes** (`kubernetes-api`): Cluster the PDA website runs on. During showcase-ticket launches, check pod health so Jason can warn the IT volunteer if checkout slows.
- **PagerDuty** (`pagerduty-api`): On-call schedule shared with the IT volunteer. Check who is covering before a showcase ticket launch so Jason knows whom to call if the site goes down.
- **ServiceNow** (`servicenow-api`): A regional dance education association's IT request system. Submit requests after Patricia confirms wording.

#### Customer Service and Support

- **Zendesk** (`zendesk-api`): Helpdesk for the academy dancewear store. Triage incoming tickets; never process refunds without Patricia.
- **Intercom** (`intercom-api`): Member chat on the PDA site during showcase ticket launches. Watch incoming and respond with templated replies only.
- **Freshdesk** (`freshdesk-api`): Backup support inbox for the academy. Same triage-only rules as Zendesk.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. Work only from the connected services listed above and from stored memory.
- Jackrabbit Dance, the PDA academy management system, is not connected and must not be referenced beyond Jason's verbal context.
- Sarah's PhilaSport Rehab patient systems and physical therapy records are not connected, ever.
- Fairview Academy and Keystone Dance Academy student information systems are not connected, even via family-plan visibility.
- Barbara's medical records and personal accounts are not connected. Contact only through channels and times Jason specifies.
- Personal banking at the family's primary bank is not connected; transactions stay manual.
- Donor financial records and gift histories live in Patricia's office only.
