# Revised Break-Even Model - Medical Transport

File: /Ward Taxi/AHCA/revised_breakeven_model_2027
Owner: ashley.ward@finthesiss.ai
Last modified: 2027-01-02
Built from: actual booked modification costs + broker rider binder + fleet books

> This model replaces the early-2026 Notion planning page. It is built on what
> the vans actually cost and the rider the broker actually bound, not the
> penciled estimates.

## Inputs (actuals, not estimates)

| Input | Value | Source |
|-------|-------|--------|
| Modification cost per van | $4,850 | QuickBooks booked bills TXN-2026-1101, TXN-2026-1104; maintenance log WO-2026-1042/1043 |
| Vans modified | 2 (VAN-01, VAN-02) | fleet_vehicle_inventory_2027.csv |
| Total modification capital | $9,700 | 2 x $4,850 |
| Medical transport insurance rider | $640 / month | Coral Gables broker binder, effective 2027-02-01 |
| MIA airport queue revenue (annualized) | $72,000 | QuickBooks actuals (declined from carried $85,000) |

## Revised contribution

- Gross incremental revenue per van holds near the plan, but the higher rider
  ($640/month vs the $480 early quote) and the higher capital base drag the net.
- Net incremental contribution recalculated at roughly **$1,020 per month for
  two vans combined** after the $640 rider and incremental operating cost.

## Revised break-even

- Total modification capital $9,700 / ~$510 per van per month net
  => **break-even projected at 19 months** on two modified vans.
- This is 5 months longer than the original 14-month plan, driven by the actual
  $4,850 modification cost and the $640 rider.

## Affordability

- $9,700 capital clears out of the **$32,000 business reserve** with room to
  spare; no draw on personal savings, the Fidelity SEP IRA, or family funds.
- Q4 estimated tax (due 2027-01-15, Max Delano preparing) should be funded first
  before the modification capital is treated as committed.

## Sensitivities

- If MIA queue revenue keeps sliding below $72,000, the incremental contribution
  thins and break-even stretches past 19 months.
- If a third van is added to scope, capital rises to $14,550 and break-even
  moves again; hold scope at two vans until the first two prove the line.
