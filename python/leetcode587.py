from functools import cmp_to_key
class Solution(object):
    def outerTrees(self, trees):
        """
        :type trees: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(trees) <= 3:
            return trees
        def cross(p, q, r):
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        def mycmp(a,b):
            diff = a[0] - b[0]
            return diff if diff else a[1] - b[1]

        trees = sorted(trees, key=cmp_to_key(mycmp))
        n = len(trees)

        lower_stack = [trees[0]]
        used = [0 for _ in range(len(trees))]
        used[0] = 1
        # calculate lower convex hull
        for i in range(1, n):
            if len(lower_stack) < 2 or cross(lower_stack[-2], lower_stack[-1], trees[i]) >= 0:
                lower_stack.append(trees[i])
                used[i] = 1
            else:
                k = 1
                while (len(lower_stack) >= 2 and cross(lower_stack[-2], lower_stack[-1], trees[i]) < 0):
                    lower_stack.pop()
                    used[i - k] = 0
                    k += 1
                lower_stack.append(trees[i])
                used[i] = 1
        lower_stack.pop(0)
        used[0] = 0

        upper_stack = [trees[-1]]
        # calculate upper convex hull
        for i in range(n - 2, -1, -1):
            if used[i] == 1:
                continue
            elif len(upper_stack) < 2 or cross(upper_stack[-2], upper_stack[-1], trees[i]) >= 0:
                upper_stack.append(trees[i])
            else:
                k = 1
                while (len(upper_stack) >= 2 and cross(upper_stack[-2], upper_stack[-1], trees[i]) < 0):
                    upper_stack.pop()
                    k += 1
                upper_stack.append(trees[i])
        upper_stack.pop(0)
        hull = lower_stack + upper_stack

        return hull

if __name__ == '__main__':
    solution = Solution()
    trees = [[0,0],[0,100],[100,100],[100,0],[50,50]]
    print(solution.outerTrees(trees))




