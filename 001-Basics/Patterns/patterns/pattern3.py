# Print 1 to 5 numbers

# 1
# 12
# 123
# 1234
# 12345

number = 5

for i in range(number):
    for j in range(i + 1):
        print(j + 1, end="")
    print()
