class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0]*n
        result = 0
        for i in range(n):
            if i==0:
                dp[i] = nums[i]
            elif i==1:
                dp[i] = max(nums[i],nums[i-1])
            else:
                cur_max_money = 0
                for j in range(i-1):
                    if dp[j]+nums[i] > cur_max_money:
                        cur_max_money = dp[j]+nums[i]
                dp[i] = cur_max_money
            if dp[i] >result:
                result = dp[i]
        return result
if __name__ == '__main__':
    solution = Solution()
    nums = [2,7,9,3,1]
    print(solution.rob(nums))