# etsy-api

**Status.** Persona-connected surface (per `julie-leach/TOOLS.md`, storefront rail D, partial catalog) but the SKOLL_GK Mock Data Generator does not carry an env schema or builder for Etsy.

**Julie-side canonical carrier.** The partial Etsy catalog lives in `Julie Leach\Data\etsy_listings_export.csv` with 12 active listings covering handmade decor and finish singles.

**Contract.** If an Etsy mock is added, it must expose listing_id, sku, title, quantity, listing_status for exactly 12 rows, and the 2 Etsy-channel pre-show orders (ORD-ETS-6001, ORD-ETS-6002) both paid via PayPal.
