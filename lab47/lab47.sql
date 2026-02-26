CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	email VARCHAR(100) UNIQUE
);

INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
SELECT * FROM users;