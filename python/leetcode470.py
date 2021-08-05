import random
def rand7():
    return random.randint(1,7)
class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """

        def sample():
            row = rand7()
            col = rand7()
            return 7 * (row - 1) + col

        sample_re = sample()
        while (sample_re > 40):
            sample_re = sample()
        result = sample_re % 10 if sample_re % 10 != 0 else 10
        return result

if __name__ == '__main__':
    solution = Solution()
    n = 1000
    D = {}
    for i in range(n):
        re = solution.rand10()
        if re not in D:
            D[re] = 1
        else:
            D[re]+=1
    print(D)