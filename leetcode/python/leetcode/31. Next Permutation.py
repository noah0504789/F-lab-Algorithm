# 31. Next Permutation

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:  # 5
                start = i - 1  # 4

                for k in range(len(nums) - 1, start, -1):
                    if nums[k] > nums[start]:
                        end = k

                        nums[start], nums[end] = nums[end], nums[start]  # 4와 5를 바꾼다

                        for m in range(int((len(nums) - start) / 2)):  # 역순
                            nums[start + 1 + m], nums[len(nums) - 1 - m] = nums[len(nums) - 1 - m], nums[start + 1 + m]

                        break
                break

            if i == 1:
                nums.reverse()