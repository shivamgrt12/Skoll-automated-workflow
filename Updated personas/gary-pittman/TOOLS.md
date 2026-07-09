# Tools: Gary Pittman

## Tool Usage

### Connected Services

#### Communication & Email

- **Gmail** (`gmail-api`): Primary email at gary.pittman@Finthesiss.ai. Drafts replies to Pastor Sorenson, Karen, and the Avera medical offices; sends only after Gary's explicit approval.
- **WhatsApp** (`whatsapp-api`): Family group chat with Karen, Jeff, Nate, and Emma. Surfaces unread photos and grandkid updates so Gary can react in the morning over coffee.
- **Twilio** (`twilio-api`): Receives appointment reminder SMS from Avera St. Luke's and Aberdeen Family Dentistry and pushes them onto Gary's Google Calendar the night before.
- **SendGrid** (`sendgrid-api`): Sends Bethlehem Lutheran's weekly congregation newsletter on Friday morning after Gary proofs the Wednesday draft Barb hands off.
- **Telegram** (`telegram-api`): Aberdeen veterans memorial event logistics chat. Gary RSVPs and confirms his chair-setup and sound-equipment assignment for the November and May observances.
- **Microsoft Teams** (`microsoft-teams-api`): Avera St. Luke's patient channel where Dr. Strand's nurse posts pulmonary results and prescription updates. Gary opens, reads, and acknowledges receipt.
- **Outlook** (`outlook-api`): Aberdeen School District retirement portal account that receives the monthly pension statement and the annual 1099-R. Both archive automatically into the Karen-shared Drive folder.
- **Mailgun** (`mailgun-api`): Routes the automated appointment confirmation emails from Avera into Gary's primary inbox with a single "Avera" label so nothing slips by.
- **Intercom** (`intercom-api`): Avera St. Luke's patient-portal chat where Gary asks the nurse line about prescription refills and receives a same-day reply.

#### Calendar, Scheduling & Video

- **Google Calendar** (`google-calendar-api`): Primary calendar that drives every reminder Gary actually sees. Holds church work days, doctor appointments, grandkids' birthdays, and Karen's visits.
- **Calendly** (`calendly-api`): Books Dr. Strand and Avera pulmonology follow-ups without a phone call; confirmation lands in Google Calendar within the minute.
- **Zoom** (`zoom-api`): Joins the family video call Karen hosts on the third Sunday of every Oct-March month so Gary can see Nate and Emma face to face.
- **Eventbrite** (`eventbrite-api`): RSVPs to Aberdeen Capitol Theatre concerts and to local veterans memorial events Gary plans to attend or help set up.

#### Health & Fitness

- **MyFitnessPal** (`myfitnesspal-api`): Logs Gary's daily walk minutes; Karen reviews the weekly trend from Sioux Falls and texts him when the count slips below the COPD walking target.
- **Strava** (`strava-api`): Auto-records Gary's afternoon neighborhood walks. Karen receives a weekly kudos summary, which gives them something to mention on the phone call.

#### Home, Weather & Property

- **Ring** (`ring-api`): Front door video doorbell Karen installed in 2024. Gary checks the live feed when he hears the porch creak and gets motion alerts pushed to the Galaxy A14 day and night.
- **Zillow** (`zillow-api`): Watches the four nearest South Kline Street comps and pings Gary when one lists or sells; useful for the every-five-year homeowners insurance reassessment.
- **OpenWeather** (`openweather-api`): Drives Gary's 5:30 AM "go outside today or not" decision. Triggers a COPD warning whenever AQI or windchill crosses the threshold Dr. Agard set.
- **Google Maps** (`google-maps-api`): Routes the Sioux Falls runs to Karen's house and the Bismarck drives to Jeff's. Flags road closures on US-281 before Gary leaves the driveway.
- **Yelp** (`yelp-api`): Confirms hardware-store and pharmacy hours before Gary makes the drive across town; pulls reviews when the Silverado needs a body shop he hasn't used.
- **Freshdesk** (`freshdesk-api`): Files Consumer Cellular support tickets when the Galaxy A14 reception drops. Karen is cc'd so she can follow up if Gary loses patience.
- **Trello** (`trello-api`): Karen's shared seasonal home maintenance board. Gary checks off the storm window swap, furnace filter change, and gutter clear each fall; Karen sees the green check from Sioux Falls.
- **Kubernetes** (`kubernetes-api`): Runs the small basement home server Roger built. Gary opens the dashboard once a week to confirm the Nest thermostat and Ring camera are both reporting in.
- **Sentry** (`sentry-api`): Pushes a text to Gary the moment the Nest thermostat or Ring camera throws an error. The alert is the only reason Gary knows the basement server needs Roger's attention.
- **Datadog** (`datadog-api`): Forwards a daily uptime digest for the home server to Karen so she can call Roger if anything dropped during the night.

#### Shopping & Delivery

- **Amazon Seller** (`amazon-seller-api`): Karen runs a small listing account that moves surplus tools and Marlene's old craft supplies out of the basement. Gary approves each listing photo and picks the pickup window.
- **Etsy** (`etsy-api`): Karen places the order for the hand-painted memorial garden stake Gary chooses each year for Marlene's perennial bed; Gary signs off on the design before checkout.
- **Instacart** (`instacart-api`): On bad-weather Saturdays Gary places a Kessler's grocery order instead of driving the Silverado on glare ice. Checkout requires his approval at the $50 threshold.
- **DoorDash** (`doordash-api`): Used on the rare blizzard morning when Gary can't make it to the Koffee Kup. Orders the same breakfast Dale would have ordered for him.
- **WooCommerce** (`woocommerce-api`): Bethlehem Lutheran's Christmas bazaar shop. Gary updates inventory after the Saturday setup and marks items sold as Barb runs the till.
- **BigCommerce** (`bigcommerce-api`): Aberdeen Central alumni merchandise store. Gary reorders the maintenance staff polos he still wears at the church each November.
- **Klaviyo** (`klaviyo-api`): Runnings' sale list. Lawn-and-garden alerts route to Gary's inbox; lumber alerts route to a folder Roger checks before any Sioux Falls visit.

#### Finance & Payments

- **QuickBooks** (`quickbooks-api`): Bethlehem Lutheran's books. Gary keys in maintenance invoices the day they land so Barb's month-end close is clean.
- **Stripe** (`stripe-api`): Processes Gary's monthly tithe to Bethlehem Lutheran automatically on the 1st. Failure alert routes to his phone.
- **Plaid** (`plaid-api`): Connects Dacotah Bank to Gary's calendar reminders and triggers a balance-low warning if checking dips under $1,000 before pension day.
- **Coinbase** (`coinbase-api`): Holds the small Bitcoin position Jeff gifted at Christmas 2022. Pushes a price alert any time the position moves more than 15%, which usually prompts a check-in call with Jeff.
- **Square** (`square-api`): Card reader for Bethlehem Lutheran bake sales and pie auctions Gary helps set up. Gary closes out the reader at the end of each event and emails the totals to Barb.
- **PayPal** (`paypal-api`): Sends the handyman invoices Gary charges neighbors for leaky-faucet and storm-window jobs. Invoices issue only after Gary approves each one.
- **Alpaca** (`alpaca-api`): Holds the standing watchlist Karen set up of the three companies the Aberdeen district pension fund is most exposed to; the weekly summary helps Gary understand his quarterly pension statement.
- **DocuSign** (`docusign-api`): Routes Bethlehem Lutheran vendor contracts (snow removal, HVAC service) to Gary's phone for the church-custodian signature.
- **Gusto** (`gusto-api`): Bethlehem Lutheran's payroll. Gary pulls his bi-weekly pay stub and his W-2 each January.
- **Xero** (`xero-api`): The church's accounting ledger. Gary pulls the maintenance expense report the morning of each building committee meeting.
- **Binance** (`binance-api`): Mirrors the Coinbase position so Jeff and Gary can compare price feeds when they talk. Karen set a $50-move alert that pages both phones.
- **Kraken** (`kraken-api`): Source of the monthly digest email Gary actually reads about Jeff's gifted holdings. The headline number is what father and son discuss on the call.

#### Church Operations & Staff

- **Slack** (`slack-api`): Bethlehem Lutheran staff channel. Gary posts a "boiler check done" or "lobby waxed" message at the end of each work morning and acknowledges Pastor Sorenson's Friday update.
- **Jira** (`jira-api`): Church maintenance ticket board. Barb logs the request, Gary picks it up, moves it to in-progress, and closes it when the work is finished.
- **PagerDuty** (`pagerduty-api`): On-call rotation for the church building. Gary is primary for boiler, pipe, and electrical alarms; the page goes straight to the Galaxy A14 with a distinct ring.
- **Notion** (`notion-api`): Bethlehem Lutheran's shared planning workspace. Gary updates the building hours page and the weekly maintenance log Barb cites in council reports.
- **Zendesk** (`zendesk-api`): Bethlehem Lutheran's congregation-facing helpdesk for facility requests. Gary triages overnight tickets each Monday morning before opening the building.
- **Monday** (`monday-api`): Tracks the multi-week renovation projects (basement classroom refresh, sanctuary lighting upgrade) Gary leads on the building committee.
- **Airtable** (`airtable-api`): Holds the church potluck signup, the volunteer roster, and the funeral-reception coordination table. Gary updates the volunteer column after each shift.
- **Linear** (`linear-api`): The building committee's priority queue. Gary tags items he plans to handle himself and reassigns the rest to the contractor list.
- **Asana** (`asana-api`): Aberdeen veterans memorial event task board for the November Veterans Day observance. Gary owns the equipment-haul and chair-setup subtasks.
- **Okta** (`okta-api`): Bethlehem Lutheran single sign-on. Gary uses it daily for the church management portal, the shared staff inbox, and the building security panel.
- **BambooHR** (`bamboohr-api`): Bethlehem Lutheran's HR portal. Gary submits his bi-weekly timesheet and any PTO request through it.
- **ServiceNow** (`servicenow-api`): Aberdeen School District retirement support portal. Gary opens a ticket if his monthly pension statement is late; the auto-response confirms a 2-day SLA.

#### Church Communications, Website & Analytics

- **HubSpot** (`hubspot-api`): The congregation outreach list. Gary tags new visitors after Sunday service so Pastor Sorenson's follow-up postcards mail out on Monday.
- **Salesforce** (`salesforce-api`): The church stewardship database. Gary pulls giving history when the annual stewardship dinner needs RSVPs targeted to active givers.
- **Mailchimp** (`mailchimp-api`): Sends the weekly church newsletter. Gary clicks send on Friday morning after Barb finalizes the layout.
- **ActiveCampaign** (`activecampaign-api`): Drives the seasonal email automations (Advent service times, Lent volunteer calls). Gary toggles each campaign live the Sunday before the season begins.
- **Typeform** (`typeform-api`): Hosts the congregation feedback survey Pastor Sorenson runs each November. Gary reads the building-comfort responses (heat, lighting) and acts on the maintenance-relevant ones.
- **Greenhouse** (`greenhouse-api`): Aberdeen School District substitute custodian listings. Gary forwards openings to two former colleagues he still mentors and submits the referral form.
- **WordPress** (`wordpress-api`): Bethlehem Lutheran's website. Gary updates the building hours and the snow-cancellation banner himself; the Friday push lands at 8 AM.
- **Contentful** (`contentful-api`): Drives the church lobby's digital signage. Gary updates the welcome screen and the event slides every Monday morning before the building opens.
- **Webflow** (`webflow-api`): The church website's design layer. Gary reviews and approves Barb's layout changes before they ship to the live WordPress install.
- **Cloudflare** (`cloudflare-api`): The church website's hosting and DNS account. Gary purges the cache after each Friday push and acknowledges the weekly security report.
- **Google Analytics** (`google-analytics-api`): Pushes a weekly visitor summary for the church website to Gary's inbox; he forwards anything notable to Barb for the council deck.
- **Figma** (`figma-api`): The shared design file for the church bulletin and event posters. Gary leaves comments on legibility from a senior-eyes perspective before Barb prints.
- **Segment** (`segment-api`): Routes the church website's event-page visits into the outreach dashboard Barb runs each month. Gary subscribes to the weekly digest.
- **Amplitude** (`amplitude-api`): Tracks usage of Bethlehem Lutheran's mobile app. Gary pulls the monthly active-user count Pastor Sorenson cites at the council meeting.
- **PostHog** (`posthog-api`): The church event registration funnel. Gary watches the drop-off chart before each season's volunteer drive launches.
- **Mixpanel** (`mixpanel-api`): Tracks engagement with the sermon recording page on the church website. Gary pulls the top-10 sermons list for Pastor Sorenson's quarterly review.

#### Family, Education & Entertainment

- **YouTube** (`youtube-api`): Subscriptions to plumbing and lawn-equipment repair channels; saves Gary at least one hardware-store trip a month.
- **Spotify** (`spotify-api`): Plays the Merle Haggard and Johnny Cash playlist Karen made for the garage. The "Hymns for Sunday Morning" playlist autoplays on the kitchen speaker at 8:45 AM.
- **Instagram** (`instagram-api`): Notification-only follow of Karen's and Roger's accounts so Gary sees Nate and Emma photos within the hour they post.
- **Pinterest** (`pinterest-api`): Karen pins garden layout and casserole ideas to a shared board. Gary marks the ones he wants to try with a thumbs-up so Karen knows to bring the recipe.
- **Discord** (`discord-api`): Nate's gaming server. Gary posts a "good game" after each tournament weekend so Nate knows he was watching.
- **TMDB** (`tmdb-api`): Provides the nightly broadcast TV schedule that Gary's phone shows on the kitchen counter at 6:30 PM each evening.
- **Twitch** (`twitch-api`): Follow on Nate's stream channel. Gary gets a push notification when Nate goes live so he can drop in for the first few minutes.
- **LinkedIn** (`linkedin-api`): Sends Gary a digest when Karen or Jeff post a career update; gives him something specific to ask about on the next call.
- **Vimeo** (`vimeo-api`): Hosts Bethlehem Lutheran's recorded Sunday sermons. Gary forwards the link to homebound members Mavis and Harold each Monday morning.
- **Ticketmaster** (`ticketmaster-api`): Books the seats Gary buys for the Aberdeen Capitol Theatre concerts he and Karen attend each November.
- **Google Classroom** (`google-classroom-api`): Karen shares Nate and Emma's class feeds. Gary gets notified when an assignment is graded so he can text a "proud of you" to Nate before bed.
- **GitHub** (`github-api`): Follow on Nate's school robotics repo. Gary gets a weekly digest of commits so he can ask Nate what he fixed that week at family dinner.
- **GitLab** (`gitlab-api`): Mirrors Nate's classroom programming workspace. Gary uses the activity feed to know which days Nate had assignments due.

#### Knowledge, Reference & Documents

- **Google Drive** (`google-drive-api`): Family folder Karen and Gary share. Holds scanned medical records, Marlene's estate documents, and the house insurance binder. Gary uploads scans from the church scanner each Friday.
- **Dropbox** (`dropbox-api`): Bethlehem Lutheran's shared maintenance folder. Gary uploads vendor-quote photos, repair receipts, and before/after pictures the same day the work happens.
- **Box** (`box-api`): Aberdeen School District retirement-document vault. Gary pulls pension statements, his 38-year service record, and his W-2s for tax season.
- **Obsidian** (`obsidian-api`): Karen-configured vault for Gary's home maintenance log and Marlene's garden journal. Gary opens it weekly to add notes; Karen syncs and reads.
- **Confluence** (`confluence-api`): Bethlehem Lutheran operations wiki. Gary updates the boiler procedure page after each annual inspection so the next person inherits clean notes.
- **OpenLibrary** (`openlibrary-api`): Places library holds at Aberdeen Public for Louis L'Amour and Clive Cussler novels; pings Gary when the hold is ready for pickup.
- **NASA** (`nasa-api`): Provides the satellite imagery overlay Gary uses on severe-weather days and pushes severe-storm alerts directly to the Galaxy A14.
- **Algolia** (`algolia-api`): Powers search on Bethlehem Lutheran's resource site. Gary uses it to pull the right bulletin or vendor quote from three years of archives in under a minute.
- **Reddit** (`reddit-api`): Subscribed to r/gardening and r/homeimprovement; the weekly top-of-subreddit digest lands in Gary's inbox Sunday evening.
- **Twitter** (`twitter-api`): Push notifications from Aberdeen American News and the National Weather Service Aberdeen office, and nothing else.

#### Travel & Shipping

- **Uber** (`uber-api`): Booked when the Silverado is at Bohl's Auto for service. Gary's account uses Karen's payment card as backup at the $50 confirmation threshold.
- **Airbnb** (`airbnb-api`): Books spare lodging when Karen's family overflows the bungalow during Christmas week, or when Gary drives to Bismarck to visit Jeff.
- **Amadeus** (`amadeus-api`): Compares flight prices when Karen books Gary on a one-off plane trip to Bismarck instead of the long winter drive. Final booking goes through Karen's account.
- **FedEx** (`fedex-api`): Tracks the care packages Karen sends from Sioux Falls and the special-order parts Gary buys for the church boiler service.
- **UPS** (`ups-api`): Tracks Runnings online orders and the prescription deliveries Avera mails when the in-person pickup window doesn't work.
- **Shippo** (`shippo-api`): Generates the labels for the Christmas care packages Gary sends to Jeff in Bismarck and to Tyler at Jeff's house.

#### Not Connected

- Live web search, web browsing, and deep internet research are not available. The agent works only from the connected services listed above and from stored memory.
- Banking transactions at Dacotah Bank (deposits, withdrawals, transfers) are handled in person at the Main Street branch or by phone, not through any connected service.
- No streaming video subscriptions (no Netflix, Disney+, Hulu, HBO Max, or Apple TV+) and no social media beyond what is listed above.
- Marlene's old desktop computer has not been powered on since December 2023 and is not connected.
