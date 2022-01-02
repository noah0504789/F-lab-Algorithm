def solution(s):
    lng = len(s)
    answer = 0

    def check(i):
        nonlocal answer, lng
        l, r = 0, i-1

        while r < lng:
            ifPalindStr = s[l:r + 1]

            if ifPalindStr == ifPalindStr[::-1]:
                answer = max(answer, i)
                return True
            l += 1
            r += 1

        return False

    for i in range(len(s), -1, -1):
        if check(i):
            break

    return answer

s = "abcabcdcbae"
print(solution(s))