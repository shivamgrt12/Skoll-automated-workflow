# Tools: Sophia Rivera

## Tool Usage

### Connected Services

#### Messaging, Email & Calls

- **Gmail** (`gmail-api`): Primary inbox at sophia.rivera@Finthesiss.ai. Doctor offices, Elena, Medicare correspondence, the credit union.
- **Outlook** (`outlook-api`): Mirrors the Albuquerque VA Medical Center's appointment reminders so veteran-benefit notices land separately from the Gmail clutter. Elena set this up after a VA letter got buried.
- **Microsoft Teams** (`microsoft-teams-api`): Elena's medical equipment company runs on Teams; three-way calls between Sophia, Elena, and Marco about care decisions happen here on a link Elena pastes.
- **Slack** (`slack-api`): Marco's HVAC company maintains a #family-photos channel where he posts Denver job-site shots; the agent surfaces new photos for Sophia.
- **Discord** (`discord-api`): Max's youth soccer team coordinates practice changes and game cancellations in a Discord server. Elena pulls schedule updates so Sophia knows when Max's weekend visit may shift.
- **WhatsApp** (`whatsapp-api`): Marco sends photos from Denver through WhatsApp; the agent pulls new messages and images for Sophia.
- **Telegram** (`telegram-api`): Bobby's cousin in Juarez routes the extended Rivera holiday photo thread through Telegram. The agent surfaces new photos during holiday seasons.
- **Twilio** (`twilio-api`): Sends her morning and evening medication SMS reminders to her Samsung.
- **SendGrid** (`sendgrid-api`): Handles outbound mail transit when you draft something for Elena to print and mail.
- **Mailgun** (`mailgun-api`): Carries transactional email from Rio Grande Credit Union and Farmers when she requests a paper statement copy or policy summary by mail.
- **Zoom** (`zoom-api`): Dr. Sorensen's cardiology practice offers Zoom telehealth for between-visit medication check-ins. Sophia accepts when winter weather makes the drive into Santa Fe unsafe.

#### Calendar & Scheduling

- **Google Calendar** (`google-calendar-api`): The medical and family calendar. Appointments, family visits, Mass, Marco's Sunday call, monthly bill day.
- **Calendly** (`calendly-api`): Dr. Park's endocrinology office routes new-patient and follow-up booking through Calendly; Elena books Sophia's quarterly A1C check slots here.
- **DocuSign** (`docusign-api`): Carries Medicare coverage forms, the annual Medigap renewal signature, and the VA enrollment update she signed in 2024.

#### Family Coordination, Files & School

- **Google Drive** (`google-drive-api`): Elena keeps shared documents here. Medication list, scanned medical records, household checklist.
- **Dropbox** (`dropbox-api`): Holds the shared Rivera family photo archive. The agent pulls new uploads from Marco and finds old photos when Father Herrera asks for one for a memorial.
- **Box** (`box-api`): Stores the scanned 1974 diesel mechanics certificate, Bobby's VA service records, and the original deed to the County Road 31 property, the documents Elena wanted in a separate vault from everyday paperwork.
- **Notion** (`notion-api`): Elena built a shared "Mom" page tracking medications, providers, allergies, and emergency contacts. The agent pulls current records from it when coordinating care.
- **Obsidian** (`obsidian-api`): Holds the property maintenance log Elena keeps: roof age, well pump service dates, septic inspection schedule. The agent surfaces upcoming service dates from it.
- **Airtable** (`airtable-api`): Tracks Sophia's medication refill cadence against her grocery runs to Kaune's, so refills line up with trips into town. Elena maintains it.
- **Google Classroom** (`google-classroom-api`): Pulls Lily's and Max's assignment streams so Sophia can follow what they are working on.

#### Health & Fitness

- **MyFitnessPal** (`myfitnesspal-api`): Dr. Park's office pushes weekly carb-log summaries here; the agent surfaces them for Sophia ahead of endocrinology visits.
- **Strava** (`strava-api`): Elena saved Sophia's fence-line walking loop here. The agent reads distance and pace estimates from it when Sophia mentions her knees acted up on the morning walk.

#### Money, Banking & Bills

- **Plaid** (`plaid-api`): Links to her Rio Grande Credit Union checking and savings. The agent checks balances and coordinates bill-paying with Elena.
- **QuickBooks** (`quickbooks-api`): Holds the small ledger Elena set up tracking the Mesa Verde pension, Social Security deposits, and the property maintenance fund in one view, surfacing it for the annual tax conversation.
- **Xero** (`xero-api`): Mirror of the QuickBooks ledger available when Elena's accountant friend needs Xero format for end-of-year filing.
- **Stripe** (`stripe-api`): Receives payments when a neighbor pays for a welding favor; the payment routes into her credit union account.
- **Square** (`square-api`): Father Herrera's parish runs the Sunday collection's envelope-replacement program through Square; her monthly tithe goes through this rail.
- **PayPal** (`paypal-api`): Receives money transfers from relatives. Marco sends this way when a check is too slow.
- **Alpaca** (`alpaca-api`): Bobby left a small brokerage account from his Mesa Verde profit-sharing years; the agent monitors the holdings at an Alpaca-connected custodian and surfaces balance changes.
- **Coinbase** (`coinbase-api`): Marco bought her $50 of Bitcoin in 2021; the agent monitors the Coinbase wallet Elena holds the keys to and reports balance shifts.
- **Binance** (`binance-api`): Backup balance-check path for the crypto wallet when Coinbase rate-limits.
- **Kraken** (`kraken-api`): Third balance-check path for the crypto wallet when Coinbase and Binance are unavailable.

#### Local Errands, Weather, Maps & Deliveries

- **Google Maps** (`google-maps-api`): Directions to the clinics, to Elena's in Albuquerque, to Mass when the back road is closed.
- **OpenWeather** (`openweather-api`): Daily forecast check at 5:30. She wants the truth, not the cheerful version.
- **Yelp** (`yelp-api`): Looks up Santa Fe restaurants and shops when Sophia or Rosa want a new place to try.
- **Instacart** (`instacart-api`): Elena schedules Instacart Kaune's pickups for the weeks she cannot drive up; Sophia retrieves the bags from the store herself.
- **DoorDash** (`doordash-api`): When Sophia's knees rule out cooking and Elena is in Albuquerque, Elena orders La Paloma posole delivered to the property.
- **FedEx** (`fedex-api`): Tracking incoming packages. Elena's Amazon orders mostly land via this.
- **UPS** (`ups-api`): Tracking incoming alongside FedEx. The two carriers split her rural delivery between them.
- **Shippo** (`shippo-api`): Handles outbound shipping when Sophia sends a gift to Marco or returns a part.

#### Travel & Events

- **Uber** (`uber-api`): Pre-arranged for rides home from any procedure that requires sedation; Elena set it up after Sophia's 2023 cardiac stress test left her stranded in the parking lot.
- **Airbnb** (`airbnb-api`): Elena books a Santa Fe rental when family visits run more than two adults. Sophia's single guest room cannot hold Marco and Elena's family together.
- **Amadeus** (`amadeus-api`): Pulls Marco's Denver-to-Albuquerque flight times when he visits, so Sophia knows when to expect the call from the airport.
- **Eventbrite** (`eventbrite-api`): Pulls Veterans Day events and Santa Fe County fair listings for Sophia.
- **Ticketmaster** (`ticketmaster-api`): Pulls Albuquerque Isotopes schedules when Max wants a game.

#### Shopping & Marketplace

- **Amazon Seller** (`amazon-seller-api`): Elena maintains a small Amazon seller account listing surplus shop hardware, hand tools, and leftover welding stock Sophia decides to part with. The connector surfaces order status when a piece sells.
- **Etsy** (`etsy-api`): Where Elena buys the hand-stitched flannel shirts Sophia wears through winter; the seller is Lily's friend's mother in Taos.
- **BigCommerce** (`bigcommerce-api`): Santa Fe Hardware's online price list runs on BigCommerce; Sophia uses the agent to check welder rod and grinder disc prices before driving in.
- **WooCommerce** (`woocommerce-api`): Kaune's weekly produce list lives on a WooCommerce site; she checks Hatch chile availability in late summer.
- **Pinterest** (`pinterest-api`): Elena pins carb-conscious New Mexican recipes she plans to cook on visits; the agent surfaces new pins for Sophia to review.

#### Home & Property

- **Ring** (`ring-api`): Driveway motion-sensor camera Elena installed in 2024 after a coyote pack came through; Sophia checks the clip log when Luna barks at night.
- **Zillow** (`zillow-api`): Pulls property comparables and market data when the roof replacement estimates start coming in.

#### Reading, Music, News & Leisure

- **OpenLibrary** (`openlibrary-api`): Looking up Western novels, military history, and the next Dale Rustad release.
- **Spotify** (`spotify-api`): Elena loaded the Linda Ronstadt, Selena, and Vicente Fernández playlists onto Sophia's phone; she plays them on the drive to Albuquerque when AM reception fades through the canyons.
- **YouTube** (`youtube-api`): Serves nature documentary clips and old Vicente Fernandez performances when Sophia wants to hear one again.
- **Vimeo** (`vimeo-api`): The VFW post archives Veterans Day ceremony footage to Vimeo; Sophia watches past ceremonies when she cannot attend in person.
- **Twitch** (`twitch-api`): Max streams his backyard soccer scrimmages to a private Twitch link; the agent surfaces new streams for Sophia.
- **TMDB** (`tmdb-api`): Looking up baseball broadcast schedules and the nature documentary lineups she follows.
- **Reddit** (`reddit-api`): Pulls threads from r/Diesel and r/MechanicAdvice when a neighbor brings Sophia a problem on a make or model she has not turned a wrench on in twenty years.
- **NASA** (`nasa-api`): Sky and weather references. She likes knowing when the next meteor shower is, even if she does not stay up for it.

#### Social

- **Instagram** (`instagram-api`): Surfaces new posts from Lily's art account so Sophia can see drawings without maintaining her own profile.
- **Twitter** (`twitter-api`): Pulls alerts from the Santa Fe County Sheriff and NM Fire Info feeds during fire season for Sophia.
- **LinkedIn** (`linkedin-api`): Mesa Verde's alumni page posts retiree milestones and obituaries; the agent surfaces updates so Sophia knows who is still around.

#### Developer & Business Tooling

- **Linear** (`linear-api`): Marco's HVAC dispatch team logs jobs in Linear; he shares a job link when he is routing through Santa Fe and might stop by on the way back to Denver.
- **Jira** (`jira-api`): Mesa Verde's equipment maintenance history was migrated to Jira; she pulls a record when a neighbor's machine matches one she serviced decades ago.
- **Trello** (`trello-api`): Elena's shared property maintenance board lives here: roof, well, fence, gate. The agent tracks card updates and surfaces pending tasks.
- **Asana** (`asana-api`): Father Herrera's parish events team uses Asana; she gets a task when she has signed up to bring posole for the Veterans Day breakfast.
- **Monday** (`monday-api`): Elena's medical equipment company tracks Sophia's CGM trial supplies and hearing-aid battery deliveries here; the agent reads ETAs from it.
- **Confluence** (`confluence-api`): Mesa Verde's archived equipment manuals live in a Confluence space retirees can read; she searches it when she forgets a torque spec on an old loader.
- **HubSpot** (`hubspot-api`): Rio Grande Credit Union uses HubSpot for member outreach; her annual relationship review and CD renewal nudges surface from it.
- **Salesforce** (`salesforce-api`): Desert View Medical Clinic runs patient outreach through Salesforce; preventive-care reminders and flu-shot prompts land via it.
- **Zendesk** (`zendesk-api`): Verizon support tickets when her Samsung refuses to update. Elena opens these on her behalf.
- **Intercom** (`intercom-api`): Phonak's hearing-aid support chat runs in Intercom; she uses it when the right aid stops syncing with her phone.
- **ServiceNow** (`servicenow-api`): The Albuquerque VA Medical Center's internal ticketing system; Elena opens tickets here for veterans' benefits questions Sophia raises.
- **Freshdesk** (`freshdesk-api`): Mutual of Santa Fe's homeowner-claims desk routes through Freshdesk; the agent files claims and tracks status when property damage occurs.
- **GitHub** (`github-api`): Marco published an HVAC load-calculation tool as an open repo; she follows the release notes when he asks her to test something.
- **GitLab** (`gitlab-api`): Mesa Verde's IT team mirrored the legacy timesheet tool to GitLab; she still uses it to look up an old pay period when a pension question comes up.
- **Sentry** (`sentry-api`): Surfaces uptime alerts on Elena's shared family photo archive; the agent flags issues so Elena can restore the upload service.
- **Datadog** (`datadog-api`): Monitors the personal AI agent's own uptime so the system reports honestly when something fails to respond.
- **Okta** (`okta-api`): Elena set up Okta to centralize Sophia's many medical-portal logins behind one Google sign-in.
- **Cloudflare** (`cloudflare-api`): Mesa Verde's alumni newsletter site sits behind Cloudflare; the connector handles the access challenge when she clicks through from an email.
- **Kubernetes** (`kubernetes-api`): Lily's school district runs its parent portal on a Kubernetes cluster; the agent navigates maintenance windows to pull grade updates for Sophia.
- **PagerDuty** (`pagerduty-api`): Rio Grande Credit Union uses PagerDuty to alert its fraud team; the agent monitors for debit card flags and notifies Sophia when action is needed.
- **Contentful** (`contentful-api`): Desert View Medical Clinic's patient education library runs on Contentful; Dr. Castillo's office links to "diabetes in cold weather" articles she reads.
- **Algolia** (`algolia-api`): Powers the search box on the New Mexico VA benefits site; she leans on it when hunting for a specific policy clause.
- **Segment** (`segment-api`): Elena's medical equipment company pipes supplier telemetry through Segment; the agent surfaces reorder timing for Sophia's CGM supplies and hearing-aid batteries.
- **Amplitude** (`amplitude-api`): The credit union's mobile app uses Amplitude; the agent pulls recent account activity for the balance reviews Elena runs on the kitchen tablet.
- **PostHog** (`posthog-api`): Marco's HVAC scheduling tool uses PostHog; when he asks Sophia to test a workflow, the agent logs the click trace for his review.
- **Mixpanel** (`mixpanel-api`): Mesa Verde's alumni site uses Mixpanel; the agent tracks newsletter engagement and surfaces retiree updates for Sophia.
- **Google Analytics** (`google-analytics-api`): The parish website uses Google Analytics; the agent confirms service times and event schedules from it.
- **BambooHR** (`bamboohr-api`): Mesa Verde's HR keeps her archived employment record here, with original hire date, role changes, and retirement paperwork accessible to retirees on request.
- **Greenhouse** (`greenhouse-api`): Mesa Verde routes diesel-mechanic referral requests to retirees through Greenhouse; Sophia flags candidates through the system when she knows someone fit for the work.
- **Gusto** (`gusto-api`): Her Mesa Verde pension runs through Gusto's payroll backend; the monthly deposit summaries and the annual 1099-R appear here.
- **Mailchimp** (`mailchimp-api`): The VFW post and Our Lady of Guadalupe parish both send their newsletters through Mailchimp; she reads them in Gmail.
- **Klaviyo** (`klaviyo-api`): Santa Fe Hardware sends specialty-tool announcements through Klaviyo; she opens these when a new welder or grinder model is announced.
- **ActiveCampaign** (`activecampaign-api`): Mesa Verde's alumni outreach team uses ActiveCampaign; the annual retiree picnic invitation arrives via it.
- **Typeform** (`typeform-api`): Dr. Castillo's office uses Typeform for pre-visit symptom intakes; she fills them out at the kitchen table the morning of an appointment.
- **Webflow** (`webflow-api`): The parish website runs on Webflow; the agent pulls Mass and confession times from it.
- **WordPress** (`wordpress-api`): The Sangre de Cristo Veterans Coalition blog runs on WordPress; she reads memorial posts when a veteran she served alongside passes.
- **Figma** (`figma-api`): Lily shares school art project boards through Figma; Sophia opens them and lets Lily walk her through the work.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. The agent works only from connected services and stored memory.
- **Rio Grande Credit Union** account access for bill-paying. Handled in person at the branch, or by Elena from her laptop.
- **VA patient portal**. Accessed by Elena on her laptop when she helps Sophia with veterans' healthcare paperwork.
- **Pharmacy app**. Prescriptions handled by phone call to the local pharmacy.
- **Medical portals** (Desert View, Southwest Heart, Rio Grande Endocrine, Santa Fe Family Dental, Desert Sky Eye). Actual booking and chart access happens by phone or through Elena.
