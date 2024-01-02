from functools import cache
from typing import List


class Solution:

    # recursive
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        ans = 1
        @cache
        def dfs(i):
            maxLen = {}
            for j in range(i-1, -1, -1):
                d = nums[i] - nums[j]
                if d not in maxLen:
                    nextMaxLen = dfs(j)
                    if d not in nextMaxLen:
                        maxLen[d] = 2
                    else:
                        maxLen[d] = nextMaxLen[d] + 1
            return maxLen
        for i in range(1, n):
            ans = max(ans, max(dfs(i).values()))
        return ans

    # iterative
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        dp = [{} for _ in range(n)]
        ans = 1
        for i in range(n):
            for j in range(i-1, -1, -1):
                d = nums[i] - nums[j]
                if d not in dp[i]:
                    if d not in dp[j]:
                        dp[i][d] = 2
                    else:
                        dp[i][d] = dp[j][d] + 1
                ans = max(ans, dp[i][d])
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestArithSeqLength([20,1,15,3,10,5,8]))