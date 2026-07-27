arr = [1, 93, 43, 54, 17, 9]

min_val = arr[0]

for i in arr:
    if i < min_val:
        min_val = i

print(min_val)

# or

print(min(arr))
