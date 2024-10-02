def find_min(arr):
    min_value = arr[0]
    min_index = 0

    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i

    return min_value, min_index

if __name__ == "__main__":
    arr = [5, 2, 4, 1, 3]
    min_value, min_index = find_min(arr)
    print(min_value, min_index)
