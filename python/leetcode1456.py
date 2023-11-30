class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        head = 0
        n = len(s)
        maxNum = 0
        curNum = 0
        vowel = {"a", "e", "i", "o", "u"}
        for i in range(n):
            if s[i] in vowel:
                curNum += 1
            if i >= k:
                if s[head] in vowel:
                    curNum -= 1
                head += 1
            maxNum = max(maxNum, curNum)
        return maxNum