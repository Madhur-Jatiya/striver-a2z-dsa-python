# ============================================================
# PYTHON LIST METHODS - ADDING AND REMOVING ELEMENTS
# ============================================================


# ------------------------------------------------------------
# 1. append(x)
# ------------------------------------------------------------
# Adds ONE element at the end of the list
#
# - Changes original list
# - Returns None
#
# ------------------------------------------------------------

arr = [10, 20, 30]

arr.append(40)

print("After append(40):")
print(arr)

# Output:
# [10, 20, 30, 40]


# append() adds the entire object as ONE element

arr = [1, 2, 3]

arr.append([4, 5])

print("\nappend([4, 5]):")
print(arr)

# Output:
# [1, 2, 3, [4, 5]]


# ------------------------------------------------------------
# 2. extend(iterable)
# ------------------------------------------------------------
# Adds ALL elements from another iterable
#
# - Changes original list
# - Returns None
#
# ------------------------------------------------------------

arr = [10, 20, 30]

arr.extend([40, 50])

print("\nAfter extend([40, 50]):")
print(arr)

# Output:
# [10, 20, 30, 40, 50]


# Difference between append() and extend()

arr1 = [1, 2, 3]

arr1.append([4, 5])

print("\nappend([4, 5]):")
print(arr1)

# Output:
# [1, 2, 3, [4, 5]]


arr2 = [1, 2, 3]

arr2.extend([4, 5])

print("\nextend([4, 5]):")
print(arr2)

# Output:
# [1, 2, 3, 4, 5]


# extend() works with strings too

arr = [1, 2]

arr.extend("ABC")

print("\nextend('ABC'):")
print(arr)

# Output:
# [1, 2, 'A', 'B', 'C']


# ------------------------------------------------------------
# 3. insert(index, value)
# ------------------------------------------------------------
# Inserts value at a specific index
#
# Existing elements shift to the right
#
# - Changes original list
# - Returns None
#
# ------------------------------------------------------------

arr = [10, 20, 30, 40]

arr.insert(1, 15)

print("\nAfter insert(1, 15):")
print(arr)

# Output:
# [10, 15, 20, 30, 40]


# ------------------------------------------------------------
# 4. remove(value)
# ------------------------------------------------------------
# Removes FIRST occurrence of value
#
# - Changes original list
# - Returns None
# - Raises ValueError if value doesn't exist
#
# ------------------------------------------------------------

arr = [10, 20, 30, 20, 40]

arr.remove(20)

print("\nAfter remove(20):")
print(arr)

# Output:
# [10, 30, 20, 40]


# ------------------------------------------------------------
# 5. pop()
# ------------------------------------------------------------
# Removes and RETURNS the last element
#
# ------------------------------------------------------------

arr = [10, 20, 30, 40]

removed = arr.pop()

print("\nAfter pop():")
print("Removed element:", removed)
print("List:", arr)

# Output:
# Removed element: 40
# List: [10, 20, 30]


# ------------------------------------------------------------
# 6. pop(index)
# ------------------------------------------------------------
# Removes and RETURNS element at given index
#
# ------------------------------------------------------------

arr = [10, 20, 30, 40]

removed = arr.pop(1)

print("\nAfter pop(1):")
print("Removed element:", removed)
print("List:", arr)

# Output:
# Removed element: 20
# List: [10, 30, 40]


# ------------------------------------------------------------
# 7. clear()
# ------------------------------------------------------------
# Removes ALL elements
#
# - Makes list empty
# - Returns None
#
# ------------------------------------------------------------

arr = [1, 2, 3, 4]

arr.clear()

print("\nAfter clear():")
print(arr)

# Output:
# []
