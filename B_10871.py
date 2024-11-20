N, X = map(int, input().split())

L = list(map(int, input().split()))

for i in range(N):
    if L[i] < X:
        print(L[i], end=' ')