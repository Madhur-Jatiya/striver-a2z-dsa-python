# ============================================================
# PYTHON LIST BASICS AND ACCESS
# ============================================================
#
# A Python list is:
# - Ordered
# - Mutable (can be changed)
# - Allows duplicate values
# - Can store different data types
#
# ============================================================


# ------------------------------------------------------------
# 1. Creating a List
# ------------------------------------------------------------

arr = [10, 20, 30, 20, 40]

print("Original list:", arr)


# ------------------------------------------------------------
# 2. List with Different Data Types
# ------------------------------------------------------------

mixed_list = [10, "Python", 3.14, True]

print("\nMixed list:")
print(mixed_list)


# ------------------------------------------------------------
# 3. List Length - len()
# ------------------------------------------------------------

print("\nLength of list:")
print(len(arr))


# ------------------------------------------------------------
# 4. Positive Indexing
# ------------------------------------------------------------

arr = [10, 20, 30, 40, 50]

print("\nPositive indexing:")

print(arr[0])  # 10
print(arr[1])  # 20
print(arr[2])  # 30
print(arr[3])  # 40
print(arr[4])  # 50


# ------------------------------------------------------------
# 5. Negative Indexing
# ------------------------------------------------------------

print("\nNegative indexing:")

print(arr[-1])  # 50
print(arr[-2])  # 40
print(arr[-3])  # 30


# ------------------------------------------------------------
# 6. Modifying List Using Index
# ------------------------------------------------------------

arr[0] = 100

print("\nAfter modifying index 0:")
print(arr)


# ------------------------------------------------------------
# 7. Membership Operators
# ------------------------------------------------------------

print("\nMembership operators:")

print(30 in arr)
# True

print(500 in arr)
# False

print(500 not in arr)
# True


# ------------------------------------------------------------
# 8. List Concatenation
# ------------------------------------------------------------

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print("\nList concatenation:")
print(result)

# Output:
# [1, 2, 3, 4, 5, 6]


# ------------------------------------------------------------
# 9. List Repetition
# ------------------------------------------------------------

arr = [1, 2, 3]

result = arr * 3

print("\nList repetition:")
print(result)

# Output:
# [1, 2, 3, 1, 2, 3, 1, 2, 3]


# Useful for initializing a list

zeros = [0] * 5

print("\nList with repeated zero:")
print(zeros)

# Output:
# [0, 0, 0, 0, 0]


# ============================================================
# END
# ============================================================
