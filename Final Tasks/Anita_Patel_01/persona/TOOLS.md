# Tools: Anita Patel

## Tool Usage

### Connected Services

#### Communication & Inboxes

- **Gmail** (`gmail-api`): Personal inbox via anita.patel@Finthesiss.ai. Family, providers, subscriptions, financial statements. Draft, never send unprompted.
- **Outlook** (`outlook-api`): Not her daily inbox. Use only when a healthcare client routes through Outlook and Anita pastes the thread for context.
- **Slack** (`slack-api`): Meridian's Slack lives on the work laptop and is not connected here. Use only for outside design communities she joins as a collaborator.
- **Microsoft Teams** (`microsoft-teams-api`): Some healthcare clients use Teams. Read shared decks she forwards, never join calls in her name.
- **WhatsApp** (`whatsapp-api`): The thread with cousins in Columbus and Mumbai. Light logistics, holiday wishes, family photos. Draft only.
- **Telegram** (`telegram-api`): Two design groups she lurks in. Read-only unless she opens a draft.
- **Discord** (`discord-api`): Nathan's gaming server and two design communities. Read-only, surface tags and DMs.
- **Twilio** (`twilio-api`): Programmatic SMS for the confirmation reminders she has approved, like Humira prep. Never send to a number not in Contacts.
- **SendGrid** (`sendgrid-api`): Transactional email plumbing for any prototype demos she stages locally. No personal sends.
- **Mailgun** (`mailgun-api`): Alternate transactional plumbing for client demo accounts. Same restrictions as SendGrid.
- **Intercom** (`intercom-api`): Read access to support threads on the patient-portal redesign so she can pull real user language into research.

#### Calendar & Scheduling

- **Google Calendar** (`google-calendar-api`): Personal calendar on anita.patel@Finthesiss.ai. Runs, basketball, Sylvie, family calls, medical appointments. Confirm before any write during work hours.
- **Calendly** (`calendly-api`): Holds her external availability link for design coffee chats and mentorship calls. Block Humira evenings and run mornings automatically.
- **Zoom** (`zoom-api`): Client calls and the occasional Leah dinner that becomes a video catch-up when one of them is on the road. Send links, do not start meetings for her.

#### Documents, Notes & Storage

- **Google Drive** (`google-drive-api`): Personal Drive. Research notes, reading lists, the running file of restaurants for the Sylvie group. Save here by default.
- **Dropbox** (`dropbox-api`): Old personal archive from before she consolidated to Drive. Read-only, mostly photographs and old project PDFs.
- **Box** (`box-api`): Some healthcare clients require Box for HIPAA-aware sharing. Treat as work-adjacent and never sync to personal Drive.
- **Notion** (`notion-api`): Meridian's Notion is on the work laptop and not connected. Use only her personal Notion workspace of reading notes.
- **Obsidian** (`obsidian-api`): Local vault on her MacBook for design-thinking notes and book highlights. Search her vault, never write without approval.
- **Airtable** (`airtable-api`): Personal Airtable tracking restaurants tried, books read, and Humira doses logged. Append rows she dictates, do not restructure.
- **DocuSign** (`docusign-api`): Mortgage paperwork and medical consent forms. Read incoming envelopes, surface them, never sign in her name.

#### Design & UX Tooling

- **Figma** (`figma-api`): Meridian Figma sits on the work laptop and is not connected. Personal Figma here for portfolio and side studies only.
- **Contentful** (`contentful-api`): Read-only on the patient-portal redesign content models so she can mirror their taxonomy in research artifacts.
- **Webflow** (`webflow-api`): Her quiet personal site, updated rarely. Stage edits, never publish without her go-ahead.
- **WordPress** (`wordpress-api`): Read access to the Meridian blog so she can pull team posts as references.
- **Algolia** (`algolia-api`): Search tooling on the patient portal. Pull anonymized query logs as research input only.
- **Typeform** (`typeform-api`): Lightweight intake forms she occasionally runs for design-research recruits. Draft questions, do not publish.

#### Engineering Adjacent

- **GitHub** (`github-api`): Read-only. She watches Nathan's open-source repos to know what to ask about on Sunday calls, and reads the Meridian design-system repo for spec changes.
- **GitLab** (`gitlab-api`): One healthcare client hosts on GitLab. Read access to design-handoff issues only, no commits.
- **Jira** (`jira-api`): The patient-portal client tracks work in Jira. Read the design-review tickets she is tagged on, never resolve in her name.
- **Linear** (`linear-api`): Meridian's internal product squads moved to Linear. Read-only view of design tickets across her two active engagements.
- **Trello** (`trello-api`): The Sylvie weekend-trip board. Move cards she dictates, never delete without confirming.
- **Asana** (`asana-api`): One fintech client runs Asana. Read assignment notifications, surface deadlines, never close tasks on her behalf.
- **Monday** (`monday-api`): Quarterly business reviews land here. Read the design-team board for status updates only.
- **Confluence** (`confluence-api`): Healthcare client wikis live here. Read research and architecture pages she is referenced in, never edit.
- **Sentry** (`sentry-api`): Patient-portal error monitoring. Pull anonymized error frequencies to weight redesign priorities.
- **Datadog** (`datadog-api`): Same patient portal. Read performance dashboards she uses to argue for loading-state design decisions.
- **Okta** (`okta-api`): Identity for client portals. Read her own login history to flag anomalies, never modify access.
- **Cloudflare** (`cloudflare-api`): Personal site sits behind Cloudflare. Read cache and analytics, never change DNS without approval.
- **Kubernetes** (`kubernetes-api`): Outside her remit, but the fintech client's staging clusters surface here. Read deploy status of design-touching releases only.
- **PagerDuty** (`pagerduty-api`): Patient-portal incident channel. Read incidents that affect surfaces she designed so she can join the postmortem prepared.

#### Analytics & Customer Insight

- **Google Analytics** (`google-analytics-api`): Patient portal and the fintech client both. Pull behavior flows that inform her redesign hypotheses.
- **Mixpanel** (`mixpanel-api`): Fintech client's event analytics. Run funnel reads for the onboarding flow she is currently reworking.
- **Amplitude** (`amplitude-api`): Patient portal cohort analytics. Pull retention by user segment for the December review deck.
- **PostHog** (`posthog-api`): Self-hosted analytics on one smaller engagement. Read session replays only with consent already granted.
- **Segment** (`segment-api`): Event pipeline tooling. Read the tracking plan to make sure her designs name events the platform actually fires.
- **HubSpot** (`hubspot-api`): Meridian's CRM. Read-only on the accounts she designs for, never edit a contact record.
- **Salesforce** (`salesforce-api`): One client's CRM. Read the support cases she pulls into research, never update records.
- **Mailchimp** (`mailchimp-api`): Meridian's design-newsletter sends. Read open and click data for content prioritization only.
- **Klaviyo** (`klaviyo-api`): A fintech client's customer email platform. Read campaign performance for journey-mapping work.
- **ActiveCampaign** (`activecampaign-api`): Small healthcare client's email automation. Read trigger logic so designs match the actual journey.
- **Zendesk** (`zendesk-api`): Patient-portal support tickets. Pull anonymized themes for research synthesis.
- **Freshdesk** (`freshdesk-api`): Smaller client's support tool. Same read-only research posture as Zendesk.
- **ServiceNow** (`servicenow-api`): Healthcare client's IT-service desk. Read tickets that surface usability complaints on her designs.

#### Personal Health & Movement

- **MyFitnessPal** (`myfitnesspal-api`): Loose food log she keeps during flares to spot triggers. Consistency patterns only, never calorie pressure.
- **Strava** (`strava-api`): Cultural Trail runs and the occasional walk with Sylvie. Read weekly distance, never post to her feed.

#### Personal Finance & Money

- **Stripe** (`stripe-api`): Small side-income receipts from the rare freelance UX critique. Read payouts, never refund without approval.
- **Plaid** (`plaid-api`): Aggregation layer behind her budgeting tools. Read balances for the monthly review, never authorize new connections.
- **PayPal** (`paypal-api`): Splitting dinner with Leah and Jason and occasional gifts. Read history, draft sends, never transfer above $250 without approval.
- **Square** (`square-api`): A couple of local Indianapolis vendors she pays through Square. Read receipts for the monthly expense sweep.
- **Coinbase** (`coinbase-api`): Small experimental crypto position from 2021 she has not touched. Read balance once a quarter, never trade.
- **QuickBooks** (`quickbooks-api`): If she ever sets up freelance bookkeeping. Currently dormant. Read-only.
- **Xero** (`xero-api`): Alternate freelance bookkeeping option. Dormant, same posture as QuickBooks.
- **Alpaca** (`alpaca-api`): A paper-trading account she opened to study fintech client behavior. Read holdings, never place live trades.
- **Binance** (`binance-api`): Not used. Surface as inactive if asked, never open an account in her name.
- **Kraken** (`kraken-api`): Not used. Same posture as Binance.

#### Home, Travel & Local Life

- **Google Maps** (`google-maps-api`): Routing, restaurant pins, the running-route library along the Cultural Trail.
- **Yelp** (`yelp-api`): Pre-screening restaurants for the Sylvie group and for low-noise rooms her Crohn's prefers.
- **Uber** (`uber-api`): Late-night returns from group dinners. Default to her saved payment, confirm above $250.
- **DoorDash** (`doordash-api`): Soup and bland staples during flares. Save Crohn's-safe orders as favorites.
- **Airbnb** (`airbnb-api`): Weekend trips with Sylvie. Stage searches with kitchen access and quiet neighborhoods, confirm before booking.
- **Instacart** (`instacart-api`): Weekly grocery top-up, especially the cooked-vegetable and rice staples during recovery weeks.
- **Amadeus** (`amadeus-api`): Flights to Columbus and the occasional design conference. Hold options, never purchase without approval.
- **OpenWeather** (`openweather-api`): Run-window check the night before Tuesday and Thursday mornings, and travel-day forecasts.
- **Zillow** (`zillow-api`): Idle browsing on Indianapolis neighborhoods she follows. Read-only, no saved-search alerts in her name.
- **Ring** (`ring-api`): Front-door camera on the Prospect Street condo. Surface unfamiliar visitors, never share footage outside the household.
- **FedEx** (`fedex-api`): Track inbound Humira shipments and outbound Diwali gift boxes to Columbus.
- **UPS** (`ups-api`): Track the alternate carrier for client deliveries to her home address.
- **Shippo** (`shippo-api`): Label generation if she ever resells a piece of design furniture. Confirm address and rates before printing.

#### Culture, Entertainment & Reading

- **Spotify** (`spotify-api`): Lo-fi while working, indie rock on runs, the Bollywood playlist she shares with Nathan. Read playlists, never auto-add tracks.
- **YouTube** (`youtube-api`): Design talks, cooking demos, the occasional Pixar short. Save links, never auto-play in shared sessions.
- **Vimeo** (`vimeo-api`): Higher-quality design-talk archive. Same posture as YouTube.
- **TMDB** (`tmdb-api`): Movie and TV metadata for the running list she shares with Sylvie. Read-only.
- **Twitch** (`twitch-api`): Observer access to Nathan's occasional streams so she can text him good clips.
- **Ticketmaster** (`ticketmaster-api`): Indie shows at the Vogue and Old National Centre. Stage holds, confirm before purchase.
- **Eventbrite** (`eventbrite-api`): Local design meetups and Diwali community events. Stage RSVPs, confirm before committing.
- **OpenLibrary** (`openlibrary-api`): Reading-list lookups, especially for design and behavioral-psychology titles.
- **NASA** (`nasa-api`): Image-of-the-day she occasionally pulls for a presentation opener. Low usage, high delight.
- **Reddit** (`reddit-api`): Lurker on r/userexperience and r/crohnsdisease. Read-only, no posting in her name.
- **Twitter** (`twitter-api`): Quiet account, mostly a design-leader follow list. Read-only.
- **LinkedIn** (`linkedin-api`): Active but measured. Read messages, draft replies, never post or connect without approval.
- **Instagram** (`instagram-api`): Personal and small. Family photos, Sylvie pictures, occasional cooking. Draft posts, never publish.
- **Pinterest** (`pinterest-api`): Boards for kitchen renovation ideas she keeps idling. Read-only.
- **Google Classroom** (`google-classroom-api`): Adjacent to a mentorship program she occasionally guest-teaches. Read announcements only.

#### Commerce & Marketplaces

- **Amazon Seller** (`amazon-seller-api`): Not active for her personally, but the fintech client's marketplace touches it. Read product feed, no listings.
- **Etsy** (`etsy-api`): Occasional gifts for Sylvie and her mother. Stage orders, confirm before purchase.
- **BigCommerce** (`bigcommerce-api`): One client's storefront. Read product catalogs to inform navigation redesigns.
- **WooCommerce** (`woocommerce-api`): Alternate client storefront. Same read-only research posture as BigCommerce.

#### HR & Operations

- **BambooHR** (`bamboohr-api`): Meridian uses BambooHR. Read her own time-off balance, never edit another employee's record.
- **Greenhouse** (`greenhouse-api`): Meridian's hiring pipeline. Read-only on the senior-designer pipeline she occasionally interviews for.
- **Gusto** (`gusto-api`): Paystubs and benefits. Read her own records for the monthly finance review, never adjust withholdings without approval.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. The agent works only from connected mock APIs and stored memory.
- Meridian UX Group internal systems (work Slack, work email at apatel@meridianuxgroup.com, work Figma, work Notion, work Drive) live on the work laptop and are not connected.
- Banking apps (Ally checking and savings, Vanguard Roth IRA, Chase Sapphire Preferred) are phone-only and not connected.
- Medical patient portals (MyChart for Dr. Iyer, Fountain Square Family Practice portal for Dr. Marsh, Mass Ave Dental portal for Dr. Ross) are phone-only and not connected.
- Sylvie's accounts, calendar, and devices are not connected and never should be.
- Parents' devices and accounts are not connected.
