from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        if n == 1:
           return 1
        words = sorted(words, key = lambda x: len(x))
        cnt = {}
        ans = 0
        for word in words:
            cnt[word] = 1
            for j in range(len(word)):
                prev_word = word[:j] + word[j + 1:]
                if prev_word in cnt:
                    cnt[word] = max(cnt[word], cnt[prev_word] + 1)
            ans = max(ans, cnt[word])
        return ans