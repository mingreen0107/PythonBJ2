# 요세푸스
# 7, 3이 주어졌을 때 반복적으로 3번째 사람을 제거

import sys

N, K = map(int, sys.stdin.readline().split())

idx = 0
queue = [i for i in range(1, N+1)]
res = []

while queue:
    idx += K-1

    if idx >= len(queue):
        idx %= len(queue)

    res.append(str(queue.pop(idx)))

print("<", ", ".join(res), ">", sep="")