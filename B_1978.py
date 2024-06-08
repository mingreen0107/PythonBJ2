# 소수 찾기

input()

numbers = map(int, input().split())

def is_prime(n):
    if n <= 1:
        return False

    for j in range(2, n):
        if n % j == 0:
            return False

    return True

prime_count = sum(is_prime(n) for n in numbers)

print(prime_count)