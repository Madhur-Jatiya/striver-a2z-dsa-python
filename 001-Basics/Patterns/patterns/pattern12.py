# 1      1
# 12    21
# 123  321
# 12344321

number = 4

for i in range(1, number + 1):
    for j in range(i):
        print(j + 1, end="")

    for k in range((2 * number) - (2 * i)):
        print(" ", end="")

    for l in range(i, 0, -1):
        print(l, end="")
    print()
