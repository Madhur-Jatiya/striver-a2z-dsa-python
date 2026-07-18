# Check Amstrong Number


def check_amstrong_number(number) -> bool:

    num_list = [int(digit) for digit in str(number)]
    digit_count = len(num_list)

    amstrong_number = 0

    for i in num_list:
        amstrong_number = amstrong_number + (i**digit_count)

    return number == amstrong_number


def main():
    try:
        number = int(input("Enter a number: "))
        print("Is Amstrong Number =", check_amstrong_number(number))
    except ValueError as e:
        print("Please enter a valid integer number.")
        print("Error: ", e)


if __name__ == "__main__":
    main()
