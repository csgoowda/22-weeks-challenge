
# Day 5 – DBMS Notes: Types of Keys

## 1. What is DBMS?

DBMS stands for **Database Management System**.

It is software used to store, manage, retrieve, and update data in a database.

Examples:
- MySQL
- PostgreSQL
- Oracle Database
- Microsoft SQL Server
- SQLite

### What is a database?

A database is an organized collection of data.

Example: A college database can store:
- Student details
- Faculty details
- Department details
- Course details
- Marks

---

## 2. What is a Key in DBMS?

A key is a column or combination of columns used to identify records in a database table.

Keys help us:
- Identify each record uniquely.
- Avoid duplicate records.
- Connect multiple tables.
- Maintain relationships between tables.

Let's understand the different types of keys.

---

## 3. Primary Key

A **Primary Key** is a column or combination of columns that uniquely identifies each row in a table.

### Rules

1. Every value must be unique.
2. It cannot contain NULL values.
3. A table can have only one primary key constraint.
4. A primary key can contain one or multiple columns.

### Example

| Student_ID | Name | Email |
|---|---|---|
| 101 | Rahul | rahul@gmail.com |
| 102 | Anil | anil@gmail.com |
| 103 | Kiran | kiran@gmail.com |

Here, `Student_ID` is the Primary Key.

Why?

- Every student has a unique ID.
- No two students have the same ID.
- The ID cannot be NULL.

### SQL Example

```sql
CREATE TABLE Students (
    Student_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Email VARCHAR(100)
);
```

---

## 4. Candidate Key

A **Candidate Key** is a column or a minimal combination of columns that can uniquely identify each row in a table.

A table can have multiple candidate keys.

### Example

| Student_ID | Email | Name |
|---|---|---|
| 101 | a@gmail.com | Rahul |
| 102 | b@gmail.com | Anil |
| 103 | c@gmail.com | Kiran |

Possible Candidate Keys:
- Student_ID
- Email

Both can uniquely identify a student.

### Important

A candidate key must be:
- Unique.
- Minimal (no unnecessary column).

---

## 5. Alternate Key

An **Alternate Key** is a candidate key that is not selected as the Primary Key.

### Example

Suppose we have two candidate keys:

- Student_ID
- Email

If we select `Student_ID` as the Primary Key, then `Email` becomes the Alternate Key.

### Remember

Candidate Keys = All possible minimal unique identifiers.

Primary Key = The selected candidate key.

Alternate Key = The remaining candidate key(s).

---

## 6. Foreign Key

A **Foreign Key** is a column or combination of columns in one table that references a key in another table.

It is used to establish relationships between tables.

### Example

**Departments Table**

| Department_ID | Department_Name |
|---|---|
| 1 | ISE |
| 2 | CSE |
| 3 | ECE |

**Students Table**

| Student_ID | Name | Department_ID |
|---|---|---|
| 101 | Rahul | 1 |
| 102 | Anil | 2 |
| 103 | Kiran | 1 |

Here:
- `Department_ID` in Departments is the Primary Key.
- `Department_ID` in Students is the Foreign Key.

The foreign key connects each student to a department.

### SQL Example

```sql
CREATE TABLE Departments (
    Department_ID INT PRIMARY KEY,
    Department_Name VARCHAR(50)
);

CREATE TABLE Students (
    Student_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department_ID INT,
    FOREIGN KEY (Department_ID)
        REFERENCES Departments(Department_ID)
);
```

### Important

A foreign key:
- Connects two tables.
- Can contain duplicate values.
- Can contain NULL values unless restricted.
- Must reference an eligible key in the parent table.

---

## 7. Composite Key

A **Composite Key** is a key made using two or more columns together to uniquely identify a record.

### Example

**Enrollment Table**

| Student_ID | Course_ID | Semester |
|---|---|---|
| 101 | C01 | 5 |
| 101 | C02 | 5 |
| 102 | C01 | 5 |
| 102 | C03 | 5 |

Here:
- Student_ID alone is not unique.
- Course_ID alone is not unique.
- Together, Student_ID and Course_ID identify an enrollment record uniquely.

Therefore, `(Student_ID, Course_ID)` is a Composite Key.

### SQL Example

```sql
CREATE TABLE Enrollment (
    Student_ID INT,
    Course_ID VARCHAR(10),
    Semester INT,
    PRIMARY KEY (Student_ID, Course_ID)
);
```

---

## 8. Difference Between DBMS Keys

| Key | Meaning |
|---|---|
| Primary Key | Selected key that uniquely identifies each row |
| Candidate Key | Minimal column or combination that can uniquely identify a row |
| Alternate Key | Candidate key not selected as the Primary Key |
| Foreign Key | References a key in another table |
| Composite Key | Uses two or more columns together as a key |

---

## 9. Quick Example to Remember All Keys

Consider a Students table:

| Student_ID | Email | Name | Department_ID |
|---|---|---|---|
| 101 | a@gmail.com | Rahul | 1 |
| 102 | b@gmail.com | Anil | 2 |
| 103 | c@gmail.com | Kiran | 1 |

Assume:
- Student_ID and Email are both unique.
- Student_ID is selected as the Primary Key.
- Department_ID references the Departments table.

Then:

- Primary Key: Student_ID
- Candidate Keys: Student_ID, Email
- Alternate Key: Email
- Foreign Key: Department_ID

For the Enrollment table, Student_ID and Course_ID together can form a Composite Key.

---

## 10. Interview Questions and Answers

### Q1. What is a Primary Key?
A Primary Key uniquely identifies each record in a table. It cannot contain NULL or duplicate values.

### Q2. What is a Candidate Key?
A Candidate Key is a minimal column or combination of columns that can uniquely identify a record.

### Q3. What is an Alternate Key?
An Alternate Key is a candidate key that was not selected as the Primary Key.

### Q4. What is a Foreign Key?
A Foreign Key is used to establish a relationship between two tables by referencing a key in another table.

### Q5. What is a Composite Key?
A Composite Key uses two or more columns together to uniquely identify a record.

### Q6. Can a table have multiple Candidate Keys?
Yes. A table can have multiple Candidate Keys, but only one Primary Key constraint.

### Q7. Can a Foreign Key contain duplicate values?
Yes. Multiple records can refer to the same parent record.

### Q8. Can a Primary Key contain NULL?
No. A Primary Key cannot contain NULL values.

---

## 11. Quick Revision

- Primary Key = Selected unique identifier.
- Candidate Key = Possible minimal unique identifier.
- Alternate Key = Candidate key not selected.
- Foreign Key = Connects tables.
- Composite Key = Two or more columns together.

---

## 12. Practice Questions

1. A student table has Student_ID and Email. Both are unique. If Student_ID is selected as Primary Key, what is Email?
2. Can a Foreign Key contain duplicate values?
3. Can a Primary Key contain NULL?
4. In an Enrollment table, Student_ID alone is not unique and Course_ID alone is not unique. What key can identify each enrollment?
5. What is the difference between a Candidate Key and an Alternate Key?

## Learning Checklist

- [ ] Understand Primary Key.
- [ ] Understand Candidate Key.
- [ ] Understand Alternate Key.
- [ ] Understand Foreign Key.
- [ ] Understand Composite Key.
- [ ] Practise the SQL table examples.
- [ ] Answer all five practice questions.
