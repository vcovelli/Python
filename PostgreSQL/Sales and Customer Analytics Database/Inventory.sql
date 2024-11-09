CREATE TABLE inventory (
    product_id INT REFERENCES products(product_id),
    store_id INT REFERENCES stores(store_id),
    quantity INT,
    PRIMARY KEY (product_id, store_id)
);