# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

number = 5
stars = 0

for i in range(1, 2 * number):

    if i > 5:
        stars -= 1
    else:
        stars += 1

    for j in range(stars):
        print("*", end="")

    for k in range((2 * number) - (2 * stars)):
        print(" ", end="")

    for l in range(stars):
        print("*", end="")

    print()
