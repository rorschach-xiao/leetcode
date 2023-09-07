class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 1:
            return 1
        tails = [0]*n
        res = 0
        for i in range(0, n):
            left,right = 0,res
            while(left<right):
                mid = (left+right)//2
                if nums[i]>tails[mid]:
                    left = mid+1
                else:
                    right=mid
            tails[left]=nums[i]
            if right==res:
                res+=1

        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [0,1,0,3,2,3]
    print(solution.lengthOfLIS(nums))