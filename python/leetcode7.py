class Solution:
    def reverse(self, x: int) -> int:
        ans, MIN, MAX = 0, -2 ** 31, 2**31 - 1
        flag = x > 0
        x = abs(x)
        while x:
            ans = ans * 10 + x % 10
            x //= 10
        if ans < MIN or ans > MAX:
            return 0
        elif flag:
            return ans
        else:
            return -ans