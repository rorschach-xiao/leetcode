class Solution(object):
    # def rotate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: None Do not return anything, modify nums in-place instead.
    #     """
    #     for i in range(k):
    #         nums.insert(0, nums[- 1])
    #         nums.pop(-1)
    #     print(nums)

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        print(nums)

    def reverse(self, nums, i, j):
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1

if __name__ == '__main__':
    solution = Solution()
    solution.rotate([1,2,3,4,5,6,7], 3)
