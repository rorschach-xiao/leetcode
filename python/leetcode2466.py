class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0 for _ in range(high + 1)]
        dp[0] = 1
        ans = 0
        for i in range(1, high + 1):
            if i - one >= 0:
                dp[i] += dp[i-one]
            if i - zero >= 0:
                dp[i] += dp[i-zero]
            if i >= low:
                ans += dp[i]
        return ans % (10 ** 9 + 7)
