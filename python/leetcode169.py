class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        majority = nums[0]
        vote = 1
        for i in range(1, len(nums)):
            if nums[i] != majority:
                vote -= 1
                if vote == 0:
                    majority = nums[i]
                    vote = 1
            else:
                vote += 1
        return majority

if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement())