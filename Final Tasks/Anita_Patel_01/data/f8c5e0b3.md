# Cardinal MyCare Portal — Redesign Engagement Brief (internal, Meridian UX Group)

**Client (anonymized):** Cardinal Health Partners
**Product:** Cardinal MyCare patient portal (web + iOS + Android)
**Engagement lead:** Anita Patel · **Manager:** Lila Fontaine · **Research:** Cass Leung · **Design:** Raj Mehta, Tanya Brooks
**Quarter:** Q3 2026 (reporting month for the review: **September 2026**)
**Do not circulate externally. Client name is anonymized in all deliverables.**

## Why we're here
Cardinal engaged Meridian to reduce drop-off in the six core patient journeys and prep a redesign. Q3 is the first full quarter with the new event instrumentation, so the review is as much about *trusting the numbers* as about the design.

## The six core journeys (what "done" means for each)
| Journey | Success event | Known pain |
|---|---|---|
| appointment_booking | slot confirmed (server API 200) | slot list fails to load on mobile; slot-race on confirm |
| message_your_provider | message_sent | HEIC photo attachments fail silently |
| prescription_refills | refill submitted + confirmed | confirmation event sometimes not emitted |
| results_viewing | result opened | large PDFs blank on iOS webview |
| bill_pay | payment authorized | Sep 12–18 payment incident (tokenization/gateway) |
| onboarding_first_run | identity verified + first login | IDV provider timeouts |

## Instrumentation history (matters for the readout)
- **Segment tracking plan v2.4 shipped 2026-09-14.** It changed `booking_completed` to fire on the server confirmation (API 200) instead of the confirmation *pageview*, and renamed `mvp_message_sent` → `message_sent`. Any apparent September "lift" in booking completion is partly this definition change, not real improvement. **Amplitude (user_id based) is our source of truth; GA4 over-counts.**
- Tools in play: GA4, Mixpanel, Amplitude, PostHog (partial sample), Segment (plan), Datadog (perf), Sentry (errors), Zendesk + Intercom (support), Algolia (in-portal search).

## Redesign hypotheses going into the review
1. Fixing the slot-selection race + mobile slot-load is the single highest-reach win (booking is the biggest funnel).
2. Bill-pay conversion will recover on its own post-incident; separate the incident dip from structural friction.
3. Onboarding identity-verify needs a fallback path (phone verify) surfaced in-product.

## Guardrails
- All external deliverables anonymize the client and strip patient identifiers.
- Health, finance, and personal (Sylvie) context never appears in client or team materials.
