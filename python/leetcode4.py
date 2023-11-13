from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1, p2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        k = (n1 + n2 + 1) // 2
        isOdd = ((n1 + n2) % 2 == 1)
        # find the kth largest number
        while p1 < n1 and p2 < n2 and k > 1:
            pre1 = p1
            pre2 = p2
            p1 = p1 + (k // 2 - 1) if p1 + (k // 2 - 1) < n1 else n1 - 1
            p2 = p2 + (k // 2 - 1) if p2 + (k // 2 - 1) < n2 else n2 - 1

            if nums1[p1] < nums2[p2]:
                k -= (p1 - pre1) + 1
                p1 = p1 + 1
                p2 = pre2
            else:
                k -= (p2 - pre2) + 1
                p2 = p2 + 1
                p1 = pre1
        if not isOdd:
            if p1 >= n1:
                return (nums2[p2 + k] + nums2[p2 + k - 1]) / 2
            if p2 >= n2:
                return (nums1[p1 + k] + nums1[p1 + k - 1]) / 2
            if nums1[p1] < nums2[p2] and p1 + 1 < n1:
                return (min(nums1[p1+1], nums2[p2]) + nums1[p1]) / 2
            elif p2 + 1 < n2:
                return (min(nums2[p2+1], nums1[p1]) + nums2[p2]) / 2
            else:
                return (nums2[p2] + nums1[p1]) / 2
        else:
            if p1 >= n1:
                return nums2[p2 + k - 1]
            if p2 >= n2:
                return nums1[p1 + k - 1]
            else:
                return nums1[p1] if nums1[p1] < nums2[p2] else nums2[p2]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays([], [2,3,4,5,6, 7]))
