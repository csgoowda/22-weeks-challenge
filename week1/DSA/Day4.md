
# Day 4 – DSA Notes

## Topics
1. Reverse Integer
2. Numeric Palindrome
3. Array Sum

---

# 1. Reverse Integer

## Problem

Given an integer, reverse its digits.

### Examples

| Input | Output |
|---|---|
| 123 | 321 |
| 456 | 654 |
| 9876 | 6789 |
| 120 | 21 |
| 100 | 1 |

## Important Operators

### Modulus (%)

Returns the remainder after division.

Using `% 10` extracts the last digit.

```python
n = 1234
digit = n % 10

print(digit)  # 4
```

### Floor Division (//)

Divides and removes the fractional part.

Using `// 10` removes the last digit.

```python
n = 1234
n = n // 10

print(n)  # 123
```

## Algorithm

1. Take an integer as input.
2. Initialise `reverse = 0`.
3. Extract the last digit using `% 10`.
4. Add the digit to the reversed number.
5. Remove the last digit using `// 10`.
6. Repeat until the number becomes zero.

## Python Code

```python
n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reversed number:", reverse)
```

## Dry Run

Input: `123`

| Iteration | Digit | Reverse | Remaining n |
|---|---:|---:|---:|
| Initial | - | 0 | 123 |
| 1 | 3 | 3 | 12 |
| 2 | 2 | 32 | 1 |
| 3 | 1 | 321 | 0 |

Output:

```text
321
```

## Understanding the Main Formula

```python
reverse = reverse * 10 + digit
```

Example:

```text
reverse = 32
digit = 1

reverse = 32 * 10 + 1
reverse = 321
```

## Handling Negative Numbers

```python
n = int(input("Enter number: "))

sign = -1 if n < 0 else 1
n = abs(n)

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print("Reverse:", reverse * sign)
```

Example: `-123` gives `-321`.

## Complexity

- Time Complexity: O(d), where d is the number of digits.
- Auxiliary Space Complexity: O(1).

---

# 2. Numeric Palindrome

## Problem

A number is a palindrome if it remains the same when its digits are reversed.

### Examples

| Number | Reversed | Result |
|---|---|---|
| 121 | 121 | Palindrome |
| 123 | 321 | Not Palindrome |
| 1331 | 1331 | Palindrome |
| 454 | 454 | Palindrome |
| 120 | 21 | Not Palindrome |
| 0 | 0 | Palindrome |

## Logic

1. Take a number.
2. Store the original number in another variable.
3. Reverse the number.
4. Compare the original number with the reversed number.
5. If both are equal, it is a palindrome.

## Python Code

```python
n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
```

## Dry Run

Input: `121`

| Iteration | Digit | Reverse | Remaining n |
|---|---:|---:|---:|
| Initial | - | 0 | 121 |
| 1 | 1 | 1 | 12 |
| 2 | 2 | 12 | 1 |
| 3 | 1 | 121 | 0 |

Comparison:

```python
original == reverse

121 == 121
```

Output:

```text
Palindrome
```

## Important Edge Cases

| Input | Expected Result |
|---|---|
| 0 | Palindrome |
| 7 | Palindrome |
| 11 | Palindrome |
| 10 | Not Palindrome |
| 123 | Not Palindrome |
| -121 | Not Palindrome |

For this exercise, negative numbers are treated as not palindrome.

## Complexity

- Time Complexity: O(d), where d is the number of digits.
- Auxiliary Space Complexity: O(1).

---

# 3. Array Sum

## Problem

Given a list of numbers, calculate the sum of all elements.

### Example

Input:

```python
numbers = [10, 20, 30, 40, 50]
```

Expected Output:

```text
Total sum: 150
```

## Logic

1. Create a list of numbers.
2. Initialise `total = 0`.
3. Visit each element using a loop.
4. Add each element to the total.
5. Print the final sum.

## Python Code

```python
numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total = total + num

print("Total sum:", total)
```

Output:

```text
Total sum: 150
```

## Understanding the Main Formula

```python
total = total + num
```

This adds the current element to the previous total.

Short form:

```python
total += num
```

## Dry Run

Input:

```python
numbers = [10, 20, 30, 40, 50]
```

| Iteration | Number | Total |
|---|---:|---:|
| Initial | - | 0 |
| 1 | 10 | 10 |
| 2 | 20 | 30 |
| 3 | 30 | 60 |
| 4 | 40 | 100 |
| 5 | 50 | 150 |

Final Output:

```text
150
```

## Using a Function

```python
def array_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total


values = [10, 20, 30, 40, 50]

result = array_sum(values)

print("Total sum:", result)
```

## Using Python's Built-in sum()

```python
numbers = [10, 20, 30, 40, 50]

print(sum(numbers))
```

Output:

```text
150
```

For DSA practice, understand the loop-based solution first.

## Edge Cases

| Input | Output |
|---|---:|
| [1, 2, 3] | 6 |
| [5] | 5 |
| [] | 0 |
| [-1, 2, 3] | 4 |
| [0, 0, 0] | 0 |

## Complexity

- Time Complexity: O(n), because every element is visited once.
- Auxiliary Space Complexity: O(1), because only one extra variable is used.

---

# 4. Important DSA Concepts

## What is an Algorithm?

An algorithm is a step-by-step procedure used to solve a problem.

## What is a Dry Run?

A dry run means manually tracing a program with sample input to understand how variables change.

## What is Time Complexity?

Time complexity describes how the running time of an algorithm grows as input size increases.

| Complexity | Meaning |
|---|---|
| O(1) | Constant time |
| O(n) | Linear time |
| O(log n) | Logarithmic time |
| O(n²) | Quadratic time |

## What is Space Complexity?

Space complexity describes how much memory an algorithm needs as input size grows.

## What is Auxiliary Space?

Auxiliary space means the extra memory used by an algorithm, excluding the input itself.

---

# 5. Important Interview Questions

**1. What is an algorithm?**

An algorithm is a sequence of steps used to solve a particular problem.

**2. What does `%` do in Python?**

It returns the remainder after division.

**3. What does `//` do in Python?**

It performs floor division.

**4. How do you reverse an integer?**

Extract the last digit using `% 10`, add it to the reversed number and remove it using `// 10`.

**5. What is a numeric palindrome?**

A number that remains the same after reversing its digits.

**6. What is time complexity?**

It describes how an algorithm's running time grows with input size.

**7. What is O(n)?**

Linear complexity. The algorithm performs work proportional to the input size.

**8. What is O(1) auxiliary space?**

The algorithm uses a constant amount of extra memory.

**9. Why do we initialise `total = 0` in array sum?**

Zero is the starting value for addition. It allows us to accumulate every list element.

**10. What is a dry run?**

Manually executing a program step by step with sample input.

---

# 6. Day 4 DSA Practice Checklist

- [ ] Understand `% 10`.
- [ ] Understand `// 10`.
- [ ] Write reverse integer without looking at notes.
- [ ] Dry-run reverse integer.
- [ ] Write numeric palindrome without looking at notes.
- [ ] Test palindrome edge cases.
- [ ] Write array sum using a loop.
- [ ] Test empty and negative-number lists.
- [ ] Explain time complexity.
- [ ] Explain auxiliary space complexity.
- [ ] Solve all three problems independently.
- [ ] Save the code in the GitHub repository.

## Today's DSA Deliverables

Create these three Python files:

1. `reverse_integer.py`
2. `numeric_palindrome.py`
3. `array_sum.py`

**Remember:** Don't just memorise code. Understand the logic, dry-run the variables, test edge cases and explain the complexity.
