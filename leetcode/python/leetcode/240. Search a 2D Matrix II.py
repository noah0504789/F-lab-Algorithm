class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        from collections import deque

        directions = {0: (0, 1), 1: (1, 0)}

        ROWS, COLS = len(matrix), len(matrix[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        visited[0][0] = True

        queue = deque()
        queue.append((0, 0))

        while queue:
            cr, cc = queue.popleft()

            if matrix[cr][cc] == target:
                return True

            for i in range(2):
                nr = cr + directions[i][0]
                nc = cc + directions[i][1]

                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if not visited[nr][nc]:
                        if matrix[nr][nc] <= target:
                            visited[nr][nc] = True
                            queue.append((nr, nc))

        return False