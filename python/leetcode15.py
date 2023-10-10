# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#
#         nums = sorted(nums)
#         if len(nums) < 3 or nums[-1] < 0 or nums[0] > 0:
#             return []
#         self.result = []
#         self.dict = {}
#         # hashmap
#         for i, n in enumerate(nums):
#             if n not in self.dict:
#                 self.dict[n] = [i]
#             else:
#                 self.dict[n] += [i]
#
#         R = len(nums) - 1
#         while (R > 0):
#             L = 0
#             while (L < R):
#                 if -(nums[R] + nums[L]) in self.dict:
#                     for idx in self.dict[-(nums[R] + nums[L])]:
#                         if idx > L and idx < R:
#                             self.result.append([nums[L], nums[R], nums[idx]])
#                             break
#                     while (L < R and nums[L] == nums[L + 1]):
#                         L += 1
#                 L += 1
#             while (0 < R and nums[R] == nums[R - 1]):
#                 R -= 1
#             R -= 1
#
#         return self.result
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        if len(nums) < 3 or nums[-1] < 0 or nums[0] > 0:
            return []
        n = len(nums)
        i = 0
        result = []
        while i < n - 2:
            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            left = i + 1
            right = n - 1
            current_sum = - nums[i]

            while left < right:
                if (nums[left] + nums[right] == current_sum):
                    result.append([nums[i], nums[left], nums[right]])
                    while (nums[left] == nums[left + 1] and left + 1 < right):
                        left += 1
                    left += 1
                    while (nums[right] == nums[right - 1] and left < right - 1):
                        right -= 1
                    right -= 1
                elif (nums[left] + nums[right] > current_sum):
                    right -= 1
                else:
                    left += 1
            i += 1
        return result
if __name__ == '__main__':
    solution = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(solution.threeSum(nums))