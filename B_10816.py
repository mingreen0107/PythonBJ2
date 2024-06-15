# Mlst에 적힌 값이 Nlst에 몇개 있는지 count

import sys
input = sys.stdin.readline

N = int(input())
Nlst = list(map(int, input().split()))
M = int(input())
Mlst = list(map(int, input().split()))

count_dict = {}
for num in Nlst:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

for num in Mlst:
    if num in count_dict:
        print(count_dict[num], end=" ")
    else:
        print(0, end=" ")