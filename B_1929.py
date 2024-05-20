# M 이상 N 이하의 소수 출력

M, N = map(int, input().split())

for i in range(M, N+1):
    for j in range(2, i/2 + 1):
        if (i%j == 0):
            break
        else:
            print(i)