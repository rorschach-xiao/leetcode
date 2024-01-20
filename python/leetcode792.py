from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n, m = len(s), len(words)
        pointers = {}
        for i, w in enumerate(words):
            if w[0] not in pointers:
                pointers[w[0]] = [(i, 0)]
            else:
                pointers[w[0]].append((i, 0))
        ans = 0
        for c in s:
            if c not in pointers:
                continue
            else:
                q = pointers[c]
                pointers[c] = []
                for i, j in q:
                    if j == len(words[i]) - 1:
                        ans += 1
                    else:
                        j += 1
                        if words[i][j] not in pointers:
                            pointers[words[i][j]] = [(i, j)]
                        else:
                            pointers[words[i][j]].append((i, j))
        return ans