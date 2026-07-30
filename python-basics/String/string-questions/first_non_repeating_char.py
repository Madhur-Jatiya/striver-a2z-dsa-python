s = "aabbbbcdde"

freq_counter = {}

for char in s:
    freq_counter[char] = freq_counter.get(char, 0) + 1

for char in s:
    if freq_counter[char] == 1:
        print(char)
        break
