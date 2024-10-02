def max_sub_array_sum(arr):
    max_so_far = max_ending_here = arr[0]

    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum Subarray Sum is", max_sub_array_sum(arr))