def solution(money):
    dp = [0 for _ in range(len(money))]

    dp[0] = money[0]
    dp[1] = dp[0]
    for i in range(2, len(money)-1):
        dp[i] = max(dp[i-1], dp[i-2]+money[i])
    value = max(dp)

    dp = [0 for _ in range(len(money))]

    dp[1] = money[1]
    for i in range(2, len(money)):
        dp[i] = max(dp[i-1], dp[i-2]+money[i])
    return max(value, max(dp))


print(solution([1,2,3,1]))