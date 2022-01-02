def solution(stones, k):
    left = 1
    right = max(stones)
    answer = 0

    while left <= right:
        blankCount = 0
        mid = (left+right) // 2

        for stone in stones:
            if stone - mid <= 0:
                blankCount += 1
            else:
                blankCount = 0

            if blankCount >= k:
                break

        if blankCount < k:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))