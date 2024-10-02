def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def calculate_prime_sum(m, n):
    prime_sum = sum(i for i in range(m, n + 1) if is_prime(i))
    return prime_sum

m, n = 10, 50
result = calculate_prime_sum(m, n)
print(result)