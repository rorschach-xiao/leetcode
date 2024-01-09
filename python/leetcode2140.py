from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        if n == 1:
            return questions[0][0]
        dp = [0 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], questions[i][0] + dp[min(n, i + questions[i][1] + 1)])
        return dp[0]
