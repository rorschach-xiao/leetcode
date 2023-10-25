from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        numStack = []
        opStack = []
        tokens = self.str2Tokens(s)

        def applyOperator():
            op = opStack.pop()
            num1 = numStack.pop()
            num2 = numStack.pop()
            if op == "+":
                numStack.append(num1 + num2)
            else:
                numStack.append(num2 - num1)

        for i, token in enumerate(tokens):
            if type(token) == int:
                numStack.append(token)
            elif token == "(":
                opStack.append(token)
            elif token == ")":
                while (len(opStack) > 0 and opStack[-1] != "("):
                    applyOperator()
                opStack.pop()

            else:
                if i == 0 or (i > 0 and tokens[i-1] == "("):
                    numStack.append(0)
                while (len(opStack) > 0 and opStack[-1] != "("):
                    applyOperator()
                opStack.append(token)
        while len(opStack) != 0:
            applyOperator()

        return numStack.pop()

    def str2Tokens(self, s: str) -> List[str]:
        tokens = []
        token = ""

        for c in s:
            if c == " ":
                continue
            elif c == "-" or c == "+" or c == "(" or c == ")":
                if token != "":
                    tokens.append(int(token))
                    token = ""
                tokens.append(c)
            elif str.isdigit(c):
                token += c
        if token != "":
            tokens.append(int(token))
        return tokens


if __name__ == '__main__':
    solution = Solution()
    print(solution.calculate("- (3 - (- (4 + 5) + 9 ) )"))
    print(solution.calculate("- (3 - (- (4 + 5) ) )"))
    print(solution.calculate("- (3)"))
    print(solution.calculate("- (3 + 4 - (5 + 6))"))