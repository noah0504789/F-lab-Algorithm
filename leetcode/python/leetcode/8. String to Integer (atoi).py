class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        minus = 0
        isDigit = True

        if s[0] == "-":
            minus = 1

        for i in range(minus, len(s)):
            if s[i].isnumeric():



