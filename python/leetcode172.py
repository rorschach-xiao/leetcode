class Solution:
    # def trailingZeroes(self, n: int) -> int:
    #     cnt_5 = 0
    #     for i in range(5, n + 1, 5):
    #         temp = i
    #         while temp % 5 == 0:
    #             cnt_5 += 1
    #             temp //= 5
    #
    #     return cnt_5

    def trailingZeroes(self, n: int) -> int:
        cnt_5 = 0
        p = 5
        while n // p > 0:
            cnt_5 += n // p
            p *= 5
        return cnt_5
