# Sum numbers from 1 to N using Recursion


def sum_using_recursion(number):

    if number == 0:
        return 0
    if number == 1:
        return 1
    elif number < 1:
        return

    return number + sum_using_recursion(number - 1)


def sum(number):

    total_sum = 0

    sign = 1

    if number == 0:
        return total_sum
    elif number < 1:
        sign = -1
    else:
        sign = 1

    number = abs(number)

    for i in range(1, number + 1):
        total_sum = total_sum + i

    return total_sum * sign


def sum_optimal(number):
    if number < 0:
        return

    return int((number * (number + 1)) / 2)


def main():
    try:
        number = int(input("Enter a number: "))
        print("Sum of Numbers =", sum_using_recursion(number))
        print("Sum of Numbers =", sum(number))
        print("Sum of Numbers =", sum_optimal(number))
    except ValueError as e:
        print("Please enter a valid integer number.")
        print("Error: ", e)


if __name__ == "__main__":
    main()
