
# Day 5 – Python Fundamentals and Production Task Tracker

## 1. Today's Learning Objectives

Today I learned:

- List comprehensions
- Dictionary comprehensions
- `sorted()` with `key`
- Lambda functions
- `pathlib` module
- File handling using `open()`
- Context managers using `with`
- File modes (`r`, `w`, `a`, `x`)
- CSV file handling
- `csv.DictReader()`
- `csv.DictWriter()`
- Building a CLI application
- Input validation using `try-except`

---

# 2. Project: Production Task Tracker v0

## Project Overview

Production Task Tracker is a Python command-line application used to manage production tasks and their estimated working hours.

### Features

1. Add a new production task.
2. Generate a unique task ID.
3. Save tasks permanently in a CSV file.
4. Display all saved tasks.
5. Sort tasks by estimated hours.
6. Export tasks into another CSV file.
7. Validate user input.
8. Handle invalid inputs without crashing.

## Project Structure

```text
production_task_tracker/
│
├── main.py
├── tasks.csv
└── tasks_export.csv
```

| File | Purpose |
|---|---|
| main.py | Main Python application |
| tasks.csv | Stores original task records |
| tasks_export.csv | Stores exported task records |

---

# 3. Python Modules

## A. pathlib

`pathlib` is a built-in Python module used to work with file and directory paths.

```python
from pathlib import Path

file = Path("tasks.csv")

print(file.exists())
```

### Important pathlib methods

| Method | Purpose |
|---|---|
| `Path.cwd()` | Gets current working directory |
| `.exists()` | Checks whether a path exists |
| `.is_file()` | Checks whether a path is a file |
| `.is_dir()` | Checks whether a path is a directory |
| `.mkdir()` | Creates a directory |

Example:

```python
from pathlib import Path

folder = Path("reports")

folder.mkdir(exist_ok=True)

file = folder / "report.csv"

print(file.exists())
```

`exist_ok=True` prevents an error if the directory already exists.

## B. csv

The `csv` module is used to read and write CSV files.

CSV means Comma-Separated Values.

Example:

```csv
id,name,hours,status
1,Python,3,Pending
2,SQL,2,Completed
```

Import:

```python
import csv
```

---

# 4. Variables and Constants

```python
DATA_FILE = Path("tasks.csv")

EXPORT_FILE = Path("tasks_export.csv")

FIELDNAMES = ["id", "name", "hours", "status"]
```

### Explanation

- `DATA_FILE`: Original task storage file.
- `EXPORT_FILE`: Exported task file.
- `FIELDNAMES`: Column names in the CSV file.

Uppercase names are commonly used for constants in Python.

---

# 5. Python Data Structures

## A. List

A list stores multiple values.

```python
names = ["Python", "SQL", "Java"]

print(names[0])
```

Output:

```text
Python
```

## B. Dictionary

A dictionary stores data using key-value pairs.

```python
task = {
    "id": 1,
    "name": "Python",
    "hours": 3,
    "status": "Pending"
}

print(task["name"])
```

Output:

```text
Python
```

## C. List of Dictionaries

Our project uses a list of dictionaries to store multiple tasks.

```python
tasks = [
    {"id": 1, "name": "Python", "hours": 3, "status": "Pending"},
    {"id": 2, "name": "SQL", "hours": 2, "status": "Completed"}
]
```

---

# 6. List Comprehensions

List comprehension provides a shorter way to create lists.

### Normal loop

```python
numbers = [1, 2, 3, 4]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)
```

### List comprehension

```python
numbers = [1, 2, 3, 4]

squares = [number ** 2 for number in numbers]

print(squares)
```

Output:

```text
[1, 4, 9, 16]
```

### General syntax

```python
new_list = [expression for item in iterable]
```

### List comprehension with condition

```python
even_numbers = [
    number for number in range(1, 11)
    if number % 2 == 0
]

print(even_numbers)
```

Output:

```text
[2, 4, 6, 8, 10]
```

### Production task example

```python
task_names = [task["name"] for task in tasks]
```

This extracts all task names from the list of dictionaries.

---

# 7. Dictionary Comprehensions

Dictionary comprehension creates dictionaries in a shorter way.

### Normal loop

```python
numbers = [1, 2, 3]

squares = {}

for number in numbers:
    squares[number] = number ** 2
```

### Dictionary comprehension

```python
squares = {
    number: number ** 2
    for number in numbers
}

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9}
```

### Difference

| List comprehension | Dictionary comprehension |
|---|---|
| Uses `[]` | Uses `{}` |
| Creates a list | Creates a dictionary |
| Stores values | Stores key-value pairs |

---

# 8. sorted() and key

The `sorted()` function sorts data and returns a new list.

Example:

```python
numbers = [5, 2, 8, 1]

result = sorted(numbers)

print(result)
```

Output:

```text
[1, 2, 5, 8]
```

### Descending order

```python
result = sorted(numbers, reverse=True)

print(result)
```

Output:

```text
[8, 5, 2, 1]
```

## Sorting dictionaries using key

```python
tasks = [
    {"name": "Machine maintenance", "hours": 5},
    {"name": "Quality inspection", "hours": 2},
    {"name": "Material planning", "hours": 4}
]

result = sorted(
    tasks,
    key=lambda task: task["hours"]
)

print(result)
```

The tasks are sorted by estimated hours.

### What is lambda?

A lambda is a small anonymous function.

Normal function:

```python
def get_hours(task):
    return task["hours"]
```

Lambda equivalent:

```python
lambda task: task["hours"]
```

In our project:

```python
tasks = sorted(
    tasks,
    key=lambda task: float(task["hours"])
)
```

`float()` converts the hours from CSV strings into numbers before sorting.

---

# 9. File Handling

Python uses the `open()` function to work with files.

## File modes

| Mode | Purpose |
|---|---|
| `r` | Read a file |
| `w` | Write and replace existing contents |
| `a` | Append data at the end |
| `x` | Create a new file; fail if it already exists |

### Read example

```python
with open("sample.txt", "r") as file:
    print(file.read())
```

### Write example

```python
with open("sample.txt", "w") as file:
    file.write("Hello Python")
```

### Append example

```python
with open("sample.txt", "a") as file:
    file.write("\nLearning Python")
```

## Why use with?

The `with` statement automatically closes the file after the block finishes.

```python
with open("sample.txt", "w") as file:
    file.write("Hello")
```

This is safer than manually opening and closing files.

---

# 10. CSV Handling

## A. DictReader()

`csv.DictReader()` reads CSV rows as dictionaries.

```python
with open("tasks.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

Example result:

```python
{
    "id": "1",
    "name": "Python",
    "hours": "3",
    "status": "Pending"
}
```

CSV values are normally returned as strings.

## B. DictWriter()

`csv.DictWriter()` writes dictionaries into CSV files.

```python
with open("tasks.csv", "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["id", "name", "hours", "status"]
    )

    writer.writeheader()

    writer.writerow({
        "id": 1,
        "name": "Python",
        "hours": 3,
        "status": "Pending"
    })
```

### Important methods

| Method | Purpose |
|---|---|
| `DictReader()` | Reads rows as dictionaries |
| `DictWriter()` | Writes dictionaries |
| `writeheader()` | Writes column names |
| `writerow()` | Writes one record |
| `writerows()` | Writes multiple records |

`newline=""` is recommended when opening CSV files.

---

# 11. Project Functions Explained

## Function 1: load_tasks()

Purpose: Read existing tasks from the CSV file.

```python
def load_tasks():

    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        return list(reader)
```

### Explanation

1. Checks whether tasks.csv exists.
2. If the file doesn't exist, returns an empty list.
3. Opens the file in read mode.
4. Uses DictReader to read CSV records.
5. Converts the reader into a list.
6. Returns the task records.

## Function 2: save_tasks()

Purpose: Save the updated task list into the CSV file.

```python
def save_tasks(tasks):

    with open(DATA_FILE, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=FIELDNAMES
        )

        writer.writeheader()
        writer.writerows(tasks)
```

### Explanation

1. Receives the task list.
2. Opens tasks.csv in write mode.
3. Creates a CSV dictionary writer.
4. Writes column headings.
5. Writes all task records.

## Function 3: add_task()

Purpose: Add a new production task.

```python
def add_task():

    tasks = load_tasks()

    name = input("Enter task name: ").strip()

    if not name:
        print("Task name cannot be empty")
        return

    try:
        hours = float(input("Enter estimated hours: "))

        if hours <= 0:
            print("Hours must be greater than zero")
            return

    except ValueError:
        print("Enter a valid number")
        return

    task_id = max(
        (int(task["id"]) for task in tasks),
        default=0
    ) + 1

    task = {
        "id": task_id,
        "name": name,
        "hours": hours,
        "status": "Pending"
    }

    tasks.append(task)

    save_tasks(tasks)

    print("Task added successfully!")
    print("Task ID:", task_id)
```

### Important concepts

**input()**

Accepts user input.

**strip()**

Removes spaces at the beginning and end of a string.

**if not name**

Checks whether the task name is empty.

**try-except**

Handles errors caused by invalid input.

**float()**

Converts input into a decimal number.

**max()**

Finds the largest existing task ID.

**default=0**

Provides a default value if there are no existing IDs.

**append()**

Adds a new task to the list.

**save_tasks()**

Saves the updated list into the CSV file.

## Function 4: list_tasks()

Purpose: Display all tasks sorted by estimated hours.

```python
def list_tasks():

    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    tasks = sorted(
        tasks,
        key=lambda task: float(task["hours"])
    )

    print("\n========== PRODUCTION TASKS ==========")

    for task in tasks:
        print("ID:", task["id"])
        print("Task:", task["name"])
        print("Hours:", task["hours"])
        print("Status:", task["status"])
        print("--------------------------------------")
```

### Explanation

1. Loads saved tasks.
2. Checks whether tasks exist.
3. Sorts tasks by estimated hours.
4. Uses a for loop to display each task.

## Function 5: export_tasks()

Purpose: Export task records into another CSV file.

```python
def export_tasks():

    tasks = load_tasks()

    if not tasks:
        print("No tasks available to export.")
        return

    with open(EXPORT_FILE, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=FIELDNAMES
        )

        writer.writeheader()
        writer.writerows(tasks)

    print("Tasks exported successfully!")
    print("File:", EXPORT_FILE)
```

### Explanation

1. Loads all tasks.
2. Checks whether tasks exist.
3. Opens tasks_export.csv.
4. Creates a CSV writer.
5. Writes headings.
6. Writes all task records.
7. Displays a success message.

## Function 6: main()

Purpose: Control the complete application using a menu.

```python
def main():

    while True:

        print("\n================================")
        print("     PRODUCTION TASK TRACKER")
        print("================================")

        print("1. Add Task")
        print("2. List Tasks")
        print("3. Export Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            export_tasks()

        elif choice == "4":
            print("Thank you for using Production Task Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")
```

### Important concepts

- `while True`: Repeats the menu.
- `input()`: Gets the user's choice.
- `if / elif / else`: Selects an operation.
- `break`: Stops the loop.

### Program entry point

```python
if __name__ == "__main__":
    main()
```

This executes the main function when the Python file is run directly.

---

# 12. Project Execution Flow

```text
Start
  |
  v
Display Main Menu
  |
  v
User Selects an Option
  |
  |---- 1. Add Task
  |        |
  |        v
  |     Load Existing Tasks
  |        |
  |        v
  |     Validate User Input
  |        |
  |        v
  |     Generate Unique ID
  |        |
  |        v
  |     Save Task to CSV
  |
  |---- 2. List Tasks
  |        |
  |        v
  |     Load Tasks
  |        |
  |        v
  |     Sort by Hours
  |        |
  |        v
  |     Display Tasks
  |
  |---- 3. Export Tasks
  |        |
  |        v
  |     Load Tasks
  |        |
  |        v
  |     Write Export CSV
  |
  |---- 4. Exit
           |
           v
          End
```

---

# 13. Example CSV Output

```csv
id,name,hours,status
1,Machine maintenance,3.0,Pending
2,Quality inspection,2.0,Pending
3,Material planning,4.5,Pending
```

---

# 14. Complexity Analysis

Let n represent the number of saved tasks.

| Operation | Time Complexity |
|---|---|
| Load tasks | O(n) |
| Save tasks | O(n) |
| Add task | O(n) |
| List tasks | O(n log n) |
| Export tasks | O(n) |

### Space Complexity

The program loads task records into a list.

Therefore, the task storage requires O(n) auxiliary space.

---

# 15. Edge Cases and Input Validation

| Test case | Expected result |
|---|---|
| Empty task name | Reject task |
| Spaces-only task name | Reject task |
| Hours = 0 | Reject task |
| Negative hours | Reject task |
| Text instead of hours | Catch ValueError |
| Missing CSV file | Return empty list |
| Empty task list | Display no tasks |

Note: Manually corrupted CSV IDs can cause errors during integer conversion. More robust file validation can be added in a future version.

---

# 16. How to Run the Project

Open the VS Code terminal in the project folder.

```bash
python main.py
```

### Test the following operations

1. Add Machine maintenance – 3 hours.
2. Add Quality inspection – 2 hours.
3. Add Material planning – 4.5 hours.
4. List all tasks.
5. Verify ascending sorting by hours.
6. Export tasks.
7. Open tasks.csv.
8. Open tasks_export.csv.
9. Restart the program and verify that records remain saved.
10. Test invalid inputs.

---

# 17. Interview Questions

1. What is a CSV file?
2. What is the difference between read() and DictReader()?
3. What is the difference between writerow() and writerows()?
4. Why do we use with open()?
5. What is the difference between w and a file modes?
6. What is list comprehension?
7. What is dictionary comprehension?
8. What does sorted(key=...) do?
9. What is a lambda function?
10. Why do we use pathlib?
11. Why do we use try-except?
12. What is the purpose of if __name__ == "__main__"?

---

# 18. GitHub Commands

```bash
git status
git add main.py
git add tasks.csv
git commit -m "Build production task tracker v0"
git push
```

Do not commit tasks_export.csv unless you want to include a sample export. Avoid uploading confidential production data.

---

# 19. Day 5 Learning Summary

Today I learned how to:

- Work with lists and dictionaries.
- Use list and dictionary comprehensions.
- Sort data using sorted() and lambda.
- Handle paths using pathlib.
- Read and write files using open().
- Use context managers.
- Read and write CSV files.
- Validate user input.
- Generate unique task IDs.
- Build a Python command-line application.
- Organize a project using reusable functions.

## Today's Project Deliverable

**Production Task Tracker v0**

Features: Add tasks, list tasks and export tasks to CSV.
