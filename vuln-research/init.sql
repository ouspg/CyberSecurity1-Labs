CREATE DATABASE company;
USE company;
CREATE TABLE employees (
    employee_id int NOT NULL, 
    name VARCHAR(50), 
    designation VARCHAR(20),
    PRIMARY KEY (employee_id)
);
CREATE TABLE tickets (
  ticket_id int NOT NULL,
  employee_id int,
  ticket TEXT,
  FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
INSERT INTO employees (employee_id, name, designation) VALUES
(1, 'Alice', 'Developer'),
(2, 'Bob', 'Manager'),
(3, 'Charlie', 'Designer');
INSERT INTO tickets (ticket_id, employee_id, ticket) VALUES
(1, 1, 'Fix bug in application'),
(2, 2, 'Review project plan'),
(3, 3, 'Design new logo'),
(4, 1, 'Update documentation'),
(5, 2, 'Conduct team meeting');