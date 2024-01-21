class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp_zero = [0 for _ in range(n)]
        dp_one = [0 for _ in range(n)]
        if s[0] == '0':
            dp_one[0] = 1
        else:
            dp_zero[0] = 1
        for i in range(1, n):
            if s[i] == '0':
                dp_one[i] = min(dp_zero[i-1], dp_one[i-1]) + 1
                dp_zero[i] = dp_zero[i-1]
            else:
                dp_one[i] = min(dp_zero[i-1], dp_one[i-1])
                dp_zero[i] = dp_zero[i-1] + 1
        return min(dp_one[n-1], dp_zero[n-1])