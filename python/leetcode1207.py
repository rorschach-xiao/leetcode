from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numDict = {}
        for i in arr:
            if i not in numDict:
                numDict[i] = 1
            else:
                numDict[i] += 1
        return len(numDict) == len(set(numDict.values()))