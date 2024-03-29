class Solution:
    # recursive
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n-1) + self.fib(n-2)

    # iterative
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        for i in range(2, n + 1):
            cur = a + b
            a = b
            b = cur
        return cur