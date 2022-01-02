n = int(input())
stack = []

for _ in range(n):
    str = input()
    flag = True

    for c in str:
        if c == '(':
            stack.append('(')

        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break

    if stack:
        flag = False

    print('YES' if flag else 'NO')
    stack = []