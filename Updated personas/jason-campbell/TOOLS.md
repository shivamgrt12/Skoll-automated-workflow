# Tools: Jason Campbell

## Tool Usage

### Connected Services

#### Email and Communication

- **Gmail** (`gmail-api`): Personal inbox at `jason.campbell@Finthesiss.ai` for research collaborators, hospital admin, family, and vendors. Send when instructed.
- **Outlook** (`outlook-api`): Catches hospital admin invites that arrive in Outlook format; convert them into Google Calendar holds and reply from Gmail.
- **WhatsApp** (`whatsapp-api`): Brother Brian in Dearborn and mother Dorothy. Tone stays warm and short; never auto-reply.
- **Microsoft Teams** (`microsoft-teams-api`): Hosts the external calls with co-PI Dr. Whitfield at Lakewood Medical Research and the Summit Heart Institute team; join, take notes, and post the agreed action items.
- **Slack** (`slack-api`): Private workspace for the TAVR study coordinators. Watch the enrollment and IRB channels and reply only when Jason directs.
- **Discord** (`discord-api`): Kyle's medical student study servers; pull the study-group schedule he flags and fold it into the Sunday call notes.
- **Telegram** (`telegram-api`): Backup channel for an international collaborator who insists on it. Surface messages; never auto-reply.
- **Twilio** (`twilio-api`): SMS reminders to Amanda Torres and the research coordinator team. Confirm before any group send.
- **Zoom** (`zoom-api`): Multi-site TAVR study calls, M&M conference dial-in, and CME webinars. Add to Google Calendar with link details.
- **SendGrid** (`sendgrid-api`): Backend for cardiology fellow program announcements. Draft and hold for approval.
- **Mailgun** (`mailgun-api`): Backup transactional sender for research collaborator outreach. Same approval rule as SendGrid.

#### Calendar, Files and Workspace

- **Google Calendar** (`google-calendar-api`): Source of truth for cath lab, clinic, tennis, research time, and Friday family dinner. Cross-reference before any time slot.
- **Google Drive** (`google-drive-api`): Manuscript drafts, IRB documents, Dorothy's BP log spreadsheet, household planning. Read and append; do not reorganize.
- **Notion** (`notion-api`): Personal workspace for CME tracking and the TAVR enrollment dashboard. Edit pages Jason owns.
- **Obsidian** (`obsidian-api`): Local notes vault for journal reading and Grand Rounds prep, with no patient identifiers. Append only.
- **Airtable** (`airtable-api`): TAVR study enrollment base shared with Amanda Torres. Update statuses; never overwrite source rows.
- **Trello** (`trello-api`): Personal board for Thanksgiving and holiday hosting prep with Karen. Move cards; do not delete.
- **Asana** (`asana-api`): Multi-site project board for the TAVR manuscript task list; update Jason's own tasks and surface blockers before Friday research time.
- **Monday** (`monday-api`): Lakewood Medical Research collaboration board shared by Dr. Whitfield's coordinators; track milestone status and flag slips against the publication clock.
- **Dropbox** (`dropbox-api`): Legacy folder where Karen keeps household warranties and receipts. Search; never restructure.
- **Box** (`box-api`): Secure folder Dr. Hussain shares for practice-wide policy memos. Read carefully; never patient records.
- **DocuSign** (`docusign-api`): IRB and consent administrative forms for the TAVR study. Prepare; never sign on Jason's behalf.
- **Calendly** (`calendly-api`): Public booking link for fellows requesting mentoring time. Approve windows weekly.
- **Confluence** (`confluence-api`): Cardiology fellowship program wiki; pull rotation and curriculum pages for fellow mentoring, never patient pages.
- **Algolia** (`algolia-api`): Search index behind the Coastal Cardiology Partners physician portal. Use to find archived clinical pathways.
- **Contentful** (`contentful-api`): Headless CMS for the practice website. Draft physician bio updates; never publish directly.
- **Typeform** (`typeform-api`): Fellow program intake forms and Grand Rounds attendance signups. Build forms; route results to Google Sheets.

#### Clinical Research and Reference

- **GitHub** (`github-api`): Tracks the TAVR study analysis scripts maintained by the biostatistics core; pull the latest results notebooks for manuscript figures, never commit.
- **GitLab** (`gitlab-api`): Mirror of the biostatistics repository on a partner institution's instance; sync the latest analysis when the primary is unreachable.
- **Linear** (`linear-api`): Internal tracker the research coordinators use for IRB action items; check status and nudge Amanda on items blocking the renewal.
- **Jira** (`jira-api`): Lakewood Medical Research IT queue shared so Jason can see study system access timelines; surface access ETAs before site visits.
- **NASA** (`nasa-api`): Photo of the day lookup Jason shares with Emily over coffee as a small shared ritual.
- **OpenLibrary** (`openlibrary-api`): Catalog lookups for "The Intern's Oath" and other reading list titles. Surface availability and library copies.

#### Health, Fitness and Wellbeing

- **MyFitnessPal** (`myfitnesspal-api`): Loose log of running and brisket Saturdays for self-monitoring. Track patterns; do not lecture.
- **Strava** (`strava-api`): Logs the three-mile St. Johns River loop on Monday, Wednesday, Friday and compares pace with Dr. Hussain's runs.

#### Family Logistics and Local Services

- **Ring** (`ring-api`): Front door and pool deck cameras at the San Jose house. Surface delivery notifications; confirm before forwarding to family.
- **Zillow** (`zillow-api`): Watches small homes near Brian in Dearborn for the long-range family conversation. Keeps saved searches current; never initiates contact.
- **Instacart** (`instacart-api`): Whole Foods delivery from the Beach Boulevard store when the clinic runs late. Confirm before checkout per the spending threshold.
- **DoorDash** (`doordash-api`): Weeknight dinner from Outback when Jason gets home past 7:00 PM. Confirm before ordering.
- **Yelp** (`yelp-api`): Vetting Jacksonville restaurants for fellow dinners and date nights as Orsay alternatives. Filter for quiet rooms.
- **Google Maps** (`google-maps-api`): Routes to Riverside Medical Center, St. Francis, Riverside Racquet Club, and the Jacksonville Heart Conference venue. Add traffic buffer for Mondays.
- **OpenWeather** (`openweather-api`): Weather for 5:15 AM running mornings and Saturday tennis. Flag rain risk before Jason leaves the house.
- **Uber** (`uber-api`): Backup ride for Emily home from Gulf Coast State when Karen cannot drive. Confirm pickup details first.
- **Google Classroom** (`google-classroom-api`): Surfaces Emily's pre-business coursework deadlines when she shares them, so Jason can ask about them on their daily texts. Never messages instructors.

#### Finance, Banking and Commerce

- **QuickBooks** (`quickbooks-api`): Household books and the Coastal Cardiology Partners practice ledger. Categorize entries; never approve distributions without the practice manager.
- **Stripe** (`stripe-api`): Practice patient portal payment processor; reconcile the daily settlements and flag anomalies to the practice manager.
- **Plaid** (`plaid-api`): Aggregates the Marcus savings, Vanguard, and Chase checking accounts into one daily balance view for the monthly budget review. Never moves money.
- **Coinbase** (`coinbase-api`): Holds a small Bitcoin position Jason set up as a gift for Kyle; check it when Kyle asks and flag any login Jason did not make.
- **Square** (`square-api`): Card reader the practice uses at community heart-health events. Reconcile receipts afterward.
- **PayPal** (`paypal-api`): Sends to Kyle for an emergency tuition gap or Brian for restaurant business. Confirm every send.
- **Alpaca** (`alpaca-api`): Holds a small taxable brokerage position Jason opened to learn the platform before guiding the kids; surface a weekly summary and any 3 percent swing.
- **Xero** (`xero-api`): Carries the prior practice administrator's historical books; pull year-over-year comparisons when Tom Richards asks at tax time.
- **Binance** (`binance-api`): Holds a small crypto position split off from Kyle's gift; reconcile the balance quarterly and log any sign-in Jason did not make.
- **Kraken** (`kraken-api`): Mirrors the remaining slice of that small crypto holding; reconcile the quarterly total against the other exchanges and flag unexpected logins.
- **Amazon Seller** (`amazon-seller-api`): Mirrors Brian's Dearborn Bistro merchandise shop so Jason can pull weekly sales totals and ask his brother how the store is doing.
- **Etsy** (`etsy-api`): Tracks Karen's shortlisted hand-thrown pottery shops; surface restocks and price drops before her birthday and the holidays.
- **BigCommerce** (`bigcommerce-api`): The practice's online store for branded heart-health pamphlets. Pull weekly sales totals for admin.
- **WooCommerce** (`woocommerce-api`): Holds the practice's archived storefront order history; pull the past pamphlet order data when admin needs a year-over-year comparison.
- **Shippo** (`shippo-api`): Shipping labels for research samples between sites. Confirm carrier and cost before printing.
- **FedEx** (`fedex-api`): Tracking for IRB documents and gifts to Kyle and Emily in Panama City.
- **UPS** (`ups-api`): Tracking for everyday household packages and Tesla parts. Surface delivery windows proactively.

#### Travel and Conference

- **Airbnb** (`airbnb-api`): Looking at quiet rentals near Panama City for family weekends near the kids. Save shortlists; never book without approval.
- **Amadeus** (`amadeus-api`): Flight options for the Jacksonville Heart Conference and Dearborn family visits. Compare; do not purchase.
- **Ticketmaster** (`ticketmaster-api`): River City Symphony season tickets and family event purchases. Confirm price first.
- **Eventbrite** (`eventbrite-api`): Registration for community heart-health fairs and CME events. Track headcount.

#### Media, Reading and Hobbies

- **YouTube** (`youtube-api`): Cardiology lecture queues for CME and classical piano practice videos. Build playlists; do not autoplay during clinic.
- **Spotify** (`spotify-api`): Chopin, Debussy, Springsteen, Mellencamp, and weekend jazz rotation. Curate; do not share externally.
- **TMDB** (`tmdb-api`): Classic film lookups for Friday family movie night. Surface runtimes so dinner ends on time.
- **Reddit** (`reddit-api`): Interventional cardiology forums for clinical pearls and conference chatter. No identifying details; never post on his behalf.
- **Twitter** (`twitter-api`): Follows cardiology key opinion leaders and ACC accounts for guideline and trial chatter; clip relevant threads to Obsidian, never post as Jason.
- **Twitch** (`twitch-api`): Background awareness of Kyle's USMLE study streams. Surface his schedule when Kyle flags one.
- **Vimeo** (`vimeo-api`): Conference talk recordings and TAVR procedural videos. Pull shareable links when requested.
- **Instagram** (`instagram-api`): Surfaces Emily's public posts and Karen's friends' feeds into a weekly family digest. Never comments as Jason.
- **Pinterest** (`pinterest-api`): Karen's holiday recipe and table-setting boards. Save shared pins only.

#### Marketing, Analytics and Engagement

- **HubSpot** (`hubspot-api`): Light CRM for the practice's referring physician outreach. Notes only; no campaigns without admin approval.
- **Salesforce** (`salesforce-api`): Tracks symposium registrations on a regional cardiology society instance; pull Jason's session assignments and attendee counts.
- **Google Analytics** (`google-analytics-api`): Practice website traffic around appointment requests. Pull weekly numbers for admin.
- **Mixpanel** (`mixpanel-api`): Engagement data on the patient portal signup funnel. Surface drop-offs; never run experiments.
- **Klaviyo** (`klaviyo-api`): Alternate newsletter platform; build the referring-physician send when the office asks and route it for admin review.
- **Segment** (`segment-api`): Data pipe behind the practice website analytics. Document changes; never reconfigure.
- **Amplitude** (`amplitude-api`): Event tracking for the Grand Rounds RSVP funnel. Read funnels during symposium season.
- **PostHog** (`posthog-api`): Self-hosted analytics the practice IT volunteer prefers; read the patient-portal funnels weekly, never change feature flags.
- **Mailchimp** (`mailchimp-api`): Practice newsletter for referring physicians. Draft and route to the admin; never send unreviewed.
- **ActiveCampaign** (`activecampaign-api`): Backup nurture sequence for CME follow-ups. Draft only; hold for approval.
- **WordPress** (`wordpress-api`): Coastal Cardiology Partners physician bios page. Draft updates; never publish without the practice manager.

#### Workplace, Developer and Career Systems

- **BambooHR** (`bamboohr-api`): Opens Karen's CarePlus Pharmacy benefits links when she forwards them, so the family can compare open-enrollment options each fall.
- **Greenhouse** (`greenhouse-api`): Track interventional cardiology fellowship openings Dr. Chen applies to. Mirror updates without commentary.
- **Gusto** (`gusto-api`): Payroll portal for the practice's part-time bookkeeper; review the run summaries for the budget, never approve a run.
- **LinkedIn** (`linkedin-api`): Tracks research-network connections and Kyle's medical school networking; draft connection notes for Jason's review, never message as him.
- **Figma** (`figma-api`): TAVR study poster design files shared by the conference designer. Comment only when invited.
- **Webflow** (`webflow-api`): Practice marketing site preview environment; review staged changes before the practice manager publishes, never publish directly.
- **Sentry** (`sentry-api`): Error feed for the practice patient portal. Surface spikes; do not silence alerts.
- **Datadog** (`datadog-api`): Practice IT volunteer dashboards for patient portal uptime; review the weekly summary and flag sustained degradation.
- **Okta** (`okta-api`): SSO directory for the practice's small tooling stack. Confirm access requests with IT; never approve.
- **Cloudflare** (`cloudflare-api`): DNS and cache layer for the practice site; check propagation after site updates, never purge cache without IT sign-off.
- **Kubernetes** (`kubernetes-api`): Cluster the patient portal runs on, maintained by the IT volunteer; check pod status during a checkout outage and brief the volunteer.
- **PagerDuty** (`pagerduty-api`): On-call schedule shared with practice IT for outage coverage; confirm who holds the pager before reporting a portal issue.
- **ServiceNow** (`servicenow-api`): Riverside Medical Center IT request queue Jason occasionally submits to. Submit after the practice manager confirms wording.

#### Customer Service and Support

- **Zendesk** (`zendesk-api`): Helpdesk for the practice's online education store. Triage tickets; never refund without admin approval.
- **Intercom** (`intercom-api`): Member chat on the patient portal during enrollment campaigns. Watch incoming; respond with templated replies only.
- **Freshdesk** (`freshdesk-api`): Backup support inbox for the practice. Same triage-only rules as Zendesk.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. Work only from the connected services listed above and from stored memory.
- Riverside Medical Center and St. Francis Medical Center electronic health record systems are not connected. Patient records, charts, and identifiers must never be accessed or referenced under any circumstances.
- UpToDate and ACC.org clinical reference logins are not connected, even though Jason uses them daily.
- The ABIM recertification portal and third-party CME tracking providers are not connected.
- Karen's CarePlus Pharmacy work systems are not connected.
- Kyle's medical school and Emily's university student portals are not connected, even via family-plan visibility.
- Personal investment accounts at Vanguard and the hospital 401(k) administrator are not connected.
- Dorothy's MyChart, nephrology portal, and personal devices are not connected. Contact only through channels and times Jason specifies.
