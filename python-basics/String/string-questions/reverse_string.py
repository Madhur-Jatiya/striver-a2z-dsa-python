s = "madhur"

reverse = ""

for char in s:
    reverse = char + reverse

print(reverse)

# ====================================================

reverse = ""

for char in reversed(s):
    reverse = reverse + char

print(reverse)

# ====================================================

s = "madhur"
print(s[::-1])

# ====================================================

reverse = ""

s = "madhur"
reverse = "".join([char for char in reversed(s)])
print(reverse)
