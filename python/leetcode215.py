import heapq
import random
from typing import List


# regular quickselect
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         self.nums = nums
#         n = len(nums)
#         return self.quickSelect(0, n - 1, n - k)
#
#     def quickSelect(self, left, right, k):
#         if left == right:
#             return self.nums[k]
#
#         pivot, i, j = left, left, right
#         while i < j:
#             while i < j and self.nums[j] > self.nums[pivot]:
#                 j -= 1
#             while i < j and self.nums[i] <= self.nums[pivot]:
#                 i += 1
#             if i < j:
#                 temp = self.nums[i]
#                 self.nums[i] = self.nums[j]
#                 self.nums[j] = temp
#         temp = self.nums[pivot]
#         self.nums[pivot] = self.nums[j]
#         self.nums[j] = temp
#         if k == j: return self.nums[k]
#         elif k < j: return self.quickSelect(left, j - 1, k)
#         else: return self.quickSelect(j + 1, right, k)

# # improved quickSelect, huge improvement when nums has lots of equal elements
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         def quickSelect(nums, k):
#             pivot = random.choice(nums)
#             less, equal, large = [], [], []
#             for num in nums:
#                 if num > pivot:
#                     large.append(num)
#                 elif num < pivot:
#                     less.append(num)
#                 else:
#                     equal.append(num)
#             if k <= len(large):
#                 return quickSelect(large, k)
#             elif k > len(large) + len(equal):
#                 return quickSelect(less, k - len(large) - len(equal))
#             else:
#                 return pivot
#         return quickSelect(nums, k)


# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         self.nums = nums
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         for i in range(n // 2 - 1, -1, -1):
#             self.heapify(n, i)
#
#         for i in range(n - 1, n - k - 1, -1):
#             self.nums[0], self.nums[i] = self.nums[i], self.nums[0]
#             self.heapify(i, 0)
#         return self.nums[n - k]
#
#     def heapify(self, n, i):
#         largest = i
#         left = i * 2 + 1
#         right = i * 2 + 2
#
#         if left < n and self.nums[largest] < self.nums[left]:
#             largest = left
#         if right < n and self.nums[largest] < self.nums[right]:
#             largest = right
#
#         if largest != i:
#             self.nums[i], self.nums[largest] = self.nums[largest], self.nums[i]
#             self.heapify(n, largest)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        while k > 0:
            cur = heapq.heappop(nums)
            k -= 1
        return -cur

if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3, 1,1,1,1, -3,-2,-1]

    print(len(nums))
    print(solution.findKthLargest(nums, 3))

