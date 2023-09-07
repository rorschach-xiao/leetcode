class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        LCP = ""
        for i in range(200):
            if len(strs[0]) <= i:
                break
            else:
                c = strs[0][i]
            flag = False
            for s in strs:
                if len(s) <= i or s[i] != c:
                    flag = True
                    break

            if flag:
                break
            else:
                LCP += c
        return LCP

if __name__ == '__main__':
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    print(solution.longestCommonPrefix(strs))