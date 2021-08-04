class Solution(object):
    def BrackerSum(self,s):
        """
        :param s:
        :return: int
        """
        stack = []
        for c in s:
            cur_result = 0
            if c == '(':
                stack.append(c)
            elif c==')':
                tmp = stack.pop(-1)
                while(isinstance(tmp,int)):
                    cur_result += tmp
                    tmp = stack.pop(-1)
                if cur_result == 0:
                    stack.append(1)
                else:
                    stack.append(cur_result*2)
        return sum(stack)


if __name__ == '__main__':
    solution = Solution()
    s = '(()(()))()'
    print(solution.BrackerSum(s))