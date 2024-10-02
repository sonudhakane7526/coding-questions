def count_occurrences(arr, element):
    count = 0

    for num in arr:
        if num == element:
            count += 1

    return count

arr = [5, 2, 4, 1, 2]
element = 2
result = count_occurrences(arr, element)
print(result)