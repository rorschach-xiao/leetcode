class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        pre = 1
        prePre = 1
        for i in range(2, n + 1):
            res = pre + prePre
            prePre = pre
            pre = res

        return res