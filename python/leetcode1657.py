class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1 = len(word1)
        n2 = len(word2)
        if n1 != n2:
            return False
        d1 = {}
        d2 = {}
        for i in range(n1):
            if word1[i] not in d1:
                d1[word1[i]] = 1
            else:
                d1[word1[i]] += 1
            if word2[i] not in d2:
                d2[word2[i]] = 1
            else:
                d2[word2[i]] += 1
        k1 = d1.keys()
        k2 = d2.keys()
        v1 = sorted(d1.values())
        v2 = sorted(d2.values())
        return v1 == v2 and k1 == k2