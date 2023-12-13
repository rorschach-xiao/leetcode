class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flip_cnt = 0
        while a or b or c:
            aBit = a & 1
            bBit = b & 1
            cBit = c & 1
            if aBit | bBit != cBit:
                if cBit == 1 and aBit | bBit == 0:
                    flip_cnt += 1
                else:
                    flip_cnt += aBit + bBit

            a >>= 1
            b >>= 1
            c >>= 1
        return flip_cnt