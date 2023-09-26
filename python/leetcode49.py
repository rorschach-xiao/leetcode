import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagramDict = collections.defaultdict(list)
        for str in strs:
            transStr = self.__strTransform(str)
            if transStr in anagramDict:
                anagramDict[transStr].append(str)
            else:
                anagramDict[transStr] = [str]
        return list(anagramDict.values())

    def __strTransform(self, str):
        if len(str) == 0:
            return str
        _dict = [0] * 26
        for c in str:
            _dict[ord(c) - ord("a")] += 1

        return tuple(_dict)

if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

