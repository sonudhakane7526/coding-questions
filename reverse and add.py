def reverse_and_add(m, n):
    total_sum = 0
    for i in range(m, n + 1):
        reversed_num = int(str(i)[::-1])
        total_sum += reversed_num + i
    return total_sum

m = 21
n = 35
result = reverse_and_add(m, n)
print(result)