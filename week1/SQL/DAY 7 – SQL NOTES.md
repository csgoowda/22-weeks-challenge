
# Day 7 – SQL Notes: PRIMARY KEY and FOREIGN KEY

**Week:** 1  
**Topic:** SQL Database Fundamentals  
**Database:** SQLite  
**Project:** OptimalTaskPlanner

---

## 1. What is SQL?

SQL stands for Structured Query Language.

It is used to communicate with relational databases.

We use SQL to:
- Create database tables.
- Insert records.
- Retrieve data.
- Update existing records.
- Delete records.
- Connect multiple tables.
- Maintain data integrity.

Example:

```sql
SELECT * FROM machines;
```

---

## 2. What is a PRIMARY KEY?

A PRIMARY KEY uniquely identifies each row in a database table.

### Rules

1. Must contain unique values.
2. Cannot contain NULL.
3. A table can have only one PRIMARY KEY constraint.
4. It can consist of multiple columns (composite primary key).

### Example

```sql
CREATE TABLE machines (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100)
);
```

Here, `id` is the PRIMARY KEY.

### Insert records

```sql
INSERT INTO machines VALUES (1, 'CNC Machine');
INSERT INTO machines VALUES (2, 'Lathe Machine');
INSERT INTO machines VALUES (3, 'Drilling Machine');
```

Trying to insert another record with ID 1 will fail because the ID already exists.

---

## 3. What is a FOREIGN KEY?

A FOREIGN KEY is a column or group of columns that references a key in another table.

It establishes relationships between tables and maintains referential integrity.

### Example

**machines table**

| id | name |
|---|---|
| 1 | CNC Machine |
| 2 | Lathe Machine |
| 3 | Drilling Machine |

**tasks table**

| id | name | machine_id |
|---|---|---|
| 1 | Cutting | 1 |
| 2 | Turning | 2 |
| 3 | Drilling | 3 |

Here:
- `machines.id` is the PRIMARY KEY.
- `tasks.machine_id` is the FOREIGN KEY.
- `machine_id` references `machines.id`.

### SQL code

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    machine_id INTEGER,
    FOREIGN KEY (machine_id)
        REFERENCES machines(id)
);
```

### What does a FOREIGN KEY prevent?

```sql
INSERT INTO tasks (id, name, machine_id)
VALUES (4, 'Welding', 99);
```

This insertion fails because machine ID 99 does not exist, provided foreign-key enforcement is enabled.

A FOREIGN KEY prevents invalid references to parent records.

A FOREIGN KEY can contain NULL unless NOT NULL is specified.

---

## 4. PRIMARY KEY vs FOREIGN KEY

| PRIMARY KEY | FOREIGN KEY |
|---|---|
| Uniquely identifies a row | References a key in another table |
| Cannot contain NULL | Can contain NULL unless NOT NULL |
| Must be unique | Values can repeat |
| One PRIMARY KEY constraint per table | Multiple FOREIGN KEY constraints allowed |
| Identifies records | Connects related records |

---

## 5. Complete Database Implementation

First, enable foreign-key enforcement in SQLite.

```sql
PRAGMA foreign_keys = ON;
```

### Create machines table

```sql
CREATE TABLE machines (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

### Create tasks table

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    machine_id INTEGER,
    FOREIGN KEY (machine_id)
        REFERENCES machines(id)
);
```

### Insert machines

```sql
INSERT INTO machines (id, name)
VALUES
(1, 'CNC Machine'),
(2, 'Lathe Machine'),
(3, 'Drilling Machine');
```

### Insert tasks

```sql
INSERT INTO tasks (id, name, machine_id)
VALUES
(1, 'Cutting', 1),
(2, 'Turning', 2),
(3, 'Drilling', 3);
```

---

## 6. SQL Queries

### Query 1: Display all machines

```sql
SELECT * FROM machines;
```

### Query 2: Display all tasks

```sql
SELECT * FROM tasks;
```

### Query 3: Connect two tables using JOIN

```sql
SELECT
    tasks.id,
    tasks.name AS task_name,
    machines.name AS machine_name
FROM tasks
JOIN machines
ON tasks.machine_id = machines.id;
```

**Explanation:**
- JOIN combines related records.
- ON specifies the matching condition.
- `tasks.machine_id` matches `machines.id`.

### Query 4: Find tasks assigned to CNC Machine

```sql
SELECT *
FROM tasks
WHERE machine_id = 1;
```

### Query 5: Count tasks per machine

```sql
SELECT
    machines.name,
    COUNT(tasks.id) AS total_tasks
FROM machines
LEFT JOIN tasks
ON machines.id = tasks.machine_id
GROUP BY machines.id, machines.name;
```

**Explanation:**
- LEFT JOIN returns all machines, including those without tasks.
- COUNT calculates the number of tasks.
- GROUP BY groups tasks by machine.

---

## 7. Important SQL Commands

### CREATE

Creates a table.

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100)
);
```

### INSERT

Adds new records.

```sql
INSERT INTO students (id, name)
VALUES (1, 'Rahul');
```

### SELECT

Retrieves records.

```sql
SELECT * FROM students;
```

### WHERE

Filters records.

```sql
SELECT *
FROM students
WHERE id = 1;
```

### UPDATE

Modifies existing records.

```sql
UPDATE students
SET name = 'Arun'
WHERE id = 1;
```

### DELETE

Deletes records.

```sql
DELETE FROM students
WHERE id = 1;
```

### JOIN

Retrieves related information from multiple tables.

```sql
SELECT *
FROM tasks
JOIN machines
ON tasks.machine_id = machines.id;
```

---

## 8. What is Referential Integrity?

Referential integrity ensures that relationships between database tables remain valid.

Example:

A task cannot reference machine ID 99 if machine ID 99 does not exist.

This is enforced using a FOREIGN KEY constraint.

It prevents invalid relationships and maintains consistent database records.

---

## 9. Real-World Example: OptimalTaskPlanner

In my OptimalTaskPlanner project:

- A machine can have multiple tasks.
- Every task can be assigned to a machine.
- Each machine has a unique ID.
- Each task has its own unique ID.
- The task's `machine_id` references the machines table.

This represents a ONE-TO-MANY relationship.

**Relationship:**

One Machine → Many Tasks

Example:

CNC Machine:
- Cutting
- Drilling
- Milling

All these tasks can reference the same machine ID.

---

## 10. Interview Questions and Answers

**Q1. What is a PRIMARY KEY?**

A PRIMARY KEY uniquely identifies each row in a database table. It cannot contain NULL or duplicate values.

**Q2. What is a FOREIGN KEY?**

A FOREIGN KEY creates a relationship between tables by referencing a key in another table.

**Q3. Can a PRIMARY KEY contain duplicate values?**

No. Primary key values must be unique.

**Q4. Can a FOREIGN KEY contain duplicate values?**

Yes. Multiple records can reference the same parent record.

**Q5. Can a FOREIGN KEY contain NULL?**

Yes, unless the column has a NOT NULL constraint.

**Q6. What happens when we insert an invalid FOREIGN KEY value?**

The database rejects the insertion when foreign-key enforcement is enabled.

**Q7. What is JOIN?**

JOIN combines related records from multiple tables based on a matching condition.

**Q8. What is a ONE-TO-MANY relationship?**

One record in a parent table can be associated with multiple records in a child table.

Example: One machine can have multiple tasks.

**Q9. What is the difference between DELETE and DROP?**

- DELETE removes records from a table.
- DROP removes the entire table structure and its data.

**Q10. Why do we use a database?**

To store, manage, retrieve and maintain application data efficiently.

---

## 11. Day 7 SQL Summary

| Concept | What I learned |
|---|---|
| SQL | Communicating with relational databases |
| PRIMARY KEY | Uniquely identifies records |
| FOREIGN KEY | Connects related tables |
| INSERT | Adds records |
| SELECT | Retrieves records |
| WHERE | Filters records |
| UPDATE | Modifies records |
| DELETE | Deletes records |
| JOIN | Combines related tables |
| GROUP BY | Groups records |
| COUNT | Counts records |
| Referential Integrity | Maintains valid relationships |

---

## 12. Completion Checklist

- [x] Understand PRIMARY KEY.
- [x] Understand FOREIGN KEY.
- [x] Create machines table.
- [x] Create tasks table.
- [x] Insert three machines.
- [x] Insert three tasks.
- [x] Understand JOIN.
- [x] Write five SQL queries.
- [x] Answer three SQL checkpoint questions.

**Day 7 SQL learning completed.**

---

*12-Week Job Preparation Plan | Python Backend Developer*
