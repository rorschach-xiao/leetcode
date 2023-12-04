from typing import Optional

from utils.Tree import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        curSum, maxSum = 0, float('-inf')
        curLevel, maxLevel = 1, 1
        cur_level_nodes, next_level_nodes = [root], []
        while cur_level_nodes:
            cur_node = cur_level_nodes.pop(0)
            curSum += cur_node.val
            if cur_node.left:
                next_level_nodes.append(cur_node.left)
            if cur_node.right:
                next_level_nodes.append(cur_node.right)
            if len(cur_level_nodes) == 0:
                if curSum > maxSum:
                    maxLevel = curLevel
                    maxSum = curSum
                curLevel += 1
                curSum = 0
                cur_level_nodes = next_level_nodes
                next_level_nodes = []
        return maxLevel

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode.list_2_tree([989,None,10250,98693,-89388,None,None,None,-32127])
    solution.maxLevelSum(root)