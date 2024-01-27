import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = {}
        for c in s:
            if c not in cnt:
                cnt[c] = 1
            else:
                cnt[c] += 1
        ans = []
        maxHeap = []
        for ch, n in cnt.items():
            heapq.heappush(maxHeap, (-n, ch))

        while maxHeap:
            n, ch = heapq.heappop(maxHeap)
            n = -n
            ans.append(ch * n)
        return ''.join(ans)