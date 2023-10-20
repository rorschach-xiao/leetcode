from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        wordNum = len(words)
        n = len(s)
        ans = []
        # construct dictionary
        wordsDict = {}
        for word in words:
            if word not in wordsDict:
                wordsDict[word] = 1
            else:
                wordsDict[word] += 1

        for i in range(n - wordLen * wordNum + 1):
            wordsDictCurrent = {x : wordsDict[x] for x in wordsDict}
            p = i
            while p + wordLen <= n and s[p: p + wordLen] in wordsDictCurrent:
                wordsDictCurrent[s[p: p + wordLen]] -= 1
                if wordsDictCurrent[s[p: p + wordLen]] == 0:
                    wordsDictCurrent.pop(s[p: p + wordLen])
                p = p + wordLen
            if len(wordsDictCurrent) == 0:
                ans.append(i)
        return ans