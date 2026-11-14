
# Day 5 – SQL Notes: NULL, IS NULL and COALESCE()

## 1. What is SQL?

SQL stands for **Structured Query Language**.

SQL is used to communicate with relational databases.

We use SQL to:
- Retrieve data.
- Insert new records.
- Update existing records.
- Delete records.
- Filter and organize data.

Examples of SQL databases:
- MySQL
- PostgreSQL
- SQLite
- Oracle Database
- Microsoft SQL Server

---

## 2. What is NULL in SQL?

`NULL` represents a missing, unknown, or unavailable value in a database.

It does not mean:
- Zero (0).
- Empty string ('').
- False.

### Example: Employees Table

| emp_id | name | salary | department |
|---|---|---:|---|
| 101 | Rahul | 30000 | IT |
| 102 | Anil | NULL | HR |
| 103 | Kiran | 40000 | NULL |
| 104 | Ravi | NULL | IT |
| 105 | Arun | 35000 | Sales |

In this table:
- Anil's salary is missing.
- Kiran's department is missing.
- Ravi's salary is missing.

These missing values are represented by `NULL`.

### Important

We cannot check NULL using:

```sql
WHERE salary = NULL;
```

This is incorrect because NULL represents an unknown value.

We must use `IS NULL`.

---

## 3. IS NULL

`IS NULL` is used to find records where a column contains NULL values.

### Syntax

```sql
SELECT column_name
FROM table_name
WHERE column_name IS NULL;
```

### Example 1: Find employees with missing salaries

```sql
SELECT *
FROM employees
WHERE salary IS NULL;
```

Expected result:

| emp_id | name | salary | department |
|---|---|---|---|
| 102 | Anil | NULL | HR |
| 104 | Ravi | NULL | IT |

### Example 2: Find employees without a department

```sql
SELECT *
FROM employees
WHERE department IS NULL;
```

Expected result:

| emp_id | name | salary | department |
|---|---|---:|---|
| 103 | Kiran | 40000 | NULL |

---

## 4. IS NOT NULL

`IS NOT NULL` is used to find records where a column has a value.

### Syntax

```sql
SELECT column_name
FROM table_name
WHERE column_name IS NOT NULL;
```

### Example 1: Find employees whose salary is available

```sql
SELECT *
FROM employees
WHERE salary IS NOT NULL;
```

Expected result:

| emp_id | name | salary | department |
|---|---|---:|---|
| 101 | Rahul | 30000 | IT |
| 103 | Kiran | 40000 | NULL |
| 105 | Arun | 35000 | Sales |

### Example 2: Find employees who have a department

```sql
SELECT *
FROM employees
WHERE department IS NOT NULL;
```

---

## 5. COALESCE()

`COALESCE()` returns the first non-NULL value from the given list of expressions.

It is useful when we want to replace missing values with a default value.

### Syntax

```sql
COALESCE(value1, value2, value3, ...);
```

It checks values from left to right and returns the first value that is not NULL.

### Example 1

```sql
SELECT COALESCE(NULL, 10, 20);
```

Output:

```text
10
```

Why?

- First value is NULL.
- Second value is 10.
- 10 is the first non-NULL value.

### Example 2: Replace missing salary with zero

```sql
SELECT
    name,
    COALESCE(salary, 0) AS salary
FROM employees;
```

Expected result:

| name | salary |
|---|---:|
| Rahul | 30000 |
| Anil | 0 |
| Kiran | 40000 |
| Ravi | 0 |
| Arun | 35000 |

Here, missing salaries are displayed as zero.

Important: This query only changes the displayed result. It does not update the original table.

### Example 3: Replace missing department

```sql
SELECT
    name,
    COALESCE(department, 'Not Assigned') AS department
FROM employees;
```

Expected result:

| name | department |
|---|---|
| Rahul | IT |
| Anil | HR |
| Kiran | Not Assigned |
| Ravi | IT |
| Arun | Sales |

---

## 6. COUNT() and NULL

SQL provides aggregate functions such as COUNT() to count records.

There is an important difference between `COUNT(*)` and `COUNT(column_name)`.

### COUNT(*)

Counts all rows in a table, including rows containing NULL values.

```sql
SELECT COUNT(*)
FROM employees;
```

Output:

```text
5
```

### COUNT(salary)

Counts only the rows where salary is not NULL.

```sql
SELECT COUNT(salary)
FROM employees;
```

Output:

```text
3
```

Why?

There are five employees, but only three have a salary value.

### Difference

| Query | Meaning |
|---|---|
| COUNT(*) | Counts all rows |
| COUNT(salary) | Counts non-NULL salary values |

---

## 7. Complete SQL Practice

Use the following sample table for practice.

### Create the employees table

```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    department VARCHAR(50)
);
```

### Insert sample records

```sql
INSERT INTO employees
(emp_id, name, salary, department)
VALUES
(101, 'Rahul', 30000, 'IT'),
(102, 'Anil', NULL, 'HR'),
(103, 'Kiran', 40000, NULL),
(104, 'Ravi', NULL, 'IT'),
(105, 'Arun', 35000, 'Sales');
```

### Query 1: Display all employees

```sql
SELECT * FROM employees;
```

### Query 2: Find employees with NULL salaries

```sql
SELECT *
FROM employees
WHERE salary IS NULL;
```

### Query 3: Find employees with available salaries

```sql
SELECT *
FROM employees
WHERE salary IS NOT NULL;
```

### Query 4: Replace NULL salary with zero

```sql
SELECT
    name,
    COALESCE(salary, 0) AS salary
FROM employees;
```

### Query 5: Replace NULL department

```sql
SELECT
    name,
    COALESCE(department, 'Not Assigned') AS department
FROM employees;
```

### Query 6: Count all employees

```sql
SELECT COUNT(*)
FROM employees;
```

### Query 7: Count employees with available salaries

```sql
SELECT COUNT(salary)
FROM employees;
```

---

## 8. Important Differences

| Concept | Purpose |
|---|---|
| NULL | Represents missing or unknown data |
| IS NULL | Finds missing values |
| IS NOT NULL | Finds available values |
| COALESCE() | Returns the first non-NULL value |
| COUNT(*) | Counts all rows |
| COUNT(column) | Counts non-NULL values in a column |

---

## 9. Common Mistakes

### Mistake 1: Using = NULL

Incorrect:

```sql
SELECT *
FROM employees
WHERE salary = NULL;
```

Correct:

```sql
SELECT *
FROM employees
WHERE salary IS NULL;
```

### Mistake 2: Confusing NULL with zero

NULL means the value is missing or unknown.

Zero is an actual numeric value.

### Mistake 3: Thinking COALESCE updates the table

`COALESCE()` in a SELECT statement changes the displayed result, not the stored data.

---

## 10. Interview Questions

### Q1. What is NULL in SQL?

NULL represents a missing, unknown, or unavailable value in a database.

### Q2. How do you find NULL values?

Use `IS NULL`.

```sql
SELECT *
FROM employees
WHERE salary IS NULL;
```

### Q3. What is the difference between IS NULL and IS NOT NULL?

- IS NULL finds missing values.
- IS NOT NULL finds available values.

### Q4. What is COALESCE()?

COALESCE() returns the first non-NULL value from a list of expressions.

### Q5. What is the difference between COUNT(*) and COUNT(column)?

- COUNT(*) counts all rows.
- COUNT(column) ignores NULL values in that column.

### Q6. Does COALESCE permanently update NULL values?

No. It only changes the value displayed by that query. To permanently update records, use UPDATE.

---

## 11. Practice Questions

Try answering these without looking at the notes.

1. Which SQL condition finds employees with missing salaries?
2. What is the output of `COALESCE(NULL, 10, 20)`?
3. What is the difference between NULL and zero?
4. What does `COUNT(salary)` count?
5. What does `COUNT(*)` count?
6. Write a query to find employees whose department is NULL.
7. Write a query to display NULL salaries as zero.
8. Write a query to replace NULL departments with 'Not Assigned'.

---

## 12. Learning Checklist

- [ ] Understand NULL.
- [ ] Understand IS NULL.
- [ ] Understand IS NOT NULL.
- [ ] Understand COALESCE().
- [ ] Understand COUNT(*) and COUNT(column).
- [ ] Create the employees table.
- [ ] Insert the sample records.
- [ ] Write and run all five required queries.
- [ ] Answer the practice questions.
- [ ] Save the SQL file in GitHub.

## Day 5 SQL Summary

Today I learned:

1. NULL represents missing or unknown data.
2. IS NULL finds missing values.
3. IS NOT NULL finds available values.
4. COALESCE() replaces NULL in query results with a chosen fallback value.
5. COUNT(*) counts all rows, while COUNT(column) ignores NULL values.

**Practice file:** `day-05-sql-null-practice.sql`

**Notes file:** `day-05-sql-null-practice.md`
