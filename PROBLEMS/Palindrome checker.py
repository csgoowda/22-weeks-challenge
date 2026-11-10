#A palindrome reads the same forward and backward.
#Examples: madam, level, 121.

word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
