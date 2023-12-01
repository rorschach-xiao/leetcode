from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        ans = []
        nums1_diff_nums2 = []
        for num in set1:
            if num not in set2:
                nums1_diff_nums2.append(num)
        ans.append(nums1_diff_nums2)
        nums2_diff_nums1 = []
        for num in set2:
            if num not in set1:
                nums2_diff_nums1.append(num)
        ans.append(nums2_diff_nums1)
        return ans