from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = MinHeap()
        for point in points:
            minheap.heappush(point)
        ans = []
        for i in range(k):
            ans.append(minheap.heappop())
        return ans


class MinHeap:
    def __init__(self):
        self.minheap = []
        self.heapsize = 0

    def heappop(self):
        if self.heapsize == 0:
            return None
        self.minheap[0], self.minheap[-1] = self.minheap[-1], self.minheap[0]
        p = self.minheap.pop(-1)
        self.heapsize -= 1
        self.__heapifyDown(self.heapsize, 0)
        return p

    def heappush(self, point):
        self.minheap.append(point)
        self.heapsize += 1
        self.__heapifyUp(self.heapsize - 1)

    def __comp(self, p1, p2):
        if p1[0] ** 2 + p1[1] ** 2 < p2[0] ** 2 + p2[1] ** 2:
            return -1
        return 1

    def __heapifyUp(self, i):
        largest = i
        parent = (i - 1) // 2
        if parent >= 0 and self.__comp(self.minheap[parent], self.minheap[i]) > 0:
            largest = parent
        if largest != i:
            self.minheap[largest], self.minheap[i] = self.minheap[i], self.minheap[largest]
            self.__heapifyUp(largest)

    def __heapifyDown(self, n, i):
        smallest = i
        left, right = i * 2 + 1, i * 2 + 2
        if left < n and self.__comp(self.minheap[smallest], self.minheap[left]) > 0:
            smallest = left
        if right < n and self.__comp(self.minheap[smallest], self.minheap[right]) > 0:
            smallest = right

        if smallest != i:
            self.minheap[smallest], self.minheap[i] = self.minheap[i], self.minheap[smallest]
            self.__heapifyDown(n, smallest)