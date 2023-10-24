class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        alphaDict = {}
        alphaDict_inv = {}
        sub = ""
        for c1, c2 in zip(s, t):
            if c1 not in alphaDict and c2 not in alphaDict_inv:
                alphaDict[c1] = c2
                alphaDict_inv[c2] = c1
            elif ((c1 in alphaDict and alphaDict[c1] != c2) or
                  (c2 in alphaDict_inv and alphaDict_inv[c2] != c1)):
                return False

        return True
