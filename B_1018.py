# 체스판 다시 칠하기

N, M = map(int, input().split())
lst = [[0] * M for _ in range(N)]

for i in range(M):
        lst[i] = input()

print(lst)