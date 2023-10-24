class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numDict = {}
        n = len(nums)
        minDistance = max(k + 1, n)
        if n == 1:
            return False
        for i, num in enumerate(nums):
            if num in numDict:
                minDistance = min(minDistance, i - numDict[num])
                if minDistance <= k:
                    return True
            numDict[num] = i
        return False