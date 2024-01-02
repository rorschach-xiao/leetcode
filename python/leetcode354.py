from functools import cache
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n == 1:
            return 1
        envelopes = sorted(envelopes, key=lambda x: -x[0])
        ans = float('-inf')

        @cache
        def dfs(i, w, h, num):
            nonlocal ans
            if num + n - i <= ans:
                return
            ans = max(ans, num)
            for j in range(i, n):
                if envelopes[j][0] < w and envelopes[j][1] < h:
                    dfs(j + 1, envelopes[j][0], envelopes[j][1], num + 1)
                if num + n - j - 1 <= ans:
                    break

        dfs(0, float('inf'), float('inf'), 0)
        return ans