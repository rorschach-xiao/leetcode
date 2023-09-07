class Solution(object):
    num2alpha = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        results = []
        for digit in digits:
            current_len = len(results)
            if current_len == 0:
                results.extend(self.num2alpha[digit])
                continue
            for _ in range(current_len):
                current_str = results.pop(0)
                for alpha in self.num2alpha[digit]:
                    results.append(current_str + alpha)

        return results
