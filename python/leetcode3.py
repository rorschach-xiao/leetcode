class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        charSet = {}
        longestLen = 1
        front, behind, n = 0, 0, len(s)
        while (front < n):
            if s[front] in charSet:
                charSet.pop(s[behind])
                behind += 1
                while (s[front] in charSet):
                    charSet.pop(s[behind])
                    behind += 1
            charSet[s[front]] = 1
            front += 1
            longestLen = max(longestLen, front - behind)

        return longestLen