DROP TABLE IF EXISTS inventory, sales, products, stores, customers;

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(100),
    price NUMERIC(10,2)
);

CREATE TABLE stores (
    store_id SERIAL PRIMARY KEY,
    location VARCHAR(100), 
    manager VARCHAR(100)
);

CREATE TABLE inventory (
    product_id INT REFERENCES products(product_id),
    store_id INT REFERENCES stores(store_id),
    quantity INT,
    PRIMARY KEY (product_id, store_id)
);

CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id)
    product_id INT REFERENCES products(product_id)
    store_id INT REFERENCES stores(store_id)
    sale_date DATE,
    sale_amount NUMERIC(10,2)
);