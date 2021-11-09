class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        from collections import deque

        fresh = 0
        q = deque()
        M = len(grid)
        N = len(grid[0])

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                if grid[i][j] == 1:
                    fresh += 1

        minute = 0
        prev = fresh
        while q:
            i,j,minute = q.popleft()
            if grid[i][j] == 2:
                for r,c in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    if 0<=r<M and 0<=c<N and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r,c,minute+1))

        if fresh > 0:
            return -1
        else:
            return minute


sol = Solution()
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))