# ============================================================
# PYTHON LIST METHODS - SEARCHING AND MODIFYING
# ============================================================


# ------------------------------------------------------------
# 1. index(value)
# ------------------------------------------------------------
# Returns the FIRST index where value is found
#
# Raises ValueError if value is not found
#
# ------------------------------------------------------------

arr = [10, 20, 50, 30, 20, 40]

index = arr.index(20)

print("Index of 20:")
print(index)

# Output:
# 1


# ------------------------------------------------------------
# index(value, start)
# ------------------------------------------------------------

arr = [10, 20, 30, 20, 40]

index = arr.index(20, 2)

print("\nIndex of 20 starting from index 2:")
print(index)

# Output:
# 3


# ------------------------------------------------------------
# 2. count(value)
# ------------------------------------------------------------
# Counts how many times a value appears
#
# ------------------------------------------------------------

arr = [10, 20, 50, 30, 20, 40, 20]

count = arr.count(20)

print("\nCount of 20:")
print(count)

# Output:
# 3


# ------------------------------------------------------------
# 3. reverse()
# ------------------------------------------------------------
# Reverses the list IN PLACE
#
# - Changes original list
# - Returns None
#
# ------------------------------------------------------------

arr = [10, 20, 30, 40, 50]

print("\nBefore reverse():")
print(arr)

arr.reverse()

print("After reverse():")
print(arr)

# Output:
# [50, 40, 30, 20, 10]


# ------------------------------------------------------------
# 4. sort()
# ------------------------------------------------------------
# Sorts list in ascending order
#
# - Changes original list
# - Returns None
#
# ------------------------------------------------------------

arr = [5, 2, 8, 1, 10]

print("\nBefore sort():")
print(arr)

arr.sort()

print("After sort():")
print(arr)

# Output:
# [1, 2, 5, 8, 10]


# ------------------------------------------------------------
# 5. sort(reverse=True)
# ------------------------------------------------------------
# Sorts list in descending order
#
# ------------------------------------------------------------

arr.sort(reverse=True)

print("\nAfter sort(reverse=True):")
print(arr)

# Output:
# [10, 8, 5, 2, 1]


# ------------------------------------------------------------
# 6. sort(key=...)
# ------------------------------------------------------------
# Sort based on a custom key
#
# Example: Sort words by length
#
# ------------------------------------------------------------

words = ["apple", "hi", "banana", "cat"]

words.sort(key=len)

print("\nWords sorted by length:")
print(words)

# Output:
# ['hi', 'cat', 'apple', 'banana']

words.sort(key=len, reverse=True)

print("\nWords sorted by length reverse:")
print(words)

# Output:
# ['banana', 'apple', 'cat', 'hi']


# ------------------------------------------------------------
# 7. any()
# ------------------------------------------------------------
# Returns True if AT LEAST ONE condition is True
#
# ------------------------------------------------------------

arr = [1, 3, 5, 8]

result = any(x % 2 == 0 for x in arr)

print("\nDoes list contain at least one even number?")
print(result)

# Output:
# True


# ------------------------------------------------------------
# 8. all()
# ------------------------------------------------------------
# Returns True if ALL conditions are True
#
# ------------------------------------------------------------

arr = [2, 4, 6, 8]

result = all(x % 2 == 0 for x in arr)

print("\nAre all numbers even?")
print(result)

# Output:
# True
