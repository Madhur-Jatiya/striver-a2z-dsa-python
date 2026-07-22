# A B C D E
# A B C D
# A B C
# A B
# A

number = 5

for i in range(number, 0, -1):
    alphabet = 65
    for j in range(i):
        print(chr(alphabet), end=" ")
        alphabet = alphabet + 1
    print()
