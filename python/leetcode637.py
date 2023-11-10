from typing import Optional, List

from utils.Tree import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if root is None:
            return res

        level = [root]
        next_level = []
        current_level_sum = 0
        current_level_cnt = 0
        while (len(level) > 0):
            node = level.pop(0)
            current_level_sum += node.val
            current_level_cnt += 1
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if len(level) == 0:
                res.append(round(current_level_sum / current_level_cnt, 5))
                level = next_level
                next_level = []
                current_level_sum = 0
                current_level_cnt = 0
        return res