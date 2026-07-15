# Tools: Karen Bell

## Tool Usage

### Connected Services

#### Crestline Consulting Workspace & Documents
- **Gmail** (`gmail-api`): Karen's primary inbox at karen.bell@voissync.ai. Practice administration, Nova course mail, insurance panels, and speaking inquiries.
- **Google Calendar** (`google-calendar-api`): The master calendar. Practice block Monday to Thursday, Friday Nova, Rosemary's appointments, and Aimovig on the 1st of each month.
- **Google Drive** (`google-drive-api`): Nova course materials, lecture slides, manuscript drafts, Rosemary care notes, and practice operational documents.
- **Outlook** (`outlook-api`): Read-only mirror used to receive Nova Southeastern administrative threads that arrive from faculty Outlook accounts.
- **Dropbox** (`dropbox-api`): Backup for speaking decks and conference handouts shared with co-panelists who do not use Drive.
- **Box** (`box-api`): Used by Anthony Beaumont (CPA) to exchange S-corp tax documents. Karen receives only; she never uploads anything patient-adjacent.
- **Notion** (`notion-api`): Karen's personal teaching workspace. Lecture outlines, reading lists, and case-formulation templates for Nova students.
- **Obsidian** (`obsidian-api`): Local vault for research notes on cultural formulation and intergenerational trauma. Never synced to cloud.
- **Airtable** (`airtable-api`): Speaking engagement tracker (date, venue, honorarium, rider, status) and the practice CE-credit log.
- **Confluence** (`confluence-api`): Read-only access to the Nova PMHNP program's faculty wiki for syllabus standards and program policies.
- **DocuSign** (`docusign-api`): Speaker agreements, practice vendor contracts, and lease addenda. Confirm with Karen before sending anything for her signature.
- **Typeform** (`typeform-api`): The speaking inquiry form on her professional site. New submissions land in Gmail; route triage entries to Airtable.

#### Communication Channels
- **Slack** (`slack-api`): Practice team channel with Rachel, Marcus, and Danielle. Quick operational coordination; never patient identifiers.
- **WhatsApp** (`whatsapp-api`): Cousin group chat across North Carolina and Pennsylvania, and Margaret (Rosemary's aide) for quick coordination.
- **Microsoft Teams** (`microsoft-teams-api`): Nova Southeastern faculty meetings and program committee calls.
- **Telegram** (`telegram-api`): One channel for a national PMHNP study group Karen contributes to occasionally.
- **Discord** (`discord-api`): Read-only on Oliver's FAU study servers so Karen can tell when he is buried in finals.
- **Zoom** (`zoom-api`): Nova lectures, panels, and speaking rehearsals. Telehealth visits run through SimplePractice, not here.
- **Twilio** (`twilio-api`): Practice appointment SMS reminders. Confirm message templates with Karen before any change.
- **SendGrid** (`sendgrid-api`): Transactional email for the speaking site, including booking confirmations and inquiry receipts.
- **Mailgun** (`mailgun-api`): Backup transactional sender used by her website host. Keep credentials in `$MAILGUN_API_KEY`.
- **Calendly** (`calendly-api`): Speaking inquiry consult calls and Nova office hours. Practice scheduling stays inside SimplePractice.

#### Practice Finance, Billing & Investing
- **Stripe** (`stripe-api`): Self-pay patient payments and speaking honorarium deposits. Reconciles into QuickBooks weekly.
- **Plaid** (`plaid-api`): Read-only ledger sync for household budgeting, family savings, and Rosemary's supplemental expenses.
- **QuickBooks** (`quickbooks-api`): Practice books (S-corp). Anthony Beaumont pulls quarterly. Karen reviews on the 1st of each month with Danielle.
- **Xero** (`xero-api`): Used only to read invoices from one vendor (the EHR-adjacent billing service) that exports in Xero format.
- **Square** (`square-api`): Card reader at the front desk for the rare in-office payment that does not route through Stripe.
- **PayPal** (`paypal-api`): Personal account for church fundraising, conference travel reimbursements, and small family transactions.
- **Coinbase** (`coinbase-api`): Karen pulls the small wallet balance and price moves here before her Monday, Wednesday, and Friday evening calls with Oliver so she can ask informed questions about what he is tracking.
- **Alpaca** (`alpaca-api`): Karen checks the paper-trading results from a Nova student's research project here so she can review the data with him during clinical supervision and fold it into her advising notes.
- **Binance** (`binance-api`): Karen reads the market data here to keep up with the coins Oliver mentions, so their Sunday-call conversations about his computer-science side projects stay grounded in real numbers.
- **Kraken** (`kraken-api`): Karen cross-checks prices here against the other exchanges when Oliver flags a discrepancy, giving her something concrete to talk through with him on their evening calls.

#### Patient-Adjacent Operations & Outreach
- **Salesforce** (`salesforce-api`): Speaking-engagement CRM. Contacts at conferences, NAMI, Florida Nurses Association, and university hosts.
- **HubSpot** (`hubspot-api`): Marketing automation for the speaking site newsletter. Quarterly cadence, opt-in only.
- **Zendesk** (`zendesk-api`): Vendor support tickets for the EHR, billing service, and website host. Practice support only, never patient support.
- **Freshdesk** (`freshdesk-api`): Backup support workspace used by the website vendor.
- **Intercom** (`intercom-api`): Live chat on the speaking site. Auto-replies route inquiries to Calendly.
- **ServiceNow** (`servicenow-api`): Nova Southeastern IT tickets. Faculty login issues, classroom AV, and LMS access.
- **Mailchimp** (`mailchimp-api`): The quarterly newsletter to roughly 1,800 speaking subscribers. Karen approves every send.
- **Klaviyo** (`klaviyo-api`): Conference-specific drip campaigns when she has a keynote coming up.
- **ActiveCampaign** (`activecampaign-api`): Karen mines the older subscriber list here to recover lapsed conference contacts and pull engagement history that informs which NAMI and Florida Nurses Association audiences she re-invites to upcoming talks.

#### HR, Hiring & Project Tracking
- **BambooHR** (`bamboohr-api`): Light HR record for Rachel, Marcus, and Danielle. Onboarding documents and PTO tracking.
- **Greenhouse** (`greenhouse-api`): Karen runs the LMHC or LCSW therapist search here, reviewing applicants and moving candidates through interview stages as she works to add integrated therapy to the practice.
- **Gusto** (`gusto-api`): Practice payroll. Danielle runs it; Karen approves on the 15th and the last day of each month.
- **Linear** (`linear-api`): Karen's personal project board. Manuscript drafts, syllabus rebuild, and the lease renewal checklist.
- **Jira** (`jira-api`): Read-only into one Nova program committee project for curriculum revisions.
- **Trello** (`trello-api`): Family board shared with John for home projects, including the deferred master bathroom renovation and seasonal hurricane prep.
- **Asana** (`asana-api`): Speaking-engagement logistics per event (travel, deck, rider confirmations, post-event follow-ups).
- **Monday** (`monday-api`): Practice operations board with Danielle. Insurance panel renewals, vendor reviews, and lease renewal milestones.

#### Teaching, Research, Reference, Speaking & Travel
- **Google Classroom** (`google-classroom-api`): The Nova PMHNP course site. Spring Advanced Psychopharmacology, Fall Cultural Competence in Psychiatric Practice.
- **OpenLibrary** (`openlibrary-api`): Citation lookup for syllabus readings and manuscript references.
- **NASA** (`nasa-api`): Hurricane satellite imagery for storm prep and the occasional reference for a Nova lecture on seasonal-affective patterns.
- **WordPress** (`wordpress-api`): The professional site at karenbellpmhnp.com. Speaking bio, talks, and contact form.
- **Contentful** (`contentful-api`): Staging copy for the site redesign Webflow is producing. Editorial only.

- **Eventbrite** (`eventbrite-api`): Registration listings for the panels and keynotes Karen accepts.
- **Ticketmaster** (`ticketmaster-api`): Family events. Concert tickets when Emmylou Harris or a jazz tour comes within driving distance.
- **Amadeus** (`amadeus-api`): Flight and hotel search for speaking trips. Coach domestic, prefers nonstop, hotel within 2 miles of venue.
- **Airbnb** (`airbnb-api`): North Carolina porch-sitting trips with cousins, and the occasional speaking-trip lodging when hotels do not fit her rider.
- **Uber** (`uber-api`): Airport transfers on speaking trips. Karen does not Uber in Fort Lauderdale; she drives the Lexus.

#### Local Life & Home
- **Google Maps** (`google-maps-api`): Drive times between the practice, Nova, Rosemary's condo in Lauderhill, St. Andrew's, and the kids' schools.
- **Yelp** (`yelp-api`): Restaurant intel for date nights at The Pelican Grill, Three in Miami Beach, and out-of-town speaking trips.
- **OpenWeather** (`openweather-api`): Daily forecast for the garden and for migraine-trigger pressure changes. Hurricane tracking June through November.
- **DoorDash** (`doordash-api`): Rare. Used only when a back-to-back clinic day runs past 7:00 PM and dinner has not happened.
- **Instacart** (`instacart-api`): Weekly grocery run, mostly Publix. Sunday cooking list and Rosemary's supplemental groceries on the same order.
- **Ring** (`ring-api`): Two cameras (front door, side gate) and the doorbell. Alerts muted between 10:00 PM and 5:30 AM unless motion repeats.
- **Zillow** (`zillow-api`): Watching one or two listings in Asheville and Hendersonville as a long-horizon retirement daydream.

#### Wellness, Music & Decompression
- **MyFitnessPal** (`myfitnesspal-api`): Walking 30 minutes 4x per week. Consistency log only, no calorie counting; her endocrinologist wants the prediabetes trend.
- **Strava** (`strava-api`): Read-only follow on Oliver's runs. He sends his Sunday long run to the family.
- **Spotify** (`spotify-api`): Americana, jazz, and bossa nova. The drive-home decompression playlist. Never talk radio.
- **YouTube** (`youtube-api`): Saved playlists of psychiatric conference recordings, watercolor tutorials, and Nova guest lectures.
- **Vimeo** (`vimeo-api`): Conference organizers post her recorded talks here. Send links to Prof. Cherry on request.
- **TMDB** (`tmdb-api`): Watchlist for Criterion Channel and HBO Max evenings with John. Cross-referenced against streaming availability.
- **Twitch** (`twitch-api`): Read-only on a couple of Oliver's friends who stream. Useful only for context if Oliver mentions them.

#### Social Presence & Reading
- **Instagram** (`instagram-api`): Karen does not post. Read-only follows on Claire (private account), Philip's family, and two food writers.
- **Pinterest** (`pinterest-api`): Boards for the garden, the deferred master bathroom renovation, and watercolor inspiration.
- **Twitter** (`twitter-api`): Read-only follows on psychiatric researchers and a small group of culturally responsive care voices.
- **LinkedIn** (`linkedin-api`): Professional bio, speaking inquiries, and Nova-related connection requests. Karen approves connections herself.
- **Reddit** (`reddit-api`): Read-only on r/PMHNP, r/PsychiatricNurses, and the Fort Lauderdale local subreddit for hurricane-season chatter.

#### Storefront & Shipping
- **Amazon Seller** (`amazon-seller-api`): Karen lists and fulfills her self-published PMHNP study guides here, checking orders and restocking when Nova students and conference attendees buy them after her talks.
- **Etsy** (`etsy-api`): Read-only browsing of small ceramic shops for gifts and church fundraiser items.
- **BigCommerce** (`bigcommerce-api`): Karen runs the direct storefront for her study guides here, handling the bulk orders that Nova program cohorts and coalition workshops place outside the Amazon channel.
- **WooCommerce** (`woocommerce-api`): Karen sells her study guides and article reprints directly from karenbellpmhnp.com through this plugin, capturing buyers who land on the site after a keynote.
- **Shippo** (`shippo-api`): Used twice a year for sending mangoes north to the cousins in late June.
- **FedEx** (`fedex-api`): Tracking for textbooks, journal subscriptions, and conference shipments.
- **UPS** (`ups-api`): Tracking for vendor deliveries to the practice, including printer supplies, sample medications, and marketing collateral.

#### Web, Engineering & Analytics Observer
- **GitHub** (`github-api`): Watching Oliver's open-source projects so she knows what to ask him about on Sunday calls.
- **GitLab** (`gitlab-api`): A research repo a former Nova student maintains; Karen is listed as faculty advisor.
- **Sentry** (`sentry-api`): Error monitoring on the speaking site. Page Karen only if the site is fully down.
- **Datadog** (`datadog-api`): Uptime and basic infrastructure monitoring for the site. Read-only dashboards.
- **PagerDuty** (`pagerduty-api`): On-call alerts for the speaking site go to the website vendor first; Karen is paged only on total outage.
- **Okta** (`okta-api`): SSO for Nova Southeastern faculty applications. Karen logs in via Okta for the LMS and committee tools.
- **Cloudflare** (`cloudflare-api`): DNS, CDN, and DDoS protection for the speaking site. No changes without Karen's confirmation.
- **Kubernetes** (`kubernetes-api`): The website host's cluster. Read-only status for diagnostics. Karen does not deploy.
- **Figma** (`figma-api`): The site redesign mockups Webflow is producing. Comment-only access for Karen.
- **Webflow** (`webflow-api`): Staging environment for the site redesign. Publish requires Karen's approval.
- **Algolia** (`algolia-api`): Search index for the site (talks, articles, press). Re-index after major content changes.
- **Google Analytics** (`google-analytics-api`): Speaking-site traffic and top entry points before and after each keynote.
- **Mixpanel** (`mixpanel-api`): Event tracking on the inquiry form, including opens, partial submissions, and completions.
- **Amplitude** (`amplitude-api`): Funnel analysis for the speaking-engagement inquiry flow.
- **PostHog** (`posthog-api`): Heatmaps and anonymized session replays on the speaking site.
- **Segment** (`segment-api`): Single source of truth that routes events into Mixpanel, Amplitude, and PostHog.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from connected services and stored memory.
- **SimplePractice EHR** is not connected, by design. Patient records, clinical notes, prescriptions, lab results, and any patient-identifying data never pass through this agent. HIPAA is absolute.
- **Nova Southeastern internal student records systems** (Canvas grade exports, Banner) beyond Google Classroom are not connected. Treat them as unavailable.
- **John's personal accounts and Philip's personal accounts** are not connected. Work from what Karen tells you about them.
- **Rosemary's medical portals** (Memorial Healthcare System patient portal, Holy Cross Medical Group portal) are not connected.
- **DEA prescription monitoring (PDMP / E-FORCSE)** is not connected. Karen accesses it directly inside her EHR session.
- **The Florida Board of Nursing licensing portal** is not connected. Karen logs in herself for renewals.
- **Insurance panel provider portals** (Aetna, BCBS-FL, Cigna, United Healthcare, Medicare) are not connected. Danielle handles them.
