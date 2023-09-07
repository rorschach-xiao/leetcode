class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        if len(nums) < 3 or nums[-1] < 0 or nums[0] > 0:
            return []
        self.result = []
        self.dict = {}
        # hashmap
        for i, n in enumerate(nums):
            if n not in self.dict:
                self.dict[n] = [i]
            else:
                self.dict[n] += [i]

        R = len(nums) - 1
        while (R > 0):
            L = 0
            while (L < R):
                if -(nums[R] + nums[L]) in self.dict:
                    for idx in self.dict[-(nums[R] + nums[L])]:
                        if idx > L and idx < R:
                            self.result.append([nums[L], nums[R], nums[idx]])
                            break
                    while (L < R and nums[L] == nums[L + 1]):
                        L += 1
                L += 1
            while (0 < R and nums[R] == nums[R - 1]):
                R -= 1
            R -= 1

        return self.result
if __name__ == '__main__':
    solution = Solution()
    nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    print(solution.threeSum(nums))