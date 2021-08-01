class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.len = len(nums)
        self.nums = nums
        self.res = []
        used = [False] * self.len
        path = []
        self.dfs(0, path, used)
        return self.res

    def dfs(self, depth, path, used):
        if depth == self.len:
            self.res.append(list(path))
        for i, num in enumerate(self.nums):
            if used[i] == False:
                path.append(num)
                used[i] = True
                self.dfs(depth + 1, path, used)
                used[i] = False
                path.pop(-1)
if __name__ == '__main__':
    solution=Solution()
    nums = [1,2,3]
    print(solution.permute(nums))