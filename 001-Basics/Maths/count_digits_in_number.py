# Count digits in a number

try:
    number = int(input("Enter a number: "))

    number = abs(number)
    print(number)

    if number == 0:
        count = 1

    else:
        count = 0

    while number > 0:
        count += 1
        number = number // 10

    print("Number of Digits = ", count)

except ValueError as e:
    print("Please enter a valid integer number.")
    print("Error:", e)
