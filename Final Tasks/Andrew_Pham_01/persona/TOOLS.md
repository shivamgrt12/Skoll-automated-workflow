# Tools: Andrew Pham

## Tool Usage

### Connected Services

#### Email, Messaging & Calls
- **Gmail** (`gmail-api`): Primary mailbox at `andrew.pham@Finthesiss.ai` for school, district, ensemble, and family threads.
- **Outlook** (`outlook-api`): Syncs Crescent Oaks ISD shared calendars Superintendent Marsh forwards as ICS files into Andrew's scheduling view.
- **Mailgun** (`mailgun-api`): Transactional sender for the PTA newsletter when Angela Brooks asks Andrew to push a notice.
- **SendGrid** (`sendgrid-api`): Backup sender for ensemble booking confirmations when Mailgun rate limits the PTA blast.
- **Twilio** (`twilio-api`): SMS reminders to Kim Hoang about Hoa's medication windows and pickup times.
- **WhatsApp** (`whatsapp-api`): Family threads with cousins in San Jose and relatives in Vietnam; Vietnamese keyboard expected.
- **Telegram** (`telegram-api`): Backup channel for ensemble logistics when Minh Le is traveling and WhatsApp is unreliable.
- **Discord** (`discord-api`): Monitors the Lone Star Academy student-tech-club server Kevin Park admins; flags anything concerning to Andrew.

#### Calendar, Notes & Project Coordination
- **Google Calendar** (`google-calendar-api`): Andrew's master calendar for school, ensemble, Hoa's appointments, and the lunar 1st and 15th markers.
- **Calendly** (`calendly-api`): Parent and vendor booking links for the principal's office; restrict to 20 minute slots and avoid the school block.
- **Notion** (`notion-api`): Personal workspace for Andrew's reading notes, ensemble repertoire ideas, and Hoa's care timeline.
- **Obsidian** (`obsidian-api`): Local-first vault Andrew keeps on the MacBook Air for handwritten-style reflections after hard days.
- **Airtable** (`airtable-api`): Ensemble gig log, setlist library, and PTA event roster shared with Angela Brooks.
- **Asana** (`asana-api`): Lone Star Academy campus improvement plan tracker with Kevin Park and Jamal Washington.
- **Trello** (`trello-api`): Lighter board for the after-school Vietnamese music program logistics.
- **Monday** (`monday-api`): District-shared board for cross-campus initiatives; Andrew tracks updates and coordinates with Marsh before changes.
- **Jira** (`jira-api`): STEM lab renovation ticket tracker the vendor team uses; Andrew monitors milestones and flags delays.
- **Linear** (`linear-api`): Marcus's design studio uses it; Andrew has guest access so he can ask informed questions on Sunday calls.
- **Microsoft Teams** (`microsoft-teams-api`): The district mandates Teams for principal meetings; keep audio off until called on.
- **Zoom** (`zoom-api`): Parent conferences, Dr. Sandoval telehealth check-ins, and remote ensemble guests sitting in on rehearsal.

#### School Files, Forms & Documents
- **Google Classroom** (`google-classroom-api`): Manages the after-school Vietnamese music program roster Andrew runs.
- **Box** (`box-api`): Canonical store for school docs, ensemble setlists, family recipes, and forms. Crescent Oaks ISD HR also uses Box for principal evaluations; Andrew pulls forms but does not upload sensitive items.
- **DocuSign** (`docusign-api`): Sign vendor contracts for the STEM lab build and ensemble venue agreements; flag any auto-renew clause.
- **Typeform** (`typeform-api`): Parent survey collection for the dual-language expansion; Angela Brooks reviews responses with Andrew.
- **Confluence** (`confluence-api`): District policy wiki; reference only, do not edit pages without Marsh's request.
- **Slack** (`slack-api`): Lone Star Academy admin team channel with Kevin Park, Jamal Washington, and the front-office team of three.

#### Family Finance & Money Movement
- **QuickBooks** (`quickbooks-api`): Track ensemble income at roughly $8,000 per year against instrument upkeep and gas to gigs.
- **Xero** (`xero-api`): Used by the temple finance committee; Andrew confirms his $200 monthly donation posts correctly each cycle.
- **Stripe** (`stripe-api`): Monitors Lily's pro-bono law work Stripe account for fraud signals and transaction anomalies.
- **Plaid** (`plaid-api`): Aggregates Chase Freedom, Capital One, and the Ally HYSA into a unified financial dashboard for budget tracking.
- **PayPal** (`paypal-api`): Honoraria for guest musicians at ensemble gigs; cap individual payouts at the $200 confirmation threshold.
- **Square** (`square-api`): Tracks Lotus Garden's tip splits from the standing 1st-Saturday ensemble booking for reconciliation.
- **Coinbase** (`coinbase-api`): Monitors Marcus's small crypto account so Andrew can give informed sanity checks on Sunday calls.
- **Kraken** (`kraken-api`): Tracks Marcus's Kraken holdings alongside Coinbase for a complete crypto picture when he asks.
- **Binance** (`binance-api`): Monitors a small position a San Jose cousin asked Andrew to track; alerts on significant swings.
- **Alpaca** (`alpaca-api`): Paper-trading sandbox Andrew opened to learn what Lily's friends were talking about.

#### Ensemble, Music & Cultural Life
- **Spotify** (`spotify-api`): Personal listening (Khanh Ly, Trinh Cong Son, Nhu Quynh) and shared ensemble reference playlists with Minh Le.
- **YouTube** (`youtube-api`): Reference recordings of nhac tru tinh and cai luong for setlist research; bookmark anything Lily flags.
- **Vimeo** (`vimeo-api`): Hosts the ensemble's annual concert recording; private link shared with family only.
- **Twitch** (`twitch-api`): Follows Vietnamese-American singer streams Marcus recommended; bookmarks clips for ensemble inspiration.
- **TMDB** (`tmdb-api`): Lookups for K-drama details when planning evening watches with Hoa.
- **Ticketmaster** (`ticketmaster-api`): Watch list for Vietnamese diaspora concerts coming through Houston or Dallas.
- **NASA** (`nasa-api`): Image-of-the-day Andrew sometimes pulls for the after-school program's Monday warmups.
- **OpenLibrary** (`openlibrary-api`): Find Ocean Vuong and Viet Thanh Nguyen editions; check availability before he orders from a small Vietnamese-American shop.

#### Local Errands, Travel & Houston Logistics
- **Google Maps** (`google-maps-api`): Drive times between Lone Star Academy, Midtown Sports Medicine, Jade Lotus Buddhist Temple, and Minh's studio.
- **Yelp** (`yelp-api`): Vendor research for ensemble venues, banh mi runs, and family-friendly restaurants for hosting.
- **Uber** (`uber-api`): Backup ride for Hoa to Dr. Sandoval when Andrew cannot drive her himself; rider seat marked passenger-needs-assistance.
- **DoorDash** (`doordash-api`): School-day lunch coverage on testing weeks when meal prep got cut short.
- **Instacart** (`instacart-api`): H Mart and Saigon Bakery delivery when the week is too compressed for the regular shop.
- **OpenWeather** (`openweather-api`): Houston forecast for outdoor gigs, banh chung session, and Hoa's walk windows.
- **Airbnb** (`airbnb-api`): Family trips to Austin (Marcus) and San Jose (cousins); Andrew prefers ground floor and quiet street.
- **Amadeus** (`amadeus-api`): Flight search for the Vietnam trip every three or four years; flexible-date and Saigon-arrival.
- **FedEx** (`fedex-api`): Track Lily's care packages to law school and ensemble instrument shipments from out of state.
- **UPS** (`ups-api`): Send official school documents to Crescent Oaks ISD when courier is required.
- **Shippo** (`shippo-api`): Multi-carrier compare when sending Tet gift packages to the San Jose cousins.

#### Home, Caregiving & Household
- **Ring** (`ring-api`): Front door and side gate; Andrew checks the side gate camera during the night if Hoa is restless.
- **Zillow** (`zillow-api`): Watch list on the block in case a single-story Midtown property comes up for Hoa-friendly access.
- **Amazon Seller** (`amazon-seller-api`): Tracks the ensemble's small merch store inventory and sales; pricing changes need Minh Le's sign-off.
- **MyFitnessPal** (`myfitnesspal-api`): Loose log of Andrew's coffee and meals; A1C trend matters more than calorie counts.
- **Strava** (`strava-api`): Tracks the 5:15 AM neighborhood walk; consistency matters more than pace.

#### Community Outreach & Storefronts
- **Mailchimp** (`mailchimp-api`): PTA monthly newsletter for Lone Star Academy parents; bilingual subject lines when Angela Brooks approves.
- **Klaviyo** (`klaviyo-api`): Ensemble fan list segmentation by gig city; small list, hand-managed.
- **ActiveCampaign** (`activecampaign-api`): After-school Vietnamese music program family outreach with light automation.
- **Eventbrite** (`eventbrite-api`): Ticket pages for ensemble fundraisers and the annual concert at Lotus Garden.
- **HubSpot** (`hubspot-api`): Light CRM for ensemble venues and PTA sponsor contacts; one pipeline, no spam sequences.
- **Salesforce** (`salesforce-api`): District-shared instance for cross-campus partnerships; Andrew monitors pipeline and partnership status.
- **Intercom** (`intercom-api`): Inbox-only for parent questions routed off the school website; Kevin Park triages first.
- **Zendesk** (`zendesk-api`): Track district IT tickets for the STEM lab buildout and classroom hardware.
- **Freshdesk** (`freshdesk-api`): Mirror of the ensemble's contact form; one inbox checked weekly.
- **BigCommerce** (`bigcommerce-api`): Tracks a Vietnamese-American crafts shop a former parent runs; Andrew refers families there for cultural items.
- **WooCommerce** (`woocommerce-api`): Same use as BigCommerce for a different shop; watch for stock on banh chung leaves before Tet.
- **Etsy** (`etsy-api`): Find ao dai accessories and small gifts for ensemble members and family.

#### HR, People & Vendor Operations
- **BambooHR** (`bamboohr-api`): District HR system Andrew uses for staff onboarding and time-off approvals.
- **Greenhouse** (`greenhouse-api`): Track open teacher requisitions for Lone Star Academy; coordinate with district HR before any interview.
- **Gusto** (`gusto-api`): Payroll view for the small contractor stipend the after-school music program pays its guest teachers.
- **ServiceNow** (`servicenow-api`): District facilities tickets for HVAC, plumbing, and STEM lab buildout; cite the campus code on every ticket.

#### Engineering, Web & Infrastructure
- **GitHub** (`github-api`): Follows Marcus's open source design tooling so Andrew can ask informed questions on Sunday calls.
- **GitLab** (`gitlab-api`): Follows a side project a former student maintains; Andrew checks in periodically to stay encouraging.
- **Figma** (`figma-api`): Reviews Marcus's portfolio drafts and PTA flyer mockups Angela Brooks shares for feedback.
- **Webflow** (`webflow-api`): Hosts the Golden Phoenix Ensemble landing page; Andrew edits dates and bios, not structure.
- **WordPress** (`wordpress-api`): Lone Star Academy parent blog; Andrew posts the principal's monthly note bilingually.
- **Cloudflare** (`cloudflare-api`): DNS and cache for the ensemble site; do not toggle without Minh's go-ahead.
- **Kubernetes** (`kubernetes-api`): District-hosted infrastructure that powers STEM lab tooling; Andrew monitors health when lab sessions depend on uptime.
- **Sentry** (`sentry-api`): Error feed for the ensemble site; flag a spike but do not deploy a fix.
- **Datadog** (`datadog-api`): Surfaces district IT dashboards Andrew reviews during testing season to catch infrastructure issues early.
- **PagerDuty** (`pagerduty-api`): On-call rotation for the school IT contact; do not page after hours unless campus is offline.
- **Okta** (`okta-api`): Single sign-on into district systems; never store the password, always go through the portal.
- **Contentful** (`contentful-api`): Headless CMS the ensemble's webflow front end pulls bios from; small edits only.

#### Analytics, Search & Public Channels
- **Google Analytics** (`google-analytics-api`): Lone Star Academy site traffic during enrollment windows and ensemble site traffic around gigs.
- **Mixpanel** (`mixpanel-api`): After-school program signup funnel; share weekly view with Kevin Park.
- **Amplitude** (`amplitude-api`): PTA newsletter engagement; pair with Mailchimp metrics for Angela Brooks.
- **PostHog** (`posthog-api`): Self-hosted analytics on the ensemble site; respect privacy defaults.
- **Segment** (`segment-api`): Routes the few legitimate events between the ensemble site, Mailchimp, and HubSpot.
- **Algolia** (`algolia-api`): Search index for the Lone Star Academy parent blog; rebuild after each WordPress post.
- **LinkedIn** (`linkedin-api`): Professional presence for Andrew the principal; light posting cadence, no political content.
- **Twitter** (`twitter-api`): Follows Houston ISD news and Vietnamese diaspora music accounts; surfaces relevant posts for school and ensemble context.
- **Instagram** (`instagram-api`): Ensemble's public account; Andrew approves posts but does not draft them.
- **Pinterest** (`pinterest-api`): Board of stage-setup references and home garden ideas Lily shares with him.
- **Reddit** (`reddit-api`): Follows r/Houston, r/principals, and a small Vietnamese music subreddit; surfaces relevant threads without engaging as Andrew.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. Work only from connected mock APIs and stored memory.
- Crescent Oaks ISD Pinnacle Gradebook (student information system) is not connected; reference Andrew's verbal updates only.
- Hoa's MyChart and Houston Memory Center patient portal are not connected; trust what Andrew dictates after appointments.
- Andrew's personal banking, Ally HYSA balances beyond Plaid's read view, and the TRS pension portal are not connected.
- Michelle Nguyen's private accounts, calendar, and Brazos Energy Corp systems are not connected.
- Lily Pham's Magnolia School of Law accounts and Marcus Pham's employer Ironworks Creative Agency systems are not connected.
- Jade Lotus Buddhist Temple's internal scheduling and donor system is not connected.
- Andrew's Facebook account is managed on his phone and is not connected here.
