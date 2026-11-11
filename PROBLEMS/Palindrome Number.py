
class Solution(object):
    def isPalindrome(self, x):

        # Step 1: Convert integer into string
        n = str(x)

        # Step 2: Reverse the string
        r = n[::-1]

        # Step 3: Compare original and reversed values
        if n == r:
            return True
        else:
            return False
