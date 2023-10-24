class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphaDict = {}
        for c in magazine:
            if c not in alphaDict:
                alphaDict[c] = 1
            else:
                alphaDict[c] += 1

        for c in ransomNote:
            if c not in alphaDict or alphaDict[c] == 0:
                return False
            else:
                alphaDict[c] -= 1
        return True