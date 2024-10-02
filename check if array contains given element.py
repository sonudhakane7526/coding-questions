def contains_element(arr, element):
    for item in arr:
        if item == element:
            return True
    return False

if __name__ == "__main__":
    arr = [5, 2, 4, 1, 3]
    element = 2
    
    result = contains_element(arr, element)
    print("True" if result else "False")
