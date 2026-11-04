# Day 2 – DSA Complete Notes



Revision notes

Week 1



These notes cover the DSA topics from Day 2 of your 22-week roadmap. Read them and practise the examples before moving to Operating Systems.

## 1. What is DSA?

DSA stands for:

- Data Structures: Ways to organize and store data.
- Algorithms: Step-by-step instructions to solve a problem.

Example: To calculate the sum of numbers from 1 to 5, we use an algorithm that adds each number.

## 2. Loops in Python

A loop executes a block of code repeatedly.

Python has two main loops:

### 2.1 `for` loop

Used when you want to iterate over a sequence or a known range of values.

```
for i in range(1, 6):    print(i)
```

Output:

```
1
2
3
4
5
```

Here:

- `for` starts the loop.
- `i` is the loop variable.
- `range(1, 6)` generates numbers from 1 to 5.
- `print(i)` displays each number.

### 2.2 `while` loop

Used when you want to repeat something while a condition is true.

```
i = 1while i <= 5:    print(i)    i += 1
```

Output:

```
1
2
3
4
5
```

Explanation:

1. Start with `i = 1`.
2. Check whether `i <= 5`.
3. Print the value.
4. Increase `i` by 1.
5. Repeat until the condition becomes false.



Important

&#x20;Always make sure your `while` loop can eventually stop. Otherwise, you may create an infinite loop.



## 3. Understanding `range()`

The `range()` function generates a sequence of numbers.

Syntax:

```
range(start, stop, step)
```

| Parameter | Meaning                    |
| --------- | -------------------------- |
| `start`   | Starting number (included) |
| `stop`    | Ending boundary (excluded) |
| `step`    | Difference between numbers |

Examples:

```
range(1, 6)# 1, 2, 3, 4, 5range(2, 11, 2)# 2, 4, 6, 8, 10range(5, 0, -1)# 5, 4, 3, 2, 1
```

Remember: The stop value is never included.

## 4. `break` and `continue`

### 4.1 `break`

Stops the entire loop immediately.

```
for i in range(1, 6):    if i == 3:        break    print(i)
```

Output:

```
1
2
```

When `i` becomes 3, the loop stops.

### 4.2 `continue`

Skips the current iteration and moves to the next iteration.

```
for i in range(1, 6):    if i == 3:        continue    print(i)
```

Output:

```
1
2
4
5
```

Difference:

| `break`               | `continue`                       |
| --------------------- | -------------------------------- |
| Stops the entire loop | Skips only the current iteration |
| No further iterations | Next iteration continues         |

## 5. Dry Run – Very Important

A dry run means manually executing a program step by step to understand how its variables change.

Example:

```
total = 0for i in range(1, 4):    total = total + iprint(total)
```

Dry-run table:

| Iteration | `i` | `total` before | `total` after |
| --------- | --- | -------------- | ------------- |
| 1         | 1   | 0              | 1             |
| 2         | 2   | 1              | 3             |
| 3         | 3   | 3              | 6             |

Output:

```
6
```

Why is the initial value `total = 0`?

Because we need a variable to store the running sum. Zero is the starting value because adding zero does not change the result.

## 6. Problem 1 – Sum of numbers from 1 to n

Problem: Calculate the sum of all numbers from 1 to `n`.

Example:

```
Input: 5
Output: 15
```

Program:

```
n = 5total = 0for i in range(1, n + 1):    total = total + iprint(total)
```

How does it work?

- First iteration: `0 + 1 = 1`
- Second iteration: `1 + 2 = 3`
- Third iteration: `3 + 3 = 6`
- Fourth iteration: `6 + 4 = 10`
- Fifth iteration: `10 + 5 = 15`

Important: We use `n + 1` because the stop value in `range()` is excluded.

### Alternative: Mathematical formula

\\[ Sum = \frac{n(n+1)}{2} \\]

For \\(n=5\\):

\\[ Sum = \frac{5(5+1)}{2} =\frac{30}{2}=15 \\]

Python:

```
n = 5total = n * (n + 1) // 2print(total)
```

Both approaches produce 15.

## 7. Problem 2 – Multiplication table

Problem: Print the multiplication table of a given number.

Example: Number = 5

```
n = 5for i in range(1, 11):    print(n, "x", i, "=", n * i)
```

Output:

```
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

The loop runs 10 times, and each time it multiplies `n` by `i`.

## 8. Edge cases

An edge case is an unusual or boundary input that we should test to check whether our program works correctly.

For the sum program:

| Input | Expected output                                  |
| ----- | ------------------------------------------------ |
| 1     | 1                                                |
| 5     | 15                                               |
| 0     | 0, if zero is allowed                            |
| -3    | Reject, if the program expects positive integers |

For the multiplication table:

- Number = 0
- Number = 1
- Number = -5

Testing edge cases helps identify errors that ordinary inputs might not reveal.

## 9. Time complexity

Time complexity describes how the number of operations grows as the input size increases.

### O(1) – Constant time

The number of operations does not depend on input size.

```
a = 10b = 20print(a + b)
```

Whether the input size is 10 or 10,000, this operation takes a constant number of steps.

### O(n) – Linear time

The number of operations grows approximately in proportion to `n`.

```
for i in range(n):    print(i)
```

If `n = 5`, the loop runs 5 times.

If `n = 100`, the loop runs 100 times.

[Time Complexity and Big O Notation](https://images.openai.com/static-rsc-4/75TcyDeAFb7rZCbVxP-YQWSLJxpuElPATgexL1DR2aNfspLEEwW78pEuLJgOU_ka6pla9iHXF9mRk4RShmFQCSz4TakYw6hsNgtvvzTab9L75xPcFpEycjMWyv4QAl9ssM6UQDcsZullMD4_3WEYVR5aszU1-SdeJ1K3kHrQZlc?purpose=inline)

[linkedin.com](https://www.linkedin.com/pulse/time-complexity-big-o-notation-kavitha-vikas?utm_source=chatgpt.com)

| Complexity | Meaning   | Example                          |
| ---------- | --------- | -------------------------------- |
| O(1)       | Constant  | Access an array element by index |
| O(n)       | Linear    | One loop through n elements      |
| O(n²)      | Quadratic | Nested loops over n elements     |

For Day 2, focus mainly on O(1) and O(n).

## 10. Space complexity

Space complexity describes how much additional memory an algorithm uses as the input size increases.

Example:

```
total = 0for i in range(1, 6):    total += i
```

The program uses only a few variables: `total` and `i`.

The extra memory stays constant, so its auxiliary space complexity is:

\\[ O(1) \\]

### Day 2 DSA quick revision

| Topic      | Remember                             |
| ---------- | ------------------------------------ |
| `for`      | Iterates over a sequence or range    |
| `while`    | Repeats while a condition is true    |
| `range()`  | Generates a sequence                 |
| `break`    | Stops the loop                       |
| `continue` | Skips current iteration              |
| Dry run    | Executes code manually, step by step |
| Sum 1 to n | `n * (n + 1) // 2`                   |
| O(1)       | Constant time                        |
| O(n)       | Linear time                          |
| Space O(1) | Constant additional memory           |

## Your Day 2 DSA practical checklist

Practice progress

# 0/9

Write a for loop to print 1 to 10.

Write a while loop to print 1 to 10.

Print even numbers from 1 to 20 using range().

Use break to stop a loop when i becomes 5.

Use continue to skip number 3.

Write a program to calculate the sum from 1 to n.

Write a multiplication table program.

Dry-run the sum program manually.

Explain O(1), O(n), and auxiliary space O(1).

Finish DSA practice

One important point: Your revision quiz score is 5/5, which is excellent. But a quiz score and coding practice are different. Make sure you can write both programs yourself without copying.

After your notes and practice, we can continue with Day 2 Operating Systems.
