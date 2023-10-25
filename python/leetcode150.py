from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.isNumber(token):
                stack.append(int(token))
            else:
                a1 = stack.pop()
                a2 = stack.pop()
                if token == "+":
                    stack.append(a1 + a2)
                elif token == "-":
                    stack.append(a2 - a1)
                elif token == "*":
                    stack.append(a1 * a2)
                elif token == "/":
                    stack.append(int(a2 / a1))
        return stack[0]

    def isNumber(self, t) -> bool:
        if t[0] == "-" and str.isnumeric(t[1:]):
            return True
        elif str.isnumeric(t):
            return True
        return False

if __name__ =='__main__':
    solution = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    solution.evalRPN(tokens)