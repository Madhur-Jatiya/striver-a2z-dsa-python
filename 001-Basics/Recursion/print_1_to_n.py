# Print numbers 1 to N using Recursion


def recursion(number):

    if number < 1:
        return

    recursion(number - 1)
    print(number)


def main():
    try:
        number = int(input("Enter a number: "))
        recursion(number)
    except ValueError as e:
        print("Please enter a valid integer number.")
        print("Error: ", e)


if __name__ == "__main__":
    main()
