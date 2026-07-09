# Wholesale Fuel Supplier Matrix - Q4 Vendor Pick

**Purpose:** consolidate Q4 wholesale fuel supply decision across three stores
**Owner:** Heidi Hart with Sam Abbott (Greenfield Store Manager)
**Decision needed by:** vendor call this week (target 2026-10-08)
**Contracts under review:** Q4 2026 wholesale fuel supply for Greenfield Fuel & Market, Schaefer Quick Stop, Warren Road Express
**Q3 volume across stores:** 460,000 gallons combined (see salesforce_fuel_distributor_tiers.md)

---

## 1. Vendor Overview

### 1.1 Lakeside Fuel (LK-01)

- **Origin:** Muskegon MI (~180 mi west)
- **Delivery terms:** 48-hour scheduled
- **Minimum load:** 6,500 gallons per delivery
- **Payment terms:** Net-15
- **Current relationship:** current supplier at Greenfield Fuel & Market and Warren Road Express (Schaefer sourced separately Q3)
- **Q3 stockouts:** 2 events (both regular_87), weeks of 2026-08-03 and 2026-09-07
- **Q3 on-time delivery rate:** 86.4 percent
- **Q3 quality pass rate:** 96.6 percent
- **Q3 invoice accuracy:** 94.7 percent
- **Q3 avg lead time:** 62.4 hours
- **Pricing:** lowest per-gallon regular_87 at $3.185 quoted current week

### 1.2 Michigan Petroleum (MP-01)

- **Origin:** Grand Rapids MI (~140 mi west)
- **Delivery terms:** 24-hour scheduled
- **Minimum load:** 7,500 gallons per delivery
- **Payment terms:** Net-15
- **Current relationship:** Q3 evaluation partner (test deliveries to Schaefer)
- **Q3 stockouts:** 0
- **Q3 on-time delivery rate:** 98.7 percent
- **Q3 quality pass rate:** 98.2 percent
- **Q3 invoice accuracy:** 98.4 percent
- **Q3 avg lead time:** 44.2 hours
- **Pricing:** second-lowest per-gallon regular_87 at $3.242 quoted current week

### 1.3 Great Lakes Distribution (GL-01)

- **Origin:** Toledo OH (~85 mi south)
- **Delivery terms:** 72-hour scheduled
- **Minimum load:** 8,500 gallons per delivery
- **Payment terms:** Net-30
- **Current relationship:** legacy vendor pulled from Warren Road Express Q1 2026
- **Q3 stockouts:** 1 event (premium_93), week of 2026-08-24
- **Q3 on-time delivery rate:** 92.1 percent
- **Q3 quality pass rate:** 95.1 percent
- **Q3 invoice accuracy:** 97.2 percent
- **Q3 avg lead time:** 81.6 hours
- **Pricing:** highest per-gallon regular_87 at $3.288 quoted current week

---

## 2. Vendor Selection Rationale

Sam and I have circled this for a month. The Q3 evaluation data is now complete and the picture is unambiguous once reliability is weighted properly against per-gallon price. On a raw per-gallon basis Lakeside is the cheapest supplier and has been our lead vendor for years. On a total-cost-of-supply basis Michigan Petroleum wins Q4.

Reasoning:

- **Stockouts.** Lakeside recorded 2 regular_87 stockouts in Q3, both at Greenfield. Each stockout event carries an estimated $8,000-$12,000 revenue impact per store per event (lost fuel margin + convenience walk-off + reputational damage per Yelp feedback pattern). Michigan Petroleum recorded 0 stockouts in Q3.
- **On-time delivery.** Michigan Petroleum 98.7 percent on-time vs Lakeside 86.4 percent. That 12-point gap translates directly into inventory buffer requirements at every store; carrying higher buffer to hedge Lakeside unreliability costs working capital.
- **Lead time.** Michigan Petroleum 44 hours vs Lakeside 62 hours vs Great Lakes 82 hours. Michigan's shorter lead time enables tighter tank inventory management and reduces demurrage risk.
- **Price delta.** Michigan is 5.7 cents higher per gallon than Lakeside on regular_87. Over Q3 460,000 gallon volume that is $26,220 gross price premium. The 2 Lakeside stockout events alone cost more than that price premium in one quarter.
- **Great Lakes.** Highest price + longest lead time + Net-30 (tighter cashflow terms). Not competitive on any dimension. Not in consideration for Q4 pick.

**Q4 pick: Michigan Petroleum for all three stores.**

Sam is on board. Vendor call this week to notify Lakeside of Q4 sourcing change and to lock the Michigan supply contract for the quarter.

---

## 3. Q3 Delivery Incident Register

| Week starting | Vendor | Grade | Event | Store | Notes |
|---|---|---|---|---|---|
| 2026-07-06 | LK-01 | mid_89 | late 8h | Greenfield | driver route reassignment |
| 2026-07-13 | LK-01 | regular_87 | on-time | Warren Road | - |
| 2026-08-03 | LK-01 | regular_87 | STOCKOUT | Greenfield | 3-hour dispenser down; est $9,200 impact |
| 2026-08-10 | MP-01 | regular_87 | on-time | Schaefer (eval) | first eval delivery Michigan |
| 2026-08-24 | GL-01 | premium_93 | STOCKOUT | Warren Road | 5-hour premium dispenser down; est $6,400 impact |
| 2026-09-07 | LK-01 | regular_87 | STOCKOUT | Greenfield | 4-hour dispenser down; est $11,600 impact |
| 2026-09-14 | MP-01 | mid_89 | on-time | Schaefer (eval) | second eval delivery Michigan |
| 2026-09-21 | LK-01 | diesel | late 6h | Warren Road | resolved same day |
| 2026-09-28 | MP-01 | regular_87 | on-time | Greenfield (eval) | eval delivery Michigan to Greenfield |

---

## 4. Contract Terms Comparison

| Term | Lakeside Q4 offer | Michigan Q4 offer | Great Lakes Q4 offer |
|---|---|---|---|
| Regular_87 per gallon | $3.185 | $3.242 | $3.288 |
| Mid_89 per gallon | $3.325 | $3.385 | $3.442 |
| Premium_93 per gallon | $3.510 | $3.588 | $3.665 |
| Diesel per gallon | $3.845 | $3.912 | $3.985 |
| Ethanol E85 per gallon | $2.945 | $3.028 | $3.098 |
| Delivery frequency (max) | weekly | weekly | biweekly |
| Delivery lead time | 48 hr | 24 hr | 72 hr |
| Minimum load | 6,500 gal | 7,500 gal | 8,500 gal |
| Payment terms | Net-15 | Net-15 | Net-30 |
| Quality guarantee | 96% | 98% | 95% |
| Stockout penalty clause | none | 3% credit on next delivery | none |
| Fuel spec deviation credit | 1% credit | 3% credit | 1% credit |
| Contract term | quarterly | quarterly | quarterly |
| Termination notice | 15 days | 15 days | 30 days |
| Distributor tier alignment | (see salesforce_fuel_distributor_tiers.md) | (see salesforce_fuel_distributor_tiers.md) | (see salesforce_fuel_distributor_tiers.md) |

---

## 5. Past Dispute Log

| Date | Vendor | Nature of dispute | Resolution |
|---|---|---|---|
| 2025-04-14 | LK-01 | invoice overcharge $840 | credited on next delivery |
| 2025-08-22 | LK-01 | delivery mixed grade contamination | 50% credit + reclean cost $1,150 |
| 2026-02-08 | GL-01 | late delivery no notice | 2% credit + Warren Road pulled Q1 2026 |
| 2026-05-11 | LK-01 | quality spec fail on premium_93 | reject + reclean |
| 2026-07-18 | LK-01 | invoice math error $215 | credited same day |

Zero disputes with Michigan Petroleum in evaluation period.

---

## 6. Post-Selection Actions

- Notify Lakeside of Q4 sourcing change (courtesy call from Sam, follow-up email from Heidi)
- Sign Q4 supply contract with Michigan Petroleum for all three stores
- Update store operations manual with new vendor contact for Sam, Rita, Angelique
- Communicate to store managers regarding delivery scheduling shifts
- Set Q1 2027 re-evaluation checkpoint on Michigan performance
- Salesforce fuel distributor tier check: Q4 volume alignment against Tier A threshold (see salesforce_fuel_distributor_tiers.md; volume adjustment implications)
