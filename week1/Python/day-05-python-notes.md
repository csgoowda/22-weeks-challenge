
# Day 5 – Python Notes
## Topic: Comprehensions, Sorting, pathlib, File Handling and CSV

---

# 1. List Comprehension

List comprehension is a short way to create a new list from an existing sequence.

### Normal method

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for num in numbers:
    squares.append(num * num)

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

### Using list comprehension

```python
numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

### Syntax

```python
new_list = [expression for item in iterable]
```

- expression: What we want to calculate.
- item: Each element.
- iterable: A list, tuple, string, etc.

### Example 1: Get even numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

### Example 2: Convert names to uppercase

```python
names = ["chethan", "rahul", "arun"]

upper_names = [name.upper() for name in names]

print(upper_names)
```

Output:

```text
['CHETHAN', 'RAHUL', 'ARUN']
```

### Important

List comprehension can include a condition:

```python
result = [expression for item in iterable if condition]
```

---

# 2. Dictionary Comprehension

Dictionary comprehension creates a new dictionary in a short way.

A dictionary stores information in key-value pairs.

### Normal method

```python
numbers = [1, 2, 3, 4]

squares = {}

for num in numbers:
    squares[num] = num * num

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16}
```

### Using dictionary comprehension

```python
numbers = [1, 2, 3, 4]

squares = {num: num * num for num in numbers}

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16}
```

### Syntax

```python
new_dict = {key: value for item in iterable}
```

### Example 1: Student marks

```python
students = ["Chethan", "Rahul", "Arun"]
marks = [85, 90, 78]

result = {
    students[i]: marks[i]
    for i in range(len(students))
}

print(result)
```

Output:

```text
{'Chethan': 85, 'Rahul': 90, 'Arun': 78}
```

### Example 2: Filter passing students

```python
marks = {
    "Chethan": 85,
    "Rahul": 35,
    "Arun": 78,
    "Kiran": 28
}

passed = {
    name: mark
    for name, mark in marks.items()
    if mark >= 40
}

print(passed)
```

Output:

```text
{'Chethan': 85, 'Arun': 78}
```

### Difference

| List comprehension | Dictionary comprehension |
|---|---|
| Creates a list | Creates a dictionary |
| Uses `[]` | Uses `{}` |
| Stores values | Stores key-value pairs |

---

# 3. sorted(key=...)

The `sorted()` function sorts elements and returns a new list.

### Example 1: Sort numbers

```python
numbers = [40, 10, 30, 20]

result = sorted(numbers)

print(result)
```

Output:

```text
[10, 20, 30, 40]
```

### Descending order

```python
numbers = [40, 10, 30, 20]

result = sorted(numbers, reverse=True)

print(result)
```

Output:

```text
[40, 30, 20, 10]
```

### Example 2: Sort names by length

```python
names = ["Chethan", "Ram", "Arun"]

result = sorted(names, key=len)

print(result)
```

Output:

```text
['Ram', 'Arun', 'Chethan']
```

### Example 3: Sort production tasks by hours

```python
tasks = [
    {"name": "Machine Repair", "hours": 5},
    {"name": "Quality Check", "hours": 2},
    {"name": "Production", "hours": 8}
]

result = sorted(tasks, key=lambda task: task["hours"])

for task in result:
    print(task)
```

Output:

```text
{'name': 'Quality Check', 'hours': 2}
{'name': 'Machine Repair', 'hours': 5}
{'name': 'Production', 'hours': 8}
```

### Understanding lambda

```python
lambda task: task["hours"]
```

This is a small anonymous function.

It receives one task and returns its hours value.

The sorting function uses that returned value to decide the order.

### Important points

```python
sorted(data)
sorted(data, reverse=True)
sorted(data, key=len)
sorted(data, key=lambda item: item["hours"])
```

`sorted()` returns a new sorted list. It does not change the original list.

---

# 4. pathlib – Working with File Paths

`pathlib` is a built-in Python module used to work with files and folders.

It makes file paths easier to manage.

### Import pathlib

```python
from pathlib import Path
```

### Example 1: Current working directory

```python
from pathlib import Path

current_location = Path.cwd()

print(current_location)
```

`Path.cwd()` returns the current working directory.

### Example 2: Create a folder

```python
from pathlib import Path

folder = Path("reports")

folder.mkdir(exist_ok=True)
```

This creates a folder named `reports` if it does not already exist.

`exist_ok=True` prevents an error if the folder already exists.

### Example 3: Create a file path

```python
from pathlib import Path

folder = Path("reports")

file_path = folder / "production.csv"

print(file_path)
```

The `/` operator joins path components.

### Example 4: Check whether a path exists

```python
from pathlib import Path

file_path = Path("production.csv")

print(file_path.exists())
```

Returns `True` if the path exists; otherwise, `False`.

### Other useful methods

```python
path.is_file()   # Checks whether it is a file
path.is_dir()    # Checks whether it is a folder
path.name       # Gets the file or folder name
path.suffix     # Gets the file extension
path.parent     # Gets the parent folder
```

### Example

```python
from pathlib import Path

file_path = Path("reports/production.csv")

print(file_path.name)
print(file_path.suffix)
print(file_path.parent)
```

Possible output:

```text
production.csv
.csv
reports
```

---

# 5. File Handling – with open()

Python can create, read, write and append files.

The `open()` function is used to open files.

### File modes

| Mode | Meaning |
|---|---|
| `"r"` | Read an existing file |
| `"w"` | Write; replaces existing contents |
| `"a"` | Append; adds content at the end |
| `"x"` | Create a new file; fails if it exists |

### Example 1: Write into a file

```python
with open("notes.txt", "w") as file:
    file.write("Learning Python")

print("File written successfully")
```

This creates `notes.txt` or replaces its previous contents.

### Example 2: Read a file

```python
with open("notes.txt", "r") as file:
    content = file.read()

print(content)
```

Output:

```text
Learning Python
```

### Example 3: Append content

```python
with open("notes.txt", "a") as file:
    file.write("\nLearning CSV")
```

This adds a new line without deleting the previous content.

### Example 4: Read line by line

```python
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
```

`strip()` removes unwanted whitespace, including the newline at the end.

### Why use `with open()`?

```python
with open("notes.txt", "r") as file:
    content = file.read()
```

The `with` statement automatically closes the file after the block finishes, including when an exception occurs.

This is safer than manually opening and closing files.

### Using pathlib with open()

```python
from pathlib import Path

file_path = Path("reports/notes.txt")

file_path.parent.mkdir(exist_ok=True)

with open(file_path, "w") as file:
    file.write("Production report")
```

---

# 6. CSV Basics

CSV means Comma-Separated Values.

It stores tabular data in a text file.

Example:

```text
id,name,hours,status
1,Machine Repair,5,Pending
2,Quality Check,2,Completed
3,Production,8,Pending
```

CSV files are useful for storing simple records and exchanging data between applications.

### Import CSV

```python
import csv
```

### Example 1: Write CSV data

```python
import csv

with open("tasks.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["id", "name", "hours", "status"])

    writer.writerow([1, "Machine Repair", 5, "Pending"])
    writer.writerow([2, "Quality Check", 2, "Completed"])
```

`newline=""` helps prevent unwanted blank rows when writing CSV files.

### Important CSV methods

| Method | Purpose |
|---|---|
| `csv.writer()` | Creates a CSV writer |
| `writer.writerow()` | Writes one row |
| `writer.writerows()` | Writes multiple rows |
| `csv.reader()` | Reads CSV rows |
| `csv.DictWriter()` | Writes dictionary records |
| `csv.DictReader()` | Reads rows as dictionaries |
| `writeheader()` | Writes column names |

### Example 2: Read CSV

```python
import csv

with open("tasks.csv", "r", newline="") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

### Example 3: Write using DictWriter

```python
import csv

tasks = [
    {"id": 1, "name": "Machine Repair", "hours": 5},
    {"id": 2, "name": "Quality Check", "hours": 2}
]

with open("tasks.csv", "w", newline="") as file:

    fieldnames = ["id", "name", "hours"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(tasks)
```

`writeheader()` writes the column names.

`writerows()` writes all dictionary records.

### Example 4: Read using DictReader

```python
import csv

with open("tasks.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
        print(row["hours"])
```

The rows are returned as dictionaries.

**Remember:** Values read from a CSV file are normally strings. Convert numeric values when you need to perform calculations.

```python
hours = int(row["hours"])
```

---

# 7. Mini Project – CLI Production Task Tracker

## Project objective

Build a command-line application to manage production tasks.

The tracker should support:

1. Add a task.
2. List all tasks.
3. Export tasks to a CSV file.
4. Assign a unique task ID.

Example task:

```python
{
    "id": 1,
    "name": "Machine Repair",
    "hours": 5,
    "status": "Pending"
}
```

## Suggested folder structure

```text
production_task_tracker/
│
├── main.py
├── tasks.csv
└── tasks_export.csv
```

## Concepts used

- Lists and dictionaries
- List and dictionary comprehensions
- Functions
- `sorted()`
- `pathlib`
- `with open()`
- CSV module
- Loops and conditions

## Starter code

```python
from pathlib import Path
import csv

DATA_FILE = Path("tasks.csv")
EXPORT_FILE = Path("tasks_export.csv")

FIELDNAMES = ["id", "name", "hours", "status"]


def load_tasks():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", newline="") as file:
        return list(csv.DictReader(file))


def save_tasks(tasks):
    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        writer.writeheader()
        writer.writerows(tasks)


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

    print("Task added successfully. ID:", task_id)


def list_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks available")
        return

    tasks = sorted(
        tasks,
        key=lambda task: float(task["hours"])
    )

    for task in tasks:
        print(
            task["id"],
            task["name"],
            task["hours"],
            task["status"]
        )


def export_tasks():
    tasks = load_tasks()

    with open(EXPORT_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        writer.writeheader()
        writer.writerows(tasks)

    print("Tasks exported to:", EXPORT_FILE)


def main():
    while True:
        print("\n--- Production Task Tracker ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Export tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            export_tasks()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
```

## How to run

Open the terminal inside the project folder.

```bash
python main.py
```

Example menu:

```text
--- Production Task Tracker ---
1. Add task
2. List tasks
3. Export tasks
4. Exit
```

Example task records:

```text
1 Machine Repair 5.0 Pending
2 Quality Check 2.0 Pending
3 Production 8.0 Pending
```

### Important project notes

- `load_tasks()` reads saved records.
- `save_tasks()` saves task records.
- `add_task()` validates input and generates a new ID.
- `list_tasks()` displays tasks sorted by hours.
- `export_tasks()` creates a separate CSV export.
- `main()` controls the menu.

This is a starter implementation. Test it with empty names, invalid hours, zero hours and an empty task file.

---

# 8. Quick Revision

| Topic | Remember |
|---|---|
| List comprehension | Creates a list in one expression |
| Dictionary comprehension | Creates key-value pairs |
| `sorted()` | Returns a new sorted list |
| `key=` | Defines what value sorting uses |
| `Path.cwd()` | Gets current directory |
| `mkdir()` | Creates a folder |
| `exists()` | Checks whether a path exists |
| `with open()` | Opens and safely closes a file |
| `"r"` | Read |
| `"w"` | Write / replace |
| `"a"` | Append |
| `csv.writer()` | Writes CSV rows |
| `csv.DictReader()` | Reads CSV as dictionaries |
| `writeheader()` | Writes CSV column names |

---

# 9. Practice Programs

Try these yourself without copying the solution.

1. Create a list of numbers and use list comprehension to find their squares.
2. Create a list of numbers and filter only odd numbers.
3. Create a dictionary of students and marks using dictionary comprehension.
4. Filter students who scored at least 40.
5. Sort production tasks by estimated hours.
6. Sort names alphabetically.
7. Create a folder called `production_reports`.
8. Create a text file and write three lines.
9. Read a text file and print every line.
10. Create a CSV file with task ID, task name, hours and status.

---

# Day 5 Learning Outcome

After completing today's work, I should be able to:

- [ ] Write list comprehensions.
- [ ] Write dictionary comprehensions.
- [ ] Sort data using `sorted(key=...)`.
- [ ] Create and inspect paths using pathlib.
- [ ] Read, write and append files.
- [ ] Create and read CSV files.
- [ ] Build a CLI production-task tracker.
- [ ] Explain the code without memorising it.
