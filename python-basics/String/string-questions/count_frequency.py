# Count frequency of each digit

s = "madhur jatiya"

freq_counter = {}

for char in s:
    if char in freq_counter:
        freq_counter[char] += 1
    else:
        freq_counter[char] = 1

print(freq_counter)
