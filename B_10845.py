# 큐

N = int(input())
lst = []

for i in range(N):
    order = input()

    if order == 'push':
        print(num := int(input()))
        lst.append(num)
    elif order == 'pop':
        print(lst.pop())
    elif order == 'size':
        print()

