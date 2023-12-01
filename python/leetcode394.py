class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                cur_str = ''
                cur_char = stack.pop()
                while len(stack) > 0 and cur_char != '[':
                    if cur_char.isalpha():
                        cur_str = cur_char + cur_str
                    cur_char = stack.pop()
                cur_num = ''
                while len(stack) > 0 and stack[-1].isdigit():
                    cur_num = stack.pop() + cur_num
                num = int(cur_num)
                stack.append(num * cur_str)
        return ''.join(stack)

if __name__ == '__main__':
    solution = Solution()
    print(solution.decodeString("10[a]2[bc]"))