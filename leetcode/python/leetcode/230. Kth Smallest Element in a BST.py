class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cnt = 0
        ans = -1
        flag = False

        def preOrder(root):
            nonlocal cnt, ans, k, flag

            if not root or flag:
                return

            preOrder(root.left)
            if cnt == k:
                flag = True
                return
            if flag:
                return
            ans = root.val
            cnt += 1
            preOrder(root.right)

        preOrder(root)

        return ans