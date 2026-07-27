# Count Frequencies of a each number in an Array Elements


from collections import defaultdict


def count_frequency(arr_list):

    frequency_dict = defaultdict(int)

    for i in range(len(arr_list)):
        frequency_dict[arr_list[i]] += 1

    for key, value in frequency_dict.items():
        print("Key:", key, end=" ")
        print("Count:", value, end=" ")
        print()


def main():
    try:
        arr_list = [1, 2, 2, 1, 4, 5, 6, 2, 5, 7, 6, 1]
        count_frequency(arr_list)
    except ValueError as e:
        print("Error while counting frequency")
        print("Error: ", e)


if __name__ == "__main__":
    main()
