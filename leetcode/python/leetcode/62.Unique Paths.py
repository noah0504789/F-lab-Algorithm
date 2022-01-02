class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        DP = [[0] * n for _ in range(m)]  # 왼쪽과 위쪽 더하면 나의 값

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    DP[i][j] = 1
                    continue

                    DP[i][j] = DP[i][j - 1] + DP[i - 1][j]

        return DP[m - 1][n - 1]

