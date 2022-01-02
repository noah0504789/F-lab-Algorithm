def solution(a):
    answer = 2

    if 0 <= len(a) <= 2:
        return len(a)

    left, right = a[0], a[-1]
    # 무조건 살아남을 수 있는 풍선만 출력하기

    for i in range(1, len(a) - 1):
        if left > a[i]:
            answer += 1
            left = a[i]
        if right > a[-1 - i]:
            answer += 1
            right = a[-1 - i]
    return answer if left != right else answer - 1

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))