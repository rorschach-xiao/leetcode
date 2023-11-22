# class Solution(object):
#     def myPow(self, x, n):
#         """
#         :type x: float
#         :type n: int
#         :rtype: float
#         """
#         def quickMul(N):
#             if N == 0:
#                 return 1.0
#             y = quickMul(N // 2)
#             return y * y if N % 2 == 0 else y * y * x
#
#         return quickMul(n) if n > 0 else 1.0 / quickMul(-n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        re = self.helper(x, abs(n))
        if n < 0:
            re = 1 / re
        return re

    def helper(self, x, n):
        if n == 0:
            return 1.0
        if n == 1:
            return x
        re = self.helper(x, n // 2)
        re *= re
        if n % 2 == 1:
            re *= x
        return re

if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(2,-2))

