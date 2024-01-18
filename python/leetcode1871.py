class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False for _ in range(n)]
        pre = [0 for _ in range(n)]
        dp[0] = True
        pre[0] = 1
        for i in range(1, n):
            if i >= minJump and s[i] == '0':
                left, right = i - maxJump, i - minJump
                dp[i] = (pre[right] - (0 if left <= 0 else pre[left - 1])) != 0
            pre[i] = pre[i - 1] + int(dp[i])

        return dp[n - 1]