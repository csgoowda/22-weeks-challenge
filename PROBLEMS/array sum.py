
# Array Sum using for loop

class Solution(object):
    def arraySum(self, nums):

        # Step 1: Initialize total
        total = 0

        # Step 2: Loop through array
        for num in nums:

            # Step 3: Add each number
            total += num

        # Step 4: Return total
        return total


# Example
nums = [1, 2, 3, 4]

obj = Solution()
print(obj.arraySum(nums))  # Output: 10




# Array Sum using sum()

class Solution(object):
    def arraySum(self, nums):

        # sum() adds all elements
        return sum(nums)


# Example
nums = [1, 2, 3, 4]

obj = Solution()
print(obj.arraySum(nums))  # Output: 10
