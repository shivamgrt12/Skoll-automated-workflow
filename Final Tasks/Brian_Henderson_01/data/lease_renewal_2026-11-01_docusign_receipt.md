# DocuSign Envelope Receipt - Residential Lease Renewal

> This is Brian's personal copy of the DocuSign envelope receipt saved from the notification email. The envelope itself is the authoritative record of record; this receipt is here so the values are visible without hitting the DocuSign service.

---

## Envelope metadata

- **Envelope ID:** env_lease_2026_1101
- **Envelope Name:** "Residential Lease Renewal - 224 Massachusetts Ave, Unit 3 - 2026-11-01 to 2027-10-31"
- **Envelope Status:** SENT - AWAITING TENANT SIGNATURE
- **Sender (Landlord):** Mike Callahan
- **Sender Email:** mike.callahan.rentals@gmail.com
- **Sender Phone:** (617) 555-0267 (text-first per landlord's preference)
- **Envelope Sent:** 2026-10-05T14:22:00-04:00
- **Envelope Voided or Corrected:** no
- **Reminder Cadence:** every 5 days from send date
- **Envelope Expiration:** 2026-10-31T23:59:59-04:00 (if unsigned by then, envelope voids and current lease month-to-month rollover applies)

## Recipients

| Order | Recipient | Role | Email | Signing Status | Last Action |
|---|---|---|---|---|---|
| 1 | Mike Callahan | Landlord | mike.callahan.rentals@gmail.com | SIGNED | 2026-10-05T14:22:00-04:00 |
| 2 | Brian Henderson | Tenant | brian.henderson@voissync.ai | AWAITING SIGNATURE | envelope opened 2026-10-06T08:14:00-04:00, read 2026-10-06T08:19:00-04:00, closed without signing |
| 3 | Sarah Henderson | Co-Tenant | sarah.henderson.design@gmail.com | AWAITING SIGNATURE | envelope opened 2026-10-06T18:22:00-04:00, closed without signing |

## Documents in envelope

1. `Residential Lease Renewal - 224 Massachusetts Ave, Unit 3 - 2026-11-01 to 2027-10-31.pdf` (12 pages, MA standard residential lease template)
2. `Rider A - Utility Allocation.pdf` (2 pages)
3. `Rider B - Snow Removal and Common Area.pdf` (1 page)
4. `Landlord Contact Sheet and Emergency Maintenance Numbers.pdf` (1 page)

## Key terms (from the cover memo and Section 3 of the main document)

- **Property:** 224 Massachusetts Ave, Unit 3, Cambridge, MA 02139 (top floor triple-decker, off Massachusetts Ave near Porter Square)
- **Term:** November 1, 2026 through October 31, 2027 (12 months, single-term)
- **Monthly Rent:** **$3,400.00** (three thousand four hundred dollars, U.S.)
- **Rent Due:** 1st of each month, late fee $75 after the 5th
- **Security Deposit:** unchanged at $3,200.00 (last month's prior rent, held from initial lease dated 2024-11-01; no top-up required)
- **Utility Allocation (Rider A):** water and sewer included in rent; electric (Eversource) and gas (National Grid) tenant-paid; internet and phone tenant-paid
- **Common Area (Rider B):** snow removal from the shared walk is landlord responsibility through the winter season; interior stairwell cleaning is on the tenants (rotating with Units 1 and 2 per informal agreement, one week each)
- **Pets:** none, unchanged
- **Sublet:** requires written landlord consent, unchanged
- **Renewal Notice:** either party to notify 60 days before expiration for a 2027-11-01 further renewal (i.e. by 2027-09-01)
- **Termination:** either party 60-day written notice for non-renewal
- **Governing Law:** Commonwealth of Massachusetts, city of Cambridge

## Author-side notes (Brian's read)

- **The DocuSign figure is $3,400.00 per month.** This is what will actually land on the 2026-11-01 effective date. Higher than the current pre-renewal rent of $3,200 (which has been on the books since November 2024). Callahan is within market for a Porter Square triple-decker top floor.
- **The earlier informal Gmail thread from Callahan on 2026-09-14** floated **$3,300 per month** during the pre-renewal conversation. Callahan said in that thread: "Thinking about $3,300, might be able to hold that if you're staying two more years." No two-year term appeared in the DocuSign envelope. **The $3,300 figure never landed on paper.** DocuSign at $3,400 is the authoritative source of record.
- **Reconciliation rule (higher-of-two written figures for conservative discipline):** the runway math and the household budget rebuild use **$3,400.00**, not $3,300 and not the average. The $3,300 hint is recorded as superseded in the Reconciliation Doc so it is named and set aside, not silently dropped.
- **Do NOT sign this envelope on Brian's behalf.** Read for the authoritative figure. The signature waits for Brian and Sarah in the same room. This is a Held-Actions Queue item: action = sign DocuSign envelope env_lease_2026_1101; surface = docusign-api; reason held = Brian and Sarah in same room; approver = Brian and Sarah jointly.

## What triggers a re-read

- If Callahan sends a corrected envelope (envelope_status becomes CORRECTED and a new envelope replaces this one), re-read the figure.
- If Callahan sends an amendment offer via Gmail, that amendment does not supersede the signed DocuSign document unless it is executed through a new envelope.
- If a lawyer reviews this and flags a term, that flag lands in the Held-Actions Queue with Brian as approver.
