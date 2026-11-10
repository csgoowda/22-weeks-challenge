#A palindrome reads the same forward and backward.
#Examples: madam, level, 121.

word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


#leetcode

class Solution(object):
    def isPalindrome(self, x):
        
        return str(x) == str(x)[::-1]
