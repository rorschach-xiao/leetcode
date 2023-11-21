class Solution:
    def reverseBits(self, n: int) -> int:
        i = 1
        rev = 0
        while(n > 0 and i <= 32):
            rev |= (n & 1) << (32 - i)
            n = n >> 1
            i += 1
        return rev