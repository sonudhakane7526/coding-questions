def find_pair(arr, sum):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == sum:
                print(f"Pair found: {arr[i]}, {arr[j]}")
                return
    print("Pair not found")

arr = [1, 4, 7, 8, 3, 9]
sum_val = 10
find_pair(arr, sum_val)