# 48. Rotate Image

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        import copy
        temp_matrix = copy.deepcopy(matrix)

        n = len(matrix[0])
        for i in range(n-1, -1, -1):
            for j in range(0, n):
                matrix[j][abs(n-1-i)] = temp_matrix[i][j]
