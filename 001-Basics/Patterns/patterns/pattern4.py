# Print 1 to 5 numbers

# 1
# 22
# 333
# 4444
# 55555

number = 5

for i in range(1, number + 1):
    for j in range(i):
        print(i, end="")
    print()
