# fedex-api

**Status.** Persona-connected shipping rail (per `julie-leach/TOOLS.md`, time-sensitive shipping). The SKOLL_GK Mock Data Generator does not carry an env schema or builder for FedEx.

**Julie-side canonical carrier.** The fulfillment queue lives in `Julie Leach\Data\preshow_kit_orders.csv` (30 orders, ship_service_hint == expedited on 6 rows for FedEx candidates given Columbus-to-CA/TX/FL/WA/MA/CO distances and December 10-11 requested_by dates).

**Contract.** If a FedEx mock is added, it must expose label staging endpoints only. Print and drop actions remain Julie's action per the "stage labels but leave the print and drop to me" red line in `PROMPT.md`.
