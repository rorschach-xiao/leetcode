class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums = nums

        left_p = 0
        right_p = len(nums)-1
        return self.helper(left_p,right_p,target)


    def helper(self,left,right,target):
        if left>right:
            return -1
        mid = (left+right)//2
        if self.nums[mid] == target:
            return mid
        else:
            if self.nums[mid]>=self.nums[left]:
                if self.nums[mid]<target or self.nums[left]>target:
                    return self.helper(mid+1,right,target)
                else:
                    return self.helper(left,mid-1,target)
            else:
                if self.nums[mid]>target or self.nums[right]<target:
                    return self.helper(left,mid-1,target)
                else:
                    return self.helper(mid+1,right,target)

if __name__ == '__main__':
    solution = Solution()
    nums = [3,1]
    print(solution.search(nums,1))
