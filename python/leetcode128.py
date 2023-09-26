class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        maxLen = 0
        _dict = {}
        for num in nums:
            if num not in _dict:
                left = _dict.get(num - 1, 0)
                right = _dict.get(num + 1, 0)
                currentLen = left + right + 1
                if (currentLen > maxLen):
                    maxLen = currentLen
                _dict[num] = currentLen
                _dict[num - left] = currentLen
                _dict[num + right] = currentLen

        return maxLen

if __name__ == "__main__" :
    solution = Solution()
    print(solution.longestConsecutive([90, 1, 100, 3, 2, 4]))
