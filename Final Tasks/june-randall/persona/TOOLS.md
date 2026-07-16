# Tools: June Marie Randall

## Tool Usage

### Connected Services

#### Communication and Messaging

- **Gmail** (`gmail-api`): Personal inbox at `june.randall@gmail.com` for family, church, and committee mail. Draft and hold for review; never send without her explicit approval.
- **Outlook** (`outlook-api`): Manage occasional Outlook invites from external partners; accept or decline after June confirms, and mirror them into Google Calendar.
- **WhatsApp** (`whatsapp-api`): Family threads with Lauren in Chicago and Karen in Richmond. Tone stays warm and short; confirm before any new thread.
- **Telegram** (`telegram-api`): Relay messages with community organizers who insist on Telegram; draft replies and send after June confirms the wording.
- **Discord** (`discord-api`): Marcus's pre-med study servers; post June's encouragement and share study resources when he asks her to weigh in.
- **Twilio** (`twilio-api`): SMS routing for committee reminders to Loretta Simms and the hospitality team. Confirm before any group send.
- **Zoom** (`zoom-api`): Church committee video calls and CEU webinars. Add to Google Calendar with dial-in details included.
- **Microsoft Teams** (`microsoft-teams-api`): External calls with Lauren's freelance clients; schedule and join invited meetings and post follow-up notes for Lauren.
- **Slack** (`slack-api`): Church volunteer workspace Pastor David set up; post hospitality updates and coordinate volunteers in the committee channels.
- **SendGrid** (`sendgrid-api`): Backend for hospitality committee bulk email when Mailchimp is too heavy. Draft and hold for approval.
- **Mailgun** (`mailgun-api`): Backup transactional sender for committee RSVPs. Same approval rule as SendGrid.

#### Calendar, Files and Workspace

- **Google Calendar** (`google-calendar-api`): Source of truth for clinic shifts, family time, and Sunday church. Cross-reference before suggesting any time slot.
- **Google Drive** (`google-drive-api`): Church committee documents, family planning files, and personal records. Read and append; never reorganize.
- **Notion** (`notion-api`): Lightweight workspace for the women's prayer group reading plan. Edit notes June owns; leave shared pages alone.
- **Obsidian** (`obsidian-api`): Local notes vault for CEU study and patient-teaching scripts (no patient identifiers). Append only.
- **Airtable** (`airtable-api`): Hospitality committee event roster and RSVP base. Update statuses; flag anything that touches money.
- **Trello** (`trello-api`): Mother's Day reception planning board with Loretta Simms. Move cards; never delete them.
- **Asana** (`asana-api`): Cross-committee task tracker for the community health fair; assign hospitality tasks and update June's deliverables as they progress.
- **Monday** (`monday-api`): Sister Karen's school staff board; sync Dorothy-related appointment dates into Google Calendar and post confirmations for Karen.
- **Dropbox** (`dropbox-api`): Old folder where Samuel keeps household receipts and warranties. Search; never restructure.
- **Box** (`box-api`): Secure folder Dr. Hartwell shares for clinic-wide policy memos (not patient records); file acknowledgements and upload June's signed sign-offs.
- **DocuSign** (`docusign-api`): Notarized forms for Dorothy's care planning documents. Prepare; never sign on June's behalf.
- **Calendly** (`calendly-api`): Public booking link for church members who want fifteen minutes with the hospitality committee. Approve windows weekly with June.
- **Confluence** (`confluence-api`): Clinic-adjacent training wikis; draft and update CEU study summaries June owns, never touching patient pages.
- **Algolia** (`algolia-api`): Search index behind the New Covenant Methodist website. Use to find old event copy when planning anniversary content.
- **Contentful** (`contentful-api`): Headless CMS for New Covenant Methodist's site. Draft content for hospitality events; never publish directly.
- **Typeform** (`typeform-api`): RSVPs for committee receptions and the community health fair signup. Build forms, share links, and route results into Airtable.

#### Health, Fitness and Wellbeing

- **MyFitnessPal** (`myfitnesspal-api`): Loose log of morning walks and sodium awareness for the borderline blood pressure Dr. Banks is monitoring. Track patterns; never lecture or add pressure.
- **Strava** (`strava-api`): Quiet follow on Samuel's weekend walks. Use to coordinate a shared route when he suggests one, not for competition.

#### Family Logistics, Schools and Local Services

- **Ring** (`ring-api`): Front porch camera at the Woodlawn house. Surface delivery notifications; confirm before forwarding package alerts to family members.
- **Zillow** (`zillow-api`): Track small Richmond homes near Karen for Dorothy; maintain saved searches and send June a weekly shortlist of new matches.
- **Instacart** (`instacart-api`): Weekly grocery delivery when clinic runs late. Confirm orders before checkout per the spending threshold rule.
- **DoorDash** (`doordash-api`): Rare weeknight dinner delivery when June gets home past 7:00 PM. Confirm before placing any order.
- **Yelp** (`yelp-api`): Vetting Baltimore restaurants for committee lunches and birthday outings. Filter for quiet rooms and private dining.
- **Google Maps** (`google-maps-api`): Routes to Community Care in Park Heights, Richmond visits, and church events. Add traffic buffer for Sunday mornings.
- **OpenWeather** (`openweather-api`): Weather for her 6:00 AM walks and outdoor events like the community health fair. Flag rain risk early so planning can shift.
- **Uber** (`uber-api`): Backup ride for Brianna after debate practice when Samuel is at work. Confirm pickup details before booking.
- **Google Classroom** (`google-classroom-api`): Brianna's Westbrook Academy assignments; sync due dates into Google Calendar and draft teacher messages for June's review before sending.

#### Church, Community and Events

- **Eventbrite** (`eventbrite-api`): Public registrations for New Covenant Methodist's community health fair and seasonal events. Track headcount and send reminders with Loretta's sign-off.
- **Ticketmaster** (`ticketmaster-api`): Gospel concert tickets and occasional family outing purchases. Confirm price before any purchase.
- **Mailchimp** (`mailchimp-api`): Hospitality committee newsletter to roughly two hundred church members. Draft and route to Loretta; never send unreviewed.
- **WordPress** (`wordpress-api`): New Covenant Methodist's main website. Draft event pages; never publish without Pastor David's sign-off.
- **Pinterest** (`pinterest-api`): Reception centerpieces, table settings, and family recipes for committee planning. Save boards; share only with Loretta.
- **ActiveCampaign** (`activecampaign-api`): Backup nurture sequence for prayer group follow-ups when Mailchimp segments get noisy. Draft only; hold for approval.

#### Finance, Banking and Commerce

- **QuickBooks** (`quickbooks-api`): Hospitality committee books for receipts and reimbursements. Categorize entries; never approve disbursements without committee sign-off.
- **Stripe** (`stripe-api`): Church online giving processor; reconcile weekly payouts against the committee books and send the treasurer an anomaly summary.
- **Plaid** (`plaid-api`): Sync Fidelity HYSA and Chase balances into the household budget sheet weekly and update spending categories; no transfers, ever.
- **Coinbase** (`coinbase-api`): Run a weekly fraud-watch sweep and send June a summary of any sign-ins or activity touching the family account.
- **Square** (`square-api`): Card reader the committee uses at the annual bake sale. Reconcile receipts after each event.
- **PayPal** (`paypal-api`): Family transfers to Lauren in Chicago and Karen in Richmond as an alternative to bank transfer. Confirm every send before it goes.
- **Alpaca** (`alpaca-api`): Export account statements and send Samuel a plain monthly summary of any balances or activity he asks June to check.
- **Xero** (`xero-api`): Migrate the prior chair's legacy committee ledgers into QuickBooks and reconcile the totals each quarter.
- **Binance** (`binance-api`): Run monthly sign-in audits and send June a fraud-watch report on any access attempts.
- **Kraken** (`kraken-api`): Run the same monthly sign-in audit as Binance and send June a fraud-watch report.
- **Amazon Seller** (`amazon-seller-api`): Lauren's freelance art-print store; pull weekly sales totals and send June a short "how are sales going" digest without prying into finances.
- **Etsy** (`etsy-api`): Lauren's illustration prints shop; pull and roll up weekly sales into the same digest June sends about Lauren's stores.
- **BigCommerce** (`bigcommerce-api`): The church's online store for cookbooks and branded items. Pull weekly sales totals for the committee report.
- **WooCommerce** (`woocommerce-api`): Backup church storefront kept after a migration; archive old orders and reconcile leftover inventory into the committee report quarterly.
- **Shippo** (`shippo-api`): Shipping labels for committee packages and cookbook orders. Confirm carrier and cost before printing any label.
- **FedEx** (`fedex-api`): Tracking for documents sent to Dorothy's care team in Richmond and gifts to Lauren and Marcus.
- **UPS** (`ups-api`): Tracking for everyday household packages including Brianna's school supplies. Surface delivery windows proactively.

#### Travel

- **Airbnb** (`airbnb-api`): Searching a quiet weekend rental in Cape May for the couples trip Samuel keeps proposing. Save shortlists; never book without explicit approval.
- **Amadeus** (`amadeus-api`): Flight and rail options for the August Richmond visit to Dorothy. Compare options; do not purchase anything.

#### Media, Reading and Family Interests

- **YouTube** (`youtube-api`): Gospel playlists for the kitchen and CEU lecture queues. Build playlists; do not autoplay during clinic hours.
- **Spotify** (`spotify-api`): CeCe Winans and classic soul rotation for Sunday morning and dinner playlists. Curate; do not share externally.
- **TMDB** (`tmdb-api`): Classic movie lookups for Friday family movie night. Surface runtimes so the evening ends at a reasonable hour.
- **Reddit** (`reddit-api`): Curate a weekly chronic-disease-management digest from NP forums into Obsidian; strip identifiers and draft any reply for June's review.
- **Twitter** (`twitter-api`): Compile a weekly digest of local Baltimore news and gospel-artist updates; draft any post for June's review before sending.
- **Twitch** (`twitch-api`): Sync Marcus's pre-med study-stream schedule into Google Calendar and send June a reminder when he flags one.
- **Vimeo** (`vimeo-api`): Mirrors of Lauren's portfolio reels. Pull shareable links when June asks for one to send.
- **NASA** (`nasa-api`): Photo of the day lookups June sometimes shares with Brianna over breakfast as a small shared ritual.
- **OpenLibrary** (`openlibrary-api`): Catalog lookups for the women's book study including current titles. Surface availability and discussion notes.
- **Instagram** (`instagram-api`): Compile a weekly highlights digest of Brianna's public posts and Lauren's design feed for June; draft any comment for review before posting.

#### Marketing, Analytics and Engagement

- **HubSpot** (`hubspot-api`): Light CRM for the hospitality committee; manage the donor and volunteer list and log interaction notes; no campaign sends without Loretta's approval.
- **Salesforce** (`salesforce-api`): Sync service-day registrations on the regional Methodist conference instance and update attendee records for the committee.
- **Google Analytics** (`google-analytics-api`): Church website traffic around event pages. Pull weekly numbers for committee reports during fair season.
- **Mixpanel** (`mixpanel-api`): Pull the online-giving funnel weekly and build a drop-off summary for the treasurer; no experiments or config changes.
- **Klaviyo** (`klaviyo-api`): Alternate hospitality newsletter platform; sync subscriber segments from Mailchimp monthly so it stays ready for Loretta to send.
- **Segment** (`segment-api`): Export the church site's routed event data weekly into the committee analytics report; the volunteer engineer owns the configuration.
- **Amplitude** (`amplitude-api`): Pull signup-funnel numbers weekly during fair season and add them to the committee report; no configuration changes.
- **PostHog** (`posthog-api`): Export church-site engagement metrics into the committee report each week; the volunteer team owns settings and feature flags.

#### Workplace, Developer and Career Systems

- **GitHub** (`github-api`): Track releases on Marcus's study scripts and Lauren's design templates; pull new versions and send June a change digest.
- **GitLab** (`gitlab-api`): Church website repository mirror; pull the change log before event launches and post a plain summary for the committee.
- **Linear** (`linear-api`): Lauren's freelance task board; sync milestone dates into Google Calendar and send June a weekly progress digest.
- **Jira** (`jira-api`): Sister Karen's school district ticket queue; track Dorothy-related approval timelines and send June reminders as dates firm up.
- **Sentry** (`sentry-api`): Church-site error feed the volunteer engineer shares; pull spike reports around event launches and send the engineer a heads-up summary.
- **Datadog** (`datadog-api`): Church-site uptime dashboard; pull a status check before each fair and send the committee a go/no-go confirmation.
- **Okta** (`okta-api`): Church staff-tools SSO directory; reconcile the volunteer roster against access requests monthly and send the admin a cleanup list.
- **Cloudflare** (`cloudflare-api`): Church-site DNS and cache layer; pull a weekly health report and send the volunteer admin a refresh request before big events.
- **Kubernetes** (`kubernetes-api`): Church website's hosting cluster; pull deployment-status reports before event launches and send the committee an uptime summary.
- **PagerDuty** (`pagerduty-api`): Sync the volunteer engineer's on-call window into June's calendar around major events and send the committee the contact-of-record before each one.
- **ServiceNow** (`servicenow-api`): Methodist conference IT request system. Submit requests after Loretta confirms the exact wording.
- **BambooHR** (`bamboohr-api`): Pull Samuel's forwarded benefits entries into the household-planning sheet and send him an enrollment-deadline reminder.
- **Greenhouse** (`greenhouse-api`): Log full-time design openings Lauren applies to into a shared sheet and update each application's status as it changes.
- **Gusto** (`gusto-api`): Payroll portal for the part-time church bookkeeper; reconcile each pay cycle's entries against committee records; never approve runs.
- **LinkedIn** (`linkedin-api`): Build and update a networking contact list for Marcus's med-school research; draft any outreach for June's review before sending.
- **Figma** (`figma-api`): Lauren's shared design files. Comment only when Lauren explicitly invites feedback on a specific file.
- **Webflow** (`webflow-api`): Lauren's client sites; post June's review comments and stage draft edits Lauren can publish, never publishing directly.

#### Customer Service and Support

- **Zendesk** (`zendesk-api`): Helpdesk for the church cookbook BigCommerce store. Triage incoming tickets; never process refunds without committee approval.
- **Intercom** (`intercom-api`): Member chat on the New Covenant Methodist site during event launches; answer incoming questions with approved templated replies and escalate the rest.
- **Freshdesk** (`freshdesk-api`): Backup support inbox for the hospitality committee. Same triage-only rules as Zendesk.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. Work only from connected mock APIs and stored memory.
- Work email (`jrandall@communitycarehealth.org`) is not connected and must never be drafted into or referenced.
- The Community Care Health Center EHR system is not integrated. Patient records and identifiers must never be accessed or referenced under any circumstances.
- The direct banking apps for Fidelity and Chase, and any Zelle activity, are not connected. The only access to these accounts is Plaid's balance aggregation (see Connected), which performs no transactions of any kind.
- Brianna's personal social accounts and direct messaging are not connected, even via family-plan visibility.
- Dorothy's and Karen's personal devices and accounts are not connected. Contact only through channels and times June specifies.
- Samuel's personal email and his work systems at Crestfield Power Systems are not connected.
