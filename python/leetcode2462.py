import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left, right = candidates - 1, n - candidates
        minHeap = []
        heapq.heapify(minHeap)
        # build index map
        for i in range(n):
            if  i <= left or i >= right:
                heapq.heappush(minHeap, (costs[i], i))
        res = 0
        while k > 0:
            smallest, idx = heapq.heappop(minHeap)
            if idx <= left and left + 1 < right:
                left += 1
                heapq.heappush(minHeap,(costs[left], left))
            elif idx >= right and right - 1 > left:
                right -= 1
                heapq.heappush(minHeap,(costs[right], right))
            res += smallest
            k -= 1
        return res