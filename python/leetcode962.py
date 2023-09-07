class Solution:
    # def maxWidthRamp(self, nums) -> int:
    #     ans = 0
    #     n = len(nums)
    #     for i in range(n):
    #         j = n - 1
    #         if j - i <= ans:
    #             break
    #         while(i < j or j - i > ans):
    #             if nums[i] > nums[j]:
    #                 j -= 1
    #             else:
    #                 ans = max(ans, j - i)
    #                 break
    #     return ans

    def maxWidthRamp(self, nums):
        ans = 0
        m = float('inf')
        for i in sorted(range(len(nums)), key=nums.__getitem__):
            ans = max(ans, i - m)
            m = min(m, i)
        return ans

if __name__ == '__main__':
    solution = Solution()
    nums = [6,0,8,2,1,5]
    print(solution.maxWidthRamp(nums))