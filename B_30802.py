# S, M, L, XL, XXL, XXXL

N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

ans = 0
for i in range(len(size)):
    if size[i]%T == 0:
        ans += int(size[i]/T)
    else:
        ans += (int(size[i]/T) + 1)

print(ans)

ans2 = [int(N/P), N%P]
print(*ans2)