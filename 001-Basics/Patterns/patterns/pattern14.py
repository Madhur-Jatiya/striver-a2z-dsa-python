# A
# A B
# A B C
# A B C D
# A B C D E

number = 5

for i in range(number):
    alphabet = 65
    for j in range(i + 1):
        print(chr(alphabet), end=" ")
        alphabet = alphabet + 1
    print()
