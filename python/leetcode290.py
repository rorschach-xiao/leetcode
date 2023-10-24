class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        char2word = {}
        word2char = {}
        n = len(pattern)

        for i in range(n):
            if pattern[i] not in char2word and words[i] not in word2char:
                char2word[pattern[i]] = words[i]
                word2char[words[i]] = pattern[i]
            elif pattern[i] in char2word and char2word[pattern[i]] != words[i]:
                return False
            elif words[i] in word2char and word2char[words[i]] != pattern[i]:
                return False
        return True