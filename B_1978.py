# 소수 찾기

# 첫 번째 입력을 받지만 사용하지 않음
input()

# 두 번째 입력을 받아 공백으로 분리한 후 정수 리스트로 변환
numbers = map(int, input().split())

# 소수 판별 함수
def is_prime(n):
    if n <= 1:
        return False
    for j in range(2, n):
        if n % j == 0:
            return False
    return True

# 소수 개수 계산
prime_count = sum(is_prime(n) for n in numbers)

# 결과 출력
print(prime_count)
