CREATE TABLE products (
    product_name VARCHAR(100)
);

INSERT INTO
    products (product_name)
VALUES
    ('Broccoli'),
    ('Shampoo'),
    ('Toothpaste'),
    ('Candy');

ALTER TABLE
    products
ADD COLUMN
    id SERIAL PRIMARY KEY;

-- We don't use CONSTRAINT here since
-- the name of the PK doesn't matter.