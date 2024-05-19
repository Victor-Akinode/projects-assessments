CREATE SCHEMA IF NOT EXISTS ASSIGNMENT;


-- Create and populate tables
create table if not exists ASSIGNMENT.AUTOS
(
    id  serial primary key,
    name varchar not null,
    fuel varchar not null,
    doors varchar not null,
    style varchar not null,
    length numeric(4, 2) not null,
    width numeric(4,2) not null,
    height numeric(4, 2) not null,
    weight smallint not null,
    eng_type varchar not null,
    cylinders varchar not null,
    rpm smallint not null,
    price integer not null
);


COPY ASSIGNMENT.AUTOS (id, name, fuel, doors, style, length, width, height, weight, eng_type, cylinders, price)
FROM '/data/autos.csv' DELIMITER ',' CSV HEADER;