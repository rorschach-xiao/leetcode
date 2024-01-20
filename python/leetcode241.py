from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def dfs(left ,right):
            if left > right:
                return []
            ans = []
            for i in range(left, right + 1):
                if expression[i].isdigit(): continue
                l_ans, r_ans = dfs(left, i - 1), dfs(i + 1, right)
                for l in l_ans:
                    for r in r_ans:
                        if expression[i] == '+':
                            ans.append(l + r)
                        elif expression[i] == '-':
                            ans.append(l - r)
                        else:
                            ans.append(l * r)
            if not ans:
                ans.append(int(expression[left: right + 1]))
            return ans

        return dfs(0, len(expression) - 1)