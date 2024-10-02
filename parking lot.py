def max_cars_parked(n, arr):
    max_cars = 0
    current_cars = 0

    for i in range(n):
        if arr[i] == 'S':
            current_cars += 1
        else:
            max_cars = max(max_cars, current_cars)
            current_cars = 0

    max_cars = max(max_cars, current_cars)
    return max_cars

if __name__ == "__main__":
    n = 16
    arr = "XXXSXXSXXSSXXSXX"
    result = max_cars_parked(n, arr)
    print(result)
