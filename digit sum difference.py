def digit_sum_difference(m, n):
    sum_divisible_by_4 = 0
    sum_divisible_by_7 = 0

    for i in range(m, n + 1):
        if i % 4 == 0:
            num = i
            while num > 0:
                sum_divisible_by_4 += num % 10
                num //= 10
        elif i % 7 == 0:
            num = i
            while num > 0:
                sum_divisible_by_7 += num % 10
                num //= 10

    return abs(sum_divisible_by_4 - sum_divisible_by_7)

m = 50
n = 120
result = digit_sum_difference(m, n)
print(result)