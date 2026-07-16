# Projet Mobilité Plateau Consultation Methodology (v3)

| Field | Value |
|---|---|
| Version | 3 |
| Author | Ruth Armstrong, Urbaniste principale |
| Reviewer | Jean-François Lavigne, Superviseur planification |
| Publication date | 2026-09-24 |
| Workspace | Service de l urbanisme et de la mobilité, Ville de Montréal |
| Status | Published, current |
| Supersedes | v2 (2026-06-30) |

*This page is the authoritative city side methodology publication for Projet Mobilité Plateau. Any prior draft, personal working note, or team hub reference is superseded by the content below where they disagree.*

## Purpose

This document sets the consultation methodology that will support the final public consultation on 2026-10-15 at the Centre communautaire du Plateau. It defines corridors in scope, corridors out of scope, language access commitments, delivery channels, and the reach weighting method used to produce any published engagement claim. It replaces v2, which carried an earlier scope frame.

## Corridors In Scope

The following corridors sit inside the Projet Mobilité Plateau final consultation frame.

1. Rue Saint Denis. Protected bike lane segment along the commercial spine of the Plateau. Delivery access design is a material subquestion inside the consultation.
2. Boulevard Saint Laurent nord corridor. Pedestrian priority zone review with integrated transit access. Reach adequacy on this corridor is monitored separately because early delivery signal suggests thinner reach on the non official language cohorts.
3. Avenue du Mont Royal. Transit stop redesign focused on accessibility, boarding time, and shelter placement.
4. Rue Rachel. Extension of the existing bike corridor eastbound, with intersection treatment at the Papineau boundary.

## Corridors Out of Scope

The following item was in earlier scope framing and has been removed from the final consultation scope.

1. Rue Saint Joseph pilot. Removed from final consultation scope at the cross departmental methodology review on 2026-09-24. Deferred to a separate feasibility track that will run outside the Mobilité Plateau cycle. Any input already gathered on this corridor is retained in the response body but is tagged for the feasibility file and is not weighted into the final consultation modal split.

The removal was recorded jointly by the Service de l urbanisme et de la mobilité, the Service de la mobilité active, and the arrondissement Plateau Mont Royal. The reviewer of record is Jean François Lavigne.

## Language Access

Consultation materials, portal content, translated summaries, and interpretation support are provided in the following cohorts.

- French. Primary language of the borough and the primary language of official publication.
- English. Second official language, co equal weight in delivery.
- Bengali. Cohort concentrated on segments of Rue Saint Laurent nord and Mile End.
- Urdu. Cohort concentrated on segments of Rue Saint Laurent nord and Mile End.
- Arabic. Cohort spread across Plateau Mont Royal and Milton Parc.
- Vietnamese. Cohort spread across Plateau Mont Royal and Jeanne Mance.
- Spanish. Cohort spread across Plateau Mont Royal and Milton Parc.

The team commits that any published reach claim for the Bengali or Urdu cohorts is verified against the delivery ledger before publication. If the delivery adjusted sample per cohort is below 60 the reach claim is held open and the cohort is reported as under adequately sampled rather than assigned a point estimate. This is a hard rule and it applies at every publication surface including any external presentation.

## Delivery Channels

The consultation reach program uses the following delivery channels for reminder and invitation traffic.

- SMS through a single carrier gateway (twilio). Used for reminder, meeting invite, survey link, and follow up. Delivery ledger sits in the messaging platform.
- Email through a two provider mix (mailgun and sendgrid). Used for translated summary, meeting invite, survey link, and follow up. Delivery ledger sits in the same messaging platform.
- Community meeting sign in. Paper and portal capture, reconciled into the response body.
- Intercept survey. Field team capture across the four corridors.
- Public portal. Open channel for structured survey and open comment.

Delivery logs are the ground truth for reach. Response counts alone do not prove reach.

## Reach Weighting

The published modal split reach estimate uses the method described below.

1. Numerator. Language cohort weighted response count. Responses are grouped by primary language of the respondent and by corridor referenced. Responses on the removed Rue Saint Joseph pilot are excluded from the final consultation numerator.
2. Denominator. Delivery adjusted denominator. The denominator uses delivered messages, not attempted messages. Bounced, failed, undelivered, or queued messages are excluded from the denominator. This corrects for the case where a cohort was mailed but not actually reached.
3. Cohort floor. If the delivery adjusted sample per cohort is below 60, the cohort is reported as under adequately sampled and no point estimate is assigned to that cohort. The narrative is held open. This rule is applied cohort by cohort, not across the aggregate.
4. Overlap check. Response body cross references (delivery id ref) are verified against the delivery ledger. Responses without a matching delivery ledger row are still counted in the numerator when the channel is a walk in surface (community meeting sign in, intercept survey), but they are excluded from the delivery adjusted denominator calculation.
5. Cross study firewall. The Parc Extension housing equity study reach numbers are not co mingled with the Plateau reach numbers. Where the same under reach pattern appears in both files it is described as parallel, never as combined.

The method is designed to be defensible under public question. The open conclusion posture on thin cohorts is intentional.

## Change Log

- v3 to v3 (2026-09-24). Current.
- v2 to v3. Rue Saint Joseph pilot removed from scope. Reach weighting rewritten to require delivery adjusted denominators. Cohort floor of 60 introduced. Cross study firewall clause added.
- v1 to v2 (2026-06-30). Corridor list finalised for the summer intake. Bengali and Urdu cohorts added to language access commitment.
- v0 to v1 (2026-04-06). Cycle open. Initial methodology.

*End of page.*
