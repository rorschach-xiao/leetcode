from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flower_pos = -2
        L = len(flowerbed)
        for i in range(L):
            if flowerbed[i] == 1:
                flower_pos = i
            else:
                if flower_pos < i - 1 and (i + 1 < L and flowerbed[i + 1] == 0 or i + 1 == L):
                    n -= 1
                    flower_pos = i
            if n <= 0:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    solution.canPlaceFlowers([0,0,1,0,0], 1)