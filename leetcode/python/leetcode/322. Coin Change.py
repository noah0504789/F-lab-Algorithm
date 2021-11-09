class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount+1): # bottom-up  11
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
                    print("dp:",dp[a], dp)

        return dp[amount] if dp[amount] != amount + 1 else -1


solution = Solution()
print(solution.coinChange([1,3,4,5], 7))