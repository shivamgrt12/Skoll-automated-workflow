# EVIDENCE INVENTORY - Vinterberg Group Investigation
**Compiled:** 2026-10-22  |  **Investigator:** Carl Dillon (Eriksson & Holm Revisionsbyra)
**Generation:** deterministic (seed 20261102). Every artifact below cross-anchors to the seeded anomalies.

## A. Structure
| File | Format | Rows/Records |
|---|---|---|
| entity_map.json / entity_ownership.yaml / entity_map.md | JSON/YAML/MD | 17 entities |

## B. Vendors
| File | Format | Rows |
|---|---|---|
| vendor_master_top50_and_shells.csv (seed) | CSV | 54 |
| vendor_master_full_population.csv | CSV | 180 |
| master_service_agreements.jsonl | JSONL | 180 |
| msa_nordkap_0118.md/.xml, msa_aurora_0133.md, msa_lindqvist_0152.md | MD/XML | 3 shells |

## C. Transactions (FY2022-2025)
| File | Format | Rows |
|---|---|---|
| invoice_register_2022_2025.csv | CSV | 5524 |
| bank_movements_2022_2025.csv | CSV | 7036 |
| general_ledger_2022_2025.csv | CSV | 11048 |
| payroll_journal_2022_2025.csv | CSV | 19158 |

## D. Payroll / HR
| File | Format | Rows |
|---|---|---|
| payroll_flagged_extract.csv (seed) | CSV | 30 |
| payroll_headcount_full.csv | CSV | 450 |
| hr_personnel_records.json | JSON | 450 |
| skatteverket_tax_filings_2025.csv | CSV | 445 |

## E. Access
| File | Format | Rows |
|---|---|---|
| access_log_anomaly_excerpt.csv (seed) | CSV | 20 |
| access_log_full_18mo.csv | CSV | 2486 |
| badge_access_records.csv | CSV | 2827 |
| vpn_session_logs.csv | CSV | 2827 |

## F. Crypto
| File | Format | Rows |
|---|---|---|
| crypto_movements_sample.csv (seed) | CSV | 14 |
| crypto_counterparty_ledger.csv | CSV | 50 |
| crypto_price_feed_settlement.csv | CSV | 32 |

## G. Nordstrom
| File | Format | Rows |
|---|---|---|
| grant_ledger_q3_2026.csv (seed) | CSV | 35 |
| nordstrom_board_allocations_2026.csv | CSV | 35 |
| nordstrom_beneficiary_acknowledgements.csv | CSV | 35 |

## H. Working papers
- linnea_vendor_workstream_notes.md
- document_exchange_index.md

## Anchor map (load-bearing linkages)
- Shell vendors 118/133/152 -> flat invoices -> bank vendor_payment to shell IBAN -> intercompany to VG-EE1 hub -> crypto_funding (diversion_ref DIV-*).
- Ghost employees ['E-1487', 'E-1622', 'E-1704', 'E-1811', 'E-1932'] (no tax filing, badge=0, vpn=0) + subtle ghosts ['E-3407', 'E-3408', 'E-3409'] (tax filed, thin footprint) -> salary routed to shell IBANs.
- J.EKSTROM admin_override 2025-11-14 03:17 on VM-IAM-01: NO badge_access_records and NO vpn_session_logs entry exists -> unanchored -> open-questions ledger.
- K.LINDQVIST (badge WKS-4312) == Lindqvist Facility Services BO.  Jaan Tamm (E-1810) surname == Aurora BO 'M Tamm'.
- Crypto: settlement-date SEK basis > reporting-date basis => reporting-date understates exposure. Coinbase = 3rd (counterparty-only) account.
- Nordstrom NG-2026-Q3-018 (approved 450000 / recorded 620000 / ack MISSING), -024 (ack MISSING), -031 (approved 180000 / recorded 182800).
