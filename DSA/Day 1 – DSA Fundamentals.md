Great! We have finished the Day 1 Python learning notes. Now let's continue with the next subject in your roadmap.

# Day 1 – DSA Fundamentals

35 minutes

Beginner level

Today's DSA topics:

1. What is an algorithm?
2. Input, Process, Output.
3. Time complexity.
4. Big-O notation: O(1), O(n), O(n²).
5. Dry-run a simple counting and summing algorithm.

## 1. What is DSA?

DSA stands for:

- Data Structures: Ways of organizing and storing data.
- Algorithms: Step-by-step instructions to solve a problem.

Example: Suppose a manufacturing company wants to calculate its total daily production.

You have production values:

```
production = [100, 150, 200, 120]
```

You need to calculate the total production.

An algorithm is the sequence of steps used to solve this problem.

## 2. What is an algorithm?

An algorithm is a finite sequence of well-defined steps used to solve a particular problem.

Example: Algorithm to add two numbers.

Start

Input A and B

Calculate A + B

Display result

Stop

### Algorithm in simple English

1. Start.
2. Read two numbers.
3. Add the numbers.
4. Display the result.
5. Stop.

### Python implementation

```
a = int(input("Enter first number: "))b = int(input("Enter second number: "))result = a + bprint("Sum:", result)
```

Important: The algorithm explains the steps. Python code implements those steps.

## 3. Input, Process and Output (IPO)

Every basic programming problem can be understood using three parts.

| Part    | Meaning             | Example   |
| ------- | ------------------- | --------- |
| Input   | Data received       | 10 and 20 |
| Process | Operation performed | 10 + 20   |
| Output  | Final result        | 30        |

Manufacturing example:

- Input: Number of products manufactured each day.
- Process: Calculate total production.
- Output: Total products manufactured.

## 4. What is time complexity?

Time complexity describes how an algorithm's running work grows as the input size increases.

It helps us understand whether an algorithm is efficient for small and large inputs.

For example:

- 10 production records.
- 100 production records.
- 10,000 production records.

We want to understand how the amount of work changes as the number of records increases.

We commonly express this using Big-O notation.

## 5. Three important Big-O complexities

### A. O(1) – Constant time

The amount of work stays approximately constant regardless of input size.

```
numbers = [10, 20, 30, 40, 50]print(numbers[0])
```

This accesses the first element directly.

Whether the list contains 5 or 5,000 elements, this particular access takes constant-time work.

[Big O: Analysis of Algorithm Efficiency | common_curriculum](https://images.openai.com/static-rsc-4/UG7ArTJLvEFgnvQ5XO_EbUYkUw3LDehzpalutMoCWVcIRQQVfyHQYpZNBhwx7bMyy9uQ5qdKxDRnt9zpNOVAmMMdAIg05bqE44_touu-97zOa208WEA8Tmw9wHyEwhqNDE9n1CIN90K3ayczW9cl03XLPQ81llMX7MrJ_nHc4g0?purpose=inline)

### B. O(n) – Linear time

The work increases in proportion to the number of elements.

```
numbers = [10, 20, 30, 40, 50]for number in numbers:    print(number)
```

If there are 5 elements, the loop runs 5 times.

If there are 100 elements, the loop runs 100 times.

Here, `n` represents the number of elements.

[Big O: Analysis of Algorithm Efficiency | common_curriculum](https://images.openai.com/static-rsc-4/-SMehVyMuIf6IJmWgdr3i0hUrSgwVqJ1GS_8NqnJtI9QZVkHDVIafu1uB5M0rQS9Sr0EwPEPZFxJ62yEcEYrg8mjC8xPBLks5c_hYZBxhMy3hyCxqIhZJlljmiQbUFB9HmlGpkiCSAbr-UmLtUADoXNE8e291fwAMBAHv-kv-Yo?purpose=inline)

### C. O(n²) – Quadratic time

The work grows approximately with the square of the input size.

```
numbers = [10, 20, 30]for i in numbers:    for j in numbers:        print(i, j)
```

For 3 elements:

- Outer loop: 3 times.
- Inner loop: 3 times for each outer iteration.
- Total: 3 × 3 = 9 iterations.

For 100 elements:

\- Total: 100 × 100 = 10,000 iterations.

[I Failed a Technical Interview and Finally Understood Why Data Structures and Algorithms Matter | by Emmanuel Nyaayo | Apr, 2026 | Medium](https://images.openai.com/static-rsc-4/ZDabhqCyqlRehbQKpv6dzgeIJPea-wNNZghcnOGQpXP7yyz8QyO3-bREtAiczosMOWY2loELFn2RI-UTdgvM5nnx7wW-dWVcZ8pvBT81D7hxeuOUKP9xSu8DqNTdAneBYkk6WKfa9s8qyymZIJhk2tIFNccJ7QqbZMvXD9_U8MM?purpose=inline)

### Comparison

| Complexity | Example for n = 10 | General meaning |
| ---------- | ------------------ | --------------- |
| O(1)       | 1                  | Constant work   |
| O(n)       | 10                 | Linear work     |
| O(n²)      | 100                | Quadratic work  |

Remember: These are simplified growth patterns, not exact execution-time measurements.

## 6. Dry run: Calculate total production

A dry run means manually tracing an algorithm step by step without executing it.

Consider:

```
production = [100, 150, 200, 120]total = 0for quantity in production:    total = total + quantityprint(total)
```

Let's trace it:

| Iteration | Quantity | Previous total | New total |
| --------- | -------- | -------------- | --------- |
| 1         | 100      | 0              | 100       |
| 2         | 150      | 100            | 250       |
| 3         | 200      | 250            | 450       |
| 4         | 120      | 450            | 570       |

Final output: 570

The loop processes each element once, so the time complexity is O(n).

## 7. Your understanding test

Answer these questions. I'll evaluate each answer and explain mistakes.

DSA Day 1 quiz

Q1. What is an algorithm?

A. A programming language

B. Step-by-step instructions to solve a problem

C. A database

D. A computer



Q2. In IPO, what does P represent?

A. Program

B. Problem

C. Process

D. Python



Q3. Which complexity represents constant time?

A. O(n)

B. O(n²)

C. O(1)

D. O(n+1)



Q4. A loop runs once for every element in a list of n elements. What is its complexity?

A. O(1)

B. O(n)

C. O(n²)

D. O(2ⁿ)



Q5. Two nested loops each run n times. What is the complexity?

A. O(1)

B. O(n)

C. O(n²)

D. O(log n)



0/5 answered

Submit answers

After this quiz: We'll do one DSA dry-run exercise, then move to Day 1 OOP fundamentals. We still need to complete aptitude, English and the final checklist before Day 1 is officially finished.
