import collections

class Solution:
    def subarraySum(self, nums, k):
        # 리스트 값의 합 카운트 사전
        sums_list = collections.Counter()
        # k와 같은 합 값이 존재할 경우를 위해
        sums_list[0] = 1

        # 리스트 값의 합
        sums = 0

        # 결과값
        answer = 0

        for num in nums:
            # 리스트 값을 하나씩 더하며 이때까지의 합 값 구하기
            sums += num

            # 만약 이전에 sums값 중 (sums-k)와 같은 값이 존재 했다면,
            # 합이 k인 subarray가 존재한다는 의미
            answer += sums_list[sums - k]

            sums_list[sums] += 1

        return answer

sol = Solution()
print(sol.subarraySum([1,2,3], 2))