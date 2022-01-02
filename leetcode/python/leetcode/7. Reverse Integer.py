class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        mystack = []
        output = ""
        flag = False
        minus = 0

        if x < 0:
            minus = 1

        for i in range(minus, len(str(x))):
            mystack.append(str(x)[i])

        while mystack:
            while not flag and mystack[-1] == 0:
                mystack.pop()

            if not flag:
                flag = True

            output += mystack.pop()

        answer = int(output) if not minus else int(output) * -1

        if math.pow(2, 31) * -1 <= answer < math.pow(2, 31):
            return answer
        else:
            return 0



