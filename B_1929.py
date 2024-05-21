# M 이상 N 이하의 소수 출력

m,n = map(int,input().split())

*l, = range(n+1)

for i in l[2:]:
    if l[i] >= m:
        print(i)

    l[i::i]=n // i*[0]