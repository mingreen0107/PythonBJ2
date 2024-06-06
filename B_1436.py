# 666 == 1, 1666 == 2, 2666 == 3, 3666 ...

n = int(input())
i = 0

while n:
    i += 1
    n -= '666' in str(i)

print(i)