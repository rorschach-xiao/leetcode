class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        farest_jump = 0
        for i in range(n):
            if i > farest_jump:
                break
            farest_jump = max(nums[i] + i, farest_jump)

        if farest_jump < n - 1:
            return False
        return True
if __name__ == '__main__':
    solution = Solution()
    print(solution.canJump([3,2,1,0,4]))