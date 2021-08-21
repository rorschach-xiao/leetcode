class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.result.append([])
        self.nums = sorted(nums)
        self.n = len(nums)
        if self.n == 0:
            return self.result
        for L in range(1, self.n + 1):
            self.helper(0, [], L)
        return self.result

    def helper(self, start, cur_set, cur_len):
        if self.n - start + len(cur_set) < cur_len:
            return
        if len(cur_set) == cur_len:
            self.result.append(list(cur_set))
            return
        cur_len_dict = {}
        for i in range(start, len(self.nums)):
            if self.nums[i] not in cur_len_dict:
                cur_len_dict[self.nums[i]] = 1
            else:
                continue
            cur_set.append(self.nums[i])
            self.helper(i + 1, cur_set, cur_len)
            cur_set.pop(-1)

if __name__ == '__main__':
    solution=Solution()
    nums = [1,2,2]
    print(solution.subsetsWithDup(nums))