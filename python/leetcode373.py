import heapq
from typing import List

#
# class ModifiedMinHeap():
#     def __init__(self):
#         self.heap = []
#         self.indexes = []
#
#     def heappush(self, value, indexes):
#         self.heap.append(value)
#         self.indexes.append(indexes)
#         self.__heapifyUp(len(self.heap) - 1)
#
#     def heappop(self):
#         self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
#         self.indexes[0], self.indexes[-1] = self.indexes[-1], self.indexes[0]
#         self.heap.pop()
#         maxValueIndexes = self.indexes.pop()
#         self.__heapifyDown(0)
#         return maxValueIndexes
#
#     def __heapifyUp(self, index):
#         while index > 0:
#             parent = (index - 1) // 2
#             if parent != index and self.heap[index] < self.heap[parent]:
#                 self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
#                 self.indexes[parent], self.indexes[index] = self.indexes[index], self.indexes[parent]
#                 index = parent
#             else:
#                 break
#
#     def __heapifyDown(self, index):
#         n = len(self.heap)
#         while index * 2 + 1 < n:
#             smallest = index
#             left = index * 2 + 1
#             right = index * 2 + 2
#
#             if self.heap[left] < self.heap[smallest]:
#                 smallest = left
#             if right < n and self.heap[right] < self.heap[smallest]:
#                 smallest = right
#
#             if smallest != index:
#                 self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
#                 self.indexes[index], self.indexes[smallest] = self.indexes[smallest], self.indexes[index]
#                 index = smallest
#             else:
#                 break
#     def __len__(self):
#         return len(self.heap)
#
# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         m, n = len(nums1), len(nums2)
#         pq = ModifiedMinHeap()
#         res = []
#         for i in range(m):
#             pq.heappush(nums1[i] + nums2[0], (i, 0))
#         while k > 0 and len(pq) > 0:
#             id1, id2 = pq.heappop()
#             res.append([nums1[id1], nums2[id2]])
#             if id2 + 1 < n:
#                 pq.heappush(nums1[id1] + nums2[id2 + 1], (id1, id2 + 1))
#             k -= 1
#         return res


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        minHeap = []
        res = []
        for i in range(m):
            heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))
        while k > 0 and len(minHeap) > 0:
            _, id1, id2 = heapq.heappop(minHeap)
            res.append([nums1[id1], nums2[id2]])
            if id2 + 1 < n:
                heapq.heappush(minHeap, (nums1[id1] + nums2[id2 + 1], id1, id2 + 1))
            k -= 1
        return res
