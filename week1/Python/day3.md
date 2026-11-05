# Day 3 – Python Loops and Functions

**Date:** 5 November 2026  
**Week:** 1  
**Topics:** Loops, range(), break, continue, functions, parameters, return values, default arguments and scope.

---

# Part 1: Python Loops

## 1. What is a Loop?

A loop is used to execute a block of code repeatedly.

Instead of writing the same code multiple times, we can use loops.

Python provides two main types of loops:

1. `for` loop
2. `while` loop

### Example without a loop

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

### Example using a loop

```python
for i in range(5):
    print("Hello")
```

Both programs produce the same output.

**Why use loops?**

- Reduce repeated code.
- Save development time.
- Make programs easier to maintain.
- Process collections of data efficiently.

---

## 2. For Loop

A `for` loop is used to repeat a block of code for each item in a sequence or iterable.

**Syntax:**

```python
for variable in sequence:
    # Code to execute
```

### Example 1: Print numbers from 1 to 5

```python
for i in range(1, 6):
    print(i)
```

**Output:**

```text
1
2
3
4
5
```

Explanation:

- `i` is the loop variable.
- `range(1, 6)` generates numbers from 1 to 5.
- The loop executes once for each number.

### Example 2: Print multiplication table

```python
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
```

**Output:**

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

---

## 3. range() Function

The `range()` function generates a sequence of numbers.

It is commonly used with `for` loops.

There are three ways to use `range()`.

### 3.1 range(stop)

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

It starts at 0 and stops before 5.

### 3.2 range(start, stop)

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

It starts at 1 and stops before 6.

### 3.3 range(start, stop, step)

```python
for i in range(2, 11, 2):
    print(i)
```

Output:

```text
2
4
6
8
10
```

Here:

- Start = 2
- Stop = 11
- Step = 2

The step controls how much the number increases or decreases each time.

### Example: Countdown

```python
for i in range(5, 0, -1):
    print(i)
```

Output:

```text
5
4
3
2
1
```

**Important:** The stop value is excluded from the generated sequence.

---

## 4. While Loop

A `while` loop repeatedly executes a block of code as long as its condition is True.

**Syntax:**

```python
while condition:
    # Code to execute
```

### Example: Print numbers from 1 to 5

```python
i = 1

while i <= 5:
    print(i)
    i = i + 1
```

Output:

```text
1
2
3
4
5
```

Explanation:

1. Initially, `i = 1`.
2. Python checks whether `i <= 5`.
3. If True, it prints `i`.
4. `i` increases by 1.
5. The condition is checked again.
6. The loop stops when `i` becomes 6.

### Important: Infinite Loop

If the condition never becomes False, the loop continues indefinitely.

Example:

```python
i = 1

while i <= 5:
    print(i)
```

This program does not update `i`, so it keeps printing 1.

Always make sure the loop has a valid stopping condition.

---

## 5. Difference Between for and while

| for loop | while loop |
|---|---|
| Used to iterate over a sequence or iterable | Used while a condition remains True |
| Often used when the number of iterations is known | Often used when the number of iterations is not known in advance |
| Commonly used with range() | Requires a condition |
| Iteration is managed by the loop | The programmer often updates the condition variable |

Example:

**For loop:**

```python
for i in range(1, 6):
    print(i)
```

**While loop:**

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Both produce the same output.

---

## 6. break Statement

The `break` statement immediately terminates the nearest enclosing loop.

### Example:

```python
for i in range(1, 10):
    if i == 5:
        break

    print(i)
```

Output:

```text
1
2
3
4
```

Explanation:

- The loop starts at 1.
- When `i` becomes 5, the condition is True.
- `break` terminates the loop.
- Numbers after 5 are not processed.

**Use case:** Stop searching when the required item is found.

---

## 7. continue Statement

The `continue` statement skips the remaining statements in the current iteration and moves to the next iteration.

### Example:

```python
for i in range(1, 6):
    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

Explanation:

- When `i` becomes 3, `continue` skips the print statement.
- The loop continues with the next value.

### Difference Between break and continue

| break | continue |
|---|---|
| Terminates the loop | Skips the current iteration |
| No more iterations execute | Remaining iterations continue |
| Used to stop a loop | Used to skip selected iterations |

---

# Part 2: Loop Practice Programs

## 8. Sum of Numbers from 1 to N

Find the sum of all numbers from 1 to N.

Example:

```text
N = 5

1 + 2 + 3 + 4 + 5 = 15
```

Program:

```python
n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)
```

Output:

```text
Enter a number: 5
Sum: 15
```

## 9. Factorial Using a Loop

Factorial is the product of all positive integers from 1 to a given number.

Example:

```text
5! = 5 x 4 x 3 x 2 x 1 = 120
```

Program:

```python
n = int(input("Enter a number: "))

factorial = 1

if n < 0:
    print("Factorial is not defined for negative numbers")

else:
    for i in range(1, n + 1):
        factorial *= i

    print("Factorial:", factorial)
```

Output:

```text
Enter a number: 5
Factorial: 120
```

Remember:

```text
0! = 1
```

## 10. Number Guessing Loop

This example repeats until the user enters the correct number.

```python
secret_number = 7

guess = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))

    if guess < secret_number:
        print("Too low")

    elif guess > secret_number:
        print("Too high")

    else:
        print("Correct guess!")
```

This demonstrates:

- `while`
- Conditions
- Repeated input
- Loop termination

---

# Part 3: Python Functions

## 11. What is a Function?

A function is a reusable block of code that performs a particular task.

Instead of writing the same logic repeatedly, we can create a function and call it whenever required.

### Without a Function

```python
a = 10
b = 20
print(a + b)

x = 30
y = 40
print(x + y)
```

### With a Function

```python
def add(a, b):
    print(a + b)

add(10, 20)
add(30, 40)
```

Output:

```text
30
70
```

Functions improve:

- Code reusability.
- Readability.
- Maintainability.
- Testing.
- Code organization.

---

## 12. Creating a Function

Python uses the `def` keyword to define a function.

**Syntax:**

```python
def function_name():
    # Function body
```

Example:

```python
def greet():
    print("Hello, welcome to Python")

greet()
```

Output:

```text
Hello, welcome to Python
```

Explanation:

- `def` defines a function.
- `greet` is the function name.
- The indented line is the function body.
- `greet()` calls the function.

Defining a function does not automatically execute its body. It runs when the function is called.

---

## 13. Function Parameters and Arguments

Parameters are variables listed in a function definition.

Arguments are the actual values passed when calling a function.

Example:

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Here:

- `a` and `b` are parameters.
- `10` and `20` are arguments.

Output:

```text
30
```

### Multiple Examples

```python
def greet(name):
    print("Hello", name)

greet("Chethan")
greet("Rahul")
greet("Arun")
```

Output:

```text
Hello Chethan
Hello Rahul
Hello Arun
```

The same function can be reused with different arguments.

---

## 14. Return Statement

The `return` statement sends a result from a function back to the place where it was called.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

### Difference Between print() and return

| print() | return |
|---|---|
| Displays output on the screen | Sends a value back to the caller |
| Does not automatically provide a reusable result | The returned value can be stored and reused |
| Mainly used for displaying information | Used to produce results from functions |

Example using return:

```python
def square(number):
    return number * number

result = square(5)

print("Square:", result)
print("Square plus 10:", result + 10)
```

Output:

```text
Square: 25
Square plus 10: 35
```

### Important

If a function does not explicitly return a value, Python returns `None`.

---

## 15. Default Arguments

A default argument is a parameter that already has a value in the function definition.

If the caller does not provide that argument, Python uses the default value.

Example:

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Chethan")
```

Output:

```text
Hello Guest
Hello Chethan
```

Explanation:

- `name="Guest"` is the default argument.
- `greet()` uses the default value.
- `greet("Chethan")` replaces the default value.

### Another Example

```python
def calculate_bill(amount, tax=18):
    total = amount + (amount * tax / 100)
    return total

print(calculate_bill(1000))
print(calculate_bill(1000, 5))
```

Output:

```text
1180.0
1050.0
```

---

## 16. Variable Scope

Scope defines where a variable can be accessed in a program.

Python mainly has:

1. Local scope.
2. Global scope.

### 16.1 Local Variable

A local variable is created inside a function and is normally accessible only inside that function.

Example:

```python
def greet():
    message = "Hello"
    print(message)

greet()
```

Output:

```text
Hello
```

Here, `message` is a local variable.

Trying to access it outside the function will cause a `NameError`:

```python
def greet():
    message = "Hello"

greet()

print(message)
```

### 16.2 Global Variable

A global variable is created outside functions and can be accessed inside functions.

Example:

```python
name = "Chethan"

def greet():
    print("Hello", name)

greet()
```

Output:

```text
Hello Chethan
```

### 16.3 Local and Global Variables with the Same Name

```python
name = "Global"

def display():
    name = "Local"
    print(name)

display()

print(name)
```

Output:

```text
Local
Global
```

The local variable does not change the global variable.

### 16.4 global Keyword

The `global` keyword allows a function to reassign a global variable.

Example:

```python
count = 10

def update_count():
    global count
    count = 20

update_count()

print(count)
```

Output:

```text
20
```

Use global variables carefully. Prefer passing values through parameters and returning results where practical.

---

# Part 4: Docstrings

## 17. What is a Docstring?

A docstring is a string written at the beginning of a function, class or module to explain its purpose.

It is used to document code.

Example:

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add(10, 20))
```

Output:

```text
30
```

We can access a function's docstring using:

```python
print(add.__doc__)
```

Output:

```text
Return the sum of two numbers.
```

### Why use Docstrings?

- Explain what a function does.
- Make code easier to understand.
- Help other developers.
- Improve project documentation.

---

# Part 5: Refactoring Programs into Functions

## 18. What is Refactoring?

Refactoring means improving the internal structure of existing code without changing its expected behaviour.

For example, instead of keeping all calculator logic in one long program, we can create separate reusable functions.

### Example 1: Marks Percentage Calculator

```python
def calculate_percentage(obtained, total):
    """Calculate percentage from obtained and total marks."""

    if total <= 0:
        return None

    if obtained < 0 or obtained > total:
        return None

    percentage = (obtained / total) * 100

    return percentage


obtained = float(input("Enter obtained marks: "))
total = float(input("Enter total marks: "))

result = calculate_percentage(obtained, total)

if result is None:
    print("Invalid marks")

else:
    print("Percentage:", result)
```

### Example 2: GST Calculator

```python
def calculate_gst(amount, gst_rate=18):
    """Calculate GST and final amount."""

    gst = amount * gst_rate / 100

    total = amount + gst

    return gst, total


amount = float(input("Enter amount: "))

gst, total = calculate_gst(amount)

print("GST:", gst)
print("Total amount:", total)
```

### Example 3: Largest of Three Numbers

```python
def largest_of_three(a, b, c):
    """Return the largest of three numbers."""

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c


print(largest_of_three(10, 30, 20))
```

Output:

```text
30
```

### Example 4: Leap Year Checker

```python
def is_leap_year(year):
    """Return True if the given year is a leap year."""

    if year % 400 == 0:
        return True

    elif year % 100 == 0:
        return False

    elif year % 4 == 0:
        return True

    else:
        return False


year = int(input("Enter year: "))

if is_leap_year(year):
    print("Leap year")

else:
    print("Not a leap year")
```

### Example 5: Grade Calculator as a Function

```python
def calculate_grade(marks):
    """Return the grade based on marks."""

    if marks < 0 or marks > 100:
        return "Invalid marks"

    elif marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 50:
        return "D"

    else:
        return "Fail"


marks = float(input("Enter marks: "))

print("Grade:", calculate_grade(marks))
```

---

# Part 6: Important Interview Questions

## 19. Python Loops

**Q1. What is a loop?**

A loop is used to execute a block of code repeatedly.

**Q2. What are the types of loops in Python?**

Python has two main loops: `for` and `while`.

**Q3. What is range()?**

`range()` generates a sequence of integers and is commonly used with a for loop.

**Q4. What is the difference between break and continue?**

`break` terminates the loop, while `continue` skips the current iteration.

**Q5. What is an infinite loop?**

An infinite loop is a loop that never stops because its condition remains True.

## 20. Python Functions

**Q1. What is a function?**

A function is a reusable block of code that performs a specific task.

**Q2. Which keyword is used to define a function?**

The `def` keyword.

**Q3. What is a parameter?**

A parameter is a variable defined in a function declaration.

**Q4. What is an argument?**

An argument is the actual value passed to a function when calling it.

**Q5. What is return?**

`return` sends a result from a function back to its caller.

**Q6. What is a default argument?**

A default argument is a parameter that has a predefined value.

**Q7. What is variable scope?**

Scope defines where a variable can be accessed.

**Q8. What is a docstring?**

A docstring describes the purpose of a function, class or module.

**Q9. What is refactoring?**

Refactoring improves code structure without changing its expected behaviour.

---

# Part 7: Day 3 Python Practice Checklist

## Loop Exercises

- [ ] Print numbers from 1 to 100.
- [ ] Print even numbers from 1 to 50.
- [ ] Print a multiplication table.
- [ ] Calculate the sum of numbers from 1 to N.
- [ ] Calculate factorial using a loop.
- [ ] Create a number guessing loop.
- [ ] Practise break and continue.

## Function Exercises

- [ ] Create a function to add two numbers.
- [ ] Create a function to calculate a square.
- [ ] Create a function to calculate factorial.
- [ ] Create a function to calculate marks percentage.
- [ ] Create a function to calculate GST.
- [ ] Create a function to find the largest of three numbers.
- [ ] Create a function to check leap years.
- [ ] Create a function to calculate grades.
- [ ] Add docstrings to every function.
- [ ] Refactor previous calculator programs into reusable functions.

---

# Part 8: Quick Revision

| Topic | Important point |
|---|---|
| for loop | Iterates over a sequence or iterable |
| while loop | Repeats while a condition is True |
| range() | Generates a sequence of integers |
| break | Terminates the nearest enclosing loop |
| continue | Skips the current iteration |
| def | Defines a function |
| Parameter | Variable in a function definition |
| Argument | Value passed to a function |
| return | Sends a result back to the caller |
| Default argument | Parameter with a predefined value |
| Local scope | Variable accessible within its local scope |
| Global scope | Variable defined outside functions |
| Docstring | Documents the purpose of code |
| Refactoring | Improves code structure without changing expected behaviour |

**Day 3 Python Goal:** Understand loops and functions, write reusable programs, and refactor previous calculator programs using functions and docstrings.
