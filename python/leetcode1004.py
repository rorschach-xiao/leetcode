from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        head = 0
        n = len(nums)
        maxNum = 0
        for i in range(n):
            if nums[i] == 0:
                k -= 1
            if k < 0:
                if nums[head] == 0:
                    k += 1
                head += 1
            maxNum = max(maxNum, i - head + 1)
        return maxNum

if __name__ == '__main__':
    solution = Solution()
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    print(solution.longestOnes(nums, 3))