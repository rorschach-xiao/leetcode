from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preNum = [0 for _ in range(numCourses)]
        edges = {}
        queue = []
        m = numCourses
        for pre in prerequisites:
            preNum[pre[0]] += 1
            if pre[1] not in edges:
                edges[pre[1]] = [pre[0]]
            else:
                edges[pre[1]].append(pre[0])
        for i, n in enumerate(preNum):
            if n == 0:
                queue.append(i)
        res = []
        while len(queue) != 0:
            cur = queue.pop(0)
            res.append(cur)
            if cur in edges:
                for neigh in edges[cur]:
                    preNum[neigh] -= 1
                    if preNum[neigh] == 0:
                        queue.append(neigh)
        if len(res) != numCourses:
            return []
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))