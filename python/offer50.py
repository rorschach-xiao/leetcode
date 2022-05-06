class Solution:
    def firstUniqChar(self, s: str) -> str:
        # ============== simple loop : O(N^2), O(1) ==============
        # if len(s) == 0:
        #     return ' '
        # single = []
        # multiple = []
        # for x in s:
        #     if x not in single and x not in multiple:
        #         single.append(x)
        #     elif x in single:
        #         multiple.append(x)
        #         single.remove(x)
        # if len(single) == 0:
        #     return ' '
        # return single[0]

        # ============== hashmap :  O(N), O(1) =================
        hm = {}
        for x in s:
            if x in hm.keys():
                hm[x] = False
            else:
                hm[x] = True
        for k,v in hm.items():
            if v:
                return k
        return ' '

if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar(''))