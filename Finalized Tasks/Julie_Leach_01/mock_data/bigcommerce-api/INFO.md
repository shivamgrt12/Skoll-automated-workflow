# bigcommerce-api

**Status.** Persona-connected surface (per `julie-leach/TOOLS.md`, storefront rail A) but the SKOLL_GK Mock Data Generator does not carry an env schema or builder for BigCommerce.

**Julie-side canonical carrier.** The equivalent SKU stock line lives in `Julie Leach\Data\bigcommerce_inventory_export.csv` (40 rows) and the reconciled product master lives in `Julie Leach\Mock Data\woocommerce-api\products.csv`. The BigCommerce endpoint set is functionally equivalent to WooCommerce for this task, so a downstream harness can proxy through `woocommerce-api` if BigCommerce is not stood up.

**Contract.** If a BigCommerce mock is added, it must expose per-SKU quantity_available and last_synced_iso with 40 SKUs matching CMP-001 through CMP-040 and the 4 kit SKUs, plus 30 pre-show orders matching the four channels named in `preshow_kit_orders.csv`.
