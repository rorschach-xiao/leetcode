class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        i = len(nums1) - 1
        while(p2 >= 0):
            while(p1 >= 0 and nums1[p1] > nums2[p2]):
                self.swap(nums1, nums1, i, p1)
                p1 -= 1
                i -= 1
            self.swap(nums1, nums2, i, p2)
            i -= 1
            p2 -= 1
        print(nums1)
    def swap(self, nums1, nums2, i, j):
        temp = nums1[i]
        nums1[i] = nums2[j]
        nums2[j] = temp


if __name__ == '__main__':
    solution = Solution()
    solution.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)

