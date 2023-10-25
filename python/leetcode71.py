class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split("/")
        for directory in directories:
            if directory == "" or directory == ".":
                continue
            elif directory == "..":
                if len(stack) > 0:
                    stack.pop(-1)
            else:
                stack.append(directory)
        return "/" + "/".join(stack)

if __name__ == '__main__':
    solution = Solution()
    print(solution.simplifyPath("/../"))