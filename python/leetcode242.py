class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alphaDict = {}

        for c in s:
            if c not in alphaDict:
                alphaDict[c] = 1
            else:
                alphaDict[c] += 1

        for c in t:
            if c not in alphaDict:
                return False
            elif alphaDict[c] == 0:
                return False
            else:
                alphaDict[c] -= 1
        return True