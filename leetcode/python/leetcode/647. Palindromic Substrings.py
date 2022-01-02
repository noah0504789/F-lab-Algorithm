class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        l, r = 0, 0

        def isPalindrom(str):
            if str == str[::-1]:
                return True
            return False

        while l < len(s):
            while r < len(s):
                if isPalindrom(s[l:r+1]):
                    ans+=1
                r += 1
            l += 1

        return ans
