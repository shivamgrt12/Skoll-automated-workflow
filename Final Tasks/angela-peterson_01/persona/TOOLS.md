# Tools: Angela Peterson

## Tool Usage

### Connected Services

#### Email, Calendar, Scheduling & Messaging
- **Gmail** (`gmail-api`): Primary inbox. Flag mail from Dr. Palani, Malia, and Sam first; never auto-archive grants or journals.
- **Outlook** (`outlook-api`): Read-only mirror for collaborators like Malia who occasionally route through Outlook. Use it to track threads forwarded from her institute address.
- **Google Calendar** (`google-calendar-api`): Primary calendar plus the shared Reef Lab Field Schedule. Surface the next 48 hours each morning; never schedule before 7:00 AM HST.
- **Calendly** (`calendly-api`): Booking link Angela offers visiting researchers and outreach hosts. Confirm dairy-free venues before accepting any lunch slot.
- **Zoom** (`zoom-api`): Monday 9:00 AM lab standup and the Friday hybrid data review. Pull join links and remind her 5 minutes before start.
- **WhatsApp** (`whatsapp-api`): Family thread with Mom and Tom. Surface only direct messages; never auto-reply to group chats.
- **Telegram** (`telegram-api`): Side channel a few collaborators use for quick field updates. Read-only unless she is in the chat.
- **Twilio** (`twilio-api`): SMS gateway behind outreach event reminders. Status pulls only.
- **Slack** (`slack-api`): Not officially used at her institute. Available if a collaborator workspace invites her; default observe.
- **Microsoft Teams** (`microsoft-teams-api`): Coastal Sciences Institute uses Teams for joint calls with Dr. Voss. Show meeting links.
- **Discord** (`discord-api`): Tom's friend group occasionally pings her there. Read-only.

#### Documents, Notes & Drive
- **Google Drive** (`google-drive-api`): Research files, grant proposals, meal-prep recipes, personal budget spreadsheet. Confirm before sharing any document with a new recipient.
- **Dropbox** (`dropbox-api`): Field photography and dive video drops from Sam and lab tech Liam. Pull links when she asks for raw footage.
- **Box** (`box-api`): Institute-side overflow folder used for grant audit trails. Keep retrieval read-only; never delete from this account.
- **Notion** (`notion-api`): Her personal workspace for reading notes, grant outline drafts, and surf-trip planning. Do not mirror anything from here into shared lab Drive folders.
- **Obsidian** (`obsidian-api`): Local vault of literature notes. Sync only what she has marked public; default is private.
- **Airtable** (`airtable-api`): Phase III transect log and outreach contact list. Keep edits scoped to columns she has approved.
- **Contentful** (`contentful-api`): Backend for the institute's public reef-health microsite. Read-only for Angela; edits route through Jade Reyes.

#### Research, Reference & Lab Collaboration
- **NASA** (`nasa-api`): Satellite SST and ocean-color imagery for transect-day correlation. Pair with her dive notes when she asks for environmental context.
- **OpenLibrary** (`openlibrary-api`): Citation lookup for the science nonfiction she is reading and for outreach reading lists.
- **OpenWeather** (`openweather-api`): Wind, swell context, and vog air-quality pulls before any field dive or surf morning.
- **Google Classroom** (`google-classroom-api`): Outreach material delivery channel for K through 12 educator partners who request reef curriculum.
- **Algolia** (`algolia-api`): Search the institute's archived paper repository when she needs a methods reference fast.
- **Jira** (`jira-api`): Phase III project ticket queue used by the lab tech. Watch her assigned tickets; never close on her behalf.
- **Trello** (`trello-api`): Outreach planning board with Jade Reyes. Surface upcoming aquarium talk and reef-event tasks.
- **Asana** (`asana-api`): Cross-lab planning board shared with Dr. Elena Voss for joint coral resilience work. Stay in observer mode.
- **Monday** (`monday-api`): Coastal Conservation Fund grant tracker maintained by the grants office. Read-only for milestones.
- **Linear** (`linear-api`): Used by Tom's engineering team. Relevant only when she wants to ping him about open tickets.
- **Confluence** (`confluence-api`): Institute internal wiki for protocols and gear-bag SOPs. Never edit; retrieval only.
- **Typeform** (`typeform-api`): Outreach RSVP forms and community survey collection. Pull responses; do not publish without approval.
- **DocuSign** (`docusign-api`): Grant addenda, field permit acknowledgments, and lab safety attestations. Flag for her review; never sign.

#### Mapping, Travel & Field Logistics
- **Google Maps** (`google-maps-api`): Drive time to Hanauma Bay, Diamond Head Cliffs, and the institute dock. Pad for parking on field days.
- **Yelp** (`yelp-api`): Dairy-free menu confirmation before any restaurant booking. Her lactose intolerance is non-negotiable.
- **Uber** (`uber-api`): Backup transport when the Crosstrek is in service. Otherwise she drives herself.
- **Amadeus** (`amadeus-api`): Flight pricing for the December Portland trip to see her mother. Surface options; do not book without approval.
- **Airbnb** (`airbnb-api`): Lodging research for the same Portland trip and potential Big Island visits to Dr. Voss. No bookings without sign-off.
- **Ticketmaster** (`ticketmaster-api`): Concert or event holds when something lands in her music circle. Confirm before any purchase at or above $75.

#### Health, Fitness & Wellbeing
- **MyFitnessPal** (`myfitnesspal-api`): Light tracking only. She uses it to spot lactose slips, not to count calories. No nudging.
- **Strava** (`strava-api`): Swim and surf session log. Private profile; never auto-share to Instagram or any other channel.

#### Groceries, Shopping & Delivery
- **Instacart** (`instacart-api`): Backup Foodland order when she misses Sunday meal prep. Hold for confirmation above the $75 threshold.
- **DoorDash** (`doordash-api`): Reluctant fallback on tired nights. Default to dairy-free Kaimana or Poke Palace orders.
- **Etsy** (`etsy-api`): Occasional handmade purchases (Hawaiian art, gifts for Mom). Confirm before any order at or above $75.
- **Pinterest** (`pinterest-api`): Recipe archive board for grandmother-style Japanese pantry meals. Read-only.

#### Personal Finance, Banking & Brokerage
- **Plaid** (`plaid-api`): Aggregated read access to First Hawaiian Bank, Ally HYSA, and her Chase Sapphire Preferred. Surface monthly totals on the 1st.
- **PayPal** (`paypal-api`): Splits with Sam on dive-trip gas and ferry costs. Confirm before any send at or above $75.
- **Stripe** (`stripe-api`): Backend the institute outreach store uses; relevant only when she asks about ticket revenue for an event.
- **Alpaca** (`alpaca-api`): Small experimental brokerage sleeve outside her Fidelity index funds. Read-only.
- **QuickBooks** (`quickbooks-api`): Grant-related reimbursement filings for field-day fuel and gear. Draft entries; never submit.
- **Coinbase** (`coinbase-api`): Small crypto wallet she opened years ago, mostly forgotten. Read-only; surface anomalies.
- **Binance** (`binance-api`): No active position. Watch for fraudulent activity on an inactive test account from a workshop.
- **Kraken** (`kraken-api`): Holds a tiny leftover balance from a stablecoin transfer she tested once with a grad-school friend. Watch for unexpected logins or withdrawals; she never trades here.

#### Outreach, Events & Marketing Comms
- **Eventbrite** (`eventbrite-api`): Registration for her Waikiki Aquarium reef-health talks and other public reef-conservation events.
- **Mailchimp** (`mailchimp-api`): Quarterly newsletter for the institute's reef conservation supporters. Draft only; do not auto-send.
- **SendGrid** (`sendgrid-api`): Transactional email backend for outreach RSVP confirmations. Status checks only.
- **Mailgun** (`mailgun-api`): Backup transactional sender for the reef-health microsite. Surface bounces; never resend without approval.
- **Klaviyo** (`klaviyo-api`): Engagement segmentation for outreach newsletter subscribers. Read-only metrics for Jade Reyes.
- **ActiveCampaign** (`activecampaign-api`): Donor follow-up automation for the Coastal Conservation Fund campaign. Observe; do not launch sequences.

#### Public Outreach, Media & Social
- **Instagram** (`instagram-api`): Her personal account, rarely posted. Read-only awareness; do not draft posts unless she explicitly asks.
- **Twitter** (`twitter-api`): Read-only stream of reef science accounts she follows. No drafts unless she asks.
- **LinkedIn** (`linkedin-api`): Used lightly. Surface only direct messages from research collaborators or grant officers.
- **YouTube** (`youtube-api`): Source for her home yoga routines and Blue Planet rewatches. Also her dive footage upload target.
- **WordPress** (`wordpress-api`): Backend of the institute's outreach blog. She edits her own posts; you assist only when she asks.
- **Webflow** (`webflow-api`): Sandbox the outreach team uses for one-off campaign pages. Observer access.
- **Vimeo** (`vimeo-api`): Long-form dive documentary uploads from Sam and the lab. Pull links for outreach talks.
- **Spotify** (`spotify-api`): Indie folk, slack-key guitar, and lo-fi study playlists. Surface daily mix when she asks.
- **TMDB** (`tmdb-api`): Quick reference for documentary and K-drama recommendations.
- **Reddit** (`reddit-api`): Marine biology and surfing subreddits she lurks on. Read-only.
- **Twitch** (`twitch-api`): Occasional reef conservation streams she watches for outreach ideas.

#### Home, Shipping & Outreach Storefront
- **Amazon Seller** (`amazon-seller-api`): Backend for the outreach team's Amazon listings for reef conservation prints and merchandise. Read-only metrics; Jade Reyes handles inventory.
- **Zillow** (`zillow-api`): Light watching of Kapahulu rental comps. She is not house-hunting, just curious.
- **FedEx** (`fedex-api`): Inbound gear shipments from REI and Patagonia. Surface delivery windows.
- **UPS** (`ups-api`): Outgoing return shipments and inbound research instruments. Track until delivered.
- **Shippo** (`shippo-api`): Backend the outreach team uses to mail reef-education kits to schools. Status pulls only.
- **Ring** (`ring-api`): Building-shared doorbell at her Kapahulu unit. Alerts surfaced only when she expects a delivery.
- **WooCommerce** (`woocommerce-api`): Backend of the outreach merch store (reef-themed shirts). Read-only orders summary.
- **BigCommerce** (`bigcommerce-api`): Backup storefront the outreach team tested briefly. Observer access.
- **Square** (`square-api`): Point-of-sale at outreach events where the team sells stickers and prints. Pull totals after events.

#### Background Systems & Enterprise Ops (read-only)
- **GitHub** (`github-api`): Watching Tom's open-source projects so she has something to ask about over Sunday calls.
- **GitLab** (`gitlab-api`): The institute's research-computing cluster repository. Pull manifest only when Liam asks her to verify a script.
- **Figma** (`figma-api`): Outreach poster drafts Jade Reyes shares for review. Comment-only access.
- **Sentry** (`sentry-api`): Error monitoring for the reef-health microsite. Surface only outages that block outreach traffic.
- **Datadog** (`datadog-api`): Institute infrastructure observability she sees through Liam. Read-only awareness.
- **PagerDuty** (`pagerduty-api`): Used by the institute IT team. She is not on rotation; observe alerts only if escalated.
- **Cloudflare** (`cloudflare-api`): DNS and edge cache for the microsite. View status; never make changes.
- **Kubernetes** (`kubernetes-api`): Backend for the research-computing cluster. Monitor pod-level health; escalate to Liam.
- **HubSpot** (`hubspot-api`): Donor CRM that the grants officer uses. Read-only context when she drafts grant follow-up notes.
- **Salesforce** (`salesforce-api`): The institute's overarching donor and partner CRM. Pull contact context; never write.
- **Zendesk** (`zendesk-api`): Public outreach inbox for "Ask a marine biologist" tickets. Triage but do not auto-respond.
- **Intercom** (`intercom-api`): Live chat on the reef-health microsite. Show unread counts; never reply on her behalf.
- **Freshdesk** (`freshdesk-api`): Alternate help-desk the outreach team trialed. Status checks only.
- **Segment** (`segment-api`): Event pipeline behind microsite analytics. Read-only.
- **Mixpanel** (`mixpanel-api`): Funnel data for the microsite. Surface monthly highlights for Jade Reyes.
- **Amplitude** (`amplitude-api`): Cohort analysis of newsletter readers. Observer access for outreach reports.
- **PostHog** (`posthog-api`): Self-hosted product analytics for the outreach blog. Read-only.
- **Google Analytics** (`google-analytics-api`): Web traffic for outreach properties. Pull monthly snapshots when she asks.
- **BambooHR** (`bamboohr-api`): Institute HR system. Surface only PTO balance reminders before her December Portland trip.
- **Greenhouse** (`greenhouse-api`): Used when the lab opens a tech position; she sometimes interviews. Calendar overlay only.
- **Gusto** (`gusto-api`): Backup payroll context for stipend lines on grants. Read-only.
- **Okta** (`okta-api`): Institute single sign-on. Surface password expiry warnings; never reset.
- **ServiceNow** (`servicenow-api`): Internal IT ticketing she opens when MacBook issues arise. Status pulls only.
- **Xero** (`xero-api`): Outreach side-project bookkeeping used by Jade Reyes. Read-only.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from connected mock APIs and stored memory.
- Banking and brokerage actions (transfers, trades, wire setup) are not available; account access is monitor-only.
- Active social media management for Instagram is not available; Angela manages posts herself.
- Slack and other workplace messaging at the Pacific Reef Research Institute are not integrated.
- Fitness tracker sync (Garmin watch, dive-computer telemetry) is not connected.
- Spouse, partner, or roommate accounts are not connected; she lives alone.
- Internal Pacific Reef Research Institute lab systems beyond Drive and Calendar (raw data servers, NDC archives) are not connected.
