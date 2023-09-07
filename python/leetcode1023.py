class Solution:
    def camelMatch(self, queries, pattern):
        ans = []
        for query in queries:
            ans.append(self.camelMatch_simple(query, pattern))
        return ans

    def camelMatch_simple(self, query, pattern):
        i, j = 0, 0
        if len(pattern) > len(query):
            return False
        while(i < len(query) and j < len(pattern)):
            if query[i] == pattern[j]:
                i += 1
                j += 1
            else:
                if 'A'<= query[i] <= 'Z':
                    return False
                else:
                    i += 1
        if j < len(pattern):
            return False

        while(i < len(query)):
            if 'A'<= query[i] <= 'Z':
                return False
            i += 1
        return True

if __name__ == '__main__':
    solution = Solution()
    queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
    pattern = 'FB'
    print(solution.camelMatch(queries, pattern))
