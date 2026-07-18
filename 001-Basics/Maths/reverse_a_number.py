# Reverse a Number


def reverse_number(number) -> int:

    sign = -1 if number < 0 else 1

    number = abs(number)

    rev_number = 0

    while number > 0:
        rev_number = (rev_number * 10) + (number % 10)
        number = number // 10

    return rev_number * sign


def main():
    try:
        number = int(input("Enter a number: "))
        print("Reverse Number =", reverse_number(number))
    except ValueError as e:
        print("Please enter a valid integer number.")
        print("Error: ", e)


if __name__ == "__main__":
    main()
