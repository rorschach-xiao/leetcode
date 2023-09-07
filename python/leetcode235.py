class Solution:
    def lowestCommonAncestor(self, root, p, q):
        path_p = self.get_path(root, p)
        path_q = self.get_path(root, q)
        ancestor = None
        while(len(path_p)!= 0 and len(path_q)!= 0):
            cur_p = path_p.pop(0)
            cur_q = path_q.pop(0)
            if cur_p.val == cur_q.val:
                ancestor = cur_p
            else:
                break
        return ancestor

    def get_path(self, root, p):
        cur = root
        path = []
        while(cur and cur.val != p.val):
            path.append(cur)
            if cur.val < p.val:
                cur = cur.right
            elif cur.val > p.val:
                cur = cur.left
        if cur:
            path.append(cur)
        return path