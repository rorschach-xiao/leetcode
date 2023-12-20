class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append((c, 1))
            elif stack[-1][0] == c and stack[-1][1] < k - 1:
                stack[-1] = (c, stack[-1][1] + 1)
            else:
                stack.pop()
        re = ''
        for c, t in stack:
            re += c * t
        return re