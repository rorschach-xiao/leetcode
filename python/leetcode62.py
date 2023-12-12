class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        last_line = [1 for _ in range(n)]
        cur_line = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                cur_line[j] = last_line[j] + cur_line[j-1]
            last_line = cur_line
        return cur_line[n-1]