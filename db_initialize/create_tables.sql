-- DROP TABLE public.agency;

CREATE TABLE public.agency (
	"AGENCY_KEY" int4 NULL,
	"ENTITY_CODE" varchar(50) NULL,
	"ENTITY_DESCRIPTION" varchar(64) NULL
);


-- DROP TABLE public.nigp;

CREATE TABLE public.nigp (
	"NIGP_KEY" int4 NULL,
	"NIGP_CODE" int4 NULL,
	"NIGP_DESC" varchar(256) NULL,
	"NIGP_CATEGORY_KEY" int4 NULL
);


-- DROP TABLE public.nigp_categories;

CREATE TABLE public.nigp_categories (
	"NIGP_CATEGORY_KEY" int4 NULL,
	"NIGP_CATEGORY_CODE" int4 NULL,
	"NIGP_CATEGORY_DESC" varchar(256) NULL
);