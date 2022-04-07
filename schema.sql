--## fuser_permission_grp
CREATE TABLE IF NOT EXISTS public.fuser_permission_grp
(
id serial NOT NULL unique primary key,
createdBy text not null,
createdOn timestamp with time zone not null DEFAULT ('now'::text)::timestamp(6) with time zone,
modifiedOn timestamp with time zone,
enabled integer not null default(1),
name text unique not null,
type integer not null default(1),
securityLevel integer not null default(1)
)
WITH (
 OIDS = FALSE
)
TABLESPACE pg_default;



--## ffacility
CREATE TABLE IF NOT EXISTS public.ffacility
(
id serial NOT NULL unique primary key,
createdBy_Id integer not null references fuser(id),
createdOn timestamp with time zone not null DEFAULT ('now'::text)::timestamp(6) with time zone,
modifiedOn timestamp with time zone,
enabled integer not null default(1),
type integer not null,
description text not null,
address1 text not null,
address2 text,
address3 text,
address4 text,
city text not null,
stateProvince text not null,
postalCode varchar(32) not null,
country text not null default('US')
)
WITH (
 OIDS = FALSE
)
TABLESPACE pg_default;


--## fuser_facility_list
CREATE TABLE IF NOT EXISTS public.fuser_facility_list
(
id serial NOT NULL unique primary key,
createdBy_Id integer not null references fuser(id),
createdOn timestamp with time zone not null DEFAULT ('now'::text)::timestamp(6) with time zone,
modifiedOn timestamp with time zone,
enabled integer not null default(1),
fUser_Id integer not null references fuser(id),
fFacility_Id integer not null references ffacility(id)
)
WITH (
 OIDS = FALSE
)
TABLESPACE pg_default;
