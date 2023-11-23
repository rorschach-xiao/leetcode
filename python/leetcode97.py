class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if len(s1) + len(s2) != len(s3):
            return False
        pre = [False for _ in range(n2 + 1)]
        dp = [False for _ in range(n2 + 1)]
        dp[0] = True
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                p = i + j - 1
                if i > 0:
                    dp[j] |= pre[j] and s1[i - 1] == s3[p]
                if j > 0:
                    dp[j] |= dp[j-1] and s2[j - 1] == s3[p]
                pre[j] = dp[j]
            if i != n1:
                dp = [False for _ in range(n2 + 1)]
        return dp[n2]

if __name__ == '__main__':
    solution = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(solution.isInterleave(s1, s2, s3))