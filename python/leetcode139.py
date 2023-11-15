from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n)]
        wordDict = set(wordDict)
        for i in range(n):
            if s[:i + 1] in wordDict:
                dp[i] = True
            else:
                for word in wordDict:
                    l = len(word)
                    j = i - l
                    if s[j + 1:i + 1] == word and dp[j]:
                        dp[i] = True
                        break
        return dp[n - 1]


if __name__ == '__main__':
    solution = Solution()
    s = "leetcode"
    wordDict = ['leet', 'code']
    print(solution.wordBreak(s, wordDict))
