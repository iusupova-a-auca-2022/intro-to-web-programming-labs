-- Lab 1
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	email VARCHAR(100) NOT NULL UNIQUE,
	age INTEGER NOT NULL,
	registration_date DATE DEFAULT CURRENT_DATE
);

INSERT INTO users (name, email, age) 
VALUES ('Alice', 'alice@example.com', 20),
		('Bruce', 'wayne@gmail.com', 41),
		('Barbara', 'barbara@gmail.com', 24);

SELECT * FROM users;

-- Lab 2
UPDATE users
SET age = 31
WHERE name = 'Alice';

UPDATE users
SET email = 'gordon@gmail.com'
WHERE name = 'Barbara';

SELECT * FROM users;

-- Lab 3
DELETE FROM users
WHERE email = 'gordon@gmail.com';

DELETE FROM users
WHERE age > 40;

SELECT * FROM users;

-- Lab 4
CREATE TABLE products (
	product_id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	price NUMERIC(10, 2) NOT NULL,
	stock_quantity INTEGER NOT NULL,
	discontinued BOOLEAN DEFAULT FALSE
);

INSERT INTO products (name, price, stock_quantity) VALUES
('Headphones', 120, 15),
('Laptop', 250, 20),
('Mouse', 80, 25);

UPDATE products 
SET price = 300
WHERE name = 'Laptop';

UPDATE products 
SET discontinued = TRUE
WHERE name = 'Mouse';

DELETE FROM products 
WHERE discontinued = TRUE;

SELECT * FROM products;

-- Lab 5
BEGIN;

INSERT INTO users (name, email, age) VALUES
('Bob', 'bob@gmail.com', 39);

UPDATE users
SET age = 43
WHERE name = 'Bob';

DELETE FROM users
WHERE name = 'Alice';

ROLLBACK;

SELECT * FROM users;