# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#
#         self.len = len(s)
#         if self.len <= 1:
#             return s
#         dp = [[False for _ in range(self.len)] for _ in range(self.len)]
#         # init dp
#         max_len = 1
#         res = s[0]
#
#         for L in range(1, self.len+1):
#             for i in range(self.len - L + 1):
#                 j = i + L - 1
#                 if L == 1:
#                     dp[i][j] = True
#                     continue
#                 if L == 2:
#                     if s[i] == s[j]:
#                         dp[i][j] = True
#                         if L > max_len:
#                             res = s[i:j + 1]
#                             max_len = L
#                 else:
#                     if s[i] == s[j] and dp[i + 1][j - 1]:
#                         dp[i][j] = True
#                         if L > max_len:
#                             res = s[i:j + 1]
#                             max_len = L
#         return res

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n == 1:
#             return s
#         dp = [[False for _ in range(n)] for _ in range(n)]
#         re = ""
#
#         for L in range(1, n + 1):
#             for i in range(0, n - L + 1):
#                 j = i + L - 1
#                 if L == 1 or L == 2 and s[i] == s[j]:
#                     dp[i][j] = True
#                 elif s[i] == s[j]:
#                     dp[i][j] = dp[i + 1][j - 1]
#                 if dp[i][j] and L > len(re):
#                     re = s[i: j + 1]
#         return re

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        start, end = 0, 0
        for i in range(n):
            left1, right1 = self.expand(i, i, s)
            left2, right2 = self.expand(i, i + 1, s)

            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

    def expand(self, start, end, s):
        while (start >= 0 and end <= len(s) - 1 and s[start] == s[end]):
            start -= 1
            end += 1
        return start + 1, end - 1




if __name__ == '__main__':
    solution = Solution()
    s = 'aaaa'
    print(solution.longestPalindrome(s))