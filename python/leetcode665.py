from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        statu = 0
        i = 0
        while (i < len(nums)):
            if i == 0:
                pre, cur, next = None, nums[i], nums[i + 1]
            elif i == len(nums) - 1:
                pre, cur, next = nums[i - 1], nums[i], None
            else:
                pre, cur, next = nums[i - 1], nums[i], nums[i + 1]

            if next is None:
                if cur < pre:
                    return statu == 0
                else:
                    return True
            else:
                if cur > next:
                    if statu == 1:
                        return False
                    else:
                        statu = 1
                        if i == 0:
                            next_next = nums[i + 2]
                            if next_next >= cur:
                                nums.pop(i + 1)
                                i += 1
                            else:
                                nums.pop(i)
                        elif i + 2 == len(nums):
                            if pre <= next:
                                nums.pop(i)
                            else:
                                nums.pop(i + 1)
                        else:
                            next_next = nums[i + 2]
                            if pre <= next:
                                nums.pop(i)
                            elif next_next >= cur:
                                nums.pop(i + 1)
                                i += 1
                            else:
                                return False
                else:
                    i += 1



if __name__ == '__main__':
    solution = Solution()
    nums = [4,2,6]
    print(solution.checkPossibility(nums))
