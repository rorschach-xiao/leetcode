class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        right_p = len(nums) - 1
        smaller_p = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                smaller_p = i - 1
                left_p = i
                break
        if smaller_p is not None:
            for i in range(len(nums) - 1, 0, -1):
                if nums[i] > nums[smaller_p]:
                    larger_p = i
                    break
            self.swap(nums, larger_p, smaller_p)
        else:
            left_p = 0

        while (left_p < right_p):
            self.swap(nums, left_p, right_p)
            left_p += 1
            right_p -= 1

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,2]
    solution.nextPermutation(nums)
    print(nums)