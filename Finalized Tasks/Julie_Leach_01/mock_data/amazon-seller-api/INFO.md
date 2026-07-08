# amazon-seller-api

**Status.** Persona-connected surface (per `julie-leach/TOOLS.md`, storefront rail C) but the SKOLL_GK Mock Data Generator does not carry an env schema or builder for Amazon Seller Central.

**Julie-side canonical carrier.** The Amazon-side inventory report lives in `Julie Leach\Data\amazon_seller_inventory_report.csv` with 40 rows dated 2026-12-01 (the most recent physical count). This rail is the winning source of truth on 2 hot SKUs (CMP-010 and CMP-026) per the hidden inventory conflict in `Julie_Leach_Files\prompt_design_notes.md` §5.

**Contract.** If an Amazon Seller mock is added, it must expose quantity_available AND quantity_reserved per SKU with report_date_iso == 2026-12-01, and the 3 pre-show orders on the amazon channel (ORD-AMZ-5001, ORD-AMZ-5002, ORD-AMZ-5003) must be visible on the orders side.
