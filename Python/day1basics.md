# Day 1 – Python Full Notes

22-Week Python, AI & Industrial Software Roadmap · Day 1 · Revision Notes

These notes cover the Python concepts we studied today, with explanations, examples, outputs and practice questions. Use them for revision.

## 1. What is Python?

Python is a high-level, general-purpose programming language.

It is used for:

- Backend development
- Web applications
- Artificial intelligence and machine learning
- Data science
- Automation
- Software development

Example:

```
print("Hello, World!")
```

Output:

```
Hello, World!
```

## 2. What is a Python interpreter?

A Python interpreter is a program that executes Python source code.

In CPython (the standard Python implementation), the general execution process is:

Python Source Code

example.py

Compilation

Python code is compiled into bytecode

Python Virtual Machine (PVM)

Executes the bytecode

Output

Remember: Python is commonly called an interpreted language, but CPython internally uses both compilation to bytecode and execution.

## 3. Python syntax

Syntax means the rules for writing valid Python code.

Correct syntax:

```
print("Hello Python")
```

Incorrect syntax:

```
print("Hello Python"
```

The second example has a missing closing parenthesis and produces a syntax error.

Python normally executes statements in order, from top to bottom.

```
print("First")print("Second")print("Third")
```

Output:

```
First
Second
Third
```

## 4. Indentation

Indentation means spaces at the beginning of a line.

Python uses indentation to identify blocks of code.

Example:

```
age = 20if age >= 18:    print("You are eligible")
```

Here, `print()` belongs to the `if` block.

Important rules:

- Use four spaces for each indentation level as the standard convention.
- Keep indentation consistent.
- Missing indentation in a required block can cause `IndentationError`.

Incorrect:

```
if age >= 18:print("Eligible")
```

## 5. Comments

Comments are notes inside code that explain its purpose.

Python ignores comments during execution.

Single-line comment:

```
# This is a commentprint("Hello")
```

Output:

```
Hello
```

Comments use the `#` symbol.

Example:

```
# Store machine informationmachine_name = "CNC Machine"# Display machine nameprint(machine_name)
```

Good comments explain the purpose of code rather than repeating obvious instructions.

## 6. Variables

A variable is a named reference used to store or access a value in a program.

Example:

```
name = "Chethan"age = 22cgpa = 7.3
```

Understanding this statement:

```
machine_capacity = 500
```

- `machine_capacity` → variable name
- `=` → assignment operator
- `500` → value

You can change a variable's value:

```
production_count = 100production_count = 150print(production_count)
```

Output:

```
150
```

The latest assignment determines the current value.

### Variable naming rules

1. A variable name can contain letters, numbers and underscores.
2. It cannot begin with a number.
3. Spaces are not allowed.
4. Variable names are case-sensitive.
5. Python keywords cannot be used as variable names.
6. Use meaningful names.

| Valid              | Invalid        |
| ------------------ | -------------- |
| `machine_name`     | `machine name` |
| `age`              | `2age`         |
| `total_price`      | `total-price`  |
| `production_count` | `class`        |

Naming convention: Python commonly uses `snake_case`, such as `machine_capacity`.

## 7. Python data types

A data type identifies the kind of value stored in a variable.

Day 1 covers four basic data types.

### A. Integer (`int`)

Stores whole numbers without decimal points.

```
age = 22production_count = 500print(type(age))
```

Output:

```
<class 'int'>
```

### B. Float (`float`)

Stores decimal numbers.

```
cgpa = 7.3temperature = 36.5print(type(cgpa))
```

Output:

```
<class 'float'>
```

### C. String (`str`)

Stores text inside single or double quotation marks.

```
name = "Chethan"language = 'Python'print(type(name))
```

Output:

```
<class 'str'>
```

### D. Boolean (`bool`)

Stores one of two logical values: `True` or `False`.

```
is_available = Trueis_machine_running = Falseprint(type(is_available))
```

Output:

```
<class 'bool'>
```

### Data type comparison

| Type    | Example | Description    |
| ------- | ------- | -------------- |
| `int`   | `100`   | Whole number   |
| `float` | `100.5` | Decimal number |
| `str`   | `"100"` | Text           |
| `bool`  | `True`  | Logical value  |

Important difference:

```
a = 100b = "100"print(type(a))print(type(b))
```

Output:

```
<class 'int'>
<class 'str'>
```

Although both look like 100, Python treats them differently.

## 8. `print()` function

The `print()` function displays output on the screen.

Example:

```
name = "Chethan"age = 22print(name)print(age)print("My name is", name)
```

Output:

```
Chethan
22
My name is Chethan
```

You can display multiple values using commas.

## 9. `input()` function

The `input()` function receives information from the user while the program is running.

Example:

```
name = input("Enter your name: ")print("Welcome", name)
```

Example execution:

```
Enter your name: Chethan
Welcome Chethan
```

Important: `input()` returns a string (`str`) by default, even if the user enters a number.

Example:

```
age = input("Enter your age: ")print(type(age))
```

If you enter `22`, the result is:

```
<class 'str'>
```

## 10. Type conversion

Type conversion means changing a value from one data type to another.

| Function  | Purpose            | Example        |
| --------- | ------------------ | -------------- |
| `int()`   | Convert to integer | `int("25")`    |
| `float()` | Convert to float   | `float("7.5")` |
| `str()`   | Convert to string  | `str(100)`     |
| `bool()`  | Convert to Boolean | `bool(1)`      |

Examples:

```
age = int("22")cgpa = float("7.3")number = str(100)print(type(age))print(type(cgpa))print(type(number))
```

Output:

```
<class 'int'>
<class 'float'>
<class 'str'>
```

### Important: String addition versus numeric addition

Consider:

```
a = "10"b = "20"print(a + b)
```

Output:

```
1020
```

Here, Python joins two strings.

For mathematical addition:

```
a = int("10")b = int("20")print(a + b)
```

Output:

```
30
```

### Taking two numbers from the user

```
num1 = int(input("Enter first number: "))num2 = int(input("Enter second number: "))result = num1 + num2print("Sum:", result)
```

Example:

```
Enter first number: 5
Enter second number: 5
Sum: 10
```

## 11. Basic Python operators

Operators perform operations on values and variables.

| Operator | Name                | Example   | Result |
| -------- | ------------------- | --------- | ------ |
| `+`      | Addition            | `10 + 5`  | 15     |
| `-`      | Subtraction         | `10 - 5`  | 5      |
| `*`      | Multiplication      | `10 * 5`  | 50     |
| `/`      | Division            | `10 / 5`  | 2.0    |
| `//`     | Floor division      | `11 // 5` | 2      |
| `%`      | Modulus (remainder) | `11 % 5`  | 1      |
| `**`     | Exponentiation      | `2 ** 3`  | 8      |

### Difference between `/`, `//` and `%`

```
a = 15b = 4print(a / b)print(a // b)print(a % b)
```

Output:

```
3.75
3
3
```

- `/` gives normal division.
- `//` gives floor division (rounds down to the nearest integer here).
- `%` gives the remainder.

For example, `15 % 4 = 3`, because 4 goes into 15 three times, leaving 3.

## 12. Complete Day 1 Python practice programs

These five exercises are part of your Day 1 practice.

### Exercise 1: Print your introduction

```
print("My name is Chethan")print("I am learning Python")print("My goal is to become a Backend Developer")
```

### Exercise 2: Student information

```
name = "Chethan"age = 22cgpa = 7.3target_role = "Python Backend Developer"print("Name:", name)print("Age:", age)print("CGPA:", cgpa)print("Target Role:", target_role)
```

### Exercise 3: Add two numbers

```
num1 = int(input("Enter first number: "))num2 = int(input("Enter second number: "))result = num1 + num2print("Sum:", result)
```

### Exercise 4: Check type before and after conversion

```
number = input("Enter a number: ")print("Before conversion:", type(number))number = int(number)print("After conversion:", type(number))
```

### Exercise 5: Machine information

```
machine_name = "CNC Machine"machine_capacity = 500is_available = Trueprint("Machine Name:", machine_name)print("Capacity:", machine_capacity)print("Available:", is_available)
```

## 13. Important interview questions

These are useful beginner questions to revise.

Q1. What is Python?

Python is a high-level, general-purpose programming language used for backend development, automation, AI, data science and other applications.

Q2. What is an interpreter?

A Python interpreter executes Python source code. In CPython, source code is compiled into bytecode and executed by the Python Virtual Machine.

Q3. What is a variable?

A variable is a named reference used to store or access a value.

Q4. What is indentation?

Indentation means spaces at the beginning of a line. Python uses it to define code blocks.

Q5. What is the difference between `int` and `float`?

`int` represents whole numbers, whereas `float` represents decimal numbers.

Q6. What is the difference between `100` and `"100"`?

`100` is an integer, while `"100"` is a string.

Q7. What does `input()` do?

It receives user input and returns it as a string by default.

Q8. What does `print()` do?

It displays information on the screen.

Q9. What is type conversion?

It is the process of converting a value from one data type to another.

Q10. What is the difference between `/`, `//` and `%`?

`/` performs division, `//` performs floor division, and `%` returns the remainder.

## 14. Final revision test

Try these questions without looking at the notes.

Day 1 Python knowledge test

8 questions

Q1. Which data type stores whole numbers?

A. float

B. int

C. str

D. bool



Q2. What does input() return by default?

A. int

B. float

C. str

D. bool



Q3. Which symbol starts a Python comment?

A. //

B. #

C. /\*

D. --



Q4. What is the output of 20 % 6?

A. 2

B. 3

C. 4

D. 6



Q5. What is the output of 3 \*\* 2?

A. 5

B. 6

C. 9

D. 8



Q6. What is the data type of True?

A. str

B. int

C. float

D. bool



Q7. Which is a valid variable name?

A. 2count

B. machine-name

C. machine_name

D. class



Q8. What converts '25' into an integer?

A. str()

B. float()

C. int()

D. type()



0 of 8 answered

Submit answers

## Day 1 Python completion summary

- Python installation and execution
- Syntax, indentation and comments
- Variables and naming rules
- Four basic data types
- `print()` and `input()`
- Type conversion
- Basic arithmetic operators
- Five beginner exercises

My recommendation: Save these notes as `Day1_Python_Notes.md` in your roadmap folder and revise them before starting Day 2.

Next, we will continue with the remaining Day 1 activities: DSA, OOP, aptitude, English practice and the final progress review.
