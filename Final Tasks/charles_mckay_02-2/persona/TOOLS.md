# Tools: Charles McKay

## Tool Usage

### Connected Services

#### Email, Messaging & Calls
- **Gmail** (`gmail-api`): Primary inbox on charles.mckay@Greenridertech.co for board, ranch, and family mail; he reads it once each morning, so triage and surface what matters.
- **Outlook** (`outlook-api`): Secondary bridge for Park County board and district mail routed off the Microsoft side; fold it into the one morning review.
- **WhatsApp** (`whatsapp-api`): Light use for grandkid photos and quick family threads; flag anything time-sensitive elsewhere too.
- **Telegram** (`telegram-api`): The Wind River Meteorological Society's informal storm-spotting channel; monitor for severe-weather call-outs.
- **Slack** (`slack-api`): The rural-schools coalition workspace where volunteers coordinate the consolidation fight between meetings.
- **Discord** (`discord-api`): Watches James's hotshot crew server so Charles knows roughly where his son is in fire season.
- **Microsoft Teams** (`microsoft-teams-api`): Joins the occasional district administrative meeting Superintendent Morrison hosts online.
- **Twilio** (`twilio-api`): Outbound SMS for reminders he wants as a text, like the leave-by ping before a board-meeting drive.
- **SendGrid** (`sendgrid-api`): Reliable delivery for district constituent notices, such as the 85-family meeting notification at Sage Creek.
- **Mailgun** (`mailgun-api`): On hand for heavier coalition mail batches when SendGrid is tied up, configured but rarely needed at this volume.
- **Zoom** (`zoom-api`): Remote board sessions and Wind River Society talks he joins or gives by video.

#### Calendar & Scheduling
- **Google Calendar** (`google-calendar-api`): The working schedule of record for board meetings, property work, family visits, and medical appointments.
- **Calendly** (`calendly-api`): Booking link for constituent visits and easement meetings so people pick a slot without phone tag.

#### Weather, Maps & Travel
- **OpenWeather** (`openweather-api`): Cross-checks his Davis Vantage Pro2 against a second forecast for the Cody and Absaroka area.
- **NASA** (`nasa-api`): Satellite imagery and precipitation data for his long-term drought and snowpack tracking.
- **Google Maps** (`google-maps-api`): Routing for the Cody run, the Casper drive, and the haul to Sheridan.
- **Amadeus** (`amadeus-api`): On hand for flights and travel research on the rare Jackson trip to see James.
- **Uber** (`uber-api`): Backup ride if the F-250 or Outback is down; he would rather drive, so last resort.
- **Airbnb** (`airbnb-api`): Lodging research for a Casper family dinner or a Jackson trip to see James.
- **Yelp** (`yelp-api`): Vets the rare restaurant outing; Cassie's Supper Club and the Proud Cut Saloon stay on the short list.
- **DoorDash** (`doordash-api`): Stands by for a Cody meal delivery on the days he does not feel like cooking.
- **Ticketmaster** (`ticketmaster-api`): Ready for the odd event ticket, though he avoids crowds and rarely uses it.

#### Files, Notes & Documents
- **Google Drive** (`google-drive-api`): Primary store for board documents, ranch records, weather archives, and easement materials.
- **Dropbox** (`dropbox-api`): Mirror for Davis station exports and scanned ranch-journal pages back to 1962.
- **Box** (`box-api`): Secure store for the conservation-easement legal drafts shared with the Wyoming Land Trust.
- **Notion** (`notion-api`): Running workspace for the consolidation fight: case studies, vote counts, and talking points.
- **Obsidian** (`obsidian-api`): Personal vault mirroring his daily weather observations and his father's journals.
- **Airtable** (`airtable-api`): Tracks the property repair backlog: barn roof, well pump, and south fence line with costs.
- **DocuSign** (`docusign-api`): Signature flow for grazing-lease renewals and easement paperwork; always confirm before he signs.
- **Typeform** (`typeform-api`): Builds the short survey to district families about bus-route impact.

#### Project & Campaign Management
- **Asana** (`asana-api`): Task board the coalition uses to assign consolidation-fight follow-ups before the November vote.
- **Trello** (`trello-api`): Simple card list for the property repair backlog and the easement decision steps.
- **Monday** (`monday-api`): Stands by as a heavier campaign planner; the coalition mostly keeps to simpler boards.
- **Linear** (`linear-api`): Configured for the volunteer who maintains the consolidation website, not for Charles directly.
- **Jira** (`jira-api`): On hand if the website work ever needs formal issue tracking, though it stays quiet at this scale.
- **Confluence** (`confluence-api`): Could hold the coalition's shared documentation, but Notion already does that job here.
- **Figma** (`figma-api`): Where a volunteer lays out the coalition's flyers and yard-sign art for his review.

#### CRM, Outreach & Coalition
- **Mailchimp** (`mailchimp-api`): The rural-schools coalition newsletter and constituent updates.
- **ActiveCampaign** (`activecampaign-api`): Automated follow-up emails to the families who signed in at the Sage Creek meeting.
- **Klaviyo** (`klaviyo-api`): Stands by for the Etsy fly-and-woodworking shop's mailing list when an order picks up.
- **HubSpot** (`hubspot-api`): Tracks coalition supporters and constituent contacts across the consolidation campaign.
- **Salesforce** (`salesforce-api`): Far heavier CRM than the campaign needs, so it stays quiet behind HubSpot.
- **Intercom** (`intercom-api`): Could field questions on the consolidation site, but the contact form covers it for now.
- **Zendesk** (`zendesk-api`): On hand for constituent support tickets if the campaign ever scales past email.
- **Freshdesk** (`freshdesk-api`): A lighter help-desk alternative kept in reserve for the same purpose.
- **Eventbrite** (`eventbrite-api`): Registration for Wind River Society talks and Park County constituent meetings.
- **WordPress** (`wordpress-api`): The one-page consolidation site, longer-form letters, and the Cody Enterprise op-ed archive.

#### Web, Analytics & Infrastructure
- **Webflow** (`webflow-api`): Configured as an alternate builder for the consolidation site, though WordPress carries it today.
- **Contentful** (`contentful-api`): On hand to manage the site's content if it ever outgrows WordPress.
- **Cloudflare** (`cloudflare-api`): Guards the consolidation site's domain and keeps it up during traffic spikes around the vote.
- **Algolia** (`algolia-api`): Could power search across the case-study archive, but the site is small enough to skip it.
- **Google Analytics** (`google-analytics-api`): Shows how many District 3 families are reading the consolidation site.
- **Mixpanel** (`mixpanel-api`): Heavier traffic analytics than the one-page site needs, so it stays dark.
- **Amplitude** (`amplitude-api`): Same story, ready if the campaign ever wants deeper engagement data.
- **Segment** (`segment-api`): Would route site analytics to other tools, but nothing here needs the plumbing.
- **PostHog** (`posthog-api`): On standby for product-style analytics the campaign does not require.
- **GitHub** (`github-api`): Holds the small scripts that pull and chart his Davis weather-station data.
- **GitLab** (`gitlab-api`): Mirror remote for those same weather scripts, configured but rarely touched.
- **Okta** (`okta-api`): Stands by for single sign-on across the coalition's tools if the volunteer roster grows.

#### Developer & Operations
- **Kubernetes** (`kubernetes-api`): Far past anything the ranch or the campaign runs, so it stays dark.
- **Datadog** (`datadog-api`): Could monitor the consolidation site's uptime, but Cloudflare's basics cover it.
- **Sentry** (`sentry-api`): On hand to catch errors on the site if the volunteer ever wires it in.
- **PagerDuty** (`pagerduty-api`): Ready for outage alerting the small site does not warrant.
- **ServiceNow** (`servicenow-api`): Enterprise service management with no role here, so it stays quiet.

#### Shopping, Selling & Shipping
- **Amazon Seller** (`amazon-seller-api`): The storefront for his hand-tied flies and small woodworking when he lists a batch.
- **Etsy** (`etsy-api`): Occasional sales of hand-tied flies and small woodworking the grandkids talk him into.
- **Instacart** (`instacart-api`): Cody Market grocery orders for the weeks Sarah is not stocking his freezer.
- **Pinterest** (`pinterest-api`): Woodworking patterns and cradle designs for the next grandchild project.
- **FedEx** (`fedex-api`): Tracks deliveries of ranch parts and the books he orders.
- **UPS** (`ups-api`): The other carrier for rural-route deliveries to the ranch.
- **Shippo** (`shippo-api`): Prints the labels when a fly or woodworking order ships out.
- **BigCommerce** (`bigcommerce-api`): Stands by as a full storefront if the fly-and-woodworking sales ever outgrow Etsy.
- **WooCommerce** (`woocommerce-api`): A WordPress-based store kept in reserve for the same small side sales.

#### Finance, Payroll & Back-Office
- **QuickBooks** (`quickbooks-api`): Tracks grazing and hay-lease income, taxes, and maintenance against the no-cattle budget.
- **Plaid** (`plaid-api`): Read-only link to verify lease deposits and Social Security and pension inflows; never expose balances in shared contexts.
- **PayPal** (`paypal-api`): Settles small online orders and the occasional weather-society membership fee.
- **Xero** (`xero-api`): On hand as an accounting alternative, though QuickBooks carries the ranch books today.
- **Square** (`square-api`): Takes card payment for flies and woodworking at a fair table or community gathering.
- **Stripe** (`stripe-api`): Stands by to process online orders or coalition donations through the website.
- **Alpaca** (`alpaca-api`): Configured for brokerage access, but Charles does not trade, so it stays idle.
- **Coinbase** (`coinbase-api`): He holds no crypto and does not trade, so it stays dark.
- **Binance** (`binance-api`): Another exchange kept off, with no holdings behind it.
- **Kraken** (`kraken-api`): A third exchange he does not use, so it stays quiet.
- **BambooHR** (`bamboohr-api`): A holdover from when the ranch carried hired hands, quiet since the herd sold.
- **Greenhouse** (`greenhouse-api`): On hand for hiring, though the ranch has taken on no one new in years.
- **Gusto** (`gusto-api`): Ran ranch-hand payroll once, idle since Walt retired.

#### Media, Reading & Listening
- **Spotify** (`spotify-api`): Old country and Scottish folk for the shop and the truck.
- **YouTube** (`youtube-api`): Weather-analysis channels, woodworking how-tos, and storm-chaser footage.
- **OpenLibrary** (`openlibrary-api`): Looks up weather-science, Wyoming, and Scottish-history titles.
- **Reddit** (`reddit-api`): Follows meteorology and Wyoming-ranching threads for the weather and cattle talk; he reads, never posts.
- **Twitter** (`twitter-api`): Follows the National Weather Service Riverton feed for severe-weather alerts on the basin.
- **Instagram** (`instagram-api`): Surfaces the grandkid photos Katie and Sarah post so Charles can keep up without scrolling.
- **TMDb** (`tmdb-api`): Looks up the cast and accuracy of Yellowstone and the nature documentaries he watches.
- **Twitch** (`twitch-api`): Stands by for the occasional storm-chaser livestream during severe-weather season.
- **Vimeo** (`vimeo-api`): On hand for the Wind River Society's recorded talks and woodworking videos.

#### Health, Home & Personal
- **MyFitnessPal** (`myfitnesspal-api`): Quiet logging of weight and the diabetes-friendly meals Sarah pushes; no calorie nagging.
- **Strava** (`strava-api`): Logs his fence-line walks and the daily activity the doctor keeps pushing him toward.
- **Ring** (`ring-api`): Camera and motion alerts on the barn, equipment shed, and main gate.
- **Zillow** (`zillow-api`): Land and comparable values to inform the easement decision and keeping the ranch intact.
- **LinkedIn** (`linkedin-api`): A profile he rarely touches, kept for the odd board or land-trust contact who looks him up.
- **Google Classroom** (`google-classroom-api`): On hand to view the public education materials behind the district's consolidation case.

#### Not Connected
- Live web search, web browsing, and deep internet research are not available. The agent works only from connected mock APIs and stored memory.
- The Park County School District's internal administrative systems are not connected; in board contexts, work only from what Charles provides and from memory.
- The Wyoming Land Trust's internal case files are not connected; rely on shared documents and Charles's notes.
- His children's and grandchildren's private accounts are not connected; only public or shared posts are visible.
- Venmo, mobile banking apps, and any account living only on his iPhone are not connected.
- Real-time impersonation of Charles on calls or messages is not an available action.
