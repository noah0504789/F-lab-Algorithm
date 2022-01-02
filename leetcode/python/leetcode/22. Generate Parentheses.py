class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        pair = '()'

        DP = set()
        DP.add('()')

        if n == 1:
            return list(DP)

        for i in range(2, n+1):
            nextDP = set()
            for v in list(DP):
                for p in range(i):
                    nextDP.add(v[:p]+pair+v[p:])
            DP = nextDP

        return list(DP)