nums = [1,3,4,2,2]

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        while True:
            slow = nums[slow] # 1step
            fast = nums[nums[fast]] # 2step
            if slow == fast: # 만나는 지점 찾기
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

