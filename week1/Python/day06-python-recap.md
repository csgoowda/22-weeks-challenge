
# Day 6 – Python Recap: Functions, Collections, Strings and Comprehensions

## 1. Today's Learning Objectives

Today we revise Python concepts from Day 1 to Day 5.

By the end of this lesson, you should understand:

1. Functions and parameters.
2. Return values and default arguments.
3. *args and **kwargs.
4. Local and global scope.
5. Lists and list operations.
6. Dictionaries and dictionary methods.
7. Sets and set operations.
8. String methods.
9. List, dictionary and set comprehensions.
10. Sorting, copying and references.
11. Assert statements and testing.

Today's practical deliverable:

`week01/day06_recap.py`

It must contain six functions, with at least two assert tests per function, including an empty-input test.

---

# PART 1 – FUNCTIONS

## 2. What is a Function?

A function is a reusable block of code that performs a specific task.

Instead of writing the same code repeatedly, we create a function and call it whenever needed.

### Example

```python
def add(a, b):
    result = a + b
    return result


answer = add(10, 20)

print(answer)
```

Output:

```text
30
```

### Explanation

- `def` – keyword used to define a function.
- `add` – function name.
- `a, b` – parameters.
- `return` – sends the result back.
- `add(10, 20)` – function call.
- `10, 20` – arguments.

## 3. Parameters and Arguments

A parameter is a variable written in a function definition.

An argument is the actual value passed when calling the function.

```python
def greet(name):
    print("Hello", name)


greet("Chethan")
```

Output:

```text
Hello Chethan
```

Here:
- `name` is a parameter.
- `"Chethan"` is an argument.

## 4. Return vs Print

### Using print()

```python
def add(a, b):
    print(a + b)


result = add(10, 20)

print(result)
```

Output:

```text
30
None
```

Why?

`print()` displays the result but does not return it. Python functions without an explicit return statement return `None`.

### Using return

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

Important:

- `print()` displays information.
- `return` sends a value back to the caller.

## 5. Default Arguments

A default argument is a parameter that already has a value.

```python
def greet(name="Guest"):
    return "Hello " + name


print(greet())
print(greet("Chethan"))
```

Output:

```text
Hello Guest
Hello Chethan
```

When no argument is supplied, Python uses the default value.

### Important: Mutable Default Arguments

Avoid using a mutable object such as a list as a default argument.

Incorrect:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

The same list can be shared between multiple function calls.

Correct:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)

    return items
```

Why use `None`?

A new list is created inside the function whenever no list is provided.

## 6. *args

`*args` allows a function to accept multiple positional arguments.

```python
def total(*args):
    result = 0

    for num in args:
        result += num

    return result


print(total(10, 20, 30))
```

Output:

```text
60
```

Explanation:

- `*args` collects positional arguments into a tuple.
- We can loop through the tuple.
- We can process any number of values.

## 7. **kwargs

`**kwargs` allows a function to accept multiple keyword arguments.

```python
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


student_details(
    name="Chethan",
    branch="ISE",
    semester=7
)
```

Output:

```text
name Chethan
branch ISE
semester 7
```

Explanation:

- `**kwargs` collects keyword arguments into a dictionary.
- Each argument has a key and a value.
- `items()` allows us to access both.

### Difference Between *args and **kwargs

| Feature | *args | **kwargs |
|---|---|---|
| Purpose | Multiple positional arguments | Multiple keyword arguments |
| Data type inside function | Tuple | Dictionary |
| Example | `add(10, 20)` | `name="Chethan"` |

## 8. Local and Global Scope

Scope determines where a variable can be accessed.

### Local Variable

A variable created inside a function is usually local to that function.

```python
def calculate():
    number = 100
    print(number)


calculate()
```

Output:

```text
100
```

The variable `number` cannot normally be accessed outside this function.

### Global Variable

A variable created outside functions is global.

```python
name = "Chethan"


def greet():
    print(name)


greet()
```

Output:

```text
Chethan
```

### Using the global Keyword

```python
count = 0


def increase():
    global count
    count += 1


increase()

print(count)
```

Output:

```text
1
```

The `global` keyword allows the function to reassign the global variable.

---

# PART 2 – LISTS

## 9. What is a List?

A list is an ordered, mutable collection of elements.

Mutable means we can change its contents.

```python
numbers = [10, 20, 30, 40]

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

Lists:
- Preserve order.
- Allow duplicate values.
- Allow different data types.
- Can be modified.

## 10. Accessing List Elements

Python uses zero-based indexing.

```python
fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[1])
print(fruits[-1])
```

Output:

```text
apple
banana
mango
```

| Index | Value |
|---:|---|
| 0 | apple |
| 1 | banana |
| 2 | mango |
| -1 | mango |

## 11. append()

Adds one element at the end of a list.

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

## 12. extend()

Adds multiple elements from another iterable.

```python
numbers = [10, 20]

numbers.extend([30, 40])

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

Difference:

- `append()` adds one object.
- `extend()` adds elements from an iterable.

## 13. insert()

Adds an element at a particular position.

```python
numbers = [10, 30, 40]

numbers.insert(1, 20)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

## 14. pop()

Removes and returns an element.

```python
numbers = [10, 20, 30]

removed = numbers.pop()

print(removed)
print(numbers)
```

Output:

```text
30
[10, 20]
```

We can also remove by index:

```python
numbers = [10, 20, 30]

numbers.pop(0)

print(numbers)
```

Output:

```text
[20, 30]
```

## 15. remove()

Removes the first matching value.

```python
numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)
```

Output:

```text
[10, 30, 20]
```

Difference:

- `pop()` removes using an index and returns the removed value.
- `remove()` removes the first matching value.

## 16. List Slicing

Slicing extracts part of a list.

Syntax:

```python
list_name[start:stop:step]
```

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
```

Output:

```text
[20, 30, 40]
[10, 20, 30]
[30, 40, 50]
[50, 40, 30, 20, 10]
```

Remember:
- Start index is included.
- Stop index is excluded.
- Step determines how many positions to move.

## 17. sort() vs sorted()

### sort()

Changes the original list.

```python
numbers = [5, 2, 4, 1]

numbers.sort()

print(numbers)
```

Output:

```text
[1, 2, 4, 5]
```

Important: `sort()` returns `None`.

### sorted()

Creates and returns a new sorted list.

```python
numbers = [5, 2, 4, 1]

result = sorted(numbers)

print(result)
print(numbers)
```

Output:

```text
[1, 2, 4, 5]
[5, 2, 4, 1]
```

### Descending Order

```python
numbers = [5, 2, 4, 1]

print(sorted(numbers, reverse=True))
```

Output:

```text
[5, 4, 2, 1]
```

### Important Difference

| sort() | sorted() |
|---|---|
| Modifies original list | Creates a new sorted list |
| Returns None | Returns sorted list |
| List method | Built-in function |

## 18. Copy vs Reference

### Reference

Two variables can refer to the same list.

```python
a = [10, 20, 30]

b = a

b.append(40)

print(a)
print(b)
```

Output:

```text
[10, 20, 30, 40]
[10, 20, 30, 40]
```

Why?

Both variables refer to the same list.

### Copy

```python
a = [10, 20, 30]

b = a.copy()

b.append(40)

print(a)
print(b)
```

Output:

```text
[10, 20, 30]
[10, 20, 30, 40]
```

`copy()` creates a shallow copy of the list.

Important: A shallow copy does not recursively copy nested mutable objects.

## 19. Changing a List While Looping

Avoid modifying a list while iterating over the same list.

Problematic example:

```python
numbers = [1, 2, 2, 3, 2]

for num in numbers:
    if num == 2:
        numbers.remove(num)

print(numbers)
```

Changing the list can cause elements to be skipped.

Safer approach:

```python
numbers = [1, 2, 2, 3, 2]

for num in numbers.copy():
    if num == 2:
        numbers.remove(num)

print(numbers)
```

Output:

```text
[1, 3]
```

---

# PART 3 – DICTIONARIES

## 20. What is a Dictionary?

A dictionary stores data in key-value pairs.

```python
student = {
    "name": "Chethan",
    "branch": "ISE",
    "semester": 7
}

print(student)
```

Output:

```text
{'name': 'Chethan', 'branch': 'ISE', 'semester': 7}
```

Important:
- Keys must be unique.
- Values can be duplicated.
- Dictionaries are mutable.
- Keys must be hashable.

## 21. Accessing Dictionary Values

```python
student = {
    "name": "Chethan",
    "age": 22
}

print(student["name"])
```

Output:

```text
Chethan
```

Using a missing key with square brackets raises a `KeyError`.

## 22. get()

`get()` safely retrieves a value.

```python
student = {
    "name": "Chethan"
}

print(student.get("name"))
print(student.get("age", 0))
```

Output:

```text
Chethan
0
```

Syntax:

```python
dictionary.get(key, default_value)
```

If the key does not exist, the default value is returned.

## 23. keys(), values() and items()

```python
student = {
    "name": "Chethan",
    "age": 22
}

print(student.keys())
print(student.values())
print(student.items())
```

These methods provide:
- `keys()` – dictionary keys.
- `values()` – dictionary values.
- `items()` – key-value pairs.

## 24. Updating a Dictionary

```python
student = {"name": "Chethan"}

student["age"] = 22

student["branch"] = "ISE"

print(student)
```

Output:

```text
{'name': 'Chethan', 'age': 22, 'branch': 'ISE'}
```

## 25. setdefault()

`setdefault()` returns the existing value for a key or inserts the default value if the key is missing.

```python
student = {"name": "Chethan"}

student.setdefault("branch", "ISE")

print(student)
```

Output:

```text
{'name': 'Chethan', 'branch': 'ISE'}
```

### Important Example

```python
groups = {}

groups.setdefault(3, []).append("cat")
groups.setdefault(3, []).append("dog")

print(groups)
```

Output:

```text
{3: ['cat', 'dog']}
```

Explanation:

1. If key `3` does not exist, create it with an empty list.
2. Append `"cat"` to that list.
3. The next call finds the existing list.
4. Append `"dog"` to the same list.

## 26. Counting Words Using a Dictionary

```python
def word_frequency(text):
    frequency = {}

    words = text.lower().split()

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


print(word_frequency("apple banana apple mango"))
```

Output:

```text
{'apple': 2, 'banana': 1, 'mango': 1}
```

Explanation:

`frequency.get(word, 0) + 1`

- Gets the current count.
- Uses zero if the word is new.
- Adds one.
- Stores the updated count.

Note: This basic function does not remove punctuation.

---

# PART 4 – SETS

## 27. What is a Set?

A set is an unordered collection of unique elements.

```python
numbers = {10, 20, 30, 20, 10}

print(numbers)
```

Output contains only:

```text
{10, 20, 30}
```

Important:
- Sets automatically remove duplicates.
- Sets do not support indexing.
- Sets are mutable.
- Elements must be hashable.

## 28. Creating an Empty Set

Correct:

```python
numbers = set()
```

Incorrect:

```python
numbers = {}
```

Why?

`{}` creates an empty dictionary, not an empty set.

## 29. add()

Adds one element.

```python
numbers = {10, 20}

numbers.add(30)

print(numbers)
```

## 30. update()

Adds multiple elements from an iterable.

```python
numbers = {10, 20}

numbers.update([30, 40])

print(numbers)
```

## 31. remove() and discard()

Both remove an element from a set.

```python
numbers = {10, 20, 30}

numbers.remove(20)
numbers.discard(40)
```

Difference:

- `remove()` raises KeyError if the element is missing.
- `discard()` does not raise an error if it is missing.

## 32. Union

Union combines elements from two sets without duplicates.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

Output:

```text
{1, 2, 3, 4, 5}
```

Alternative:

```python
print(a.union(b))
```

## 33. Intersection

Intersection returns common elements.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)
```

Output:

```text
{3}
```

Alternative:

```python
print(a.intersection(b))
```

## 34. Difference

Difference returns elements present in the first set but not the second.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a - b)
```

Output:

```text
{1, 2}
```

---

# PART 5 – STRINGS

## 35. What is a String?

A string is a sequence of characters.

```python
name = "Python"

print(name)
```

Strings are immutable. This means we cannot change individual characters directly.

## 36. String Indexing

```python
language = "Python"

print(language[0])
print(language[1])
print(language[-1])
```

Output:

```text
P
y
n
```

## 37. String Slicing

```python
language = "Python"

print(language[0:3])
print(language[::-1])
```

Output:

```text
Pyt
nohtyP
```

## 38. split()

Splits a string into a list.

```python
text = "Python is easy"

words = text.split()

print(words)
```

Output:

```text
['Python', 'is', 'easy']
```

We can specify a separator:

```python
text = "apple,banana,mango"

print(text.split(","))
```

Output:

```text
['apple', 'banana', 'mango']
```

## 39. join()

Combines strings from an iterable into one string.

```python
words = ["Python", "is", "easy"]

result = " ".join(words)

print(result)
```

Output:

```text
Python is easy
```

Another example:

```python
words = ["apple", "banana", "mango"]

print(",".join(words))
```

Output:

```text
apple,banana,mango
```

Remember:

- `split()` – string to list.
- `join()` – iterable of strings to string.

## 40. strip()

Removes whitespace from the beginning and end of a string.

```python
name = "   Chethan   "

print(name.strip())
```

Output:

```text
Chethan
```

Related methods:

- `lstrip()` – removes leading whitespace.
- `rstrip()` – removes trailing whitespace.

## 41. replace()

Replaces part of a string with another value.

```python
text = "I like Java"

result = text.replace("Java", "Python")

print(result)
```

Output:

```text
I like Python
```

## 42. lower() and upper()

```python
text = "Python Programming"

print(text.lower())
print(text.upper())
```

Output:

```text
python programming
PYTHON PROGRAMMING
```

## 43. title() and capitalize()

```python
text = "hello python WORLD"

print(text.title())
print(text.capitalize())
```

Output:

```text
Hello Python World
Hello python world
```

- `title()` capitalizes the beginning of each word and lowercases the remaining letters.
- `capitalize()` capitalizes the first character and lowercases the rest of the string.

## 44. f-Strings

f-strings allow variables and expressions to be inserted into strings.

```python
name = "Chethan"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Chethan and I am 22 years old.
```

Example with calculations:

```python
price = 100
quantity = 3

print(f"Total amount: {price * quantity}")
```

Output:

```text
Total amount: 300
```

---

# PART 6 – COMPREHENSIONS

## 45. What is a Comprehension?

A comprehension is a concise way to create a new collection from an iterable.

Python supports:
1. List comprehension.
2. Dictionary comprehension.
3. Set comprehension.

## 46. List Comprehension

Syntax:

```python
[expression for item in iterable if condition]
```

### Normal Loop

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)
```

### List Comprehension

```python
numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

### With a Condition

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    num for num in numbers
    if num % 2 == 0
]

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

## 47. Dictionary Comprehension

Syntax:

```python
{key_expression: value_expression for item in iterable}
```

Example:

```python
numbers = [1, 2, 3, 4]

squares = {
    num: num ** 2
    for num in numbers
}

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16}
```

### With a Condition

```python
numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    num: num ** 2
    for num in numbers
    if num % 2 == 0
}

print(even_squares)
```

Output:

```text
{2: 4, 4: 16, 6: 36}
```

## 48. Set Comprehension

Syntax:

```python
{expression for item in iterable}
```

Example:

```python
numbers = [1, 2, 2, 3, 3, 4]

unique_squares = {
    num ** 2 for num in numbers
}

print(unique_squares)
```

Output contains:

```text
{1, 4, 9, 16}
```

### With a Condition

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {
    num for num in numbers
    if num % 2 == 0
}

print(even_numbers)
```

Output:

```text
{2, 4, 6}
```

### When Should You Use Comprehensions?

Use comprehensions for short transformations and filtering.

Use normal loops when:
- The logic is complicated.
- Multiple operations are required.
- You need several conditions or statements.
- Readability would suffer.

---

# PART 7 – SIX DAY 6 PRACTICAL FUNCTIONS

## 49. Function 1: word_frequency(text)

Purpose: Count how many times each word appears.

```python
def word_frequency(text):
    frequency = {}

    words = text.lower().split()

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency
```

Example:

```python
print(word_frequency("apple banana apple mango"))
```

Output:

```text
{'apple': 2, 'banana': 1, 'mango': 1}
```

Complexity:
- Time: O(n), where n is the number of words.
- Space: O(k), where k is the number of unique words.

## 50. Function 2: unique_sorted(items)

Purpose: Remove duplicates and sort the values.

```python
def unique_sorted(items):
    return sorted(set(items))
```

Example:

```python
print(unique_sorted([5, 2, 3, 2, 5, 1]))
```

Output:

```text
[1, 2, 3, 5]
```

Explanation:
- `set()` removes duplicates.
- `sorted()` returns a sorted list.

Complexity:
- Average time: O(n log n).
- Space: O(n).

## 51. Function 3: even_squares(nums)

Purpose: Return squares of even numbers.

```python
def even_squares(nums):
    return [
        num ** 2
        for num in nums
        if num % 2 == 0
    ]
```

Example:

```python
print(even_squares([1, 2, 3, 4, 5, 6]))
```

Output:

```text
[4, 16, 36]
```

Explanation:
- `num ** 2` calculates the square.
- `num % 2 == 0` checks whether the number is even.

Complexity:
- Time: O(n).
- Space: O(n) in the worst case.

## 52. Function 4: invert_dict(d)

Purpose: Exchange dictionary keys and values.

```python
def invert_dict(d):
    return {
        value: key
        for key, value in d.items()
    }
```

Example:

```python
print(invert_dict({
    "Python": 1,
    "Java": 2,
    "C++": 3
}))
```

Output:

```text
{1: 'Python', 2: 'Java', 3: 'C++'}
```

Important:
- Original values become new keys.
- Original keys become new values.
- Original values must be hashable to serve as dictionary keys.
- If original values repeat, earlier entries can be overwritten.

Complexity:
- Time: O(n).
- Space: O(n).

## 53. Function 5: normalize_name(s)

Purpose: Remove leading and trailing spaces and format a name.

```python
def normalize_name(s):
    return s.strip().title()
```

Example:

```python
print(normalize_name("   chethan gowda   "))
```

Output:

```text
Chethan Gowda
```

Explanation:
- `strip()` removes leading and trailing whitespace.
- `title()` capitalizes the beginning of each word.

Complexity:
- Time: O(n).
- Space: O(n) for the resulting string.

## 54. Function 6: group_by_length(words)

Purpose: Group words according to their length.

```python
def group_by_length(words):
    groups = {}

    for word in words:
        length = len(word)

        groups.setdefault(length, []).append(word)

    return groups
```

Example:

```python
print(
    group_by_length(
        ["cat", "dog", "apple", "bat", "mango"]
    )
)
```

Output:

```text
{
    3: ['cat', 'dog', 'bat'],
    5: ['apple', 'mango']
}
```

Explanation:

1. Create an empty dictionary.
2. Loop through each word.
3. Find the length of the word.
4. Use that length as a dictionary key.
5. Append the word to the corresponding list.
6. Return the dictionary.

Complexity:
- Time: O(n) for n words, excluding the cost of processing the characters to calculate their lengths.
- Space: O(n) for the grouped words.

---

# PART 8 – ASSERT TESTING

## 55. What is assert?

`assert` is used to check whether a condition is true.

If the condition is true, execution continues.

If it is false, Python raises an AssertionError.

Example:

```python
assert 10 + 20 == 30

print("Test passed")
```

Output:

```text
Test passed
```

Incorrect assertion:

```python
assert 10 + 20 == 40
```

This raises:

```text
AssertionError
```

## 56. Why Do We Use Assert?

- To verify function output.
- To catch logical mistakes.
- To test different inputs.
- To verify empty inputs.
- To check that code behaves as expected.

## 57. Assert Tests for All Six Functions

### Test 1: word_frequency()

```python
assert word_frequency("apple banana apple") == {
    "apple": 2,
    "banana": 1
}

assert word_frequency("") == {}
```

### Test 2: unique_sorted()

```python
assert unique_sorted([5, 2, 3, 2, 1]) == [1, 2, 3, 5]

assert unique_sorted([]) == []
```

### Test 3: even_squares()

```python
assert even_squares([1, 2, 3, 4]) == [4, 16]

assert even_squares([]) == []
```

### Test 4: invert_dict()

```python
assert invert_dict({
    "Python": 1,
    "Java": 2
}) == {
    1: "Python",
    2: "Java"
}

assert invert_dict({}) == {}
```

### Test 5: normalize_name()

```python
assert normalize_name("  chethan gowda  ") == "Chethan Gowda"

assert normalize_name("") == ""
```

### Test 6: group_by_length()

```python
assert group_by_length(["cat", "dog", "apple"]) == {
    3: ["cat", "dog"],
    5: ["apple"]
}

assert group_by_length([]) == {}
```

---

# PART 9 – COMPLETE PROJECT FILE

## 58. Folder Structure

```text
practice-repo/
│
└── week01/
    └── day06_recap.py
```

## 59. Complete day06_recap.py

Copy the following complete code into your Python file.

```python
# Day 6 - Python Recap
# Functions, Collections, Strings and Comprehensions


# 1. Count word frequency
def word_frequency(text):
    frequency = {}

    words = text.lower().split()

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


# 2. Remove duplicates and sort
def unique_sorted(items):
    return sorted(set(items))


# 3. Return squares of even numbers
def even_squares(nums):
    return [
        num ** 2
        for num in nums
        if num % 2 == 0
    ]


# 4. Invert dictionary
def invert_dict(d):
    return {
        value: key
        for key, value in d.items()
    }


# 5. Normalize a name
def normalize_name(s):
    return s.strip().title()


# 6. Group words by their length
def group_by_length(words):
    groups = {}

    for word in words:
        length = len(word)

        groups.setdefault(length, []).append(word)

    return groups


# ASSERT TESTS

# Function 1
assert word_frequency("apple banana apple") == {
    "apple": 2,
    "banana": 1
}

assert word_frequency("") == {}


# Function 2
assert unique_sorted([5, 2, 3, 2, 1]) == [1, 2, 3, 5]

assert unique_sorted([]) == []


# Function 3
assert even_squares([1, 2, 3, 4]) == [4, 16]

assert even_squares([]) == []


# Function 4
assert invert_dict({
    "Python": 1,
    "Java": 2
}) == {
    1: "Python",
    2: "Java"
}

assert invert_dict({}) == {}


# Function 5
assert normalize_name("  chethan gowda  ") == "Chethan Gowda"

assert normalize_name("") == ""


# Function 6
assert group_by_length(["cat", "dog", "apple"]) == {
    3: ["cat", "dog"],
    5: ["apple"]
}

assert group_by_length([]) == {}


print("All assert tests passed!")
```

## 60. How to Run the Project

Open the terminal in your project folder.

Run:

```bash
python week01/day06_recap.py
```

Expected output:

```text
All assert tests passed!
```

If an assertion fails, Python will show an AssertionError. Check the function and the expected output.

---

# PART 10 – IMPORTANT INTERVIEW QUESTIONS

## Functions

1. What is a function?
2. What is the difference between parameters and arguments?
3. What is the difference between print and return?
4. What are default arguments?
5. What is the difference between *args and **kwargs?
6. What is local scope?
7. What is global scope?
8. Why should mutable default arguments be avoided?

## Lists

1. What is a list?
2. What is the difference between append() and extend()?
3. What is the difference between pop() and remove()?
4. What is list slicing?
5. What is the difference between sort() and sorted()?
6. What is the difference between copying a list and assigning a reference?
7. Why should we avoid modifying a list while iterating over it?

## Dictionaries

1. What is a dictionary?
2. What is the difference between get() and square bracket access?
3. What does items() return?
4. What is setdefault()?
5. How do you count word frequency using a dictionary?

## Sets

1. What is a set?
2. Why does a set remove duplicates?
3. What is the difference between union and intersection?
4. What is the difference between remove() and discard()?

## Strings

1. What is a string?
2. Are strings mutable or immutable?
3. What does split() do?
4. What does join() do?
5. What is the difference between strip() and replace()?
6. What are f-strings?

## Comprehensions

1. What is list comprehension?
2. What is dictionary comprehension?
3. What is set comprehension?
4. Why do we use comprehensions?
5. When should we use a normal loop instead?

---

# PART 11 – COMMON MISTAKES TO AVOID

1. `list.sort()` returns None. Use `sorted()` when you need a new list.
2. Changing a list while looping over it can skip elements.
3. Avoid mutable default arguments such as `def function(items=[])`.
4. Use `get()` when a dictionary key may be missing.
5. Sets do not guarantee sorted order.
6. Strings are immutable.
7. `strip()` removes whitespace at the beginning and end, not all spaces everywhere.
8. `title()` converts the remaining letters of each word to lowercase.
9. Repeated values in an inverted dictionary can overwrite earlier entries.
10. An assert test checks a condition; it does not automatically test every possible input.

---

# PART 12 – DAY 6 COMPLETION CHECKLIST

## Python Core

- [ ] Create week01 folder.
- [ ] Create day06_recap.py.
- [ ] Write word_frequency(text).
- [ ] Write unique_sorted(items).
- [ ] Write even_squares(nums).
- [ ] Write invert_dict(d).
- [ ] Write normalize_name(s).
- [ ] Write group_by_length(words).
- [ ] Add at least two assert tests per function.
- [ ] Include an empty-input test for every function.
- [ ] Run the Python file successfully.

## GitHub

- [ ] Review the final code.
- [ ] Commit the changes.
- [ ] Push to GitHub.

Commit message:

```bash
git add week01/day06_recap.py
git commit -m "Add Python recap functions with asserts"
git push
```

## Final Learning Summary

Today I revised:

- Functions, parameters and return values.
- Default arguments, *args and **kwargs.
- Local and global scope.
- Lists and list operations.
- Dictionaries and dictionary methods.
- Sets and set operations.
- Strings and string methods.
- List, dictionary and set comprehensions.
- Assert testing.

**Final deliverable:** `week01/day06_recap.py`

**Goal:** Six working functions with assert tests and a successful Git commit.
