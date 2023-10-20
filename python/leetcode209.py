from typing import List


# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         """
#         :type target: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         min_len=float('inf')
#         start=0
#         cur_sum=0
#         for i in range(n):
#             cur_sum+=nums[i]
#             end = i
#             if cur_sum>=target:
#                 if end-start+1 < min_len: min_len = end-start+1
#                 while(start<=end):
#                     cur_sum-=nums[start]
#                     start += 1
#                     if cur_sum<target:
#                         break
#                     else:
#                         if end - start + 1 < min_len: min_len = end - start + 1
#         if min_len==float('inf'):
#             return 0
#         else:
#             return min_len

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        front, behind, n, minLen, currentSum = 0, 0, len(nums), 0, 0
        while(front < n):
            currentSum += nums[front]
            if currentSum >= target:
                minLen = front - behind + 1 if minLen == 0 else min(minLen, front - behind + 1)
                currentSum -= nums[behind]
                behind += 1
                while(behind <= front and currentSum >= target):
                    minLen = min(minLen, front - behind + 1)
                    currentSum -= nums[behind]
                    behind += 1
            front += 1
        return minLen

if __name__=='__main__':
    solution=Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    print(solution.minSubArrayLen(target,nums))
