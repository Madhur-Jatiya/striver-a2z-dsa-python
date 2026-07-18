# Find factorial of N


def factorial_using_recursion(number):

    if number == 0:
        return 1
    elif number < 1:
        return

    return number * factorial_using_recursion(number - 1)


def factorial(number):

    factorial_number = 1

    sign = 1

    if number < 0:
        sign = -1
    else:
        sign = 1

    number = abs(number)

    for i in range(1, number + 1):
        factorial_number = factorial_number * i

    return factorial_number * sign


def main():
    try:
        number = int(input("Enter a number: "))
        print("Factorial =", factorial_using_recursion(number))
        print("Factorial =", factorial(number))
    except ValueError as e:
        print("Please enter a valid integer number.")
        print("Error: ", e)


if __name__ == "__main__":
    main()
