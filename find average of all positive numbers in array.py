def average_positive(arr):
    total = count = 0
    for num in arr:
        if num > 0:
            total += num
            count += 1
    return total / count if count > 0 else -1

arr = [5, 2, -4, 1, 3]
result = average_positive(arr)

print("Output:", result)