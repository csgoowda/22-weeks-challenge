'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input:
s = "anagram"
t = "nagaram"


Output: true

Example 2:

Input:
s = "rat"
t = "car"


Output: false
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
    
        sorted_t = "".join(sorted(t))
        sorted_s = "".join(sorted(s))

        
        if sorted_s != sorted_t :
            return False
        
        return True
        
