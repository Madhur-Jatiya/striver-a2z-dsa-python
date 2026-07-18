# Print all Divisors of a given Number

import math


def find_divisor_optimal(number) -> list:

    divisor = []

    # for i in range(1, int(number**0.5) + 1):
    for i in range(1, int(math.isqrt(number)) + 1):
        if number % i == 0:
            divisor.append(i)

            if i != number // i:
                divisor.append(number // i)

    divisor.sort()
    return divisor


def find_divisor(number) -> list:

    divisor = []

    for i in range(1, number + 1):
        if number % i == 0:
            divisor.append(i)

    return divisor


def main():
    try:
        number = int(input("Enter a number: "))
        print("Divisors =", find_divisor(number))
        print("Divisors =", find_divisor_optimal(number))
    except ValueError as e:
        print("Please enter a valid integer number.")
        print("Error: ", e)


if __name__ == "__main__":
    main()
