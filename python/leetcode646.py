from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: x[1])
        n = len(pairs)
        if n == 1:
            return 1
        ans = 1
        cur = pairs[0]
        for i in range(1, n):
            if pairs[i][0] > cur[1]:
                cur = pairs[i]
                ans += 1

        return ans