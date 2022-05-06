class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm.keys():
                if i - hm[nums[i]] <= k:
                    return True
            hm[nums[i]] = i

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))
