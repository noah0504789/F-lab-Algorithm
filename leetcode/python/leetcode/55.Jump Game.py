class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastGoodIndexPosition = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastGoodIndexPosition:
                lastGoodIndexPosition = i

        return lastGoodIndexPosition == 0
