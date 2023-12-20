from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        n = len(pushed)
        j = 0
        for i in range(n):
            stack.append(pushed[i])
            if pushed[i] == popped[j]:
                while stack and stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
        return len(stack) == 0