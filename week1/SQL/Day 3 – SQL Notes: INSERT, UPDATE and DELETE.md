# Day 3 – SQL Notes: INSERT, UPDATE and DELETE

**Date:** 5 November 2026  
**Week:** 1  
**Database:** PostgreSQL  
**Topics:** SQL basics, INSERT, UPDATE, DELETE, WHERE, Transactions, COMMIT and ROLLBACK.

---

# 1. What is SQL?

SQL stands for **Structured Query Language**.

It is used to communicate with relational databases.

We use SQL to:

1. Insert new records.
2. Retrieve existing records.
3. Update existing records.
4. Delete records.
5. Manage database information.

### Example

Imagine a college database containing a `students` table.

| id | name | age | department |
|---:|---|---:|---|
| 1 | Arun | 21 | ISE |
| 2 | Rahul | 22 | CSE |
| 3 | Kiran | 20 | ECE |

We can use SQL to add, modify and delete student records.

---

# 2. What is a Database Table?

A table stores data in rows and columns.

Example:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50)
);
```

### Explanation

| SQL | Meaning |
|---|---|
| CREATE TABLE | Creates a new table |
| id | Student ID column |
| INT | Integer data type |
| PRIMARY KEY | Uniquely identifies each row |
| VARCHAR(100) | Stores text up to 100 characters |

A row represents one record, and a column represents one attribute.

---

# 3. INSERT – Add New Records

The `INSERT` command adds new records into a database table.

### Syntax

```sql
INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);
```

### Example

```sql
INSERT INTO students (id, name, age, department)
VALUES (4, 'Chethan', 22, 'ISE');
```

This adds a new student record.

### Result

| id | name | age | department |
|---:|---|---:|---|
| 4 | Chethan | 22 | ISE |

### Insert Multiple Records

We can insert multiple records using one INSERT statement.

```sql
INSERT INTO students (id, name, age, department)
VALUES
(5, 'Manoj', 21, 'CSE'),
(6, 'Vijay', 23, 'ECE');
```

### Important Points

- Text values must be inside single quotes.
- Numeric values normally do not need quotes.
- Values must match the specified column order and data types.
- Primary key values must be unique.

---

# 4. UPDATE – Modify Existing Records

The `UPDATE` command changes existing records in a table.

### Syntax

```sql
UPDATE table_name
SET column_name = new_value
WHERE condition;
```

### Example

Suppose Rahul's age changes from 22 to 23.

```sql
UPDATE students
SET age = 23
WHERE id = 2;
```

Now Rahul's record becomes:

| id | name | age | department |
|---:|---|---:|---|
| 2 | Rahul | 23 | CSE |

### Update Multiple Columns

```sql
UPDATE students
SET age = 24,
    department = 'ISE'
WHERE id = 2;
```

This changes both age and department for the student whose ID is 2.

### Why is WHERE Important?

Consider:

```sql
UPDATE students
SET department = 'ISE';
```

This updates the department of every row in the table.

**Important:** Always check your WHERE condition before executing an UPDATE query.

---

# 5. DELETE – Remove Existing Records

The `DELETE` command removes records from a table.

### Syntax

```sql
DELETE FROM table_name
WHERE condition;
```

### Example

Delete the student whose ID is 3.

```sql
DELETE FROM students
WHERE id = 3;
```

The record with ID 3 is removed.

### Important Warning

Never casually execute:

```sql
DELETE FROM students;
```

This deletes all rows from the table.

The table structure remains, but its records are removed.

Always verify your WHERE condition before deleting records.

---

# 6. Difference Between INSERT, UPDATE and DELETE

| Command | Purpose | Example |
|---|---|---|
| INSERT | Add records | Add a new student |
| UPDATE | Modify records | Change student age |
| DELETE | Remove records | Delete a student |

These three commands belong to SQL's **Data Manipulation Language (DML)**.

---

# 7. WHERE Clause

The `WHERE` clause specifies which records should be affected by a SQL statement.

It is commonly used with SELECT, UPDATE and DELETE.

### Example 1: Select a particular student

```sql
SELECT *
FROM students
WHERE id = 2;
```

### Example 2: Update a particular student

```sql
UPDATE students
SET age = 25
WHERE id = 2;
```

### Example 3: Delete a particular student

```sql
DELETE FROM students
WHERE id = 2;
```

### Common Operators Used with WHERE

| Operator | Meaning |
|---|---|
| `=` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `AND` | Both conditions must be true |
| `OR` | At least one condition must be true |

### Example Using AND

```sql
SELECT *
FROM students
WHERE age > 20 AND department = 'ISE';
```

This selects students older than 20 who belong to ISE.

### Example Using OR

```sql
SELECT *
FROM students
WHERE department = 'ISE' OR department = 'CSE';
```

This selects students from either ISE or CSE.

---

# 8. Transactions in SQL

A transaction allows us to group database operations so they can be committed or rolled back together.

Transactions help protect database consistency.

### Important Transaction Commands

1. BEGIN
2. COMMIT
3. ROLLBACK

### 8.1 BEGIN

Starts a transaction.

```sql
BEGIN;
```

### 8.2 COMMIT

Saves the changes made in the current transaction.

```sql
COMMIT;
```

### 8.3 ROLLBACK

Cancels uncommitted changes made in the current transaction.

```sql
ROLLBACK;
```

---

# 9. Safe SQL Execution Using Transactions

Suppose we want to update Rahul's age.

We can first start a transaction, perform the update and verify the result before committing.

```sql
BEGIN;

UPDATE students
SET age = 23
WHERE id = 2;

SELECT *
FROM students
WHERE id = 2;

COMMIT;
```

### What happens?

1. BEGIN starts the transaction.
2. UPDATE changes Rahul's age.
3. SELECT checks the updated record.
4. COMMIT saves the transaction.

### What if we find a mistake?

Before committing, we can execute:

```sql
ROLLBACK;
```

This cancels the uncommitted changes.

**Remember:**

- COMMIT = Save changes.
- ROLLBACK = Cancel uncommitted changes.

---

# 10. Complete Practical SQL Exercise

Let's create a students table and perform all the operations.

## Step 1: Create the table

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50)
);
```

## Step 2: Insert records

```sql
INSERT INTO students (id, name, age, department)
VALUES
(1, 'Arun', 21, 'ISE'),
(2, 'Rahul', 22, 'CSE'),
(3, 'Kiran', 20, 'ECE');
```

## Step 3: Display records

```sql
SELECT * FROM students;
```

Expected result:

| id | name | age | department |
|---:|---|---:|---|
| 1 | Arun | 21 | ISE |
| 2 | Rahul | 22 | CSE |
| 3 | Kiran | 20 | ECE |

## Step 4: Update Rahul's age

```sql
UPDATE students
SET age = 23
WHERE id = 2;
```

## Step 5: Update Kiran's department

```sql
UPDATE students
SET department = 'ISE'
WHERE id = 3;
```

## Step 6: Delete Arun's record

```sql
DELETE FROM students
WHERE id = 1;
```

## Step 7: Display final records

```sql
SELECT * FROM students;
```

Expected final result:

| id | name | age | department |
|---:|---|---:|---|
| 2 | Rahul | 23 | CSE |
| 3 | Kiran | 20 | ISE |

---

# 11. Important Interview Questions

### Q1. What is SQL?

SQL is a language used to communicate with relational databases.

### Q2. What is INSERT?

INSERT adds new records to a table.

### Q3. What is UPDATE?

UPDATE modifies existing records in a table.

### Q4. What is DELETE?

DELETE removes records from a table.

### Q5. Why do we use WHERE?

WHERE specifies which records should be affected by a query.

### Q6. What happens if we execute UPDATE without WHERE?

All rows in the table may be updated.

### Q7. What happens if we execute DELETE without WHERE?

All records in the table are deleted.

### Q8. What is a transaction?

A transaction is a group of database operations treated as one logical unit.

### Q9. What is COMMIT?

COMMIT permanently saves the changes made in the current transaction.

### Q10. What is ROLLBACK?

ROLLBACK cancels uncommitted changes made in the current transaction.

### Q11. What is the difference between DELETE and DROP?

DELETE removes records from a table, while DROP removes the database object itself, such as the entire table.

---

# 12. Common SQL Mistakes

1. Forgetting single quotes around text values.
2. Using an incorrect column name.
3. Inserting duplicate primary key values.
4. Forgetting the WHERE clause in UPDATE.
5. Forgetting the WHERE clause in DELETE.
6. Using the wrong data type.
7. Committing a transaction before checking the result.
8. Assuming ROLLBACK can undo changes after COMMIT.

---

# 13. Day 3 SQL Practice Checklist

- [ ] Understand SQL basics.
- [ ] Understand database tables, rows and columns.
- [ ] Understand CREATE TABLE.
- [ ] Practise INSERT.
- [ ] Practise inserting multiple records.
- [ ] Practise UPDATE.
- [ ] Practise updating multiple columns.
- [ ] Practise DELETE.
- [ ] Understand WHERE.
- [ ] Practise SELECT.
- [ ] Understand BEGIN.
- [ ] Understand COMMIT.
- [ ] Understand ROLLBACK.
- [ ] Create a students table.
- [ ] Insert three records.
- [ ] Update Rahul's age.
- [ ] Update Kiran's department.
- [ ] Delete Arun's record.
- [ ] Verify the final records.
- [ ] Save queries in `day-03-sql.sql`.

---

# 14. Quick Revision

| SQL command | Purpose |
|---|---|
| CREATE TABLE | Creates a table |
| INSERT | Adds records |
| SELECT | Retrieves records |
| UPDATE | Modifies records |
| DELETE | Removes records |
| WHERE | Filters records |
| BEGIN | Starts a transaction |
| COMMIT | Saves transaction changes |
| ROLLBACK | Cancels uncommitted changes |

**Day 3 SQL Goal:** Learn to insert, update and delete database records safely, understand transactions, and practise SQL queries using PostgreSQL.
