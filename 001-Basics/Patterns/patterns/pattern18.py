# E
# DE
# CDE
# BCDE
# ABCDE

number = 5

for i in range(number):
    alphabet = 69

    for j in range(i + 1, 0, -1):
        print(chr(alphabet - j + 1), end="")

    print()
