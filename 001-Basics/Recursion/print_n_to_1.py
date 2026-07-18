# Print numbers N to 1 using Recursion


def recursion(number):

    if number < 1:
        return

    print(number)
    recursion(number - 1)


def main():
    try:
        number = int(input("Enter a number: "))
        recursion(number)
    except ValueError as e:
        print("Please enter a valid integer number.")
        print("Error: ", e)


if __name__ == "__main__":
    main()
