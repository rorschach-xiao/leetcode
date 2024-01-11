class Solution:
    def countSubstrings(self, s: str) -> int:
        self.s = s
        self.ans = 0
        n = len(s)
        for i in range(n):
            self.expand(i, i)
            if i < n - 1:
                self.expand(i, i + 1)
        return self.ans

    def expand(self, left, right):
        while left >= 0 and right < len(self.s):
            if self.s[left] == self.s[right]:
                self.ans += 1
                left -= 1
                right += 1
            else:
                break