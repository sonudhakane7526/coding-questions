def rotate_array(arr, n, d):
    temp = arr[n - d:]

    for i in range(n - 1, d - 1, -1):
        arr[i] = arr[i - d]

    for i in range(d):
        arr[i] = temp[i]

if __name__ == "__main__":
    n = 5
    arr = [1, 2, 3, 4, 5]
    d = 3
    
    rotate_array(arr, n, d)

    print("Output:", arr)
