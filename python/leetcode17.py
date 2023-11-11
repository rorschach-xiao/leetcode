# class Solution(object):
#     num2alpha = {
#         '2': ['a', 'b', 'c'],
#         '3': ['d', 'e', 'f'],
#         '4': ['g', 'h', 'i'],
#         '5': ['j', 'k', 'l'],
#         '6': ['m', 'n', 'o'],
#         '7': ['p', 'q', 'r', 's'],
#         '8': ['t', 'u', 'v'],
#         '9': ['w', 'x', 'y', 'z']
#     }
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         results = []
#         for digit in digits:
#             current_len = len(results)
#             if current_len == 0:
#                 results.extend(self.num2alpha[digit])
#                 continue
#             for _ in range(current_len):
#                 current_str = results.pop(0)
#                 for alpha in self.num2alpha[digit]:
#                     results.append(current_str + alpha)
#
#         return results
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.digit2letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        if len(digits) == 0:
            return []
        self.res = []
        self.helper(digits, "")
        return self.res

    def helper(self, digits, cur_letters):
        if len(digits) == 0:
            self.res.append(cur_letters)
            return
        digit = digits[0]
        for letter in self.digit2letter[digit]:
            cur_letters += letter
            self.helper(digits[1:], cur_letters)
            cur_letters = cur_letters[:-1]
