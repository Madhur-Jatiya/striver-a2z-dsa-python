# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 

number = 5
digit = 1

for i in range(number):
    for j in range(i + 1):
        print(digit, end=" ")
        digit = digit + 1
    print()
