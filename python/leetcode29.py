class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        if dividend == 0: return 0
        if divisor == 1: return dividend
        if divisor == -1:
            if dividend == INT_MIN:
                return INT_MAX
            else:
                return -dividend
        sign = 1
        if dividend < 0 < divisor or dividend > 0 > divisor:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = self.quickDiv(dividend, divisor)
        if sign < 0:
            return -res
        else:
            return res if res < INT_MAX else INT_MAX

    def quickDiv(self, x, N):
        if x < N:
            return 0
        current_divisor = N
        result = 1
        while (True):
            if current_divisor + current_divisor > x:
                break
            current_divisor += current_divisor
            result += result

        return result + self.quickDiv(x - current_divisor, N)

if __name__ == '__main__':
    solution = Solution()
    print(solution.divide(1000,10))
