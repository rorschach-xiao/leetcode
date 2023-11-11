from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.k = k
        left, right = 1, n
        self.helper(left, right, [])
        return self.res

    def helper(self, left, right, comb):
        if len(comb) == self.k:
            self.res.append(list(comb))
            return
        for i in range(left, right+1):
            comb.append(i)
            self.helper(i + 1, right, comb)
            comb.pop(-1)

if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))
