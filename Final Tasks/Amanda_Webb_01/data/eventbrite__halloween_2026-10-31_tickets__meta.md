# Eventbrite — Rhythm Dance Studio Halloween Social

- **service:** Eventbrite
- **report_type:** Event Attendee Report
- **event_id:** evt-aw-halloween-2026
- **event_name:** Rhythm Dance Studio Halloween Social
- **event_date:** 2026-10-31
- **doors:** 20:00 ET
- **venue:** Rhythm Dance Studio, 1218 Penn Avenue, West Reading PA
- **ticket_price_usd:** 30.0
- **ticket_capacity:** 60
- **snapshot_taken_at:** 2026-10-12T09:25:01-04:00
- **advance_tickets_sold:** 37
- **gross_advance_usd:** 1110.0
- **fees_collected_by_eventbrite_usd:** 86.42
- **net_after_eventbrite_fees_usd:** 1023.58
- **note:** Total includes 3 block-of-three prepays (Rachel Goldberg, Elena Vasquez, Anastasia Reilly each bought 3 tickets) which routed through the studio Stripe processor and appear in stripe/halloween_online_tickets.json. The remaining 28 tickets paid through Eventbrite's native processor.
- **unique_buyer_email_count:** 32
- **ticket_count:** 37
- **note_on_buyer_vs_ticket_count:** Three buyers bought blocks of 3 each, accounting for 9 of the 37 tickets while contributing only 3 unique buyer emails. The remaining 28 tickets are 1-per-buyer.
- **duplicates_with_square_in_studio_signups:**
  ```json
  [
    "Megan Rodriguez",
    "Maya Kapoor",
    "Rachel Goldberg (one of three)",
    "Elena Vasquez (one of three)",
    "Mia Whitfield",
    "Anastasia Reilly (one of three)"
  ]
  ```
- **duplicate_count:** 6
- **true_projected_attendance:** 49
- **note_on_reconciliation:** Naive math: 37 advance + 18 in-studio = 55. Six names overlap between the two rails. True projected attendance is 49. Studio capacity for an evening social is 60. Comfortable, not capacity-strained, no door-cap action needed.
