class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        intervals = sorted(intervals)
        ans.append(intervals.pop(0))

        while intervals:
            target = intervals.pop(0)
            flag = False
            for v in ans:
                if v[0] <= target[0] <= v[1]:
                    v[1] = max(v[1], target[1])
                    flag = True
                    break

            if not flag:
                ans.append(target)

        return ans

sol = Solution()
print(sol.merge([[1,4],[4,5]]))