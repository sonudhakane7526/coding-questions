import math

def square_root_difference(m, n):
    even_sum = sum(math.sqrt(i) for i in range(m, n + 1) if i % 2 == 0)
    odd_sum = sum(math.sqrt(i) for i in range(m, n + 1) if i % 2 != 0)

    return even_sum - odd_sum

m, n = 1, 10
result = square_root_difference(m, n)
print(f"{result:.5f}")