# A 
# B B 
# C C C 
# D D D D 
# E E E E E 

number = 5
alphabet = 65

for i in range(number):
    for j in range(i + 1):
        print(chr(alphabet), end=" ")
    alphabet = alphabet + 1
    print()
