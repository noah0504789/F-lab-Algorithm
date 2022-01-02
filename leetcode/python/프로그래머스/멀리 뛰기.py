n = 4
# n = 3

def solution(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    front2, front = 1, 2
    answer = 0

    for _ in range(n - 2):
        answer = front2 + front
        front2, front = front, answer

    return answer % 1234567

print(solution(n))