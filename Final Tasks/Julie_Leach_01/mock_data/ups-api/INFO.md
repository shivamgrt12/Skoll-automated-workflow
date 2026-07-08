# ups-api

**Status.** Persona-connected shipping rail (per `julie-leach/TOOLS.md`, ground rail alternative to FedEx). The SKOLL_GK Mock Data Generator does not carry an env schema or builder for UPS.

**Julie-side canonical carrier.** The fulfillment queue lives in `Julie Leach\Data\preshow_kit_orders.csv`. Ground rail is the default for OH/PA/KY/MI/IN/GA/NC/VA/IL destinations with December 8-10 requested_by dates.

**Contract.** If a UPS mock is added, it must expose label staging endpoints only. Print and drop actions remain Julie's action per PROMPT.md.
