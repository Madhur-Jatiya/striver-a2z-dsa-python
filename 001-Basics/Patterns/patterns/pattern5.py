# Print 5 to 1 stars

# *****
# ****
# ***
# **
# *

number = 5

for i in range(number, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
