
# LeetCode 509 – Fibonacci Number

## 1. Problem Statement

The Fibonacci sequence is a sequence where each number is the sum of the previous two numbers.

Sequence:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34

Formula:

F(n) = F(n-1) + F(n-2)

Base conditions:

- F(0) = 0
- F(1) = 1

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

F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5

---

## 2. Approach 1 – Recursion

Recursion means a function calls itself.

```python
class Solution:
    def fib(self, n):
        if n <= 1:
            return n

        return self.fib(n-1) + self.fib(n-2)
```

Complexity:
- Time: O(2^n) approximately
- Space: O(n)

Disadvantage: Repeated calculations make this approach slow.

---

## 3. Approach 2 – Memoization

Memoization stores previously calculated results.

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

---

## 4. Approach 3 – Dynamic Programming

Store Fibonacci values in an array.

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

Complexity:
- Time: O(n)
- Space: O(n)

---

## 5. Approach 4 – Iterative (Best Space Complexity)

Use only two variables.

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

Meaning:

- New a = old b
- New b = old a + old b

Python calculates both right-side values before updating the variables.

Example:

```python
a = 2
b = 3

a, b = b, a + b
```

New values:

```python
a = 3
b = 5
```

### Dry Run

Input: n = 5

| Step | a | b |
|---|---:|---:|
| Initial | 0 | 1 |
| 1 | 1 | 1 |
| 2 | 1 | 2 |
| 3 | 2 | 3 |
| 4 | 3 | 5 |
| 5 | 5 | 8 |

Output: 5

Complexity:
- Time: O(n)
- Space: O(1)

---

## 6. Approach Comparison

| Approach | Time | Space |
|---|---|---|
| Recursion | O(2^n) approximately | O(n) |
| Memoization | O(n) | O(n) |
| Dynamic Programming | O(n) | O(n) |
| Iterative | O(n) | O(1) |

Best choice: Iterative approach.

Reason: It calculates each Fibonacci number once and uses constant extra space.

---

## 7. Python Concepts Learned

1. Function definition – def
2. Recursion
3. For loop
4. Range()
5. Multiple variable assignment
6. Return statement
7. Time complexity
8. Space complexity

---

## 8. Interview Questions

1. What is the Fibonacci sequence?
2. What is recursion?
3. What is memoization?
4. What is dynamic programming?
5. Why is iterative Fibonacci better than normal recursion?
6. What does a, b = b, a + b mean?
7. What is the time complexity of iterative Fibonacci?
8. What is its space complexity?

---

## 9. Practice Checklist

- [ ] Understand Fibonacci sequence.
- [ ] Understand recursion.
- [ ] Understand memoization.
- [ ] Understand dynamic programming.
- [ ] Understand iterative approach.
- [ ] Write the optimal solution without notes.
- [ ] Dry-run n = 5.
- [ ] Explain O(n) time and O(1) space.
- [ ] Submit LeetCode 509.
