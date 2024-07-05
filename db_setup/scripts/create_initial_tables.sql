-- DROP TABLE IF EXISTS public.agency;
-- DROP TABLE IF EXISTS public.nigp;
-- DROP TABLE IF EXISTS public.nigp_categories;
-- DROP TABLE IF EXISTS public.vendor;

CREATE TABLE IF NOT EXISTS public.agency (
	"AGENCY_KEY" int4 NULL,
	"ENTITY_CODE" varchar(50) NULL,
	"ENTITY_DESCRIPTION" varchar(64) NULL
);

CREATE TABLE IF NOT EXISTS public.nigp (
	"NIGP_KEY" int4 NULL,
	"NIGP_CODE" int4 NULL,
	"NIGP_DESC" varchar(256) NULL,
	"NIGP_CATEGORY_KEY" int4 NULL
);

CREATE TABLE IF NOT EXISTS public.nigp_categories (
	"NIGP_CATEGORY_KEY" int4 NULL,
	"NIGP_CATEGORY_CODE" int4 NULL,
	"NIGP_CATEGORY_DESC" varchar(256) NULL
);

CREATE TABLE IF NOT EXISTS public.vendor (
	vendor_key int4 NULL,
	"REGISTRATION_TYPE" varchar(50) NULL,
	"VENDOR_ID" varchar(25) NULL,
	"VENDOR_NAME" varchar(100) NULL,
	"VENDOR_ADDRESS" varchar(250) NULL
);
