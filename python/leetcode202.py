class Solution:
    def isHappy(self, n: int) -> bool:
        _set = set([])
        s = n
        while (s not in _set):
            _set.add(s)
            s = self.getSumOfSquares(s)
        return 1 in _set

    def getSumOfSquares(self, n: int) -> int:
        re = 0
        while (n > 0):
            re += (n % 10) ** 2
            n //= 10
        return re

if __name__ == '__main__' :
    solution = Solution()
    print(solution.isHappy(19))