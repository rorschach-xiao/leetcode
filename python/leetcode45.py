class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jump = 0
        start = 0
        end = 1
        n = len(nums)
        while end < n:
            maxPos = 0
            for i in range(start, end):
                if nums[i] + i > maxPos:
                    maxPos = nums[i] + i
            start = end
            end = maxPos + 1
            jump += 1
        return jump

if __name__ == '__main__':
    solution = Solution()
    print(solution.jump([1,2,3]))