import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1
        heap = []
        heapq.heapify(heap)
        for key, val in cnt.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        for i in range(k):
            ans.insert(0, heapq.heappop(heap)[1])
        return ans