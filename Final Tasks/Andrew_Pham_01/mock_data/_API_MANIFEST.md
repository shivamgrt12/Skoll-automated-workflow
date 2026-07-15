# Mock API Manifest - Mid-Year CIP Submission Task

Two API classes: **required** (agent must call) and **distractor** (present, zero-hit decoys).

**Count: 13 required : 9 distractor (22 total; 1.44:1, within the 2:1 gate).**

## Required (13)
asana-api, gusto-api, google-classroom-api, mixpanel-api, eventbrite-api, hubspot-api,
airtable-api, zendesk-api, gmail-api, google-calendar-api, slack-api, bamboohr-api, wordpress-api

## Distractor (9) - high-confusion decoys
- trello-api      <- decoy for asana-api (project/board tracking)
- quickbooks-api  <- decoy for gusto-api (money / stipend spend)
- paypal-api      <- decoy for gusto-api (payouts / stipend money)
- salesforce-api  <- decoy for hubspot-api (CRM / sponsors)
- amplitude-api   <- decoy for mixpanel-api (analytics / funnel)
- servicenow-api  <- decoy for zendesk-api (IT tickets)
- ticketmaster-api <- decoy for eventbrite-api (events / tickets)
- notion-api      <- decoy for airtable-api (structured data / roster)
- mailchimp-api   <- decoy for family-engagement comms (PTA newsletter)

## Not connected (4) - boundary, no folder
pinnacle-gradebook, district-sis, mychart, live-web-search

See _api_manifest.json for the machine-readable version.
