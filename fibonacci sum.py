def fibonacci_sum(m, n):
    a, b = 0, 1
    sum_fib = 0

    while b <= n:
        if b >= m:
            sum_fib += b
        a, b = b, a + b

    return sum_fib

if __name__ == "__main__":
    m = 5
    n = 20
    result = fibonacci_sum(m, n)
    print(result)
