# Count Words in the Sentence

s = "  My name is Madhur   Jatiya  "
s = s.strip()

if not s:
    count = 0
else:
    count = 1
    last_char = ""
    for char in s:
        if char == " " and char != last_char:
            count += 1
        last_char = char

print(count)

# ====================================================

count = len(s.split())

print(count)
