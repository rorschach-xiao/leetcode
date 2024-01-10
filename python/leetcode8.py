class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        ans, MIN, MAX = 0, -2 ** 31, 2 ** 31 - 1
        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            i += 1
        s = s[i:]
        sign = None
        digit_flag = False
        for i, c in enumerate(s):
            if (c == '-' or c == '+') and not sign and not digit_flag:
                sign = 1 if c == '+' else -1
            elif c.isdigit():
                ans = ans * 10 + int(c)
                digit_flag = True
            else:
                break
        if sign:
            ans = sign * ans
        return min(max(ans, MIN), MAX)