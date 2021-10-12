class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]

        N = len(nums)
        st, end = -1, -1
        l, r = 0, N

        # binary search left
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        if l < N and nums[l] == target: st = l

        l, r = 0, N
        # binary search right
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid

        if nums[r - 1] == target: end = r - 1

        return [st, end]