
# Day 5 – DSA Notes

## Topics
1. LeetCode 509 – Fibonacci Number
2. LeetCode 231 – Power of Two

---

# Problem 1: LeetCode 509 – Fibonacci Number

## 1. Problem Statement

The Fibonacci sequence is a sequence where each number is the sum of the previous two numbers.

The sequence starts with 0 and 1.

Example:

```text
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

Mathematical formula:

```text
F(n) = F(n-1) + F(n-2)
```

Base conditions:

```text
F(0) = 0
F(1) = 1
```

Example:

Input:
```text
n = 5
```

Output:
```text
5
```

Explanation:

```text
F(0) = 0
F(1) = 1
F(2) = 0 + 1 = 1
F(3) = 1 + 1 = 2
F(4) = 1 + 2 = 3
F(5) = 2 + 3 = 5
```

## 2. Approach 1 – Recursion

Recursion means a function calls itself.

Python code:

```python
class Solution:
    def fib(self, n):
        if n <= 1:
            return n

        return self.fib(n-1) + self.fib(n-2)
```

Explanation:

- If n is 0 or 1, return n.
- Otherwise, calculate the previous two Fibonacci numbers.
- Add them and return the result.

Complexity:

- Time: O(2^n) approximately
- Space: O(n) due to the recursion stack.

Disadvantage:

The same Fibonacci values are calculated repeatedly, so this approach becomes slow for large n.

## 3. Approach 2 – Recursion with Memoization

Memoization means storing previously calculated results to avoid repeated calculations.

Python code:

```python
class Solution:
    def fib(self, n):
        memo = {}

        def solve(num):
            if num <= 1:
                return num

            if num in memo:
                return memo[num]

            memo[num] = solve(num-1) + solve(num-2)

            return memo[num]

        return solve(n)
```

Complexity:

- Time: O(n)
- Space: O(n)

Advantage:

Previously calculated values are reused.

## 4. Approach 3 – Dynamic Programming (Array)

Dynamic programming stores previously calculated Fibonacci numbers in an array.

Python code:

```python
class Solution:
    def fib(self, n):
        if n <= 1:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
```

Explanation:

- Create an array of size n + 1.
- Store the first Fibonacci number as 0.
- Store the second Fibonacci number as 1.
- Calculate the remaining numbers using previous values.
- Return dp[n].

Complexity:

- Time: O(n)
- Space: O(n)

## 5. Approach 4 – Iterative (Optimal Space)

This approach uses only two variables instead of an array.

Python code:

```python
class Solution:
    def fib(self, n):
        a = 0
        b = 1

        for i in range(n):
            a, b = b, a + b

        return a
```

### Explanation

Initially:

```python
a = 0
b = 1
```

- a stores the current Fibonacci number.
- b stores the next Fibonacci number.

Important statement:

```python
a, b = b, a + b
```

This updates both variables.

New a = old b

New b = old a + old b

Python calculates both right-hand values before updating the variables.

Example:

Initially:

```python
a = 2
b = 3
```

After:

```python
a, b = b, a + b
```

New values:

```python
a = 3
b = 5
```

### Dry Run

Input:

```python
n = 5
```

| Step | a | b |
|---|---:|---:|
| Initial | 0 | 1 |
| 1 | 1 | 1 |
| 2 | 1 | 2 |
| 3 | 2 | 3 |
| 4 | 3 | 5 |
| 5 | 5 | 8 |

Output:

```text
5
```

Complexity:

- Time: O(n)
- Space: O(1)

### Fibonacci Approach Comparison

| Approach | Time | Space |
|---|---|---|
| Recursion | O(2^n) approximately | O(n) |
| Memoization | O(n) | O(n) |
| DP Array | O(n) | O(n) |
| Iterative | O(n) | O(1) |

Best choice: Iterative approach because it uses constant extra space and calculates each Fibonacci number only once.

---

# Problem 2: LeetCode 231 – Power of Two

## 1. Problem Statement

Given an integer n, return True if n is a power of two. Otherwise, return False.

A power of two can be written as:

```text
2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
```

Examples:

| Input | Output |
|---:|---|
| 1 | True |
| 2 | True |
| 4 | True |
| 8 | True |
| 16 | True |
| 6 | False |
| 10 | False |
| 0 | False |

## 2. Approach 1 – Using a While Loop

Python code:

```python
class Solution:
    def isPowerOfTwo(self, n):
        if n < 1:
            return False

        while n % 2 == 0:
            n = n // 2

        return n == 1
```

### Explanation

First condition:

```python
if n < 1:
    return False
```

Zero and negative numbers are not powers of two.

While condition:

```python
while n % 2 == 0:
```

- `%` is the modulus operator.
- It returns the remainder after division.
- If the remainder is zero, the number is divisible by 2.

Example:

```python
8 % 2 = 0
7 % 2 = 1
```

Update:

```python
n = n // 2
```

- `//` is floor division.
- It divides the number and keeps the whole-number result.

Example:

```python
8 // 2 = 4
```

### Dry Run – n = 16

| Step | Condition | Updated n |
|---|---|---:|
| Initial | n = 16 | 16 |
| 1 | 16 % 2 == 0 | 8 |
| 2 | 8 % 2 == 0 | 4 |
| 3 | 4 % 2 == 0 | 2 |
| 4 | 2 % 2 == 0 | 1 |
| 5 | 1 % 2 != 0 | Stop |

Finally:

```python
return n == 1
```

Since n is 1:

```python
return True
```

### Example – n = 12

```text
12 // 2 = 6
6 // 2 = 3
```

Now:

```python
3 % 2 != 0
```

The loop stops.

```python
return 3 == 1
```

Output:

```text
False
```

Complexity:

- Time: O(log n)
- Space: O(1)

---

## 3. Approach 2 – Bitwise AND (Optimal)

Python code:

```python
class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0
```

### Understand Binary Numbers

Computers represent numbers using binary digits:

- 0
- 1

Examples:

| Decimal | Binary |
|---:|---|
| 1 | 0001 |
| 2 | 0010 |
| 4 | 0100 |
| 8 | 1000 |
| 16 | 10000 |
| 6 | 0110 |
| 12 | 1100 |

Important observation:

Every positive power of two has exactly one set bit (1) in its binary representation.

### Understand the & Operator

The `&` symbol is called Bitwise AND.

Rules:

| First bit | Second bit | Result |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

AND returns 1 only when both bits are 1.

### Example 1 – n = 8

Step 1: Convert 8 to binary.

```text
8 = 1000
```

Step 2: Subtract 1.

```text
8 - 1 = 7

7 = 0111
```

Step 3: Perform Bitwise AND.

```text
    1000
    0111
    ----
    0000
```

Result:

```python
8 & 7 == 0
```

True. Therefore, 8 is a power of two.

### Example 2 – n = 6

Step 1:

```text
6 = 0110
```

Step 2:

```text
6 - 1 = 5

5 = 0101
```

Step 3:

```text
    0110
    0101
    ----
    0100
```

Result:

```python
6 & 5 = 4
```

Since the result is not zero, 6 is not a power of two.

### Why does this work?

A positive power of two has exactly one set bit.

When we subtract 1:

- The only set bit becomes 0.
- All bits to its right become 1.

Therefore, performing AND between n and n - 1 gives zero.

### Understand the Complete Code

```python
return n > 0 and (n & (n - 1)) == 0
```

| Expression | Meaning |
|---|---|
| `n > 0` | Checks that n is positive |
| `n - 1` | Subtracts 1 from n |
| `n & (n - 1)` | Performs bitwise AND |
| `== 0` | Checks whether the result is zero |
| `and` | Both conditions must be True |

Why do we need `n > 0`?

Because when n = 0:

```python
0 & (0 - 1) == 0
```

The bitwise condition alone would be True, but zero is not a power of two.

Complexity:

- Time: O(1) under the usual fixed-width integer model.
- Space: O(1) auxiliary space.

### Power of Two Approach Comparison

| Approach | Time | Space |
|---|---|---|
| While loop | O(log n) | O(1) |
| Bitwise AND | O(1) | O(1) |

Best choice: Bitwise AND for the standard LeetCode complexity model.

---

# Important Python Concepts Learned

## 1. Function Definition

```python
def fib(self, n):
```

- `def` creates a function.
- `fib` is the function name.
- `self` refers to the current object.
- `n` is the input parameter.

## 2. Return Statement

```python
return n
```

Returns a value from a function.

## 3. For Loop

```python
for i in range(n):
    print(i)
```

Repeats code n times.

## 4. While Loop

```python
while n > 0:
    n = n - 1
```

Repeats while the condition is True.

## 5. Modulus Operator

```python
10 % 2 = 0
```

Returns the remainder.

## 6. Floor Division

```python
10 // 2 = 5
```

Returns the whole-number quotient.

## 7. Bitwise AND

```python
8 & 7
```

Compares binary bits and returns 0.

## 8. Multiple Variable Assignment

```python
a, b = b, a + b
```

Updates two variables simultaneously.

---

# Final Complexity Comparison

| Problem | Best approach | Time | Space |
|---|---|---|---|
| Fibonacci Number | Iterative | O(n) | O(1) |
| Power of Two | Bitwise AND | O(1)* | O(1) |

*O(1) for the usual fixed-width integer model used in algorithm analysis.*

---

# Practice Checklist

- [ ] Understand Fibonacci sequence.
- [ ] Understand recursion.
- [ ] Understand memoization.
- [ ] Understand dynamic programming.
- [ ] Understand iterative Fibonacci.
- [ ] Understand `%` and `//`.
- [ ] Understand while loops.
- [ ] Understand binary numbers.
- [ ] Understand bitwise AND.
- [ ] Solve LeetCode 509.
- [ ] Solve LeetCode 231.
- [ ] Explain time and space complexity.

# Interview Questions

1. What is the Fibonacci sequence?
2. What is recursion?
3. What is memoization?
4. What is dynamic programming?
5. Why is iterative Fibonacci better than normal recursion?
6. What is the difference between `%` and `//`?
7. What is a power of two?
8. What is binary representation?
9. What does the bitwise AND operator do?
10. Why does `n & (n - 1)` become zero for powers of two?
11. What is the time complexity of Fibonacci's iterative approach?
12. What is the space complexity of the Power of Two bitwise approach?
