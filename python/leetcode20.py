class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop(-1)
            elif c == '}' and len(stack) > 0 and stack[-1] == '{':
                stack.pop(-1)
            elif c == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop(-1)
            else:
                return False
        return len(stack) == 0