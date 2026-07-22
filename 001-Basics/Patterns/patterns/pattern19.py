# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

number = 5

for i in range(number):

    for j in range(number - i):
        print("*", end="")

    for k in range(i * 2):
        print(" ", end="")

    for l in range(number - i):
        print("*", end="")

    print()


for i in range(number, 0, -1):

    for j in range(number - i + 1):
        print("*", end="")

    for k in range((i - 1) * 2):
        print(" ", end="")

    for l in range(number - i + 1):
        print("*", end="")

    print()
