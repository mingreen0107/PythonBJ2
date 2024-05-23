# () -> YES / (( -> NO

T = int(input())

for i in range(T):
    stack = []
    a = input()

    for j in a:
        if j == '(':
            stack.append(j)

        elif j == ')':
            if stack:
                stack.pop()

            # 스택에 괄호가 없을경우
            else:
                print("NO")
                break

    # break문으로 끊기지 않고 수행됐을 경우
    else:
        # break문으로 안 끊기고 스택이 비어있는 경우
        if not stack:
            print("YES")

        # break에서 안 걸렸더라도 스택에 괄호가 들어있을 경우
        else:
            print("NO")