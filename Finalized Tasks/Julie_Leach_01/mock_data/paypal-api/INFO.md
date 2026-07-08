# paypal-api

**Status.** Persona-connected surface (per `julie-leach/TOOLS.md`, payment rail for a subset of buyers) but the SKOLL_GK Mock Data Generator does not carry an env schema or builder for PayPal. It is not the `stripe-api` schema either since chargebacks and case handling differ.

**Julie-side canonical carrier.** The 20 PayPal transactions live in `Julie Leach\Data\paypal_transactions.csv` (19 cleared, 1 disputed chargeback CB-2026-011) plus `Julie Leach\Data\chargeback_case_notes.md` for the open case details.

**Contract.** If a PayPal mock is added, it must expose the 20 counterparty transactions with realistic public-consumer emails (gmail x9, yahoo x4, icloud x4, outlook x3), one disputed row PP-70011 with case_ref CB-2026-011 and 109.00 USD on hold reducing the reconciled cleared total.

**Boundary note.** The chargeback hold is a load-bearing math input for the December kit run cleared-payment total in the prompt.
