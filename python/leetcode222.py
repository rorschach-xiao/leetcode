
class Solution:
    # binary search + bit
    def countNodes(self, root) -> int:
        if root is None:
            return 0

        level = 0
        cur = root
        while (cur):
            cur = cur.left
            level += 1
        low = 2 ** (level - 1)
        high = 2 ** level - 1
        while (low < high):
            mid = (high - low + 1) // 2 + low
            print(low, high, mid)
            if self.node_exist(root, level, mid):
                low = mid
            else:
                high = mid - 1

        return low

    def node_exist(self, root, level, k):
        bit = 1 << (level - 2)
        cur = root
        while (cur and bit > 0):
            if bit & k == 0:
                cur = cur.left
            else:
                cur = cur.right
            bit = bit >> 1
        if cur:
            return True
        else:
            return False

    # # dfs
    # def countNodes(self, root) -> int:
    #     self.num = 0
    #     def dfs(root):
    #         if root is None:
    #             return
    #         self.num += 1
    #         dfs(root.left)
    #         dfs(root.right)
    #     dfs(root)
    #     return self.num


