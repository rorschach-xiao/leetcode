import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        minheap = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(minheap)

        for i in range(k - 1):
            _, r, c = heapq.heappop(minheap)
            if c + 1 < n:
                heapq.heappush(minheap, (matrix[r][c + 1], r, c + 1))
        return heapq.heappop(minheap)[0]