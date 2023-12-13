from typing import List


class Solution:

    # Brain Kernighan
    # def countBits(self, n: int) -> List[int]:
    #     ans = []
    #     for i in range(n + 1):
    #         ones = 0
    #         while i:
    #             ones += 1
    #             i &= i - 1
    #         ans.append(ones)
    #     return ans

    # dynamic programming-- highBit
    def countBits(self, n: int) -> List[int]:
        ans = [0 for _ in range(n + 1)]
        highBit = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                highBit = i
            ans[i] = ans[i - highBit] + 1
        return ans