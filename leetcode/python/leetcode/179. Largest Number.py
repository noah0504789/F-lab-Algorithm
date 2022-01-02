class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not any(map(bool, nums)):
            return '0'

        lng = len(nums)
        nums = list(map(str, nums))

        if len(nums) < 2:
            return "".join(nums)

        l, r = 0, 1

        def compare(l, r):
            return int(nums[l] + nums[r]) > int(nums[r] + nums[l])

        for l in range(lng):
            r = l + 1
            while l < lng and r < lng:
                if compare(l, r):
                    pass
                else:
                    nums[r], nums[l] = nums[l], nums[r]
                r += 1

        return "".join(nums)

sol = Solution()
print(sol.largestNumber([31,30,34,5,9]))