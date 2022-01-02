def check(s):
    mystack = []
    left, right = 0, 0
    open, close = ['(', '{', '['], [')', '}', ']']

    idx = 0
    for c in s:
        if c in open:
            mystack.append(c)
            idx = open.index(c)
            left += 1
        else:
            if c is not close[idx] or not mystack:
                return False

            mystack.pop()
            if mystack:
                idx = open.index(mystack[-1])
            right += 1

    if left == right:
        return True

    return False


def solution(s):
    answer = 0

    for i in range(len(s)):
        if check(s[i:] + s[:i]):
            answer += 1

    return answer

s = "[](){}"
# s = "}]()[{"
print(solution(s))