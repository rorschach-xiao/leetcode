class Solution:
    def similarPairs(self, words):
        _D = {}
        ans = 0
        for word in words:
            cur_unique = set()
            for c in word:
                cur_unique.add(c)
            cur_unique = sorted(list(cur_unique))
            cur_unique_str = ''.join(cur_unique)
            if cur_unique_str not in _D:
                _D[cur_unique_str] = 1
            else:
                _D[cur_unique_str] += 1
        for k in _D:
            ans += (_D[k] * (_D[k] - 1)) // 2
        return ans




if __name__ == '__main__':
    solution = Solution()
    words = ["nba","cba","dba"]
    print(solution.similarPairs(words))