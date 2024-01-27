import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        maxHeap = []
        if a: heapq.heappush(maxHeap, (-a, 'a'))
        if b: heapq.heappush(maxHeap, (-b, 'b'))
        if c: heapq.heappush(maxHeap, (-c, 'c'))

        while True:
            nextHeap = []
            hasNext = False
            while maxHeap:
                n, ch = heapq.heappop(maxHeap)
                if len(ans) >= 2 and ans[-1] == ch and ans[-2] == ch:
                    heapq.heappush(nextHeap, (n, ch))
                    continue
                hasNext = True
                n = -n
                ans.append(ch)
                if n - 1 != 0:
                    heapq.heappush(nextHeap, (1-n, ch))
                break
            maxHeap = nextHeap + maxHeap
            heapq.heapify(maxHeap)
            if not hasNext:
                break

        return ''.join(ans)

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestDiverseString(1, 1, 7))