class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # unsolvable cases
        length1 = len(nums1)
        length2 = len(nums2)
        if length1 > 6 * length2 or length2 > 6 * length1:
            return -1

        sum1, sum2 = sum(nums1), sum(nums2)
        nums1, nums2 = (nums1, nums2) if sum1 > sum2 else (nums2, nums1)
        operation_num = 0
        diff = abs(sum1 - sum2)
        cnt = [0] * 6
        for x in nums1: cnt[x - 1] += 1
        for x in nums2: cnt[6 - x] += 1
        for i in range(5, 0 , -1):
            if diff > i * cnt[i]:
                diff -= i * cnt[i]
                operation_num += cnt[i]
            else:
                return operation_num + (diff + i - 1) // i

        return operation_num
if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 3, 4, 5, 6]
    nums2 = [1, 1, 2, 2, 2, 2]
    print(solution.minOperations(nums1, nums2))