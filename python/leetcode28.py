# brutal force
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         n, m = len(haystack), len(needle)
#         if m > n:
#             return -1
#         for i in range(n):
#             for j in range(m):
#                 if i + j >= n:
#                     return -1
#                 if needle[j] != haystack[i + j]:
#                     break
#             if j == m - 1 and needle[j] == haystack[i + j]:
#                 return i
#         return -1

# KMP algorithm
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m > n:
            return -1
        lps = [0] * m
        pre = 0
        # initialize lps
        for i in range(1, m):
            while (pre > 0 and needle[i] != needle[pre]):
                pre = lps[pre - 1]

            if (needle[pre] == needle[i]):
                pre += 1
                lps[i] = pre

        # main KMP algorithm
        j = 0  # pointer to needle
        for i in range(n):  # pointer to haystack
            while (j > 0 and needle[j] != haystack[i]):
                j = lps[j - 1]
            if (needle[j] == haystack[i]):
                j += 1
            if j == m:
                return i - j + 1
        return -1