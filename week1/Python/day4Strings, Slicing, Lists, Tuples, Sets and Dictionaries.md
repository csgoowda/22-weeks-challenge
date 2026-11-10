# Day 4 – Python Core Notes
## Topic: Strings, Slicing, Lists, Tuples, Sets and Dictionaries

## 1. Strings

A string is a sequence of characters enclosed in quotation marks.

```python
name = "Chethan"
language = "Python"

print(name)
print(language)
```

### String indexing

Python indexing starts from `0`.

```python
name = "Chethan"

print(name[0])  # C
print(name[1])  # h
print(name[2])  # e
```

Negative indexing starts from the end.

```python
print(name[-1])  # n
print(name[-2])  # a
```

### String length

Use `len()` to find the number of characters.

```python
name = "Chethan"

print(len(name))  # 7
```

### Common string methods

```python
text = "  hello python  "

print(text.upper())       # HELLO PYTHON
print(text.lower())       # hello python
print(text.strip())       # Removes spaces at beginning and end
print(text.title())       # Hello Python
print(text.replace("python", "world"))
```

Important:
- `upper()` – converts to uppercase.
- `lower()` – converts to lowercase.
- `strip()` – removes spaces at the beginning and end.
- `title()` – capitalizes the first letter of each word.
- `replace()` – replaces one part of a string with another.

## 2. String Slicing

Slicing extracts a portion of a string.

Syntax:

```python
string[start:stop:step]
```

Example:

```python
name = "Chethan"

print(name[0:3])   # Che
print(name[2:5])   # eth
print(name[:4])    # Chet
print(name[2:])    # ethan
print(name[::-1])  # nahtehC
```

Important:
- Start index is included.
- Stop index is excluded.
- Step controls the direction and interval.
- `[::-1]` reverses a string.

## 3. Lists

A list stores multiple values in one variable.

Lists are mutable, meaning we can change their contents.

```python
fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[1])
```

### List operations

```python
fruits.append("orange")       # Add an item
fruits.remove("banana")       # Remove a specific item
fruits.insert(1, "grapes")    # Insert at an index
fruits.pop()                  # Remove the last item

print(fruits)
```

### Loop through a list

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

Important:
- `append()` – adds an item at the end.
- `remove()` – removes a matching item.
- `insert()` – adds an item at a specified position.
- `pop()` – removes and returns an item.

## 4. Tuples

A tuple is similar to a list, but it cannot be modified after creation.

Tuples are immutable.

```python
coordinates = (10, 20)

print(coordinates[0])
print(coordinates[1])
```

### List vs Tuple

| List | Tuple |
|---|---|
| Uses `[]` | Uses `()` |
| Mutable | Immutable |
| Items can be changed | Items cannot be changed |
| Supports adding/removing items | Does not support item modification |

## 5. Sets

A set stores unique values. Duplicate values are automatically removed.

```python
numbers = {10, 20, 10, 30, 20}

print(numbers)
```

Output contains only unique values:

```text
{10, 20, 30}
```

### Set operations

```python
numbers = {10, 20, 30}

numbers.add(40)
numbers.remove(20)

print(numbers)
```

Important:
- Sets do not allow duplicate values.
- Sets are unordered.
- Sets are useful for removing duplicates.
- Do not depend on set iteration order.

## 6. Dictionaries

A dictionary stores information as key-value pairs.

Example:

```python
employee = {
    "name": "Rahul",
    "department": "IT",
    "salary": 30000
}

print(employee["name"])
print(employee["salary"])
```

### Add and update values

```python
employee["city"] = "Mysore"
employee["salary"] = 35000

print(employee)
```

### Loop through a dictionary

```python
for key, value in employee.items():
    print(key, value)
```

Important:
- A key is used to access its value.
- Keys must be unique.
- Dictionaries are mutable.
- `items()` returns key-value pairs.

## 7. Program – Username Cleaner

Problem: Convert a username into lowercase, remove unnecessary spaces at the beginning and end, and replace spaces between words with underscores.

Input:

```text
   Chethan Gowda 123
```

Expected output:

```text
chethan_gowda_123
```

Solution:

```python
def clean_username(username):
    username = username.strip()
    username = username.lower()
    username = username.replace(" ", "_")

    return username


name = input("Enter username: ")

result = clean_username(name)

print("Clean username:", result)
```

Concepts used:
- `strip()`
- `lower()`
- `replace()`
- Functions
- `return`

Note: This program replaces each ordinary space with an underscore. It does not remove spaces between words.

## 8. Program – Word Counter

Problem: Count the number of words in a sentence.

Solution:

```python
def word_counter(sentence):
    words = sentence.split()
    return len(words)


text = input("Enter a sentence: ")

result = word_counter(text)

print("Total words:", result)
```

Example:

Input:

```text
I am learning Python
```

Output:

```text
Total words: 4
```

Concepts:
- `split()` separates a sentence into words.
- `len()` counts the elements in a list.
- `return` sends the result back.

## 9. Program – Duplicate Remover

Problem: Remove repeated values from a list.

Input:

```python
numbers = [10, 20, 10, 30, 20, 40]
```

### Method 1: Using set()

```python
numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = list(set(numbers))

print(unique_numbers)
```

Note: Set conversion does not guarantee the original order.

### Method 2: Preserve original order

```python
numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)
```

Output:

```text
[10, 20, 30, 40]
```

### Reusable function

```python
def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))


values = [10, 20, 10, 30, 20, 40]

result = remove_duplicates(values)

print(result)
```

Concepts:
- Sets store unique values.
- Dictionary keys are unique.
- `dict.fromkeys()` preserves the insertion order of keys.
- `list()` converts the result into a list.

## 10. Program – Palindrome Checker

A palindrome reads the same forward and backward.

Examples:
- madam
- level
- radar

Solution:

```python
def is_palindrome(word):
    word = word.lower().strip()

    return word == word[::-1]


text = input("Enter a word: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")
```

Example:

```text
Enter a word: Madam
Palindrome
```

### Understanding the logic

```python
word[::-1]
```

This reverses the string.

```python
word == word[::-1]
```

This compares the original word with the reversed word.

If both are equal, it is a palindrome.

## 11. Important Differences

| Concept | Meaning |
|---|---|
| String | Sequence of characters |
| List | Mutable collection of items |
| Tuple | Immutable collection of items |
| Set | Collection of unique items |
| Dictionary | Collection of key-value pairs |
| `len()` | Returns the length |
| `split()` | Splits a string into a list |
| `strip()` | Removes surrounding whitespace |
| `replace()` | Replaces part of a string |
| `[::-1]` | Reverses a sequence |
| `dict.fromkeys()` | Creates a dictionary from unique keys |

## 12. Interview Questions

**1. What is a string?**

A string is a sequence of characters enclosed in quotation marks.

**2. What is string slicing?**

Slicing extracts a portion of a string using start, stop and step.

**3. What is the difference between a list and a tuple?**

A list is mutable, whereas a tuple is immutable.

**4. What is a set?**

A set is a collection of unique values.

**5. What is a dictionary?**

A dictionary stores information in key-value pairs.

**6. What does `split()` do?**

It separates a string into a list of words or parts.

**7. What does `strip()` do?**

It removes whitespace at the beginning and end of a string.

**8. How do you reverse a string in Python?**

Using slicing:

```python
text[::-1]
```

**9. How do you remove duplicates from a list?**

Using `set()` or `dict.fromkeys()`.

**10. What is a palindrome?**

A word or sequence that reads the same forward and backward.

## 13. Day 4 Python Completion Checklist

- [ ] Understand strings and indexing.
- [ ] Practise string slicing.
- [ ] Understand list operations.
- [ ] Understand tuples.
- [ ] Understand sets.
- [ ] Understand dictionaries.
- [ ] Build username cleaner.
- [ ] Build word counter.
- [ ] Build duplicate remover.
- [ ] Build palindrome checker.
- [ ] Organise programs in the project repository.
- [ ] Add a README explaining the programs.
- [ ] Run and test all programs.

**Day 4 Python deliverable:** Four practical programs, the five core data types/topics, organised code and a README.

**Remember:** Understand the logic and write the programs yourself. Do not just copy and paste code.
