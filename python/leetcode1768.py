class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        re = ""
        p1, p2 = 0, 0
        n1, n2 = len(word1), len(word2)
        while p1 < n1 or p2 < n2:
            if p1 < n1:
                re += word1[p1]
                p1 += 1
            if p2 < n2:
                re += word2[p2]
                p2 += 1

        return re