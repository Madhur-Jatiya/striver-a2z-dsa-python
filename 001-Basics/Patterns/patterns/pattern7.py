# Print Pyramid

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

number = 5

for i in range(number):
    for j in range(number - i - 1):
        print("  ", end="")
    for k in range(2 * i + 1):
        print("* ", end="")
    for l in range(number - i - 1):
        print("  ", end="")
    print()
