#    A
#   ABA
#  ABCBA
# ABCDCBA

number = 4

for i in range(1, number + 1):
    alphabet = 64

    for j in range(number - i):
        print(" ", end="")

    for k in range((2 * i) - 1):
        mid = (2 * i - 1) // 2

        if k > mid:
            alphabet -= 1
        else:
            alphabet += 1

        print(chr(alphabet), end="")

    for l in range(number - i):
        print(" ", end="")
    print()
