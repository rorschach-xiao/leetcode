# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#
#         LCP = ""
#         for i in range(200):
#             if len(strs[0]) <= i:
#                 break
#             else:
#                 c = strs[0][i]
#             flag = False
#             for s in strs:
#                 if len(s) <= i or s[i] != c:
#                     flag = True
#                     break
#
#             if flag:
#                 break
#             else:
#                 LCP += c
#         return LCP
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        common_prefix = ""
        cursor = 0
        end_flag = False
        while(not end_flag):
            current_common_letter = None
            for s in strs:
                if len(s) < cursor + 1:
                    end_flag = True
                    break
                if current_common_letter is None:
                    current_common_letter = s[cursor]
                elif s[cursor] != current_common_letter:
                    end_flag = True
                    break
            if not end_flag:
                common_prefix += current_common_letter
                cursor += 1

        return common_prefix

if __name__ == '__main__':
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    print(solution.longestCommonPrefix(strs))