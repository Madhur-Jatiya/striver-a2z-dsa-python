# Print Reverse Pyramid

# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

number = 5

for i in range(number):
    for j in range(i):
        print("  ", end="")
    for k in range(2 * number - (i * 2 + 1)):
        print("* ", end="")
    for l in range(i):
        print("  ", end="")
    print()
