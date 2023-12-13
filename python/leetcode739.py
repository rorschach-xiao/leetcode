from typing import List


class Solution:

    # brute force
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = []
        for i in range(n):
            wait = 0
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    wait = j - i
                    break
            ans.append(wait)

        return ans

    # monotonic stack
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0 for _ in range(n)]
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                topIdx = stack.pop()
                ans[topIdx] = i - topIdx
            stack.append(i)

        return ans

