-- INNER JOIN
CREATE TABLE customers (
	customer_id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	email TEXT NOT NULL
);

CREATE TABLE orders (
	order_id SERIAL PRIMARY KEY,
	customer_id INTEGER,
	total_amount DECIMAL(10, 2) NOT NULL
);

INSERT INTO customers (name, email) VALUES
('Alice', 'alice@email.com'),
('Bob', 'bob@email.com'),
('John', 'john@email.com');

INSERT INTO orders (order_id, customer_id, total_amount) VALUES
(101, 1, 250.00),
(102, 2, 120.00),
(103, 1, 80.00);

SELECT customers.name, orders.order_id, orders.total_amount
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id;


--------
CREATE TABLE employees (
	emp_id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	dept_id INTEGER
);

CREATE TABLE departments (
	dept_id SERIAL PRIMARY KEY,
	dept_name TEXT NOT NULL
);

INSERT INTO employees (name, dept_id) VALUES
('Alex', 10),
('Ben', 20),
('Clara', 30);

INSERT INTO departments (dept_id, dept_name) VALUES
(10, 'HR'),
(20, 'IT');

SELECT employees.name, departments.dept_name
FROM employees
INNER JOIN departments ON employees.dept_id = departments.dept_id;


--------
CREATE TABLE students (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE enrollments (
	id SERIAL PRIMARY KEY,
	student_id INTEGER NOT NULL,
	course_id INTEGER NOT NULL
);

CREATE TABLE courses (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL
);

INSERT INTO students (name) VALUES
('Emma'),
('David');

INSERT INTO enrollments (student_id, course_id) VALUES
(1, 101),
(2, 102);

INSERT INTO courses (id, name) VALUES
(101, 'Math'),
(102, 'Science');

SELECT students.name, courses.name
FROM students
INNER JOIN enrollments ON students.id = enrollments.student_id
INNER JOIN courses ON enrollments.course_id = courses.id;



-- LEFT JOIN
SELECT customers.name, orders.order_id, orders.total_amount 
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id;

SELECT employees.name, departments.dept_name
FROM employees
LEFT JOIN departments ON employees.dept_id = departments.dept_id;


INSERT INTO students (name) VALUES ('Lisa');

SELECT students.name, courses.name
FROM students
LEFT JOIN enrollments ON students.id = enrollments.student_id
LEFT JOIN courses ON enrollments.course_id = courses.id;



-- RIGHT JOIN
INSERT INTO orders (order_id, total_amount) VALUES (104, 300.00);

SELECT orders.order_id, orders.total_amount, customers.name
FROM customers
RIGHT JOIN orders ON customers.customer_id = orders.customer_id;


INSERT INTO departments (dept_id, dept_name) VALUES (40, 'Finance');

SELECT employees.name, departments.dept_name
FROM employees
RIGHT JOIN departments ON employees.dept_id = departments.dept_id;


INSERT INTO courses (id, name) VALUES (103, 'History');

SELECT students.name, courses.name
FROM students
RIGHT JOIN enrollments ON students.id = enrollments.student_id
RIGHT JOIN courses ON enrollments.course_id = courses.id;



-- FULL JOIN
INSERT INTO customers (name, email) VALUES ('Carol', 'carol@email.com');
INSERT INTO orders (order_id, total_amount) VALUES (105, 180.00);

SELECT customers.name, orders.order_id, orders.total_amount
FROM customers
FULL JOIN orders ON customers.customer_id = orders.customer_id;


INSERT INTO employees (name) VALUES ('Clark');

SELECT employees.name, employees.dept_id, departments.dept_name
FROM employees
FULL JOIN departments ON employees.dept_id = departments.dept_id;


SELECT students.name, courses.name
FROM students
FULL JOIN enrollments ON students.id = enrollments.student_id
FULL JOIN courses ON enrollments.course_id = courses.id;