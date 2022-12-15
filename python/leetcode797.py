class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        stack = []
        # dfs
        n = len(graph)
        def dfs(x):
            if x == n - 1:
                result.append(stack[:])
                return
            for node in graph[x]:
                stack.append(node)
                dfs(node)
                stack.pop(-1)
        stack.append(0)
        dfs(0)
        return result

if __name__ == '__main__':
    solution = Solution()
    G = [[1,2],[3],[3],[]]
    print(solution.allPathsSourceTarget(G))