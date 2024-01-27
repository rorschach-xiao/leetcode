import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        minHeap = [2, 3, 5]
        uglySet = set()
        uglySet.add(1)
        i = 2
        while i <= n:
            cur = heapq.heappop(minHeap)
            uglySet.add(cur)
            if cur * 2 not in uglySet:
                heapq.heappush(minHeap, cur * 2)
                uglySet.add(cur * 2)
            if cur * 3 not in uglySet:
                heapq.heappush(minHeap, cur * 3)
                uglySet.add(cur * 3)
            if cur * 5 not in uglySet:
                heapq.heappush(minHeap, cur * 5)
                uglySet.add(cur * 5)
            i += 1
        return cur