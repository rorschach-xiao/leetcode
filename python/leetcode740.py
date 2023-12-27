from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        cntDict = {}
        for i in range(n):
            if nums[i] not in cntDict:
                cntDict[nums[i]] = 1
            else:
                cntDict[nums[i]] += 1

        uni_nums = sorted(cntDict.keys())
        m = len(uni_nums)
        dp = [0 for _ in range(m+1)]
        dp[1] = uni_nums[0] * cntDict[uni_nums[0]]
        for i in range(2, m+1):
            if uni_nums[i-1] == uni_nums[i-2] + 1:
                dp[i] = max(uni_nums[i-1] * cntDict[uni_nums[i-1]] + dp[i-2] , dp[i-1])
            else:
                dp[i] = uni_nums[i-1] * cntDict[uni_nums[i-1]] + dp[i-1]
        return dp[m]

if __name__ == '__main__':
    solution = Solution()
    print(solution.deleteAndEarn([3,4,2]))