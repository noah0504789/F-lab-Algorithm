class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        nums = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        res = []

        # for d in digits:
        #     if not res:
        #         res = nums[int(d)]
        #     else:
        #         tmp = []
        #         for c1 in res:
        #             for c2 in nums[int(d)]:
        #                 tmp.append(c1+c2)
        #         res = tmp
        # return res

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            for c in nums[digits[i]]:
                backtrack(i+1, curStr+c)

        if digits:
            backtrack(0, "")

        return res

sol = Solution()
print(sol.letterCombinations("23"))