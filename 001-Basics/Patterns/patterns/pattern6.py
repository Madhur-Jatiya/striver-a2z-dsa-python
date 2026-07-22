# Print 5 to 1 numbers

# 12345
# 1234
# 123
# 12
# 1

number = 5

for i in range(number, 0, -1):
    for j in range(i):
        print(j + 1, end="")
    print()
