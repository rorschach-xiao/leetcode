class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.dfs([], n, n)
        return self.result

    def dfs(self, cur_res, left_n, right_n):
        if left_n < 0 or right_n < 0:
            return

        if left_n == 0 and right_n == 0:
            self.result.append(''.join(cur_res))
            return
        if right_n < left_n:
            return

        cur_res.append('(')
        self.dfs(cur_res, left_n - 1, right_n)
        cur_res.pop(-1)

        cur_res.append(')')
        self.dfs(cur_res, left_n, right_n - 1)
        cur_res.pop(-1)
if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))