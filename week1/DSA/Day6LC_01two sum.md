Day 6 – DSA: Two Sum (LeetCode 1)

1. Problem Statement

Given an array of integers "nums" and an integer "target", return the indices of the two numbers whose sum is equal to the target.

Important conditions:

- You must return indices, not the actual numbers.
- You cannot use the same element twice.
- Exactly one valid answer is guaranteed.

Example 1

nums = [2, 7, 11, 15]
target = 9

Output:

[0, 1]

Explanation: "nums[0] + nums[1] = 2 + 7 = 9".

Example 2

nums = [3, 2, 4]
target = 6

Output:

[1, 2]

Explanation: "nums[1] + nums[2] = 2 + 4 = 6".

---

2. Approach 1 – Brute Force

Check every possible pair of numbers using two loops.

Code

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

Explanation

1. The first loop selects one number.
2. The second loop checks the numbers after it.
3. Add both numbers.
4. If their sum equals the target, return their indices.

Dry Run

nums = [2, 7, 11, 15]
target = 9

i| j| Calculation| Result
0| 1| 2 + 7 = 9| Match

Output:

[0, 1]

Complexity

- Time Complexity: O(n²) – two nested loops.
- Space Complexity: O(1) – no extra data structure is used.

---

3. Approach 2 – Optimal Solution Using Dictionary

Instead of checking every pair, use a dictionary to remember numbers and their indices.

Main Idea

For every number:

1. Calculate the missing number (complement).
2. Check whether that complement is already in the dictionary.
3. If found, return both indices.
4. Otherwise, store the current number and its index.

Formula:

complement = target - num

Code

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

Explanation of Each Line

1. Create an empty dictionary

seen = {}

It stores each number and its index.

Example:

{2: 0, 7: 1}

Here, "2" is at index "0", and "7" is at index "1".

2. Get index and value

for i, num in enumerate(nums):

"enumerate()" gives two values:

- "i" = index
- "num" = actual number

3. Find the complement

complement = target - num

Example:

target = 9
num = 7

complement = 9 - 7
complement = 2

We need the number "2" to make the target "9".

4. Check the dictionary

if complement in seen:

If the required number is already stored, we found the answer.

5. Return the indices

return [seen[complement], i]

"seen[complement]" gives the earlier number's index. "i" gives the current number's index.

6. Store the current number

seen[num] = i

If the complement is not found, save the current number for future checks.

---

4. Dry Run – Optimal Solution

Input:

nums = [2, 7, 11, 15]
target = 9

Step| Index| Number| Complement| Dictionary| Action
1| 0| 2| 7| "{2: 0}"| Store 2
2| 1| 7| 2| "{2: 0}"| Found 2

At step 2:

complement = 9 - 7
complement = 2

The number "2" is already in the dictionary.

Therefore:

return [0, 1]

Output:

[0, 1]

---

5. Important Edge Cases

Case 1 – Duplicate Numbers

nums = [3, 3]
target = 6

Output:

[0, 1]

Both values are "3", but their indices are different.

Case 2 – Negative Numbers

nums = [-3, 4, 3, 90]
target = 0

Output:

[0, 2]

Because "-3 + 3 = 0".

Case 3 – Numbers in Different Positions

nums = [3, 2, 4]
target = 6

Output:

[1, 2]

---

6. Time and Space Complexity Comparison

Approach| Time Complexity| Space Complexity
Brute Force| O(n²)| O(1)
Dictionary| O(n) average| O(n)

Why is the dictionary approach faster?

- Brute force checks multiple pairs.
- Dictionary lookup takes O(1) average time.
- We only need to traverse the array once.

The optimal dictionary approach is preferred.

---

7. Important Python Concepts Used

Dictionary

A dictionary stores data as key-value pairs.

student = {
    "name": "Chethan",
    "age": 22
}

enumerate()

Returns the index and value while looping.

nums = [2, 7, 11]

for i, num in enumerate(nums):
    print(i, num)

Output:

0 2
1 7
2 11

Dictionary Lookup

seen = {2: 0, 7: 1}

print(2 in seen)  # True
print(seen[2])    # 0

---

8. Interview Questions

Q1. What is the Two Sum problem?

Find two different elements whose sum equals the target and return their indices.

Q2. Why do we use a dictionary?

To store numbers and their indices so we can quickly check whether the required complement exists.

Q3. What is a complement?

The missing number required to reach the target.

complement = target - num

Q4. What is the time complexity of the optimal solution?

O(n) average time because we traverse the array once and use average O(1) dictionary lookups.

Q5. Why do we check before storing the current number?

To ensure that we use two different array elements, not the same element twice.

---

9. Practice Tasks

- [ ] Solve Two Sum using brute force.
- [ ] Solve Two Sum using a dictionary.
- [ ] Dry-run "[2, 7, 11, 15]", target "9".
- [ ] Test duplicate values "[3, 3]", target "6".
- [ ] Test negative numbers.
- [ ] Explain the dictionary approach without looking at notes.
- [ ] Record time and space complexity.
- [ ] Submit the solution on LeetCode.

10. Final Revision

Remember these four steps:

1. Create an empty dictionary.
2. Calculate "target - num".
3. Check whether the complement exists.
4. If not found, store "seen[num] = i".

Key takeaway: Use a dictionary to reduce the Two Sum solution from O(n²) to O(n) average time.
