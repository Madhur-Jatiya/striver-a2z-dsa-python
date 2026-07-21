# ============================================================
# PYTHON LIST - IMPORTANT PYTHON TECHNIQUES
# ============================================================


# ============================================================
# 1. LIST COMPREHENSION
# ============================================================

arr = [1, 2, 3, 4, 5]


# Normal approach

squares = []

for x in arr:
    squares.append(x * x)

print("Squares using normal loop:")
print(squares)


# List comprehension

squares = [x * x for x in arr]

print("\nSquares using list comprehension:")
print(squares)


# ------------------------------------------------------------
# List comprehension with condition
# ------------------------------------------------------------

even_numbers = [x for x in arr if x % 2 == 0]

print("\nEven numbers:")
print(even_numbers)

# Output:
# [2, 4]


# ============================================================
# 2. enumerate()
# ============================================================

arr = [10, 20, 30, 40]

print("\nUsing enumerate():")

for index, value in enumerate(arr):
    print(index, value)

# Output:
#
# 0 10
# 1 20
# 2 30
# 3 40


# ============================================================
# 3. zip()
# ============================================================

names = ["A", "B", "C"]

marks = [90, 80, 70]

print("\nUsing zip():")

for name, mark in zip(names, marks):
    print(name, mark)


# Convert two lists into dictionary

result = dict(zip(names, marks))

print("\nDictionary using zip():")
print(result)


# ============================================================
# 4. LIST UNPACKING
# ============================================================

arr = [10, 20, 30]

a, b, c = arr

print("\nList unpacking:")
print(a)
print(b)
print(c)


# Extended unpacking

arr = [10, 20, 30, 40, 50]

first, *middle, last = arr

print("\nExtended unpacking:")

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# ============================================================
# 5. NESTED LISTS
# ============================================================

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Accessing elements

print("\nNested list:")

print(matrix[0][0])
# 1

print(matrix[1][2])
# 6


# Loop through matrix

print("\nMatrix elements:")

for row in matrix:
    for value in row:
        print(value)


# ============================================================
# 6. CREATING A MATRIX
# ============================================================

rows = 3
cols = 4

matrix = [[0] * cols for _ in range(rows)]

print("\nCreated matrix:")
print(matrix)

# Output:
#
# [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]


# ============================================================
# 7. MEMBERSHIP CHECK
# ============================================================

arr = [10, 20, 30, 40]

print("\nMembership check:")

if 30 in arr:
    print("30 is present")

if 100 not in arr:
    print("100 is not present")


# ============================================================
# 8. LIST CONCATENATION
# ============================================================

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

result = arr1 + arr2

print("\nConcatenated list:")
print(result)


# ============================================================
# 9. LIST REPETITION
# ============================================================

arr = [1, 2, 3]

result = arr * 3

print("\nRepeated list:")
print(result)


# ============================================================
# 10. COMMON DSA LIST PATTERN
# ============================================================

# Find maximum manually

arr = [5, 2, 8, 1, 10]

maximum = arr[0]

for value in arr:

    if value > maximum:
        maximum = value

print("\nMaximum value:")
print(maximum)


# ============================================================
# 11. COMMON DSA LIST PATTERN
# ============================================================

# Find minimum manually

arr = [5, 2, 8, 1, 10]

minimum = arr[0]

for value in arr:

    if value < minimum:
        minimum = value

print("\nMinimum value:")
print(minimum)


# ============================================================
# 12. COMMON DSA LIST PATTERN
# ============================================================

# Count frequency using a dictionary

arr = [1, 2, 2, 3, 1, 2]

frequency = {}

for value in arr:

    if value in frequency:
        frequency[value] += 1

    else:
        frequency[value] = 1

print("\nFrequency:")
print(frequency)


# ============================================================
# 13. REVERSE LIST USING TWO POINTERS
# ============================================================

arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

while left < right:

    arr[left], arr[right] = arr[right], arr[left]

    left += 1
    right -= 1

print("\nReversed using two pointers:")
print(arr)


# ============================================================
# END
# ============================================================
