from typing import List, Optional

from utils.Tree import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        def dfs(up, down):

            if up == down:
                return [TreeNode(up)]
            elif up > down:
                return [None]
            curTrees = []
            for v in range(up, down + 1):
                leftTrees = dfs(up, v - 1)
                rightTrees = dfs(v + 1, down)
                for l in leftTrees:
                    for r in rightTrees:
                        root = TreeNode(v)
                        root.left = l
                        root.right = r
                        curTrees.append(root)
            return curTrees
        return dfs(1, n)