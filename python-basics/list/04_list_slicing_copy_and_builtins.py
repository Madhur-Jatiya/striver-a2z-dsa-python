# ============================================================
# PYTHON LIST - SLICING, COPYING AND BUILT-IN FUNCTIONS
# ============================================================


# ============================================================
# LIST SLICING
# ============================================================

arr = [10, 20, 30, 40, 50]

print("Original list:")
print(arr)


# ------------------------------------------------------------
# 1. First n elements
# ------------------------------------------------------------

print("\nFirst 3 elements:")
print(arr[:3])

# Output:
# [10, 20, 30]


# ------------------------------------------------------------
# 2. From index 2 onwards
# ------------------------------------------------------------

print("\nFrom index 2:")
print(arr[2:])

# Output:
# [30, 40, 50]


# ------------------------------------------------------------
# 3. From index 2 to index 4
# ------------------------------------------------------------
# Start is included
# End is excluded
#
# ------------------------------------------------------------

print("\nFrom index 2 to 4:")
print(arr[2:4])

# Output:
# [30, 40]


# ------------------------------------------------------------
# 4. Complete copy using slicing
# ------------------------------------------------------------

copy_list = arr[:]

print("\nCopy using slicing:")
print(copy_list)


# ------------------------------------------------------------
# 5. Reverse list using slicing
# ------------------------------------------------------------
# Does NOT modify original list
#
# ------------------------------------------------------------

print("\nReverse copy:")
print(arr[::-1])

print("\nOriginal list:")
print(arr)


# ------------------------------------------------------------
# 6. Slicing with step
# ------------------------------------------------------------

print("\nEvery second element:")
print(arr[::2])

# Output:
# [10, 30, 50]


# ============================================================
# LIST COPY
# ============================================================


# ------------------------------------------------------------
# 7. copy()
# ------------------------------------------------------------

original = [1, 2, 3]

copy_list = original.copy()

original.append(4)

print("\nOriginal:")
print(original)

print("Copied list:")
print(copy_list)

# Output:
# Original: [1, 2, 3, 4]
# Copied list: [1, 2, 3]


# ------------------------------------------------------------
# 8. Assignment vs copy()
# ------------------------------------------------------------

original = [1, 2, 3]

new_list = original

copy_list = original.copy()

original.append(4)

print("\nOriginal:")
print(original)

print("Assigned list:")
print(new_list)

print("Copied list:")
print(copy_list)

# Output:
#
# Original:       [1, 2, 3, 4]
# Assigned list:  [1, 2, 3, 4]
# Copied list:    [1, 2, 3]


# ============================================================
# SHALLOW COPY VS DEEP COPY
# ============================================================

import copy

# ------------------------------------------------------------
# 9. Shallow Copy
# ------------------------------------------------------------

original = [[1, 2], [3, 4]]

shallow_copy = original.copy()

shallow_copy[0][0] = 100

print("\nOriginal after modifying shallow copy:")
print(original)

print("Shallow copy:")
print(shallow_copy)

# Both lists are affected because
# nested lists are still shared.


# ------------------------------------------------------------
# 10. Deep Copy
# ------------------------------------------------------------

original = [[1, 2], [3, 4]]

deep_copy = copy.deepcopy(original)

deep_copy[0][0] = 100

print("\nOriginal after modifying deep copy:")
print(original)

print("Deep copy:")
print(deep_copy)

# Original remains unchanged.


# ============================================================
# BUILT-IN FUNCTIONS
# ============================================================

arr = [5, 2, 8, 1]

print("\nOriginal list:")
print(arr)


# ------------------------------------------------------------
# 11. len()
# ------------------------------------------------------------

print("\nLength:")
print(len(arr))


# ------------------------------------------------------------
# 12. min()
# ------------------------------------------------------------

print("\nMinimum:")
print(min(arr))


# ------------------------------------------------------------
# 13. max()
# ------------------------------------------------------------

print("\nMaximum:")
print(max(arr))


# ------------------------------------------------------------
# 14. sum()
# ------------------------------------------------------------

print("\nSum:")
print(sum(arr))


# ------------------------------------------------------------
# 15. sorted()
# ------------------------------------------------------------
# Creates a NEW sorted list
# Does NOT modify original list
#
# ------------------------------------------------------------

sorted_arr = sorted(arr)

print("\nOriginal after sorted():")
print(arr)

print("New sorted list:")
print(sorted_arr)


# Descending order

sorted_desc = sorted(arr, reverse=True)

print("\nSorted descending:")
print(sorted_desc)
