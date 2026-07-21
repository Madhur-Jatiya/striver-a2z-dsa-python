# Python Strings — Quick Reference

A **string** is an ordered sequence of characters enclosed in quotes.

```python
s = "Python"
```

## Important Properties

- **Ordered** → Characters have indexes.
- **Immutable** → Existing characters cannot be changed directly.
- **Supports indexing** → `s[0]`
- **Supports negative indexing** → `s[-1]`
- **Supports slicing** → `s[start:end:step]`
- **Supports duplicates** → `"hello"` contains repeated `l`.
- **Supports `in` / `not in`** → Check whether a substring exists.

---

# STRING METHODS

```text
STRING METHODS
│
├── Case
│   ├── lower()       -> converts all characters to lowercase; returns a new string
│   ├── upper()       -> converts all characters to uppercase; returns a new string
│   ├── capitalize()  -> capitalizes first character and lowercases the rest; returns a new string
│   ├── title()       -> capitalizes the first character of each word; returns a new string
│   └── swapcase()    -> swaps uppercase characters to lowercase and vice versa; returns a new string
│
├── Whitespace
│   ├── strip()       -> removes leading and trailing whitespace; returns a new string
│   ├── lstrip()      -> removes leading whitespace; returns a new string
│   └── rstrip()      -> removes trailing whitespace; returns a new string
│
├── Modify / Transform
│   └── replace()     -> replaces occurrences of a substring; returns a new string
│
├── Split / Join
│   ├── split()       -> splits a string into parts; returns a list
│   └── join()        -> joins strings from an iterable using a separator; returns a new string
│
├── Search
│   ├── find()        -> finds first occurrence; returns index or -1 if not found
│   ├── index()       -> finds first occurrence; returns index or raises ValueError
│   └── count()       -> counts non-overlapping occurrences; returns an integer
│
├── Check Start / End
│   ├── startswith()  -> checks whether string starts with a value; returns True/False
│   └── endswith()    -> checks whether string ends with a value; returns True/False
│
├── Character Checks
│   ├── isalpha()     -> checks whether all characters are alphabetic; returns True/False
│   ├── isdigit()     -> checks whether all characters are digits; returns True/False
│   ├── isalnum()     -> checks whether all characters are letters or digits; returns True/False
│   ├── isspace()     -> checks whether all characters are whitespace; returns True/False
│   ├── isupper()     -> checks whether all cased characters are uppercase; returns True/False
│   └── islower()     -> checks whether all cased characters are lowercase; returns True/False
│
└── Other
    ├── len()         -> returns the number of characters
    ├── in            -> checks whether a substring exists; returns True/False
    ├── not in        -> checks whether a substring does not exist; returns True/False
    ├── +             -> concatenates strings; returns a new string
    └── *             -> repeats a string; returns a new string
```

# Detailed Examples

## Case Methods

```python
s = "hello PYTHON world"

print(s.lower())       # hello python world
print(s.upper())       # HELLO PYTHON WORLD
print(s.capitalize())  # Hello python world
print(s.title())       # Hello Python World
print(s.swapcase())    # HELLO python WORLD
```

## Whitespace Methods

```python
s = "   Hello Python   "

print(s.strip())   # Hello Python
print(s.lstrip())  # Hello Python   
print(s.rstrip())  #    Hello Python
```

## `replace()`

```python
s = "I like Java"
result = s.replace("Java", "Python")
print(result)  # I like Python
```

**Returns:** New string.

## `split()`

```python
s = "hello world python"
print(s.split())  # ['hello', 'world', 'python']

s = "apple,banana,mango"
print(s.split(","))  # ['apple', 'banana', 'mango']
```

**Returns:** List of strings.

## `join()`

```python
words = ["Hello", "Python", "World"]
print(" ".join(words))  # Hello Python World
```

**Returns:** New string.

Remember:

```text
split() -> String to List
join()  -> Iterable of Strings to String
```

## Search Methods

```python
s = "hello python hello"

print(s.find("python"))  # 6
print(s.find("java"))    # -1

print(s.index("python")) # 6

print(s.count("hello"))  # 2
```

- `find()` → index or `-1`
- `index()` → index or `ValueError`
- `count()` → integer

## Start / End Checks

```python
s = "Python Programming"

print(s.startswith("Python"))       # True
print(s.endswith("Programming"))    # True
```

**Returns:** `True` or `False`.

## Character Checks

```python
print("Python".isalpha())       # True
print("Python123".isalpha())    # False

print("12345".isdigit())        # True
print("123abc".isdigit())       # False

print("Python123".isalnum())    # True
print("Python 123".isalnum())   # False

print("   ".isspace())          # True
print("Hello".isspace())        # False

print("HELLO".isupper())        # True
print("Hello".isupper())        # False

print("hello".islower())        # True
print("Hello".islower())        # False
```

All return `True` or `False`.

## `len()`

```python
s = "Python"
print(len(s))  # 6
```

**Returns:** Integer length.

## `in` / `not in`

```python
s = "Hello Python"

print("Python" in s)       # True
print("Java" in s)         # False
print("Java" not in s)    # True
```

**Returns:** `True` or `False`.

## Concatenation `+`

```python
first = "Hello"
second = "World"

result = first + " " + second
print(result)  # Hello World
```

**Returns:** New string.

## Repetition `*`

```python
s = "Hi "
result = s * 3
print(result)  # Hi Hi Hi
```

**Returns:** New string.

# Indexing and Slicing

```python
s = "Python"

print(s[0])    # P
print(s[-1])   # n
print(s[:3])   # Pyt
print(s[2:])   # thon
print(s[1:4])  # yth
print(s[::-1]) # nohtyP
```

Syntax:

```python
s[start:end:step]
```

# Important: Strings Are Immutable

You cannot modify a character directly.

```python
s = "Python"

# s[0] = "J"  # TypeError
```

Instead, create a new string:

```python
s = "J" + s[1:]
print(s)  # Jython
```

```text
List   -> Mutable
String -> Immutable
```

# Most Important for DSA ⭐

Focus first on:

```text
Indexing
Slicing
len()
lower()
upper()
strip()
split()
join()
replace()
find()
count()
in
not in
```

Then practice:

1. Reverse a string
2. Check palindrome
3. Count character frequency
4. Check anagram
5. Remove duplicate characters
6. Find first non-repeating character
7. Longest substring without repeating characters
8. Valid palindrome
9. Reverse words in a string
10. Character frequency using dictionary / `Counter`

# Return Value Quick Reference

| Method / Operation | Returns |
|---|---|
| `lower()` | New string |
| `upper()` | New string |
| `capitalize()` | New string |
| `title()` | New string |
| `swapcase()` | New string |
| `strip()` | New string |
| `lstrip()` | New string |
| `rstrip()` | New string |
| `replace()` | New string |
| `split()` | List |
| `join()` | New string |
| `find()` | Index / `-1` |
| `index()` | Index / `ValueError` |
| `count()` | Integer |
| `startswith()` | Boolean |
| `endswith()` | Boolean |
| `isalpha()` | Boolean |
| `isdigit()` | Boolean |
| `isalnum()` | Boolean |
| `isspace()` | Boolean |
| `isupper()` | Boolean |
| `islower()` | Boolean |
| `len()` | Integer |
| `in` | Boolean |
| `not in` | Boolean |
| `+` | New string |
| `*` | New string |

> **Important:** String methods generally do not modify the original string because strings are immutable. They return a new value instead.
