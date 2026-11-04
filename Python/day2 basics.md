These notes cover the Python portion of Day 2 in your roadmap:

1. Python operators
2. Conditional statements
3. `if`, `elif`, `else`
4. Input validation
5. Functions and `return`
6. `isinstance()`
7. Five practical programs
8. Test cases and common mistakes

Keep these notes in your Python study notebook. I'll explain each topic with simple definitions, syntax, examples and outputs.

# Day 2 – Python Programming Notes

WEEK 1 · PYTHON FUNDAMENTALS · 4 NOVEMBER 2026

## Step 1. Python operators

Definition: Operators are special symbols used to perform operations on variables and values.

Example:

```
a = 10b = 3print(a + b)
```

Output:

```
13
```

Here, `+` is an arithmetic operator.

### 1.1 Arithmetic operators

Used for mathematical calculations.

| Operator | Meaning             | Example   | Result   |
| -------- | ------------------- | --------- | -------- |
| `+`      | Addition            | `10 + 3`  | 13       |
| `-`      | Subtraction         | `10 - 3`  | 7        |
| `*`      | Multiplication      | `10 * 3`  | 30       |
| `/`      | Division            | `10 / 3`  | 3.333... |
| `//`     | Floor division      | `10 // 3` | 3        |
| `%`      | Modulus (remainder) | `10 % 3`  | 1        |
| `**`     | Exponentiation      | `10 ** 2` | 100      |

Important differences:

```
print(10 / 3)   # 3.333...print(10 // 3)  # 3print(10 % 3)   # 1
```

- `/` gives the division result.
- `//` gives the floor of the division result.
- `%` gives the remainder.

### 1.2 Comparison operators

Used to compare two values. The result is always a Boolean value: `True` or `False`.

| Operator | Meaning               | Example    | Result |
| -------- | --------------------- | ---------- | ------ |
| `==`     | Equal to              | `10 == 10` | True   |
| `!=`     | Not equal to          | `10 != 5`  | True   |
| `>`      | Greater than          | `10 > 5`   | True   |
| `<`      | Less than             | `10 < 5`   | False  |
| `>=`     | Greater than or equal | `10 >= 10` | True   |
| `<=`     | Less than or equal    | `5 <= 10`  | True   |

Remember the difference:

```
age = 20       # Assignmentprint(age == 20)  # Comparison
```

- `=` assigns a value.
- `==` checks equality.

### 1.3 Logical operators

Used to combine or reverse conditions.

| Operator | Meaning                                  |
| -------- | ---------------------------------------- |
| `and`    | True when both conditions are True       |
| `or`     | True when at least one condition is True |
| `not`    | Reverses True and False                  |

Example:

```
age = 20has_id = Trueprint(age >= 18 and has_id)
```

Output:

```
True
```

Both conditions are true, so the final result is true.

Another example:

```
print(not True)
```

Output:

```
False
```

## Step 2. Conditional statements

Definition: Conditional statements allow a program to make decisions based on whether a condition is true or false.

For example, a program can check whether a person is eligible to vote.

### 2.1 `if` statement

Executes a block of code when the condition is true.

Syntax:

```
if condition:    statement
```

Example:

```
age = 20if age >= 18:    print("Eligible to vote")
```

Output:

```
Eligible to vote
```

### 2.2 `if-else` statement

Used when there are two possible outcomes.

Example:

```
age = 16if age >= 18:    print("Eligible")else:    print("Not eligible")
```

Output:

```
Not eligible
```

### 2.3 `if-elif-else` statement

Used when multiple conditions need to be checked.

- `if` checks the first condition.
- `elif` checks another condition if previous conditions are false.
- `else` executes when all previous conditions are false.

Example:

```
marks = 82if marks >= 90:    print("A Grade")elif marks >= 75:    print("B Grade")elif marks >= 50:    print("C Grade")else:    print("Fail")
```

Output:

```
B Grade
```

Important: Python checks conditions from top to bottom. Once a condition is true, its block executes and the remaining branches are skipped.

### 2.4 Multiple conditions using `and` and `or`

Example using `and`:

```
age = 22if age >= 18 and age <= 60:    print("Eligible")else:    print("Not eligible")
```

Example using `or`:

```
day = "Saturday"if day == "Saturday" or day == "Sunday":    print("Weekend")else:    print("Weekday")
```

### 2.5 Nested `if`

An `if` statement inside another `if` statement is called a nested `if`.

```
age = 22has_id = Trueif age >= 18:    if has_id:        print("Entry allowed")    else:        print("ID required")else:    print("Underage")
```

## Step 3. Functions

Definition: A function is a reusable block of code designed to perform a particular task.

Functions help us:

- Reuse code.
- Avoid repetition.
- Organize programs.
- Make code easier to maintain.

### 3.1 Creating a function

Python uses the `def` keyword to define a function.

```
def greet():    print("Hello!")
```

Calling the function:

```
greet()
```

Output:

```
Hello!
```

### 3.2 Function parameters

Parameters are variables listed in a function definition. They receive values when the function is called.

```
def add(a, b):    print(a + b)add(10, 20)
```

Output:

```
30
```

Here, `a` and `b` are parameters.

### 3.3 Arguments

Arguments are the actual values passed when calling a function.

```
add(10, 20)
```

Here, `10` and `20` are arguments.

### 3.4 Return statement

`return` sends a result back from a function to the code that called it.

```
def add(a, b):    return a + bresult = add(10, 20)print(result)
```

Output:

```
30
```

Difference between `print()` and `return`:

| `print()`                                         | `return`                          |
| ------------------------------------------------- | --------------------------------- |
| Displays output                                   | Sends a value back                |
| Mainly for showing information                    | Used to provide a function result |
| Does not automatically give the caller that value | Can be stored in a variable       |

### 3.5 Function with default parameters

A default parameter has a value that is used when no argument is provided for it.

```
def greet(name="Student"):    print("Hello", name)greet()greet("Chethan")
```

Output:

```
Hello Student
Hello Chethan
```

### 3.6 Multiple return values

Python functions can return more than one value.

```
def calculate(a, b):    total = a + b    difference = a - b    return total, differencex, y = calculate(20, 10)print(x)print(y)
```

Output:

```
30
10
```

Python packages these returned values into a tuple, which can be unpacked into separate variables.

## Step 4. Input validation

Definition: Input validation means checking whether the input provided by a user is acceptable before processing it.

Example:

```
marks = 120if marks < 0 or marks > 100:    print("Invalid marks")else:    print("Valid marks")
```

Output:

```
Invalid marks
```

### Why is input validation important?

Consider a percentage calculator. If maximum marks are zero, division by zero causes an error.

```
maximum_marks = 0if maximum_marks <= 0:    print("Invalid maximum marks")
```

We validate inputs to prevent invalid calculations and unexpected results.

### Common validation conditions

```
if age < 0:    print("Invalid age")if price < 0:    print("Invalid price")if marks > 100:    print("Marks cannot exceed 100")
```

## Step 5. `isinstance()` function

Definition: `isinstance()` checks whether a value belongs to a particular data type or class.

Syntax:

```
isinstance(value, data_type)
```

Example:

```
gst = "Invalid price"if isinstance(gst, str):    print(gst)
```

Output:

```
Invalid price
```

More examples:

```
print(isinstance(10, int))       # Trueprint(isinstance(10.5, float))   # Trueprint(isinstance("Hello", str))  # Trueprint(isinstance(True, bool))    # True
```

Why did we use it in the GST calculator?

Our function returns either:

- A GST amount and total bill (two numeric values).
- An error message (string).

We use `isinstance()` to identify the error message before displaying the bill.

## Step 6. Five practical Python programs

These are the five programs required for your Day 2 core deliverable.

### Program 1 – Marks percentage calculator

Purpose: Calculate the percentage from obtained and maximum marks.

Formula:

\\[ Percentage = \frac{Obtained\ Marks}{Maximum\ Marks}\times100 \\]

Code:

```
def calculate_percentage(obtained_marks, maximum_marks):    if maximum_marks <= 0:        return "Invalid maximum marks"    elif obtained_marks < 0:        return "Obtained marks cannot be negative"    elif obtained_marks > maximum_marks:        return "Obtained marks cannot exceed maximum marks"    else:        percentage = (obtained_marks / maximum_marks) * 100        return percentage
```

Calling the function:

```
result = calculate_percentage(420, 500)print("Percentage:", result)
```

Output:

```
Percentage: 84.0
```

### Program 2 – GST and bill calculator

Purpose: Calculate GST amount and final bill.

Formula:

\\[ GST = \frac{Price\times GST\ Rate}{100} \\]

\\[ Total = Price + GST \\]

Code:

```
def calculate_bill(price, gst_rate):    if price < 0:        return "Price cannot be negative"    elif gst_rate < 0:        return "GST rate cannot be negative"    else:        gst_amount = (price * gst_rate) / 100        total_amount = price + gst_amount        return gst_amount, total_amount
```

Calling the function:

```
result = calculate_bill(1000, 18)if isinstance(result, str):    print(result)else:    gst, total = result    print("GST Amount:", gst)    print("Final Bill:", total)
```

Output:

```
GST Amount: 180.0
Final Bill: 1180.0
```

### Program 3 – Grade calculator

Purpose: Display a grade based on marks.

```
def calculate_grade(marks):    if marks < 0 or marks > 100:        return "Invalid marks"    elif marks >= 90:        return "A Grade"    elif marks >= 75:        return "B Grade"    elif marks >= 60:        return "C Grade"    elif marks >= 50:        return "D Grade"    else:        return "Fail"
```

Calling the function:

```
grade = calculate_grade(85)print("Your Grade:", grade)
```

Output:

```
Your Grade: B Grade
```

### Program 4 – Largest of three numbers

Purpose: Find the largest number among three values.

```
def largest_of_three(a, b, c):    if a >= b and a >= c:        return a    elif b >= a and b >= c:        return b    else:        return c
```

Calling the function:

```
result = largest_of_three(25, 50, 35)print("Largest number:", result)
```

Output:

```
Largest number: 50
```

Notice that we used `>=` instead of `>` so equal values are handled correctly.

### Program 5 – Leap year checker

Purpose: Check whether a given year is a leap year.

Rules:

- Divisible by 400 → Leap year.
- Divisible by 100 but not by 400 → Not a leap year.
- Divisible by 4 but not by 100 → Leap year.
- Otherwise → Not a leap year.

Code:

```
def check_leap_year(year):    if year % 400 == 0:        return "Leap Year"    elif year % 100 == 0:        return "Not a Leap Year"    elif year % 4 == 0:        return "Leap Year"    else:        return "Not a Leap Year"
```

Calling the function:

```
result = check_leap_year(2024)print(result)
```

Output:

```
Leap Year
```

## Step 7. Important Python concepts to remember

| Concept        | Meaning                                     |
| -------------- | ------------------------------------------- |
| `def`          | Defines a function                          |
| `if`           | Checks a condition                          |
| `elif`         | Checks another condition                    |
| `else`         | Handles remaining cases                     |
| `and`          | Both conditions must be true                |
| `or`           | At least one condition must be true         |
| `not`          | Reverses a Boolean value                    |
| `return`       | Sends a result back                         |
| `input()`      | Accepts user input                          |
| `float()`      | Converts a value to a floating-point number |
| `isinstance()` | Checks an object's type                     |
| `%`            | Calculates remainder                        |
| `==`           | Checks equality                             |
| `=`            | Assigns a value                             |

## Step 8. Common mistakes

Mistake 1: Using `=` instead of `==`

Incorrect:

```
if age = 18:
```

Correct:

```
if age == 18:
```

Mistake 2: Forgetting indentation

Incorrect:

```
if age >= 18:print("Eligible")
```

Correct:

```
if age >= 18:    print("Eligible")
```

Mistake 3: Forgetting to return a result

```
def add(a, b):    print(a + b)
```

This displays the result but returns `None`.

If you need the result for another calculation, use `return`.

Mistake 4: Incorrect condition order

In a grade calculator, check the highest grade first. Otherwise, a score of 95 could match a lower threshold first.

## Step 9. Day 2 revision checklist

Python revision progress

# 0%

0 of 13 items checked

I understand arithmetic operators.

I understand comparison operators.

I understand logical operators.

I can use if, elif and else.

I understand functions and parameters.

I understand arguments and return.

I understand input validation.

I understand isinstance().

I completed the marks percentage calculator.

I completed the GST calculator.

I completed the grade calculator.

I completed the largest-of-three program.

I completed the leap-year checker.

Review my progress

Important: These are your study notes, not proof that every program has been tested. Keep only the items you have actually understood and verified as completed.

Once you've revised these notes, we'll continue with the remaining Day 2 roadmap sections:

1. DSA – loops, sum of 1 to n, multiplication table.
2. CS – operating system fundamentals.
3. Aptitude – averages.
4. English – explain today's CS topic.
5. Git commit and Day 2 evidence.

My recommendation: First revise Steps 1–5, then try writing the five programs without looking at the notes. This will help you remember the concepts during interviews.
