# Python Lists — Quick Reference

A **list** is an ordered, mutable collection of elements.

```python
arr = [10, 20, 30, 20, 40]
```

## Important Properties

* **Ordered** → Elements maintain their insertion order.
* **Mutable** → Elements can be changed after the list is created.
* **Allows duplicates** → The same value can appear multiple times.
* **Allows different data types** → A list can contain integers, strings, floats, booleans, etc.
* **Supports indexing** → `arr[0]`
* **Supports negative indexing** → `arr[-1]`
* **Supports slicing** → `arr[start:end:step]`
* **Can be nested** → A list can contain another list.

Example:

```python
arr = [10, 20, 30, 20, 40]

print(arr[0])     # 10
print(arr[-1])    # 40
print(arr[1:4])   # [20, 30, 20]
```

---

# LIST METHODS

```text
LIST METHODS
│
├── Add / Insert
│   ├── append(x)        -> adds ONE element at the end; returns None
│   ├── extend(iterable) -> adds ALL elements from an iterable; returns None
│   └── insert(i, x)     -> inserts an element at a specific index; returns None
│
├── Remove
│   ├── remove(x)        -> removes FIRST occurrence of a value; returns None
│   ├── pop()            -> removes and returns the LAST element
│   ├── pop(i)           -> removes and returns the element at index i
│   └── clear()          -> removes ALL elements; returns None
│
├── Search / Count
│   ├── index(x)         -> returns FIRST index of a value; raises ValueError if not found
│   └── count(x)         -> counts occurrences of a value; returns an integer
│
├── Modify / Sort
│   ├── reverse()        -> reverses list in-place; returns None
│   └── sort()           -> sorts list in-place; returns None
│
├── Copy
│   └── copy()           -> creates a SHALLOW COPY; returns a new list
│
├── Slicing
│   └── arr[start:end:step] -> extracts part of a list; returns a new list
│
└── Built-in Functions
    ├── len(arr)         -> returns number of elements
    ├── min(arr)         -> returns smallest element
    ├── max(arr)         -> returns largest element
    ├── sum(arr)         -> returns sum of elements
    └── sorted(arr)      -> returns a NEW sorted list; original remains unchanged
```

---

# 1. `append(x)`

Adds **ONE element** to the end of the list.

* Modifies the original list.
* Returns `None`.

```python
arr = [10, 20, 30]

result = arr.append(40)

print(arr)
# [10, 20, 30, 40]

print(result)
# None
```

Important:

```python
arr.append([50, 60])

print(arr)
# [10, 20, 30, 40, [50, 60]]
```

`append()` adds the entire list as **one element**.

---

# 2. `extend(iterable)`

Adds **ALL elements** from another iterable.

* Modifies the original list.
* Returns `None`.

```python
arr = [10, 20, 30]

result = arr.extend([40, 50])

print(arr)
# [10, 20, 30, 40, 50]

print(result)
# None
```

Unlike `append()`:

```python
arr = [1, 2, 3]

arr.append([4, 5])

print(arr)
# [1, 2, 3, [4, 5]]
```

`extend()`:

```python
arr = [1, 2, 3]

arr.extend([4, 5])

print(arr)
# [1, 2, 3, 4, 5]
```

Remember:

```text
append([4, 5])
    -> Adds [4, 5] as ONE element

extend([4, 5])
    -> Adds 4 and 5 separately
```

---

# 3. `insert(index, value)`

Inserts a value at a specific index.

* Existing elements shift to the right.
* Modifies the original list.
* Returns `None`.

```python
arr = [10, 20, 30]

result = arr.insert(1, 15)

print(arr)
# [10, 15, 20, 30]

print(result)
# None
```

---

# 4. `remove(value)`

Removes the **FIRST occurrence** of a value.

* Modifies the original list.
* Returns `None`.
* Raises `ValueError` if the value doesn't exist.

```python
arr = [10, 20, 30, 20, 40]

result = arr.remove(20)

print(arr)
# [10, 30, 20, 40]

print(result)
# None
```

Only the first `20` is removed.

---

# 5. `pop()`

Removes and returns the **last element**.

```python
arr = [10, 20, 30]

removed = arr.pop()

print(removed)
# 30

print(arr)
# [10, 20]
```

**Returns:** Removed element.

---

# 6. `pop(index)`

Removes and returns the element at a specific index.

```python
arr = [10, 20, 30, 40]

removed = arr.pop(1)

print(removed)
# 20

print(arr)
# [10, 30, 40]
```

**Returns:** Removed element.

If the index is invalid:

```python
arr.pop(10)
```

Raises:

```text
IndexError
```

---

# 7. `clear()`

Removes **ALL elements** from the list.

* Modifies the original list.
* Returns `None`.

```python
arr = [10, 20, 30]

result = arr.clear()

print(arr)
# []

print(result)
# None
```

---

# 8. `index(value)`

Returns the **FIRST index** of a value.

* Returns an integer.
* Raises `ValueError` if value is not found.

```python
arr = [10, 20, 30, 20, 40]

result = arr.index(20)

print(result)
# 1
```

The second `20` is at index `3`, but `index()` returns the first occurrence.

If value is not found:

```python
arr.index(100)
```

Raises:

```text
ValueError
```

---

# 9. `count(value)`

Counts how many times a value appears in the list.

* Returns an integer.
* Does not modify the list.

```python
arr = [10, 20, 30, 20, 40, 20]

result = arr.count(20)

print(result)
# 3
```

---

# 10. `reverse()`

Reverses the list **in-place**.

* Modifies the original list.
* Returns `None`.

```python
arr = [10, 20, 30, 40]

result = arr.reverse()

print(arr)
# [40, 30, 20, 10]

print(result)
# None
```

Important:

```python
arr.reverse()
```

is different from:

```python
arr[::-1]
```

`reverse()` modifies the original list.

`arr[::-1]` creates a new reversed list.

---

# 11. `sort()`

Sorts the list in ascending order **in-place**.

* Modifies the original list.
* Returns `None`.

```python
arr = [5, 2, 8, 1]

result = arr.sort()

print(arr)
# [1, 2, 5, 8]

print(result)
# None
```

### Descending Order

```python
arr.sort(reverse=True)

print(arr)
# [8, 5, 2, 1]
```

---

# 12. `copy()`

Creates a **shallow copy** of the list.

* Returns a new list.
* Original and copied list are separate outer list objects.

```python
original = [1, 2, 3]

copy_list = original.copy()

original.append(4)

print(original)
# [1, 2, 3, 4]

print(copy_list)
# [1, 2, 3]
```

Compare with assignment:

```python
original = [1, 2, 3]

new_list = original

original.append(4)

print(original)
# [1, 2, 3, 4]

print(new_list)
# [1, 2, 3, 4]
```

Why?

```text
new_list = original
    -> Both variables refer to the SAME list

new_list = original.copy()
    -> A NEW outer list is created
    -> This is a shallow copy
```

---

# LIST SLICING ⭐

Syntax:

```python
arr[start:end:step]
```

The `end` index is **not included**.

```python
arr = [10, 20, 30, 40, 50]
```

## First 3 Elements

```python
print(arr[:3])
# [10, 20, 30]
```

## From Index 2 Onwards

```python
print(arr[2:])
# [30, 40, 50]
```

## Index 2 to Index 4

```python
print(arr[2:4])
# [30, 40]
```

Index `4` is excluded.

## Reverse List

```python
print(arr[::-1])
# [50, 40, 30, 20, 10]
```

This does **not modify** the original list.

```python
print(arr)
# [10, 20, 30, 40, 50]
```

---

# BUILT-IN FUNCTIONS

These are not list methods, but they are frequently used with lists.

---

## `len(arr)`

Returns the number of elements.

```python
arr = [10, 20, 30, 40]

print(len(arr))
# 4
```

**Returns:** Integer.

---

## `min(arr)`

Returns the smallest element.

```python
arr = [5, 2, 8, 1]

print(min(arr))
# 1
```

**Returns:** Smallest element.

---

## `max(arr)`

Returns the largest element.

```python
arr = [5, 2, 8, 1]

print(max(arr))
# 8
```

**Returns:** Largest element.

---

## `sum(arr)`

Returns the sum of all elements.

```python
arr = [5, 2, 8, 1]

print(sum(arr))
# 16
```

**Returns:** Numeric sum.

---

# `sort()` vs `sorted()` ⭐⭐⭐

This is very important.

## `sort()`

```python
arr = [5, 2, 8, 1]

result = arr.sort()

print(arr)
# [1, 2, 5, 8]

print(result)
# None
```

`sort()`:

* Modifies the original list.
* Returns `None`.

---

## `sorted()`

```python
arr = [5, 2, 8, 1]

result = sorted(arr)

print(arr)
# [5, 2, 8, 1]

print(result)
# [1, 2, 5, 8]
```

`sorted()`:

* Does NOT modify the original list.
* Returns a NEW sorted list.

Remember:

```text
arr.sort()
    -> Modifies original
    -> Returns None

sorted(arr)
    -> Original unchanged
    -> Returns new sorted list
```

---

# LIST INDEXING

Lists use zero-based indexing.

```python
arr = [10, 20, 30, 40, 50]

print(arr[0])
# 10

print(arr[2])
# 30

print(arr[-1])
# 50

print(arr[-2])
# 40
```

---

# LIST MODIFICATION

Because lists are mutable, you can change elements directly.

```python
arr = [10, 20, 30]

arr[0] = 100

print(arr)
# [100, 20, 30]
```

Unlike strings:

```text
List   -> Mutable
String -> Immutable
```

---

# LIST RETURN VALUE QUICK REFERENCE

| Method / Function  | Modifies Original? | Returns              |
| ------------------ | ------------------ | -------------------- |
| `append(x)`        | Yes                | `None`               |
| `extend(iterable)` | Yes                | `None`               |
| `insert(i, x)`     | Yes                | `None`               |
| `remove(x)`        | Yes                | `None`               |
| `pop()`            | Yes                | Removed element      |
| `pop(i)`           | Yes                | Removed element      |
| `clear()`          | Yes                | `None`               |
| `index(x)`         | No                 | Index / `ValueError` |
| `count(x)`         | No                 | Integer              |
| `reverse()`        | Yes                | `None`               |
| `sort()`           | Yes                | `None`               |
| `copy()`           | No                 | New list             |
| `arr[start:end]`   | No                 | New list             |
| `len(arr)`         | No                 | Integer              |
| `min(arr)`         | No                 | Smallest element     |
| `max(arr)`         | No                 | Largest element      |
| `sum(arr)`         | No                 | Numeric sum          |
| `sorted(arr)`      | No                 | New sorted list      |

---

# MOST IMPORTANT FOR DSA ⭐

Focus on these first:

```text
Indexing
Slicing
append()
extend()
insert()
pop()
remove()
sort()
sorted()
reverse()
count()
index()
len()
min()
max()
sum()
```

Then practice:

1. Find maximum element
2. Find minimum element
3. Find second largest element
4. Reverse a list
5. Rotate a list
6. Remove duplicates
7. Count frequency of elements
8. Find missing number
9. Move zeroes to the end
10. Two Sum
11. Merge sorted arrays
12. Remove duplicates from sorted array
13. Maximum subarray sum
14. Majority element
15. Intersection of two arrays

---

# IMPORTANT INTERVIEW CONCEPTS

## `append()` vs `extend()`

```text
append([4, 5])
    -> [1, 2, 3, [4, 5]]

extend([4, 5])
    -> [1, 2, 3, 4, 5]
```

---

## `remove()` vs `pop()`

```text
remove(value)
    -> Removes by VALUE
    -> Returns None

pop(index)
    -> Removes by INDEX
    -> Returns removed element
```

---

## `sort()` vs `sorted()`

```text
sort()
    -> Modifies original list
    -> Returns None

sorted()
    -> Does not modify original
    -> Returns new sorted list
```

---

## `reverse()` vs `[::-1]`

```text
reverse()
    -> Modifies original list
    -> Returns None

[::-1]
    -> Creates new reversed list
    -> Original unchanged
```

---

## Assignment vs `copy()`

```text
new_list = original
    -> Same list reference

new_list = original.copy()
    -> New outer list
    -> Shallow copy
```

---

# FINAL MENTAL MODEL

```text
PYTHON LIST
│
├── Ordered
├── Mutable
├── Allows duplicates
├── Supports indexing
├── Supports slicing
├── Supports different data types
│
├── ADD
│   ├── append()
│   ├── extend()
│   └── insert()
│
├── REMOVE
│   ├── remove()
│   ├── pop()
│   └── clear()
│
├── SEARCH
│   ├── index()
│   └── count()
│
├── MODIFY
│   ├── reverse()
│   └── sort()
│
├── COPY
│   └── copy()
│
└── BUILT-IN FUNCTIONS
    ├── len()
    ├── min()
    ├── max()
    ├── sum()
    └── sorted()
```

> **Important:** List methods such as `append()`, `extend()`, `insert()`, `remove()`, `reverse()`, and `sort()` modify the original list and return `None`. Methods such as `pop()` return the removed element, while `copy()` returns a new list.
