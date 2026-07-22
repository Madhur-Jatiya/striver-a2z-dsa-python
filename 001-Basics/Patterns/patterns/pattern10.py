# Print Reverse Pyramid

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

number = 5

for i in range(1, 2 * number):
    x = i
    if i > number:
        x = (2 * number) - i
    for j in range(x):
        print("* ", end="")
    print()
