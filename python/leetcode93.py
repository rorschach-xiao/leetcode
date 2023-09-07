class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.segNum = 4
        self.result = []
        self.s = s
        self.segment = [0, 0, 0, 0]
        self.dfs(0, 0)
        return self.result

    def dfs(self, segID, segStart):
        if segID == self.segNum:
            if segStart == len(self.s):
                addr = '.'.join([str(i) for i in self.segment])
                self.result.append(addr)
            return

        if segStart == len(self.s):
            return

        if self.s[segStart] == '0':
            self.segment[segID] = 0
            self.dfs(segID + 1, segStart + 1)
            return

        val = 0
        for segEnd in range(segStart, len(self.s)):
            val = val * 10 + (ord(self.s[segEnd]) - ord("0"))
            if 0 < val <= 255:
                self.segment[segID] = val
                self.dfs(segID + 1, segEnd + 1)
            else:
                break
if __name__ == '__main__':
    solution=Solution()
    s = "25525511135"
    print(solution.restoreIpAddresses(s))