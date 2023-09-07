from functools import cmp_to_key
class Solution:
    # def cycleLengthQueries(self, n: int, queries):
    #     num_query = len(queries)
    #     ans = [0 for _ in range(num_query)]
    #     level_a, level_b = 0, 0
    #     new_queries = [query if query[0] < query[1] else query[::-1] for query in queries]
    #     def cmp(i, j):
    #         x = new_queries.__getitem__(i)
    #         y = new_queries.__getitem__(j)
    #         return x[0] - y[0]
    #     sorted_indexs = sorted(range(len(new_queries)), key=cmp_to_key(cmp))
    #     for idx in sorted_indexs:
    #         query = new_queries[idx]
    #         a, b = query[0], query[1]
    #         for level in range(level_a, n + 1):
    #             if 2 ** level <= a <= 2 ** (level + 1) - 1:
    #                 level_a = level
    #                 break
    #         for level in range(level_a, n + 1):
    #             if 2 ** level <= b <= 2 ** (level + 1) - 1:
    #                 level_b = level
    #                 break
    #
    #         # if two query on the same path
    #         if level_a != 0 and level_b != 0:
    #             pointer_a = 1 << (level_a - 1)
    #             pointer_b = 1 << (level_b - 1)
    #             common_path = 0
    #             while(pointer_a != 0 and pointer_b != 0):
    #                 cur_bit_a = a & pointer_a
    #                 cur_bit_b = b & pointer_b
    #                 if cur_bit_a == cur_bit_b or (cur_bit_b != 0 and cur_bit_a != 0):
    #                     common_path += 1
    #                     pointer_a = pointer_a >> 1
    #                     pointer_b = pointer_b >> 1
    #                 else:
    #                     break
    #         else:
    #             common_path = 0
    #
    #         ans[idx] = level_a + level_b + 1 - common_path * 2
    #     return ans

    def cycleLengthQueries(self, n: int, queries):
        num_query = len(queries)
        ans = [0 for _ in range(num_query)]
        # new_queries = [query if query[0] < query[1] else query[::-1] for query in queries]
        # def cmp(i, j):
        #     x = new_queries.__getitem__(i)
        #     y = new_queries.__getitem__(j)
        #     return x[0] - y[0]
        # sorted_indexs = sorted(range(len(new_queries)), key=cmp_to_key(cmp))
        for idx in range(num_query):
            a, b = queries[idx][0], queries[idx][1]

            circle_len = 0
            while(a != b and a != 0 and b != 0):
                if b > a:
                    b = b >> 1
                elif a > b:
                    a = a >> 1
                circle_len += 1
            circle_len += 1
            ans[idx] = circle_len
        return ans



if __name__ == '__main__':
    solution = Solution()
    n = 5
    queries = [[23,5]]
    print(solution.cycleLengthQueries(n, queries=queries))

