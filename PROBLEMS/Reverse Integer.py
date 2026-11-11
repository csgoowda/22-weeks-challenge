
class Solution(object):
    def reverse(self, x):

        # Step 1: Check if number is negative
        if x < 0:

            # Step 2: Convert number to string
            # abs() removes the negative sign
            # [::-1] reverses the string
            r = -int(str(abs(x))[::-1])

        else:
            # Step 3: Convert and reverse positive number
            r = int(str(x)[::-1])

        # Step 4: Check 32-bit integer range
        if r < -(2**31) or r > (2**31 - 1):
            return 0

        # Step 5: Return reversed number
        return r
