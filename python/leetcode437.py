from typing import Optional

from utils.Tree import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        preSum = {0: 1}
        self.cnt = 0
        self.targetSum = targetSum
        self.dfs(0, root, preSum)
        return self.cnt


    def dfs(self, curSum, node, preSum):
        if not node:
            return
        curSum += node.val
        if curSum - self.targetSum in preSum:
            self.cnt += preSum[curSum - self.targetSum]

        if curSum not in preSum:
            preSum[curSum] = 1
            self.dfs(curSum, node.left, preSum)
            self.dfs(curSum, node.right, preSum)
            preSum.pop(curSum)
        else:
            preSum[curSum] += 1
            self.dfs(curSum, node.left, preSum)
            self.dfs(curSum, node.right, preSum)
            preSum[curSum] -= 1