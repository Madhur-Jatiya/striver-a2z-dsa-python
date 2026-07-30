s = "madhur jatiya"

vowels = ["a", "e", "i", "o", "u"]

count = 0

for char in s:
    if char in vowels:
        count += 1

print(count)


# ====================================================


s = "programming"

count = sum(1 for char in s if char in "aeiou")

print(count)
