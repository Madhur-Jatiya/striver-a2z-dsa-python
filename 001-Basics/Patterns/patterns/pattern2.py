# Print 1 to 5 stars

# *
# **
# ***
# ****
# *****

number = 5

for i in range(number):
    for j in range(i + 1):
        print("*", end="")
    print()
