from typing import List


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        pre = [0 for _ in range(n + 1)]
        left, right, ans = 0, 0, 0
        while right < n:
            pre[right + 1] = max(pre[right], right - left + 1)
            ans = max(ans, right - left + 1 + pre[left])
            right += 1
            while right < n and prizePositions[right] - prizePositions[left] > k:
                left += 1
        return ans