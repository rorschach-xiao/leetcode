class Solution:
    def smallestValue(self, n: int) -> int:
        cur_breakdown = self.breakdown(n)
        while(sum(cur_breakdown) < n):
            n = sum(cur_breakdown)
            cur_breakdown = self.breakdown(n)
        return sum(cur_breakdown)

    def breakdown(self, n):
        result = []
        i = 2
        while(i ** 2 <= n):
            if n % i == 0:
                while(n % i == 0):
                    n = n // i
                    result.append(i)
            i += 1
        if n != 1:
            result.append(n)
        return result

if __name__ == '__main__':
    solution = Solution()
    n = 6
    print(solution.smallestValue(n))