arr = [1, 93, 43, 54, 17, 9]

max_val = arr[0]

for i in arr:
    if i > max_val:
        max_val = i

print(max_val)

# or

print(max(arr))
