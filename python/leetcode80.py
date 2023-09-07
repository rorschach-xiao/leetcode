class Solution:
    def removeDuplicates(self, nums):
        prev = None
        cur_ele_len = 1
        i = 0
        while (i < len(nums)):
            cur = nums[i]
            if prev is None or prev is not None and prev != cur:
                cur_ele_len = 1
                prev = cur
                i += 1
            elif prev == cur and cur_ele_len < 2:
                cur_ele_len += 1
                i += 1
            elif prev == cur and cur_ele_len >= 2:
                nums.pop(i)

        return len(nums)

if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,2,2,3]
    print(solution.removeDuplicates(nums))