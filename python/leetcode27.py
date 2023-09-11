class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        right = len(nums)
        left = 0
        while(left < right):
            if nums[left] == val:
                while(left < right - 1 and nums[right - 1] == val):
                    right -= 1
                self.swap(nums, right - 1, left)
                right -= 1
            else:
                left += 1

        print(nums)
        return left

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement([4, 5], 5))
    print(solution.removeElement([2], 2))
    print(solution.removeElement([0,1,2,2,3,0,4,2], 2))
