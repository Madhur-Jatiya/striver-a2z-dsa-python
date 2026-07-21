# ============================================
# Python String Methods Reference
# ============================================
#
# A string is:
# - Ordered
# - Immutable (cannot be changed directly)
# - Allows duplicate characters
# - Supports indexing
# - Supports slicing
# - Can contain letters, numbers, spaces, and special characters
#
# Example:
s = "Hello Python"

print("Original string:", s)


# ============================================
# IMPORTANT: STRING INDEXING
# ============================================
#
# String indexes start from 0
#
# H    e    l    l    o
# 0    1    2    3    4
#
# Negative indexes:
#
# H    e    l    l    o
# -5  -4   -3   -2   -1
#

print("\nFirst character:")
print(s[0])
# Output: H

print("\nLast character:")
print(s[-1])
# Output: n


# ============================================
# 1. lower()
# ============================================
# Converts all characters to lowercase
# Does NOT modify original string
# Returns a NEW string

result = s.lower()

print("\nAfter lower():")
print(result)
# Output: hello python

print("Original string:")
print(s)
# Output: Hello Python


# ============================================
# 2. upper()
# ============================================
# Converts all characters to uppercase
# Does NOT modify original string
# Returns a NEW string

result = s.upper()

print("\nAfter upper():")
print(result)
# Output: HELLO PYTHON


# ============================================
# 3. capitalize()
# ============================================
# Converts first character to uppercase
# Converts remaining characters to lowercase
# Returns a NEW string

s = "hello PYTHON"

result = s.capitalize()

print("\nAfter capitalize():")
print(result)
# Output: Hello python


# ============================================
# 4. title()
# ============================================
# Converts first character of each word to uppercase
# Returns a NEW string

s = "hello python programming"

result = s.title()

print("\nAfter title():")
print(result)
# Output: Hello Python Programming


# ============================================
# 5. swapcase()
# ============================================
# Converts uppercase characters to lowercase
# Converts lowercase characters to uppercase
# Returns a NEW string

s = "Hello PYTHON"

result = s.swapcase()

print("\nAfter swapcase():")
print(result)
# Output: hELLO python


# ============================================
# 6. strip()
# ============================================
# Removes whitespace from both ends
# Does NOT remove spaces in the middle
# Returns a NEW string

s = "   Hello Python   "

result = s.strip()

print("\nAfter strip():")
print(result)
# Output: Hello Python


# ============================================
# 7. lstrip()
# ============================================
# Removes whitespace from the LEFT side
# Returns a NEW string

result = s.lstrip()

print("\nAfter lstrip():")
print(result)
# Output: Hello Python


# ============================================
# 8. rstrip()
# ============================================
# Removes whitespace from the RIGHT side
# Returns a NEW string

result = s.rstrip()

print("\nAfter rstrip():")
print(result)
# Output:    Hello Python


# ============================================
# 9. replace(old, new)
# ============================================
# Replaces occurrences of old substring
# with new substring
# Returns a NEW string

s = "I like Java"

result = s.replace("Java", "Python")

print("\nAfter replace('Java', 'Python'):")
print(result)
# Output: I like Python

print("Original string:")
print(s)
# Output: I like Java


# ============================================
# 10. split()
# ============================================
# Splits a string into multiple parts
# By default, splits on whitespace
# Returns a LIST

s = "Hello Python World"

result = s.split()

print("\nAfter split():")
print(result)
# Output: ['Hello', 'Python', 'World']


# Split using a separator

s = "apple,banana,mango"

result = s.split(",")

print("\nAfter split(','):")
print(result)
# Output: ['apple', 'banana', 'mango']


# ============================================
# 11. join()
# ============================================
# Joins elements of an iterable into a string
# Uses the string before .join() as separator
# Returns a NEW string

words = ["Hello", "Python", "World"]

result = " ".join(words)

print("\nAfter ' '.join(words):")
print(result)
# Output: Hello Python World


# Using comma as separator

result = ",".join(words)

print("\nAfter ','.join(words):")
print(result)
# Output: Hello,Python,World


# IMPORTANT:
#
# split() -> String to List
# join()  -> List/Iterable to String


# ============================================
# 12. find(value)
# ============================================
# Finds the FIRST occurrence of a substring
# Returns the index
# Returns -1 if value is not found

s = "Hello Python"

result = s.find("Python")

print("\nAfter find('Python'):")
print(result)
# Output: 6

result = s.find("Java")

print("\nAfter find('Java'):")
print(result)
# Output: -1


# ============================================
# 13. index(value)
# ============================================
# Finds the FIRST occurrence of a substring
# Returns the index
# Raises ValueError if value is not found

s = "Hello Python"

result = s.index("Python")

print("\nAfter index('Python'):")
print(result)
# Output: 6


# If value does not exist:
#
# s.index("Java")
#
# Raises:
# ValueError


# ============================================
# 14. count(value)
# ============================================
# Counts how many times a substring occurs
# Returns an INTEGER

s = "banana"

result = s.count("a")

print("\nAfter count('a'):")
print(result)
# Output: 3


# ============================================
# 15. startswith(value)
# ============================================
# Checks whether string starts with a value
# Returns True or False

s = "Python Programming"

result = s.startswith("Python")

print("\nAfter startswith('Python'):")
print(result)
# Output: True

result = s.startswith("Java")

print("\nAfter startswith('Java'):")
print(result)
# Output: False


# ============================================
# 16. endswith(value)
# ============================================
# Checks whether string ends with a value
# Returns True or False

s = "hello.py"

result = s.endswith(".py")

print("\nAfter endswith('.py'):")
print(result)
# Output: True

result = s.endswith(".java")

print("\nAfter endswith('.java'):")
print(result)
# Output: False


# ============================================
# 17. isalpha()
# ============================================
# Checks whether ALL characters are alphabetic
# Returns True or False
#
# Spaces and numbers make it False

s = "Python"

result = s.isalpha()

print("\nAfter isalpha() on 'Python':")
print(result)
# Output: True

s = "Python123"

result = s.isalpha()

print("\nAfter isalpha() on 'Python123':")
print(result)
# Output: False


# ============================================
# 18. isdigit()
# ============================================
# Checks whether ALL characters are digits
# Returns True or False

s = "12345"

result = s.isdigit()

print("\nAfter isdigit() on '12345':")
print(result)
# Output: True

s = "123abc"

result = s.isdigit()

print("\nAfter isdigit() on '123abc':")
print(result)
# Output: False


# ============================================
# 19. isalnum()
# ============================================
# Checks whether ALL characters are
# alphabetic or numeric
# Returns True or False
#
# Spaces and special characters make it False

s = "Python123"

result = s.isalnum()

print("\nAfter isalnum() on 'Python123':")
print(result)
# Output: True

s = "Python 123"

result = s.isalnum()

print("\nAfter isalnum() on 'Python 123':")
print(result)
# Output: False


# ============================================
# 20. isspace()
# ============================================
# Checks whether ALL characters are whitespace
# Returns True or False

s = "   "

result = s.isspace()

print("\nAfter isspace() on '   ':")
print(result)
# Output: True

s = "Hello"

result = s.isspace()

print("\nAfter isspace() on 'Hello':")
print(result)
# Output: False


# ============================================
# 21. isupper()
# ============================================
# Checks whether all cased characters are uppercase
# Returns True or False

s = "HELLO"

result = s.isupper()

print("\nAfter isupper() on 'HELLO':")
print(result)
# Output: True

s = "Hello"

result = s.isupper()

print("\nAfter isupper() on 'Hello':")
print(result)
# Output: False


# ============================================
# 22. islower()
# ============================================
# Checks whether all cased characters are lowercase
# Returns True or False

s = "hello"

result = s.islower()

print("\nAfter islower() on 'hello':")
print(result)
# Output: True

s = "Hello"

result = s.islower()

print("\nAfter islower() on 'Hello':")
print(result)
# Output: False


# ============================================
# 23. len()
# ============================================
# Returns the number of characters in the string
# Includes spaces and special characters
# Returns an INTEGER

s = "Python"

result = len(s)

print("\nLength of string:")
print(result)
# Output: 6


# ============================================
# 24. in
# ============================================
# Checks whether a substring exists in a string
# Returns True or False

s = "Hello Python"

result = "Python" in s

print("\n'Python' in string:")
print(result)
# Output: True

result = "Java" in s

print("\n'Java' in string:")
print(result)
# Output: False


# ============================================
# 25. not in
# ============================================
# Checks whether a substring does NOT exist
# Returns True or False

s = "Hello Python"

result = "Java" not in s

print("\n'Java' not in string:")
print(result)
# Output: True

result = "Python" not in s

print("\n'Python' not in string:")
print(result)
# Output: False


# ============================================
# 26. STRING CONCATENATION (+)
# ============================================
# Combines two or more strings
# Returns a NEW string

first = "Hello"
second = "World"

result = first + " " + second

print("\nAfter string concatenation:")
print(result)
# Output: Hello World


# ============================================
# 27. STRING REPETITION (*)
# ============================================
# Repeats a string multiple times
# Returns a NEW string

s = "Hi "

result = s * 3

print("\nAfter string repetition:")
print(result)
# Output: Hi Hi Hi


# ============================================
# STRING SLICING
# ============================================
#
# Syntax:
#
# string[start:end:step]
#
# end index is NOT included
#

arr = "Python"

print("\nOriginal string:")
print(arr)
# Output: Python


# First 3 characters

print("\nFirst 3 characters:")
print(arr[:3])
# Output: Pyt


# From index 2 onwards

print("\nFrom index 2:")
print(arr[2:])
# Output: thon


# From index 1 to index 4

print("\nFrom index 1 to 4:")
print(arr[1:4])
# Output: yth


# Reverse string using slicing

print("\nReverse string:")
print(arr[::-1])
# Output: nohtyP


# ============================================
# STRING IMMUTABILITY
# ============================================
# Strings are IMMUTABLE
# We cannot modify individual characters directly
#
# Example:
#
# s = "Python"
# s[0] = "J"
#
# This gives:
# TypeError
#
# Instead, create a NEW string

s = "Python"

s = "J" + s[1:]

print("\nAfter changing first character:")
print(s)
# Output: Jython


# ============================================
# STRING METHODS - QUICK REVISION
# ============================================
#
# Case:
#   lower()       -> Returns new lowercase string
#   upper()       -> Returns new uppercase string
#   capitalize()  -> Returns new string with first character capitalized
#   title()       -> Returns new title-cased string
#   swapcase()    -> Returns new string with cases swapped
#
# Whitespace:
#   strip()       -> Returns new string without leading/trailing whitespace
#   lstrip()      -> Returns new string without leading whitespace
#   rstrip()      -> Returns new string without trailing whitespace
#
# Modify:
#   replace()     -> Returns new string with replacements
#
# Split / Join:
#   split()       -> Returns a LIST
#   join()        -> Returns a NEW STRING
#
# Search:
#   find()        -> Returns index or -1
#   index()       -> Returns index or raises ValueError
#   count()       -> Returns INTEGER
#
# Check:
#   startswith()  -> Returns True/False
#   endswith()    -> Returns True/False
#
# Character Checks:
#   isalpha()     -> Returns True/False
#   isdigit()     -> Returns True/False
#   isalnum()     -> Returns True/False
#   isspace()     -> Returns True/False
#   isupper()     -> Returns True/False
#   islower()     -> Returns True/False
#
# Other:
#   len()         -> Returns INTEGER
#   in            -> Returns True/False
#   not in        -> Returns True/False
#   +             -> Returns NEW STRING
#   *             -> Returns NEW STRING
#
# IMPORTANT:
#
# Strings are IMMUTABLE.
#
# Most string methods do NOT change the original string.
# They return a NEW STRING instead.
#
# ============================================
