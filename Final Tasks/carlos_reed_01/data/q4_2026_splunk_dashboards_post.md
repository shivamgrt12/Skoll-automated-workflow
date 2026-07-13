# Splunk Dashboards for Detection Engineering: Cutting the Noise Without Cutting the Signal

Status: draft, awaiting Carlos Reed's approval
Publish Target: December 31, 2026
Author: Carlos Reed
Category: Reed Security Notes, Q4 2026

## Reconciliation

Three candidate drafts of this post were on the table when the reconciliation pass ran on December 22, 2026. The Contentful staged entry carried a modification timestamp of December 21, 2026. The Notion editorial page carried a modification timestamp of December 18, 2026. The WordPress draft slot carried a modification timestamp of December 14, 2026.

- Trusted source: Contentful staged entry (December 21, 2026).
- Set aside: Notion editorial page (December 18, 2026) - three-day drift, missing the revised MITRE mapping section.
- Set aside: WordPress draft slot (December 14, 2026) - one-week drift, missing both the MITRE mapping section and the revised false-positive taxonomy.
- Tie-breaker rule applied: most-recently-modified authoritative source.
- Open finding: the Notion editorial page carried a newer header-image caption than the Contentful entry. Caption copied forward, body text sourced from Contentful.

---

## Why This Post Exists

Every detection engineer I know has too many dashboards and not enough signal. The tooling scales. The attention does not. This post is about the small number of Splunk dashboards that have actually moved my detection posture at Torchwood and in home lab work over the last twelve months, and the failure modes to look for when you build them yourself.

I am not going to tell you which SIEM to buy. I am going to tell you what a dashboard has to earn to keep its screen real estate.

## The Four-Question Filter

Before a dashboard gets built, it answers four questions. If it cannot, it does not ship.

1. What decision does this dashboard drive? If the answer is "situational awareness," kill it. That is not a decision.
2. Who looks at it and when? If the answer is "the whole SOC, sometime," kill it. Dashboards without owners rot.
3. What is the noise floor of this data source? If you do not know, you will spend six months tuning the panel and never trust the number.
4. What is the recovery time if this dashboard is wrong? If a false negative here means a real breach goes cold for forty-eight hours, the panel needs a redundant alerting path and cannot stand alone.

## Dashboard One: Authentication Anomaly by Geo-Velocity

The premise is old and the implementation is where most teams go wrong. Panel one shows failed authentication attempts by user, bucketed into fifteen-minute windows. Panel two shows the geographic delta between successive successful authentications for the same account, computed as great-circle distance divided by elapsed time.

The failure mode almost every team hits: they alert on the delta panel and ignore the failed-attempts panel. Real credential stuffing shows up first as a failed-attempt spike and only later as a successful login from an unexpected geo. Alerting only on the second signal means you catch attackers after they have credentials, not before.

Reed rule: panel one is the primary alert. Panel two is the corroboration. The dashboard shows both because the analyst on-call needs to see the corroboration inside two clicks, not three.

## Dashboard Two: Process Lineage for Living-Off-The-Land Binaries

This one is where the Splunk Common Information Model earns its keep. The panel walks parent-child process trees for a curated list of native binaries (I keep the list to the ones I have actually seen abused in incidents I worked, not the exhaustive published list). It highlights any tree where the parent is Office, a browser, or a mail client, and the descendant is one of the curated binaries.

The failure mode: the list of watched binaries grows every time someone reads a blog post, and the false positive rate creeps up until analysts stop looking at the panel. Prune quarterly. Anything on the list without a corresponding true-positive detection in the last two quarters comes off.

Reed rule: the dashboard has an explicit last-pruned timestamp in the header. If it is over ninety days stale, the dashboard reads red.

## Dashboard Three: Egress Volume by Destination Class

Volumetric anomalies get called cliché until they catch something real. The panel bucks outbound bytes by destination class (cloud storage providers, known SaaS, everything else). It flags spikes in the third bucket by comparing rolling seven-day windows.

The failure mode: analysts alert on absolute volume. Absolute volume tracks business activity. Alert on rate-of-change against the same day-of-week baseline. A month of holiday traffic will teach you why.

Reed rule: no anomaly panel without a seasonality-adjusted baseline. If you cannot compute the baseline in Splunk, precompute it in a summary index and pull from there.

## Dashboard Four: Detection Rule Health

Every detection rule you own has a shelf life. This dashboard tracks per-rule fire rate, per-rule true-positive rate as tagged by the analyst who closed the ticket, and per-rule days-since-last-tuned. It is the single most useful dashboard I have built and the one my colleagues underinvest in the most.

The failure mode: the dashboard exists but nobody looks at it because it is not tied to a review meeting. Tie it to a review meeting.

Reed rule: rules with a true-positive rate under five percent over ninety days go into a quarterly tuning queue. Rules with a fire rate of zero over ninety days go into a retirement queue. Retirement is not deletion. Retirement is a documented shelf.

## What I Did Not Include

I left off dashboards for things I do not personally tune anymore. Threat intel feed hit-rates. DLP category breakdowns. Both of those are dashboards worth having, but the tuning discipline is different and the audience is different, and stuffing them into the same visual layout confuses the on-call analyst.

## Closing

The dashboard is not the detection. The dashboard is the interface to the detection. If the detection engineering underneath is sloppy, no dashboard will save it. If the detection engineering is solid, the dashboard's job is to keep the analyst on the panel that matters and off the panel that flatters.

Next post lands in Q1 2027 and Monica Stevens is running it. Coverage from me resumes June 2027.

---

## Pre-Publish Checklist

- [ ] Search index refresh confirmed against the on-site search surface, target refresh window under fifteen minutes.
- [ ] Landing-page prototype published on the promo surface, redirect from the post CTA validated end-to-end.
- [ ] Error-telemetry baseline captured December 30, 2026 for the twenty-four hours preceding publish. Post-publish error rate to be compared against this baseline in the seventy-two hours following December 31, 2026.
- [ ] Header image sourced from the Contentful December 18, 2026 revision as noted in Reconciliation above.
- [ ] Author bio unchanged from Q3 2026 post.
- [ ] Do not auto-publish. Publish requires Carlos's manual click on December 31, 2026.

## Open Findings

- The Sentry error-tracking baseline currently includes a known false-positive from a plugin update on December 12, 2026. Filter the noise class before comparing post-publish error rate.
- The Algolia index has a stale entry for the Q3 2026 post title that was edited on December 5, 2026. Non-blocking for this publish, flagged for next reindex sweep.
