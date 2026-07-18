# Check Palindrome Number


def palindrome_number(number) -> bool:

    temp_number = abs(number)

    if temp_number == 0:
        return True

    rev_number = 0

    while temp_number > 0:
        rev_number = (rev_number * 10) + (temp_number % 10)
        temp_number = temp_number // 10

    return number == rev_number


def main():
    try:
        number = int(input("Enter a number: "))
        print("Is Palindrome =", palindrome_number(number))
    except ValueError as e:
        print("Please enter a valid integer number.")
        print("Error: ", e)


if __name__ == "__main__":
    main()
