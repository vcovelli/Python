CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id)
    product_id INT REFERENCES products(product_id)
    store_id INT REFERENCES stores(store_id)
    sale_date DATE,
    sale_amount NUMERIC(10,2)
);