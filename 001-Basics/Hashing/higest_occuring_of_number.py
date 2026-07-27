# Higest Occuring of a number in an Array Elements


from collections import defaultdict


def higest_frequency(arr_list):

    frequency_dict = defaultdict(int)

    for i in range(len(arr_list)):
        frequency_dict[arr_list[i]] += 1

    max_number = 0
    max_count = 0

    for key, value in frequency_dict.items():
        if value > max_count:
            max_number = key
            max_count = value

    print("Max Number:", max_number, end=" ")
    print("Max Value:", max_count, end=" ")


def main():
    try:
        arr_list = [1, 2, 2, 1, 4, 2, 5, 6, 2, 5, 7, 6, 1]
        higest_frequency(arr_list)
    except ValueError as e:
        print("Error while counting higest frequency")
        print("Error: ", e)


if __name__ == "__main__":
    main()
