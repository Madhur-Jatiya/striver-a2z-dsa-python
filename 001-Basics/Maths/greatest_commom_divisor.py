# Greatest Commom Divisor of 2 Numbers


def find_divisor(number) -> list:

    divisor = []

    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisor.append(i)

            if i != number // i:
                divisor.append(number // i)

    divisor.sort()
    return divisor


def gcd_number(number1, number2) -> int:

    divisors1 = find_divisor(abs(number1))
    divisors2 = find_divisor(abs(number2))

    gcd = 1

    for num1 in divisors1:
        for num2 in divisors2:
            if num1 == num2 and num1 > gcd:
                gcd = num1

    return gcd


def gcd_number_optimal(number1, number2) -> int:

    gcd = 1

    for i in range(min(number1, number2), 0, -1):
        if number1 % i == 0 and number2 % i == 0:
            return i

    return gcd


def main():
    try:
        number1 = int(input("Enter a number 1: "))
        number2 = int(input("Enter a number 2: "))
        print("Greated =", gcd_number(number1, number2))
        print("Greated =", gcd_number_optimal(number1, number2))
    except ValueError as e:
        print("Please enter a valid integer number.")
        print("Error: ", e)


if __name__ == "__main__":
    main()
