# Count digits in a number

import math


def count_digits(number):

    number = abs(number)

    if number == 0:
        return 1

    count = 0

    while number > 0:
        count += 1
        number = number // 10

    return count


def count_digits_optimal(number):
    number = abs(number)

    if number == 0:
        count = 1
    else:
        count = int(math.log10(number) + 1)

    return count


def main():
    try:
        number = int(input("Enter a number: "))
        print("Number of Digits =", count_digits(number))
        print("Number of Digits =", count_digits_optimal(number))
    except ValueError as e:
        print("Please enter a valid integer number.")
        print("Error: ", e)


if __name__ == "__main__":
    main()
