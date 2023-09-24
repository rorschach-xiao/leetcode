class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        L = [0] * n
        R = [0] * n
        for i in range(n):
            if i == 0:
                L[i] = 1
                R[n-1-i] = 1
            else:
                L[i] = L[i-1] * nums[i - 1]
                R[n-1-i] = R[n-i] * nums[n-i]
        for i in range(n):
            result[i] = L[i] * R[i]
        return result