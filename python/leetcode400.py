class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        while length * 9 * (10 ** (length - 1)) < n:
            n -= length * 9 * (10 ** (length - 1))
            length += 1
        s = 10 ** (length - 1)
        x = n // length - 1 + s
        n -= (x - s + 1) * length
        if n == 0:
            return x % 10
        else:
            return ((x + 1) // (10 ** (length - n))) % 10