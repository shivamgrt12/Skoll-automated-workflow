# Budget rebuild worksheet - target

Written 2026-10-19. Sarah and I sat down after the Bright Path milestone shipped. The old rebuild used the current lease and the $85K straight-line for her income. Both are stale now. Rebuild target below. Assistant fills the bracketed rows during the runway math.

## Rebuild rules (do not violate)

- Rent line uses the **DocuSign figure** ($3,400), not the current lease pre-renewal ($3,200), not the older Callahan Gmail hint ($3,300). Higher-of-two written figures for conservative discipline.
- Sarah income line uses **QuickBooks trailing four months of paid receipts** midpoint, not the $85K annual straight-line divided by 12. Newest categorized data wins. The straight-line assumption goes to the superseded column with a date and a source.
- IVF savings HYSA transfer stays at **$2,000 monthly**. Do not reduce it to make the rebuild look easier. That is the point of the discipline.
- Parents remittance stays at **$300 on the first**. Do not move it. Do not bump it. Any proposed change lands in the Held-Actions Queue.
- **Retirement pieces untouched** in every runway line: Windbridge 401(k) at Alight (~$45,231), Sarah's Roth at Herongate Partners (~$28,113). Informational only. They do not appear as available capital.
- Nothing in this worksheet contradicts what Plaid actually shows in `plaid_balances_snapshot_2026-10-19.csv` or `plaid_transactions_trailing_90d.csv`.

## Inflow (rebuild)

| Line | Amount | Source | Superseded? |
|---|---|---|---|
| Brian Windbridge salary net | [$5,850/mo per Plaid 3-mo rolling] | Plaid Citizens checking direct-deposit average | no |
| Brian Amberfield adjunct | $833.33/mo | Plaid stipend deposit ($10K annual / 12) | no |
| Brian Etsy data viz shop | [~$105/mo variable] | Plaid Etsy deposits, low confidence | no |
| Sarah freelance monthly | **[QuickBooks trailing 4mo midpoint - use `quickbooks_trailing_4mo_sarah.csv`]** | replaces the $7,083 straight-line | **YES for old line** |
| Household inflow total (rebuilt) | [ ] | derived | |

## Outflow (rebuild under new lease)

| Line | Amount | Source | Superseded? |
|---|---|---|---|
| Rent | **[DocuSign envelope `env_lease_2026_1101` figure]** | `lease_renewal_2026-11-01_docusign_receipt.md` | **YES for old $3,200 line** |
| Federal student loans Pinecrest MPH | $420 | Nelnet fixed IDR | no |
| IVF savings HYSA transfer | $2,000 | scheduled 5th monthly, do not reduce | no |
| Groceries | $900 | Instacart / TJ / H Mart / Market Basket avg | no |
| Dining | $350 | Plaid categorized avg | no |
| Healthcare copays | $390 | PT + therapy + psychiatry + neurology + occasional | no |
| Utilities (electric + gas) | $200 | Eversource + National Grid | no |
| Phone + internet | $160 | Verizon + Xfinity | no |
| Gas / auto | $180 | Subaru Crosstrek avg | no |
| Sarah ACA | $380 | healthcare.gov MA marketplace | no |
| Subscriptions | $85 | Peets / streaming / AMC / REI | no |
| Progressive auto insurance | $145 | monthly, renewal March 2027 | no |
| **Parents remittance PayPal (fixed rail)** | **$300 on the 1st** | never moves without Brian and Sarah approval | no |
| Hobbies (basketball league / running gear) | $200 | YMCA + REI avg | no |
| Household outflow total (rebuilt) | [ ] | derived | |

## Net monthly delta (rebuilt inflow minus rebuilt outflow)

[ ] - this feeds the projected monthly savings line in the runway math.

## Runway math (both reads)

### Conservative read

`(IVF HYSA current + Marcus emergency reserve) / per_cycle_all_in_midpoint`

- IVF HYSA current: **$14,108.60** (Plaid, 2026-10-19)
- Marcus emergency reserve: **$12,047.32** (Plaid, 2026-10-19)
- Per-cycle all-in midpoint including medication: **$21,150** (see `ivf_cost_projection_v3.csv`)
- Conservative attempts fundable: [ ]

### Projected read

`(IVF HYSA projected + Marcus + Alpaca ladder current mark + projected monthly savings through 2027-02-15) / per_cycle_midpoint − $25K Windbridge lifetime cap credit`

- IVF HYSA projected at 2027-02-15: $14,108.60 + $2,000 × (months between 2026-10-19 and 2027-02-15) = [ ]
- Marcus reserve: $12,047.32
- Alpaca ladder current mark: **$3,184.20** (read-only, no trades)
- Projected monthly savings × months to horizon: [ ]
- Gross projected: [ ]
- Minus $25,000 Windbridge lifetime fertility cap credit (applies once against first cycle): [ ]
- Per-cycle midpoint including medication: $21,150
- Projected attempts fundable: [ ]

### Excluded from every read (untouched)

- Windbridge 401(k) ~$45,231 - retirement, untouched.
- Sarah's Roth at Herongate ~$28,113 - retirement, untouched.

## Sensitivity notes

- If Sarah's QuickBooks trailing midpoint lands at the low end of the $7,000-$8,000 band, projected monthly savings drops accordingly and the projected runway tightens.
- If Callahan bumps rent again at the 12-month renewal in 2027-11-01, this rebuild is only good through Oct 2027.
- Grant applications (Baby Quest, Cade Foundation, Pay It Forward Fertility) are not funded and are not counted in either read.
- Any Amadeus or Airbnb Thanksgiving/Christmas travel at or above $200 is held in the Held-Actions Queue and does not appear in this rebuild until approved.
