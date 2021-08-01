class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        self.len = len(s)
        if self.len <= 1:
            return s
        dp = [[False for _ in range(self.len)] for _ in range(self.len)]
        # init dp
        max_len = 1
        res = s[0]

        for L in range(1, self.len+1):
            for i in range(self.len - L + 1):
                j = i + L - 1
                if L == 1:
                    dp[i][j] = True
                    continue
                if L == 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        if L > max_len:
                            res = s[i:j + 1]
                            max_len = L
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if L > max_len:
                            res = s[i:j + 1]
                            max_len = L
        return res
if __name__ == '__main__':
    solution = Solution()
    s = 'ccc'
    print(solution.longestPalindrome(s))