from typing import List


class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     re = 0
    #     for i in range(32):
    #         n = sum([(num >> i) & 1 for num in nums])
    #         if n % 3 == 1:
    #             if i == 31:
    #                 re -= (1 << i)
    #             else:
    #                 re |= (1 << i)
    #     return re

    def singleNumber(self, nums: List[int]) -> int:
        b = a = 0
        for num in nums:
            b = ~a & (b ^ num)
            a = ~b & (a ^ num)
        return b

