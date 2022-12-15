from functools import cmp_to_key
class Solution(object):
    def get_convexhull(self, trees):
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
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def TriangleArea(x1, y1, x2, y2, x3, y3):
            return abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2

        convex_hull = self.get_convexhull(points)
        n = len(convex_hull)
        ans = 0
        for i in range(n - 2):
            p = convex_hull[i]
            k = i + 2
            for j in range(i + 1, n - 1):
                q = convex_hull[j]
                while(k + 1 < n):
                    curArea = TriangleArea(p[0], p[1], q[0], q[1], convex_hull[k][0], convex_hull[k][1])
                    nextArea = TriangleArea(p[0], p[1], q[0], q[1], convex_hull[k+1][0], convex_hull[k+1][1])
                    if curArea > nextArea:
                        break
                    k += 1
                ans = max(ans, TriangleArea(p[0], p[1], q[0], q[1], convex_hull[k][0], convex_hull[k][1]))
        return ans

if __name__ == '__main__':
    solution = Solution()
    points = [[1,0],[0,0],[0,1]]
    print(solution.largestTriangleArea(points))

