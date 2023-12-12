import copy


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        last_line = [0 for _ in range(n + 1)]
        cur_line = [0 for _ in range(n + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    cur_line[j] = last_line[j-1] + 1
                else:
                    cur_line[j] = max(last_line[j], last_line[j-1], cur_line[j-1])
            last_line = copy.deepcopy(cur_line)
        return cur_line[n]