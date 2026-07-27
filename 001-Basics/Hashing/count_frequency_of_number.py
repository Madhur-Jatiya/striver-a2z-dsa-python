# Count Frequencies of a number in an Array Elements


from collections import Counter


def count_frequency(arr_list, number):
    count = 0

    for i in arr_list:
        if i == number:
            count += 1

    return count


def count_frequency_optimal(arr_list, number):
    count = Counter(arr_list)

    return count


def main():
    try:
        arr_list = [1, 2, 2, 1, 4, 5, 6, 2, 5, 7, 6, 1]
        number = int(input("Enter number: "))
        print("Count: ", count_frequency(arr_list, number))
        print("Count: ", count_frequency_optimal(arr_list, number))
    except ValueError as e:
        print("Please enter correct integer value")
        print("Error: ", e)


if __name__ == "__main__":
    main()
