from typing import List


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A = sorted(A)
        n = len(A)
        if n <= 1:
            return -1
        left, right = 0, n - 1
        res = float("-inf")
        while left < right - 1:
            if A[left] + A[right] >= K:
                right -= 1
            else:
                res = max(res, A[left] + A[right])
                left += 1
        return -1 if res == float('-inf') else res

if __name__ == '__main__':
    solution = Solution()
    # A = [34,23,1,24, 75,33,54,8]
    A = [10, 20, 30]
    K = 15
    print(solution.twoSumLessThanK(A, K))
