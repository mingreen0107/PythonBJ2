# 666, 1666, 2666, 3666 ...

n = int(input())
i = 0

while n:
    i += 1
    n -= '666' in '%s'%i

print(i)