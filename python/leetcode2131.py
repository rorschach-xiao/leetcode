class Solution:
    def longestPalindrome(self, words) -> int:
        _D = {}
        for word in words:
            if word not in _D:
                _D[word] = 1
            else:
                _D[word] += 1
        ans = 0
        repeat_flag = 0
        for s in _D:
            if s[0] == s[1]:
                if _D[s] % 2 == 1 and repeat_flag == 0:
                    ans += _D[s] * 2
                    repeat_flag = 1
                elif _D[s] > 1:
                    ans += _D[s] // 2 * 4
            else:
                if s[::-1] in _D:
                    ans += min(_D[s], _D[s[::-1]]) * 2
        return ans

if __name__ == '__main__':
    solution = Solution()
    words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
    print(solution.longestPalindrome(words))