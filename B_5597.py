L = [0]* 30

for i in range(28):
    n = int(input())
    L[n-1] = 1

for i in range(30):
    if L[i] == 0:
        print(i+1)