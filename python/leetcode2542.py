from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums3 = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        minheap = []
        heapq.heapify(minheap)
        # minheap = minHeap()
        cur_sum = 0
        res = float("-inf")
        for i, e in enumerate(nums3):
            n1, n2 = e
            if i < k:
                heapq.heappush(minheap, n1)
                # minheap.push(n1)
                cur_sum += n1
            else:
                # cur_sum -= minheap.pop()
                cur_sum -= heapq.heappop(minheap)
                # minheap.push(n1)
                heapq.heappush(minheap, n1)
                cur_sum += n1

            if i >= k-1:
                cur_score = cur_sum * n2
                res = max(res, cur_score)
        return res


class minHeap:
    def __init__(self):
        self.minheap = []
        self.heapsize = 0

    def push(self, num):
        self.minheap.append(num)
        self.heapsize += 1
        self.heapifyUp(self.heapsize - 1)

    def pop(self):
        self.minheap[0], self.minheap[-1] = self.minheap[-1], self.minheap[0]
        smallest = self.minheap.pop()
        self.heapsize -= 1
        self.heapifyDown(self.heapsize, 0)
        return smallest

    def heapifyUp(self, i):
        parent = (i - 1) // 2
        cur = i
        if parent >= 0 and self.minheap[parent] > self.minheap[cur]:
            cur = parent

        if cur != i:
            self.minheap[i], self.minheap[cur] = self.minheap[cur], self.minheap[i]
            self.heapifyUp(cur)

    def heapifyDown(self, n, i):
        smallest = i
        left, right = i * 2 + 1, i * 2 + 2

        if left < n and self.minheap[left] < self.minheap[smallest]:
            smallest = left
        if right < n and self.minheap[right] < self.minheap[smallest]:
            smallest = right

        if smallest != i:
            self.minheap[i], self.minheap[smallest] = self.minheap[smallest], self.minheap[i]
            self.heapifyDown(n, smallest)



if __name__ == '__main__':
    solution = Solution()
    nums1 = [1,3,3,2]
    nums2 = [2,1,3,4]
    k = 3
    solution.maxScore(nums1, nums2, k)