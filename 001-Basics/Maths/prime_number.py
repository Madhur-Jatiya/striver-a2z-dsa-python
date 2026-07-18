# Check Prime Number
# import math


def check_prime_number(number) -> bool:

    if number < 2:
        return False

    # for i in range(2, int(math.isqrt(number)) + 1):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


def main():
    try:
        number = int(input("Enter a number: "))
        print("Is Prime Number =", check_prime_number(number))
    except ValueError as e:
        print("Please enter a valid integer number.")
        print("Error: ", e)


if __name__ == "__main__":
    main()
