# Print Reverse Pyramid

# 1 
# 1 0 
# 1 0 1 
# 1 0 1 0 
# 1 0 1 0 1 

number = 5

for i in range(number):
    for j in range(i + 1):
        if j % 2 == 0:
            x = 1
        else:
            x = 0
        print(x, end=" ")
    print()
