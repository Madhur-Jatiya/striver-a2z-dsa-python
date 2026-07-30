def remove_duplicate(s):

    non_dup = ""
    unique_set = set()

    for char in s:
        if not char in unique_set:
            unique_set.add(char)
            non_dup = non_dup + char
    return non_dup


print(remove_duplicate("programming"))
