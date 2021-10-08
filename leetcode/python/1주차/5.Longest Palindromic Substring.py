# 5. Longest Palindromic Substring

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

        return result

if __name__ == "__main__":
    solution = Solution()
    s = "babad"
    print(solution.longestPalindrome(s))