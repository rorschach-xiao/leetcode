from typing import List


# class Solution(object):
    # def moveZeroes(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: None Do not return anything, modify nums in-place instead.
    #     """
    #     if len(nums) <= 1:
    #         return;
    #     pointer = 0
    #     numOfZeros = 0
    #     while pointer < len(nums) - numOfZeros:
    #         if nums[pointer] == 0:
    #             nums.pop(pointer)
    #             nums.append(0)
    #             numOfZeros += 1
    #         else:
    #             pointer += 1

    # def moveZeroes(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: None Do not return anything, modify nums in-place instead.
    #     """
    #     if len(nums) <= 1:
    #         return;
    #     n = len(nums)
    #     numOfNonZeros = 0
    #     for i in range(n):
    #         if nums[i] != 0:
    #             nums[numOfNonZeros] = nums[i]
    #             numOfNonZeros+=1
    #     for j in range(numOfNonZeros, n):
    #         nums[j] = 0

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write, read = 0, 0
        n = len(nums)
        while read < n:
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
            read += 1




if __name__ == '__main__':
    solution = Solution()
    nums = [0,1,0,0,10,2]
    solution.moveZeroes(nums)
    print(nums)