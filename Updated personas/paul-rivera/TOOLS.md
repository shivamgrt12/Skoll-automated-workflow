# Tools: Paul Rivera

## Tool Usage

### Connected Services

#### Communication & Messaging
- **Gmail** (`gmail-api`): Primary inbox. Triage Judith, Brett, Kelsey, Tom Hadley, and Dr. Kaplan's office first.
- **Outlook** (`outlook-api`): SkyBridge alumni mirror for pension notices. Forward actionable items to Gmail; never send without approval.
- **WhatsApp** (`whatsapp-api`): "Rivera Family" group with Brett, Kelsey, Hannah, Daniel. Photo shares and visit coordination only.
- **Telegram** (`telegram-api`): Quiet monthly dinner thread with Captain Ed Mulvaney and one retired colleague.
- **Discord** (`discord-api`): Coordinates Owen's chess club server messages; drafts Paul's responses for approval before posting.
- **Slack** (`slack-api`): Drafts replies in Aviation Heritage Museum docent workspace; posts after Paul's review and approval.
- **Microsoft Teams** (`microsoft-teams-api`): Manages SkyBridge pension quarterly briefings; surfaces invites and RSVPs after Paul's explicit confirmation.
- **Zoom** (`zoom-api`): Cardiologist telehealth and quarterly museum volunteer meeting. Surface join links 5 minutes before start.
- **Twilio** (`twilio-api`): SMS reminders to the Saturday golf group for tee times and weather changes.
- **SendGrid** (`sendgrid-api`): Sends museum docent roster updates and tour confirmations; uses plain templates with no marketing styling.
- **Mailgun** (`mailgun-api`): Backup sender for school-group tour confirmations when SendGrid is throttled in spring.
- **Mailchimp** (`mailchimp-api`): Sends quarterly docent volunteer newsletter Paul co-writes; keeps copy plain with no marketing flourish.
- **Intercom** (`intercom-api`): Museum public-site widget. Triage school-group and tour requests; route the rest to coordinator.
- **Klaviyo** (`klaviyo-api`): Sends spring gala invitations and donor follow-ups; Paul reviews and approves all copy.
- **ActiveCampaign** (`activecampaign-api`): Tracks out-of-state former docents and sends spring gala invitations plus quarterly museum updates.

#### Calendar, Files & Productivity
- **Google Calendar** (`google-calendar-api`): Schedule of record, shared with Judith. Tee times tagged "do not move."
- **Google Drive** (`google-drive-api`): Travel itineraries, park research, tour scripts, medical scans. Never rename folders without checking.
- **Calendly** (`calendly-api`): Museum school-group bookings Tuesdays and Thursdays. 60-minute blocks, never overlapping golf or appointments.
- **Dropbox** (`dropbox-api`): Stores park trip photo albums and grandkid FaceTime screenshots; keeps originals immutable and shares duplicates.
- **Box** (`box-api`): Stores SkyBridge alumni pension statements and historical flight records; retrieves quarterly statements for tax review.
- **Notion** (`notion-api`): Travel notebook. Park checklists, packing lists, restaurant short lists. Cross-link to Drive.
- **Obsidian** (`obsidian-api`): Local golf journal. Round notes, course strategy, handicap tracking. Paul owns structure.
- **Airtable** (`airtable-api`): National park bucket list with status and trip logistics. Shared read with Judith.
- **Monday** (`monday-api`): Museum quarterly exhibit board. Docent assignments tracked here. Paul adds shift notes.
- **Asana** (`asana-api`): Tracks spring gala planning board: venue, catering, guest lists; Paul comments and approves tasks.
- **Trello** (`trello-api`): Family board for holiday rotation, grandkid birthdays, and Owen and Lily mail list.
- **Typeform** (`typeform-api`): Hosts museum tour booking form and annual docent feedback survey; exports responses for coordinator review.
- **DocuSign** (`docusign-api`): Prepares estate documents, vehicle renewals, and travel waivers; always confirms with Paul before he signs.

#### Finance & Banking
- **Plaid** (`plaid-api`): Aggregates Sonoran credit union, SkyBridge pension, and Desert Ridge portfolio. Monthly reconciliation.
- **Stripe** (`stripe-api`): Museum online ticket sales for tours and gala. Reconcile with coordinator monthly.
- **Square** (`square-api`): Processes walk-up gift shop and event-day ticket sales; Paul reviews daily totals and reconciles weekly.
- **PayPal** (`paypal-api`): Sends occasional grandkid college fund contributions and processes rare collector pin purchases for Paul.
- **QuickBooks** (`quickbooks-api`): Personal ledger for charitable giving and travel expenses. Reconciled quarterly with advisor.
- **Xero** (`xero-api`): Museum volunteer reimbursement ledger. Submit mileage and receipts each quarter; verify deposits.
- **Coinbase** (`coinbase-api`): Practice wallet Daniel set up. Paul reviews quarterly and forwards screenshots to Daniel.
- **Binance** (`binance-api`): Global crypto price reference. Pull weekly BTC and ETH spots for Daniel's spreadsheet.
- **Kraken** (`kraken-api`): Cross-check on Coinbase USD value. Tighter spreads make for a clean sanity number.
- **Alpaca** (`alpaca-api`): Paper-trading sandbox modeling conservative rebalances. Paul reviews monthly and feeds back assumptions.

#### Travel & Logistics
- **Amadeus** (`amadeus-api`): Flights and hotels for park trips and visits to Brett and Kelsey. Confirm exit-row.
- **Airbnb** (`airbnb-api`): Park lodging when entrance hotels are full. Judith decides; Paul handles logistics.
- **Uber** (`uber-api`): Airport transfers where rental parking is not worth it. Standard rides only, never Black.
- **DoorDash** (`doordash-api`): Rare. Travel-day evenings when cooking is not happening and Judith is tired.
- **Instacart** (`instacart-api`): Backup grocery delivery before trips or day after returning. Judith approves before checkout.
- **FedEx** (`fedex-api`): Birthday and Christmas packages to Owen, Lily, and Kelsey. Track inbound to Scottsdale.
- **UPS** (`ups-api`): Receiving for golf equipment from pro shop and occasional REI travel gear shipments.
- **Shippo** (`shippo-api`): Multi-carrier labels for museum gift-shop outbound and occasional collectible shipments to patrons.
- **Google Maps** (`google-maps-api`): Drive times and 4Runner road trip routes. Cache offline maps for remote stretches.
- **OpenWeather** (`openweather-api`): Pulls tee-time forecasts, monsoon afternoon alerts, and park trip weather windows for Judith and Paul.

#### Health & Wellness
- **MyFitnessPal** (`myfitnesspal-api`): Logs light post-cardiac sodium tracking and salt-watch on dining-out days; ignores calorie totals.
- **Strava** (`strava-api`): Logs morning walks with Judith and walked-eighteen golf rounds. Private to followers.

#### Golf, Culture & Media
- **Spotify** (`spotify-api`): Queues Miles Davis and Steely Dan on patio, classic rock for 4Runner, kitchen "Sunday" playlist.
- **YouTube** (`youtube-api`): Queues PGA Tour highlights, swing instruction, and aviation documentaries for Paul; disables autoplay between sessions.
- **Twitch** (`twitch-api`): PGA Tour Live and golf instruction on rainy mornings. Followed channels only.
- **TMDB** (`tmdb-api`): Cast, director, and year lookups on classic Westerns. Never trusts a single review site.
- **Eventbrite** (`eventbrite-api`): Docent training sessions and spring gala ticket page. Paul tracks RSVPs for his sessions.
- **Ticketmaster** (`ticketmaster-api`): Phoenix Symphony with Judith and occasional spring training games with Tom Hadley.
- **Vimeo** (`vimeo-api`): Museum archive of pilot interviews and exhibit launch videos. Public share links live here.
- **Reddit** (`reddit-api`): Pulls trip ideas and equipment threads from r/golf, r/nationalparks, and r/aviation for Paul's review.
- **Twitter** (`twitter-api`): Drafts replies for PGA Tour, National Park Service, and aviation historians; Paul approves morning posts.

#### Home, Local & Civic
- **Ring** (`ring-api`): Front door and driveway cameras at Scottsdale house. Motion alerts at night only.
- **Zillow** (`zillow-api`): Annual house comps for insurance review. Also Arizona listings when Brett asks.
- **Yelp** (`yelp-api`): Scouts Scottsdale and Sedona restaurants; weights repeat reviewers higher than aggregate stars for shortlists.

#### Shopping & Visual
- **Amazon Seller** (`amazon-seller-api`): Museum gift shop storefront dashboard. Review monthly sales; forward numbers to coordinator.
- **Etsy** (`etsy-api`): Sources leather headcovers and small artisan gifts for Judith. Trusted sellers only.
- **BigCommerce** (`bigcommerce-api`): Museum online gift shop. Hats, model planes, collector pins. Review inventory before gala.
- **WooCommerce** (`woocommerce-api`): Places Pinnacle Golf Supply orders with saved payment; always confirms cart total before checkout.
- **Pinterest** (`pinterest-api`): Receives Judith's park lodge boards. Paul keeps a private golf photography board.
- **Instagram** (`instagram-api`): Follows family, NPS, and PGA Tour; drafts grandkid-photo reactions for Paul to approve and post.

#### Engineering, DevOps & Analytics
- **GitHub** (`github-api`): Watches Daniel's open-source projects. Stars repos; opens issues only when Daniel walks him through.
- **GitLab** (`gitlab-api`): Mirrors one of Daniel's collaborator repos; surfaces issue updates for FaceTime questions Paul prepares ahead.
- **Jira** (`jira-api`): Tracks museum exhibit-renovation tickets; updates statuses, flags blockers, and reports progress to coordinator weekly.
- **Linear** (`linear-api`): Tracks one aviation history nonprofit project for grant deliverables; comments updates and flags missed milestones.
- **Confluence** (`confluence-api`): Edits docent handbook, SOPs, and tour scripts; cross-links entries with Drive and Notion references.
- **Sentry** (`sentry-api`): Monitors museum website errors and forwards overnight pages to the coordinator with triage notes.
- **Datadog** (`datadog-api`): Monitors public exhibit kiosk observability; surfaces outage alerts and routes incidents to the coordinator.
- **PagerDuty** (`pagerduty-api`): Manages ticket portal escalation tree; wakes Paul only when sustained outages cross threshold.
- **Okta** (`okta-api`): Manages museum admin SSO logins, password resets, and access tokens for Paul's authorized workspaces.
- **Cloudflare** (`cloudflare-api`): DNS and edge for museum site. Paul monitors traffic spikes around exhibit launches.
- **Kubernetes** (`kubernetes-api`): Checks Daniel's side-project cluster health quarterly; surfaces informed questions for FaceTime conversations.
- **Figma** (`figma-api`): Annotates exhibit posters and gala invitation comps; routes consolidated feedback to coordinator and outside designers.
- **Segment** (`segment-api`): Pipes museum events into Amplitude and Mixpanel. Taxonomy tuned post-gala with coordinator.
- **Amplitude** (`amplitude-api`): Pulls primary museum analytics; runs RSVP channel breakdown after each gala announcement for the coordinator.
- **Mixpanel** (`mixpanel-api`): Runs alternate funnel view for the school-tour booking conversion path; flags drop-offs for coordinator follow-up.
- **PostHog** (`posthog-api`): Pulls exhibit feedback widget sentiment trends; flags negative patterns for coordinator review after each launch.
- **Algolia** (`algolia-api`): Powers search on museum exhibit archive and event listings; tunes synonyms after each exhibit launch.
- **Contentful** (`contentful-api`): Manages museum public site content; Paul edits his docent bio and tour-script entries directly.
- **Webflow** (`webflow-api`): Updates museum static event pages with Paul's docent bio, current exhibit notes, and gala details.
- **WordPress** (`wordpress-api`): Publishes docent blog for tour notes and cross-posts; Paul reviews and approves drafts before publish.

#### CRM, HR & Support
- **HubSpot** (`hubspot-api`): Maintains museum donor CRM; segments spring gala touchpoints and logs interactions for coordinator follow-up.
- **Salesforce** (`salesforce-api`): Maintains grant and partner database; pulls funder profiles and prepares briefs before gala-season meetings.
- **BambooHR** (`bamboohr-api`): Logs volunteer hours in HR portal; surfaces annual docent acknowledgement letter for Paul's records.
- **Greenhouse** (`greenhouse-api`): Volunteer coordinator hiring pipeline. Paul screens cover letters when search is open.
- **Gusto** (`gusto-api`): Museum stipend payroll view. Check records before tax season; flag discrepancies to coordinator.
- **Zendesk** (`zendesk-api`): Triages museum visitor inquiries inbox; answers school-group questions and routes the rest to coordinator.
- **ServiceNow** (`servicenow-api`): IT ticketing for simulator exhibit. File hardware tickets; follow up on spring renewal.
- **Freshdesk** (`freshdesk-api`): Handles alternate support inbox for online ticket holders; auto-routes refund requests to coordinator queue.
- **LinkedIn** (`linkedin-api`): Maintains Paul's retired-captain profile; surfaces alumni updates and drafts reactions for him to approve.

#### Research & Knowledge
- **NASA** (`nasa-api`): Imagery for "Sky and Flight" exhibit panels and park trip night-sky planning.
- **OpenLibrary** (`openlibrary-api`): Lookup for Connelly novels and aviation memoirs. Surface OCLC numbers for library loans.
- **Google Classroom** (`google-classroom-api`): School-group tour rosters and accommodation notes. Pull the morning of each Tuesday and Thursday tour.
- **Google Analytics** (`google-analytics-api`): Pulls exhibit launch pageviews when an exhibit gets local press; flags traffic spikes weekly.
