# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = [101 for _ in range(100)]
        visited = [False for _ in range(100)]
        cnt = 0

        def dfs(depth, node):

            if not node:
                return depth - 1

            if not visited[depth]:
                ans[depth] = node.val

            visited[depth] = True

            dpt = max(dfs(depth + 1, node.right),
                      dfs(depth + 1, node.left))

            return dpt

        cnt = dfs(0, root)
        return ans[:cnt + 1]
