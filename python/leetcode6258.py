class Solution:
    def longestSquareStreak(self, nums):
        if len(nums) < 2:
            return -1
        nums = sorted(nums)
        _Dict = {}
        for num in nums:
            _Dict[num] = 1

        ans = -1
        for num in nums:
            if num * num not in _Dict:
                continue
            else:
                _Dict[num * num] = _Dict[num] + 1
                ans = max(_Dict[num * num], ans)
        return ans

if __name__ == '__main__':
    solution = Solution()
    nums = [4, 3, 6, 16, 8, 2]
    print(solution.longestSquareStreak(nums))
