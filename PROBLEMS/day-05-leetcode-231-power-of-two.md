
# LeetCode 231 – Power of Two

## 1. Problem Statement

Given an integer n, return True if n is a power of two. Otherwise, return False.

Powers of two:

2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32

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

---

## 2. Approach 1 – While Loop

This is the beginner-friendly approach.

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

- % is the modulus operator.
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

- // is floor division.
- It returns the whole-number quotient.

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

Output: True

### Example – n = 12

```text
12 // 2 = 6
6 // 2 = 3
```

Now 3 is not divisible by 2.

```python
return 3 == 1
```

Output: False

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

Computers represent numbers using binary digits 0 and 1.

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

The & symbol is called Bitwise AND.

Rules:

| First bit | Second bit | Result |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

AND returns 1 only when both bits are 1.

### Example 1 – n = 8

Step 1:

```text
8 = 1000
```

Step 2:

```text
8 - 1 = 7

7 = 0111
```

Step 3: Perform AND.

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

### Why Does This Work?

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
| n > 0 | Checks that n is positive |
| n - 1 | Subtracts 1 |
| n & (n - 1) | Performs bitwise AND |
| == 0 | Checks whether result is zero |
| and | Both conditions must be True |

Why do we need n > 0?

When n = 0:

```python
0 & (0 - 1) == 0
```

The bitwise condition alone is True, but zero is not a power of two.

Complexity:
- Time: O(1) under the usual fixed-width integer model.
- Space: O(1) auxiliary space.

---

## 4. Approach Comparison

| Approach | Time | Space |
|---|---|---|
| While loop | O(log n) | O(1) |
| Bitwise AND | O(1)* | O(1) |

Best choice: Bitwise AND for the standard LeetCode complexity model.

---

## 5. Python Concepts Learned

1. Function definition – def
2. If condition
3. While loop
4. Modulus operator (%)
5. Floor division (//)
6. Binary numbers
7. Bitwise AND (&)
8. Boolean operators (and)
9. Return statement
10. Time complexity
11. Space complexity

---

## 6. Interview Questions

1. What is a power of two?
2. What is binary representation?
3. What is the bitwise AND operator?
4. What is the difference between % and //?
5. Why do powers of two have only one set bit?
6. Why does n & (n - 1) become zero for powers of two?
7. Why do we check n > 0?
8. What is the time complexity of the while-loop solution?
9. What is the time complexity of the bitwise solution?
10. What is its space complexity?

---

## 7. Practice Checklist

- [ ] Understand powers of two.
- [ ] Understand the while-loop solution.
- [ ] Understand % and //.
- [ ] Understand binary numbers.
- [ ] Understand bitwise AND.
- [ ] Understand n & (n - 1).
- [ ] Dry-run n = 8.
- [ ] Dry-run n = 6.
- [ ] Write the optimal solution without notes.
- [ ] Explain O(1) time and O(1) space.
- [ ] Submit LeetCode 231.

---

## Final Revision

| Problem | Best Approach | Time | Space |
|---|---|---|---|
| Fibonacci Number | Iterative | O(n) | O(1) |
| Power of Two | Bitwise AND | O(1)* | O(1) |

*For the usual fixed-width integer model.*
