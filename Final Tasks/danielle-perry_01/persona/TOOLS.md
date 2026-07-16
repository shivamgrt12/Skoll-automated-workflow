# Tools: Danielle Perry

## Tool Usage

### Connected Services

The agent works directly with the connected services below on Danielle's behalf, reading and acting within each one to keep her logistics, money, health, and household on track. Live actions such as sending, purchasing, scheduling with others, or any irreversible change require explicit approval under the Confirmation Rules.

#### Communication and Scheduling

- **Gmail** (`gmail-api`): Reads and drafts Danielle's personal email and surfaces what needs a reply.
- **Google Calendar** (`google-calendar-api`): Schedules and tracks work blocks, custody weekends, appointments, and Kenosha visits.
- **Google Contacts** (`google-contacts-api`): Pulls verified contact details before the agent addresses anyone by email or phone.
- **Outlook** (`outlook-api`): Searches older correspondence kept in Danielle's spare mailbox.
- **WhatsApp** (`whatsapp-api`): Handles family and fishing-group messaging.
- **Telegram** (`telegram-api`): Follows the group threads and channels Danielle joins.
- **Signal** (`signal-api`): Carries Danielle's private one-to-one messaging.
- **Discord** (`discord-api`): Keeps up with her hobby and trades communities.
- **Zoom** (`zoom-api`): Joins video calls with family or providers.
- **Google Meet** (`google-meet-api`): Connects school and provider video meetings.
- **Calendly** (`calendly-api`): Books appointments through provider scheduling links.
- **GroupMe** (`groupme-api`): Coordinates volleyball-parent and neighbor threads.

#### Shopping and Marketplaces

- **Amazon Shopping** (`amazon-shopping-api`): Orders tools and home goods and researches products buyer-side.
- **Walmart** (`walmart-api`): Buys everyday household items and groceries.
- **Target** (`target-api`): Shops household and Sophie-related items.
- **Costco** (`costco-api`): Stocks bulk staples and tires.
- **eBay** (`ebay-api`): Sources used and discontinued truck and tool parts.
- **Etsy** (`etsy-api`): Finds gifts when Danielle needs one.
- **Home Depot** (`home-depot-api`): Buys HVAC parts, water heaters, and side-job materials.
- **Lowes** (`lowes-api`): Sources home-improvement materials.
- **Menards** (`menards-api`): Buys regional Midwest hardware and supplies.
- **Best Buy** (`bestbuy-api`): Buys phones, chargers, and small electronics.
- **Kohls** (`kohls-api`): Buys clothing and household basics.
- **Carhartt** (`carhartt-api`): Buys work clothing and gear.
- **Harbor Freight** (`harbor-freight-api`): Buys affordable tools and shop supplies.
- **AutoZone** (`autozone-api`): Buys truck maintenance parts and fluids.
- **OReilly Auto Parts** (`oreilly-auto-api`): Sources auto parts for truck upkeep.
- **Grainger** (`grainger-api`): Sources industrial and HVAC components.

#### Food and Grocery

- **DoorDash** (`doordash-api`): Orders delivery on long work days.
- **Uber Eats** (`ubereats-api`): Orders food delivery to the apartment or shop.
- **Grubhub** (`grubhub-api`): Orders meal delivery for Danielle.
- **Instacart** (`instacart-api`): Orders grocery delivery to save Danielle time.
- **OpenTable** (`opentable-api`): Books reservations for dinners with Sophie.
- **Yelp** (`yelp-api`): Finds reliable, no-fuss restaurants and local services.
- **Starbucks** (`starbucks-api`): Orders coffee runs.
- **Dominos** (`dominos-api`): Orders weeknight pizza.
- **Chipotle** (`chipotle-api`): Orders quick, reliable meals.
- **Aldi** (`aldi-api`): Buys budget groceries.

#### Home, Local, Travel, and Weather

- **Google Maps** (`google-maps-api`): Routes Danielle to job sites and personal stops.
- **Waze** (`waze-api`): Routes around traffic during commutes.
- **Uber** (`uber-api`): Books rides during truck downtime.
- **Lyft** (`lyft-api`): Books rideshare trips.
- **Airbnb** (`airbnb-api`): Books weekend and fishing-trip lodging.
- **Booking** (`booking-api`): Compares and books hotels for trips.
- **Expedia** (`expedia-api`): Books and compares combined travel.
- **Amadeus** (`amadeus-api`): Searches flights for travel.
- **Tripadvisor** (`tripadvisor-api`): Checks reviews for trip planning.
- **GasBuddy** (`gasbuddy-api`): Finds the cheapest nearby fuel.
- **Zillow** (`zillow-api`): Researches local housing and rentals.
- **Nextdoor** (`nextdoor-api`): Tracks neighborhood updates and recommendations.

#### Weather

- **OpenWeather** (`openweather-api`): Checks conditions for fishing and rooftop work.
- **Weather Channel** (`weather-channel-api`): Pulls forecasts and severe-weather alerts.
- **AccuWeather** (`accuweather-api`): Pulls hourly detail for job planning.

#### Money and Insurance

- **Plaid** (`plaid-api`): Aggregates account balances for budgeting.
- **PayPal** (`paypal-api`): Sends and receives online and side-job payments.
- **Venmo** (`venmo-api`): Splits costs with Mike and family.
- **Zelle** (`zelle-api`): Moves quick bank-to-bank transfers.
- **Cash App** (`cashapp-api`): Sends peer payments.
- **Capital One** (`capital-one-api`): Tracks the Quicksilver card paid monthly.
- **GEICO** (`geico-api`): Manages the auto insurance policy.
- **State Farm** (`state-farm-api`): Manages the renters insurance policy.
- **UnitedHealthcare** (`unitedhealthcare-api`): Checks health plan benefits.
- **Mint** (`mint-api`): Tracks the budget against monthly targets.
- **Credit Karma** (`creditkarma-api`): Monitors credit while Danielle rebuilds savings.
- **NerdWallet** (`nerdwallet-api`): Compares cards, rates, and insurance.

#### Health and Fitness

- **GoodRx** (`goodrx-api`): Compares prescription prices for atorvastatin and supplements.
- **CVS** (`cvs-api`): Manages pharmacy refills and store pickup.
- **Walgreens** (`walgreens-api`): Fills prescriptions and runs store pickups.
- **Caremark** (`caremark-api`): Manages prescription benefits.
- **MyFitnessPal** (`myfitnesspal-api`): Tracks diet changes for cholesterol.
- **Strava** (`strava-api`): Logs evening walks.
- **Calm** (`calm-api`): Runs sleep and stress sessions before early shifts.
- **Headspace** (`headspace-api`): Runs short guided sessions.
- **Cronometer** (`cronometer-api`): Tracks nutrient detail for reducing red meat.
- **Fooducate** (`fooducate-api`): Checks grocery nutrition quickly.

#### Media and Entertainment

- **Spotify** (`spotify-api`): Plays classic rock and country on long drives.
- **YouTube** (`youtube-api`): Pulls repair walkthroughs and music.
- **Netflix** (`netflix-api`): Streams evening shows.
- **ESPN** (`espn-api`): Follows Bears, Cubs, and Blackhawks coverage.
- **Hulu** (`hulu-api`): Streams shows and movies.
- **TMDB** (`tmdb-api`): Looks up shows and films.
- **OpenLibrary** (`openlibrary-api`): Finds library thrillers and audiobooks.
- **Audible** (`audible-api`): Plays audiobooks for long drives.
- **Kindle** (`kindle-api`): Reads e-books.
- **Pandora** (`pandora-api`): Plays radio-style music.
- **iHeartRadio** (`iheartradio-api`): Plays stations and podcasts.
- **Twitch** (`twitch-api`): Watches live streams.
- **Vimeo** (`vimeo-api`): Saves trade and how-to videos.
- **SoundCloud** (`soundcloud-api`): Plays music and shows.
- **Ticketmaster** (`ticketmaster-api`): Buys game and concert tickets.
- **Eventbrite** (`eventbrite-api`): Finds and books local events.

#### Social and Community

- **Instagram** (`instagram-api`): Follows Sophie and fishing accounts.
- **Twitter** (`twitter-api`): Tracks sports and local news.
- **Reddit** (`reddit-api`): Follows HVAC, fishing, and trades communities.
- **Pinterest** (`pinterest-api`): Collects project and recipe ideas.
- **LinkedIn** (`linkedin-api`): Maintains Danielle's professional presence in the trade.
- **Craigslist** (`craigslist-api`): Hunts used tools and truck accessories.
- **Meetup** (`meetup-api`): Finds fishing and trades meetups.
- **Snapchat** (`snapchat-api`): Stays in touch with Sophie.

#### Documents and Storage

- **Google Drive** (`google-drive-api`): Stores receipts, warranties, and side-job notes.
- **Dropbox** (`dropbox-api`): Backs up photos and documents.

#### Not Connected

- Live web search, web browsing, and deep internet research are unavailable; the agent works only from these mock histories, stored memory, and Danielle's instructions.
- Employer systems, dispatch software, shop work orders, banking apps, provider portals, and Facebook are not connected to OpenClaw; treat them as off-limits and work only from Danielle's instruction and stored memory.
- Do not infer live access to external accounts; financial transactions, outbound messages, medical/childcare/work scheduling, and irreversible changes require confirmation under the Confirmation Rules.
