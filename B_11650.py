# x, y축을 준 후 x 기준으로 오름차순, 같으면 y 기준으로 오름차순

N = int(input())

lst = []
for i in range(N):
    [x, y] = map(int, input().split())
    lst.append([x, y])

lst.sort()
for i in lst:
    print(i[0], i[1])