from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)

        def binarySearch(spell, success):
            nonlocal potions
            if potions[-1] * spell < success:
                return 0
            left, right = 0, len(potions) - 1
            while left < right:
                mid = (left + right) // 2
                if potions[mid] * spell >= success:
                    right = mid
                elif potions[mid] * spell < success:
                    left = mid + 1
            return len(potions) - left
        ans = []
        for spell in spells:
            ans.append(binarySearch(spell, success))
        return ans