DAY 7 – SQL NOTES

Topic: PRIMARY KEY and FOREIGN KEY

1. What is SQL?

SQL stands for Structured Query Language.

SQL is used to communicate with relational databases.

We use SQL to:

- Create tables.
- Insert data.
- Read data.
- Update data.
- Delete data.
- Connect multiple tables.

Example:

SELECT * FROM machines;

This retrieves all records from the machines table.

---

2. What is a Database?

A database is an organized collection of data.

Example: A factory database may contain:

- Machines
- Tasks
- Employees
- Production records

3. What is a Table?

A table stores data in rows and columns.

Example: machines table

id| name
1| CNC Machine
2| Lathe Machine
3| Drilling Machine

- Column: A field in a table.
- Row: One complete record.
- Cell: One individual value.

---

4. What is a PRIMARY KEY?

A PRIMARY KEY uniquely identifies each row in a table.

Example:

CREATE TABLE machines (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100)
);

Here, "id" is the PRIMARY KEY.

Rules:

1. A primary key cannot contain duplicate values.
2. A primary key cannot contain NULL.
3. A table can have only one primary key constraint.
4. A primary key can consist of one or multiple columns (composite primary key).

Example:

INSERT INTO machines VALUES (1, 'CNC Machine');
INSERT INTO machines VALUES (2, 'Lathe Machine');

The following is invalid because ID 1 already exists:

INSERT INTO machines VALUES (1, 'Drilling Machine');

5. What is a FOREIGN KEY?

A FOREIGN KEY connects two tables.

It references a PRIMARY KEY or another eligible unique key in the parent table.

Example:

Parent table: machines

id| name
1| CNC Machine
2| Lathe Machine
3| Drilling Machine

Child table: tasks

id| name| machine_id
1| Cutting| 1
2| Turning| 2
3| Drilling| 3

Here:

- "machines.id" is the PRIMARY KEY.
- "tasks.machine_id" is the FOREIGN KEY.

SQL:

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    machine_id INTEGER,
    FOREIGN KEY (machine_id)
        REFERENCES machines(id)
);

Rules:

1. A foreign key must reference an existing key value in the parent table.
2. A foreign key can contain duplicate values.
3. A foreign key can contain NULL unless NOT NULL is specified.
4. A table can have multiple foreign keys.
5. Foreign keys maintain referential integrity.

Important: SQLite requires foreign-key enforcement to be enabled using:

PRAGMA foreign_keys = ON;

---

6. Difference Between PRIMARY KEY and FOREIGN KEY

PRIMARY KEY| FOREIGN KEY
Uniquely identifies a row| Connects tables
Cannot contain NULL| Can contain NULL by default
Cannot contain duplicates| Can contain duplicates
One primary key constraint per table| Multiple foreign keys allowed
Identifies records| Maintains relationships

---

7. Complete SQL Implementation

Create machines table:

CREATE TABLE machines (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

Create tasks table:

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    machine_id INTEGER,
    FOREIGN KEY (machine_id)
        REFERENCES machines(id)
);

Insert machines:

INSERT INTO machines VALUES (1, 'CNC Machine');
INSERT INTO machines VALUES (2, 'Lathe Machine');
INSERT INTO machines VALUES (3, 'Drilling Machine');

Insert tasks:

INSERT INTO tasks VALUES (1, 'Cutting', 1);
INSERT INTO tasks VALUES (2, 'Turning', 2);
INSERT INTO tasks VALUES (3, 'Drilling', 3);

---

8. Important SQL Queries

Query 1: Display all machines.

SELECT * FROM machines;

Query 2: Display all tasks.

SELECT * FROM tasks;

Query 3: Find a particular machine.

SELECT * FROM machines
WHERE id = 1;

Query 4: Connect machines and tasks using JOIN.

SELECT
    tasks.name,
    machines.name AS machine_name
FROM tasks
JOIN machines
ON tasks.machine_id = machines.id;

Query 5: Find tasks assigned to CNC Machine.

SELECT *
FROM tasks
WHERE machine_id = 1;

Query 6: Count tasks per machine.

SELECT
    machines.name,
    COUNT(tasks.id) AS total_tasks
FROM machines
LEFT JOIN tasks
ON machines.id = tasks.machine_id
GROUP BY machines.id, machines.name;

---

9. What is a JOIN?

JOIN is used to retrieve related data from multiple tables.

Common JOIN types:

1. INNER JOIN – Returns matching records from both tables.
2. LEFT JOIN – Returns all records from the left table and matching records from the right table.
3. RIGHT JOIN – Returns all records from the right table and matching records from the left table.
4. FULL OUTER JOIN – Returns matching and non-matching records from both tables.

Example:

SELECT *
FROM tasks
INNER JOIN machines
ON tasks.machine_id = machines.id;

---

10. What is Referential Integrity?

Referential integrity ensures that relationships between database tables remain valid.

Example:

Machine IDs available:
1, 2, 3.

This is valid:

INSERT INTO tasks VALUES (4, 'Welding', 2);

This is invalid:

INSERT INTO tasks VALUES (5, 'Painting', 99);

Why?

Machine ID 99 does not exist in the machines table.

The FOREIGN KEY constraint rejects the invalid insertion when enforcement is enabled.

---

11. Important Interview Questions

Q1. What is SQL?
Answer: SQL is a language used to communicate with relational databases.

Q2. What is a PRIMARY KEY?
Answer: A primary key uniquely identifies each record in a table.

Q3. What is a FOREIGN KEY?
Answer: A foreign key creates a relationship between two tables and maintains referential integrity.

Q4. Can a PRIMARY KEY contain duplicate values?
Answer: No.

Q5. Can a FOREIGN KEY contain duplicate values?
Answer: Yes.

Q6. Can a FOREIGN KEY contain NULL?
Answer: Yes, unless NOT NULL is specified.

Q7. What happens if we insert an invalid FOREIGN KEY?
Answer: The database rejects the insertion when foreign-key enforcement is enabled.

Q8. What is the difference between PRIMARY KEY and FOREIGN KEY?
Answer: A primary key identifies records, while a foreign key connects tables.

Q9. What is JOIN?
Answer: JOIN retrieves related records from multiple tables.

Q10. What is referential integrity?
Answer: It ensures that foreign-key references remain valid.

---

12. Quick Revision

PRIMARY KEY = Unique identification.

FOREIGN KEY = Relationship between tables.

JOIN = Retrieve data from multiple tables.

NULL = Missing or unknown value.

UNIQUE = Prevents duplicate values.

NOT NULL = Value is mandatory.

WHERE = Filters records.

GROUP BY = Groups records.

COUNT() = Counts records.

Day 7 SQL Learning Goal

You should be able to:

- Explain PRIMARY KEY.
- Explain FOREIGN KEY.
- Create related database tables.
- Insert records into both tables.
- Write SELECT queries.
- Use JOIN.
- Explain referential integrity.

End of Day 7 SQL Notes.