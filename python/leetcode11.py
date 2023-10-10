class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxArea = 0
        while(right > left):
            currentArea = (right - left) * min(height[left], height[right])
            if currentArea > maxArea:
                maxArea = currentArea
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))