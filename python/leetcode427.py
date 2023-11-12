from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        self._grid = grid
        n = len(grid)
        return self.helper(0, n - 1, 0, n - 1)

    def helper(self, left, right, up, bottom):
        if left == right:
            return Node(self._grid[up][left], 1, None, None, None, None)
        root = Node(1, 0, None, None, None, None)
        topLeft_node = self.helper(left, (left + right)//2, up, (bottom + up) // 2)
        bottomLeft_node = self.helper(left, (left + right)//2, (bottom + up) // 2 + 1, bottom)
        topRight_node = self.helper((left + right)//2 + 1, right, up, (bottom + up) // 2)
        bottomRight_node = self.helper((left + right)//2 + 1, right, (bottom + up) // 2 + 1, bottom)

        if topLeft_node.val == topRight_node.val == bottomLeft_node.val == bottomRight_node.val\
                and topRight_node.isLeaf == topLeft_node.isLeaf == bottomRight_node.isLeaf == bottomLeft_node.isLeaf == 1:
            root.isLeaf = 1
            root.val = topLeft_node.val
        else:
            root.topLeft = topLeft_node
            root.topRight = topRight_node
            root.bottomLeft = bottomLeft_node
            root.bottomRight = bottomRight_node
        return root


if __name__ == '__main__':
    solution = Solution()
    board = [[1,1,1,1,0,0,0,0],
             [1,1,1,1,0,0,0,0],
             [1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1],
             [1,1,1,1,0,0,0,0],
             [1,1,1,1,0,0,0,0],
             [1,1,1,1,0,0,0,0],
             [1,1,1,1,0,0,0,0]]
    solution.construct(board)