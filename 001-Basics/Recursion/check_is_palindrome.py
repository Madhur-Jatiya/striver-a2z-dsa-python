# Check weather if string is palindrome or not using Recursion


def recursion(text):

    if text < 1:
        return

    recursion(text - 1)
    print("Hello my name is Madhur Jatiya", text)


def check_palindrome(text):
    rev_text = text[::-1]
    return text == rev_text


def main():
    try:
        text = input("Enter text: ")
        recursion(5)
        print("Is Palindrom: ", check_palindrome(text))
    except ValueError as e:
        print("Error while checking palindrome")
        print("Error: ", e)


if __name__ == "__main__":
    main()
