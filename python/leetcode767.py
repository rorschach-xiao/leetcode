import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = []
        cnt = {}
        for c in s:
            if c not in cnt:
                cnt[c] = 1
            else:
                cnt[c] += 1

        for k, v in cnt.items():
            heapq.heappush(maxHeap, (-v, k))

        ans = []
        while True:
            nextHeap = []
            hasNext = False
            while maxHeap:
                n, ch = heapq.heappop(maxHeap)
                if len(ans) >= 1 and ans[-1] == ch:
                    heapq.heappush(nextHeap, (n, ch))
                    continue
                hasNext = True
                ans.append(ch)
                n = -n
                n -= 1
                if n > 0:
                    heapq.heappush(nextHeap, (-n, ch))
                break
            maxHeap = nextHeap + maxHeap
            heapq.heapify(maxHeap)
            if not hasNext:
                break
        if len(ans) != len(s):
            return ''
        return ''.join(ans)