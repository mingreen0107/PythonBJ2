# M 이상 N 이하의 소수 출력

M, N = map(int, input().split())
sosu = []

for i in range(M, N+1):
    if i == 1:
        continue

    for j in range(2, int(i/2) + 1):
        if (i%j == 0):
            break
        else:
            sosu.append(i)

print(set(sosu))