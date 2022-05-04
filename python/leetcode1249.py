class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        replace_idxs = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append('(')
                replace_idxs.append(i)
            if c == ')':
                if len(stack) == 0:
                    replace_idxs.append(i)
                else:
                    stack.pop()
                    replace_idxs.pop()
        remain = []
        last_idx = 0
        for j in replace_idxs:
            remain.append(s[last_idx:j])
            last_idx = j+1
        remain.append(s[last_idx:])
        return ''.join(remain)

if __name__ == '__main__':
    solution = Solution()
    s = "))(("
    solution.minRemoveToMakeValid(s)
