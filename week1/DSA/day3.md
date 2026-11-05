# Day 3 – DSA Notes (Data Structures and Algorithms)

**Date:** 5 November 2026  
**Week:** 1  
**Topics:** Factorial, Digit Sum, Prime Number Check, Dry Run, Edge Cases, Time Complexity and Space Complexity.

---

# 1. What is DSA?

DSA stands for Data Structures and Algorithms.

- **Data Structures:** Ways of organizing and storing data.
- **Algorithms:** Step-by-step instructions to solve a problem.

Example:

To find the factorial of 5, we need an algorithm that multiplies all numbers from 1 to 5.

```text
5 × 4 × 3 × 2 × 1 = 120
```

DSA helps us write programs that are correct and efficient.

# 2. Factorial of a Number

## 2.1 What is factorial?

Factorial is the product of all positive integers from 1 up to a given number.

It is represented using the symbol `!`.

**Example:**

```text
5! = 5 × 4 × 3 × 2 × 1
   = 120
```

Other examples:

| Number | Factorial |
|---:|---:|
| 0 | 1 |
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |

**Important:**

- Factorial of 0 is 1.
- Factorial of 1 is 1.
- Factorial is not defined for negative integers.

## 2.2 Algorithm

1. Start.
2. Read a number `n`.
3. If `n` is negative, display an invalid message.
4. Initialize `factorial = 1`.
5. Repeat from 1 to n.
6. Multiply factorial by the current number.
7. Display the result.
8. Stop.

## 2.3 Python Program

```python
n = int(input("Enter a number: "))

factorial = 1

if n < 0:
    print("Factorial is not defined for negative numbers")

else:
    for i in range(1, n + 1):
        factorial = factorial * i

    print("Factorial:", factorial)
```

**Output:**

```text
Enter a number: 5
Factorial: 120
```

## 2.4 Understanding the Logic

Initially:

```python
factorial = 1
```

We use 1 because multiplying by 1 does not change the result.

The loop:

```python
for i in range(1, n + 1):
    factorial = factorial * i
```

For n = 5:

```text
Initial factorial = 1

Iteration 1: 1 × 1 = 1
Iteration 2: 1 × 2 = 2
Iteration 3: 2 × 3 = 6
Iteration 4: 6 × 4 = 24
Iteration 5: 24 × 5 = 120
```

Final result = 120.

## 2.5 Dry Run

Input: `5`

| Iteration | i | Previous factorial | New factorial |
|---|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 2 | 1 | 2 |
| 3 | 3 | 2 | 6 |
| 4 | 4 | 6 | 24 |
| 5 | 5 | 24 | 120 |

## 2.6 Complexity Analysis

**Time Complexity: O(n)**

The loop executes n times.

**Auxiliary Space Complexity: O(1)**

Only a fixed number of variables are used.

## 2.7 Edge Cases

| Input | Expected output |
|---:|---:|
| -2 | Invalid |
| 0 | 1 |
| 1 | 1 |
| 2 | 2 |
| 5 | 120 |

---

# 3. Digit Sum of a Number

## 3.1 What is digit sum?

Digit sum means adding all individual digits of a number.

**Example:**

```text
1234 = 1 + 2 + 3 + 4
     = 10
```

More examples:

| Number | Calculation | Digit sum |
|---:|---|---:|
| 123 | 1 + 2 + 3 | 6 |
| 456 | 4 + 5 + 6 | 15 |
| 789 | 7 + 8 + 9 | 24 |
| 1005 | 1 + 0 + 0 + 5 | 6 |
| 999 | 9 + 9 + 9 | 27 |

## 3.2 Important Operators

Two operators are important for digit-based problems.

### Modulo Operator (%)

The modulo operator returns the remainder after division.

Example:

```python
1234 % 10
```

Output:

```text
4
```

It extracts the last digit.

### Floor Division (//)

Floor division divides two numbers and rounds the result down to an integer.

Example:

```python
1234 // 10
```

Output:

```text
123
```

It removes the last digit of a positive integer.

### Difference

| Number | `% 10` | `// 10` |
|---:|---:|---:|
| 1234 | 4 | 123 |
| 123 | 3 | 12 |
| 12 | 2 | 1 |
| 1 | 1 | 0 |

## 3.3 Algorithm

1. Start.
2. Read a number `n`.
3. Initialize `total = 0`.
4. Repeat while n is greater than 0.
5. Extract the last digit using `n % 10`.
6. Add the digit to total.
7. Remove the last digit using `n // 10`.
8. Display total.
9. Stop.

## 3.4 Python Program

```python
n = int(input("Enter a number: "))

total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Digit sum:", total)
```

**Output:**

```text
Enter a number: 1234
Digit sum: 10
```

## 3.5 Understanding the Logic

Initially:

```python
total = 0
```

We use 0 because adding 0 does not change the sum.

Inside the loop:

```python
digit = n % 10
```

Extracts the last digit.

```python
total = total + digit
```

Adds that digit to the total.

```python
n = n // 10
```

Removes the last digit.

The loop continues until n becomes 0.

## 3.6 Dry Run

Input: `1234`

| Iteration | n | digit = n % 10 | total | n = n // 10 |
|---|---:|---:|---:|---:|
| 1 | 1234 | 4 | 4 | 123 |
| 2 | 123 | 3 | 7 | 12 |
| 3 | 12 | 2 | 9 | 1 |
| 4 | 1 | 1 | 10 | 0 |

Final result = 10.

## 3.7 Complexity Analysis

**Time Complexity: O(d)**

Here, d represents the number of digits.

The loop executes once for every digit.

**Auxiliary Space Complexity: O(1)**

Only a fixed number of variables are used.

## 3.8 Edge Cases

| Input | Expected digit sum |
|---:|---:|
| 0 | 0 |
| 5 | 5 |
| 10 | 1 |
| 100 | 1 |
| 999 | 27 |

**Note:** The basic program assumes non-negative input. To support negative numbers, use `abs(n)` before the loop.

---

# 4. Prime Number Check

## 4.1 What is a prime number?

A prime number is a number greater than 1 that has exactly two factors:

1. 1
2. The number itself

Examples:

| Number | Prime? | Factors |
|---:|---|---|
| 2 | Yes | 1, 2 |
| 3 | Yes | 1, 3 |
| 4 | No | 1, 2, 4 |
| 5 | Yes | 1, 5 |
| 6 | No | 1, 2, 3, 6 |
| 7 | Yes | 1, 7 |
| 9 | No | 1, 3, 9 |
| 11 | Yes | 1, 11 |

**Important:**

- 2 is the smallest prime number.
- 2 is the only even prime number.
- 0 and 1 are not prime numbers.
- Negative numbers are not prime numbers.

## 4.2 Understanding the Logic

Suppose the input is 7.

We check whether any number between 2 and 6 divides 7 exactly.

```text
7 % 2 = 1
7 % 3 = 1
7 % 4 = 3
7 % 5 = 2
7 % 6 = 1
```

None gives a remainder of 0.

Therefore, 7 is prime.

Now consider 8:

```text
8 % 2 = 0
```

It is divisible by 2, so 8 is not prime.

## 4.3 Basic Algorithm

1. Start.
2. Read a number `n`.
3. If n is less than or equal to 1, it is not prime.
4. Otherwise, assume it is prime.
5. Check divisibility from 2 to n - 1.
6. If any number divides n exactly, mark it as not prime.
7. Stop checking.
8. Display the result.

## 4.4 Basic Python Program

```python
n = int(input("Enter a number: "))

if n <= 1:
    print("Not a prime number")

else:
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
```

**Output:**

```text
Enter a number: 7
Prime number
```

## 4.5 Understanding is_prime

Initially:

```python
is_prime = True
```

We assume the number is prime.

If a divisor is found:

```python
is_prime = False
```

The number is not prime.

Then:

```python
break
```

Stops the loop because we have already found a divisor.

## 4.6 Dry Run – Input 7

| Iteration | i | 7 % i | Result |
|---|---:|---:|---|
| 1 | 2 | 1 | Continue |
| 2 | 3 | 1 | Continue |
| 3 | 4 | 3 | Continue |
| 4 | 5 | 2 | Continue |
| 5 | 6 | 1 | Continue |

No divisor found.

Output: Prime number.

## 4.7 Dry Run – Input 9

| Iteration | i | 9 % i | Result |
|---|---:|---:|---|
| 1 | 2 | 1 | Continue |
| 2 | 3 | 0 | Not prime; break |

Output: Not a prime number.

---

# 5. Optimized Prime Number Check

## 5.1 Why optimize?

The basic approach checks all possible divisors from 2 to n - 1.

But we don't need to check every number.

We only need to check divisors up to the square root of n.

### Example

Suppose:

```text
n = 36

Square root of 36 = 6
```

If 36 has a divisor greater than 6, its corresponding factor must be smaller than 6.

Therefore, checking up to the square root is sufficient.

## 5.2 Optimized Python Program

```python
n = int(input("Enter a number: "))

if n <= 1:
    print("Not a prime number")

else:
    is_prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
```

## 5.3 Complexity Comparison

| Approach | Time complexity | Auxiliary space |
|---|---|---|
| Basic approach | O(n) | O(1) |
| Optimized approach | O(√n) | O(1) |

The optimized approach performs fewer checks for large numbers.

---

# 6. Time Complexity

## 6.1 What is time complexity?

Time complexity describes how the number of operations in an algorithm grows as the input size increases.

It helps us understand the efficiency of an algorithm.

### Common complexities

| Complexity | Meaning | Example |
|---|---|---|
| O(1) | Constant time | Accessing an array element |
| O(log n) | Logarithmic time | Binary search |
| O(n) | Linear time | Single loop through n elements |
| O(n log n) | Linearithmic time | Merge sort |
| O(n²) | Quadratic time | Two nested loops over n items |

### Examples from Day 3

**Factorial:**

```python
for i in range(1, n + 1):
    factorial *= i
```

The loop executes n times.

Time complexity = O(n).

**Digit sum:**

```python
while n > 0:
    digit = n % 10
    n //= 10
```

The loop executes once per digit.

Time complexity = O(d), where d is the number of digits.

**Prime check:**

Basic approach: O(n).

Optimized approach: O(√n).

---

# 7. Space Complexity

## 7.1 What is space complexity?

Space complexity describes how memory usage grows as the input size increases.

For these three iterative programs, we use a fixed number of variables.

| Problem | Auxiliary space |
|---|---|
| Factorial | O(1) |
| Digit sum | O(1) |
| Prime check | O(1) |

**Auxiliary space** means the extra memory used by the algorithm, excluding the input storage.

---

# 8. Edge Case Testing

Edge cases are special or boundary inputs that may expose errors in a program.

Testing only normal inputs is not enough.

### Factorial

| Input | Expected output |
|---:|---|
| -2 | Invalid |
| 0 | 1 |
| 1 | 1 |
| 5 | 120 |

### Digit Sum

| Input | Expected output |
|---:|---:|
| 0 | 0 |
| 5 | 5 |
| 100 | 1 |
| 999 | 27 |

### Prime Number

| Input | Expected output |
|---:|---|
| -5 | Not prime |
| 0 | Not prime |
| 1 | Not prime |
| 2 | Prime |
| 4 | Not prime |
| 17 | Prime |
| 25 | Not prime |

---

# 9. DSA Interview Questions

**Q1. What is factorial?**

Factorial is the product of all positive integers from 1 up to a given number.

**Q2. Why is 0! equal to 1?**

It is defined mathematically as 1. This also makes factorial formulas consistent.

**Q3. Why do we initialize factorial with 1?**

Because 1 is the multiplicative identity. Multiplying by 1 does not change the result.

**Q4. What is the difference between `%` and `//`?**

`%` returns the remainder, while `//` performs floor division.

**Q5. How do you extract the last digit of a number?**

Using the modulo operator with 10:

```python
digit = n % 10
```

**Q6. How do you remove the last digit?**

Using floor division by 10:

```python
n = n // 10
```

**Q7. What is a prime number?**

A number greater than 1 that has exactly two factors: 1 and itself.

**Q8. Why is 1 not a prime number?**

Because it has only one positive factor.

**Q9. Why do we use break in the prime-checking program?**

Once we find a divisor, we know the number is not prime. There is no need to continue checking.

**Q10. Why does the optimized prime checker stop at the square root?**

Factors greater than the square root have corresponding factors smaller than the square root. Therefore, checking up to the square root is sufficient.

**Q11. What is time complexity?**

It describes how the number of operations grows with input size.

**Q12. What is space complexity?**

It describes how memory usage grows with input size.

---

# 10. Practice Problems

## Beginner Level

1. Find the factorial of 6.
2. Find the factorial of 7.
3. Find the digit sum of 5678.
4. Find the digit sum of 9876.
5. Check whether 13 is prime.
6. Check whether 21 is prime.

## Dry-Run Practice

**Question 1:**

What is the output?

```python
n = 4
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial)
```

**Question 2:**

What is the output?

```python
n = 567
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print(total)
```

**Question 3:**

Is 29 prime? Explain how you checked it.

---

# 11. Day 3 DSA Completion Checklist

- [ ] Understand factorial.
- [ ] Write factorial program independently.
- [ ] Dry-run factorial.
- [ ] Test factorial edge cases.
- [ ] Understand digit sum.
- [ ] Understand `% 10` and `// 10`.
- [ ] Write digit sum program independently.
- [ ] Dry-run digit sum.
- [ ] Test digit sum edge cases.
- [ ] Understand prime numbers.
- [ ] Write basic prime-checking program.
- [ ] Understand optimized prime checking.
- [ ] Compare O(n) and O(√n).
- [ ] Explain time complexity.
- [ ] Explain auxiliary space complexity.
- [ ] Solve at least one problem independently.

## Final Revision Table

| Problem | Approach | Time complexity | Auxiliary space |
|---|---|---|---|
| Factorial | Iterative loop | O(n) | O(1) |
| Digit Sum | While loop with `%` and `//` | O(d) | O(1) |
| Prime Check – Basic | Divisibility loop | O(n) | O(1) |
| Prime Check – Optimized | Check up to square root | O(√n) | O(1) |

**Day 3 DSA Goal:** Solve problems independently, understand the logic, perform dry runs, test edge cases and explain time and space complexity.
