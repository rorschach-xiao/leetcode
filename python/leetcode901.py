class StockSpanner:

    def __init__(self):
        self.stack = [(-1, float('inf'))]
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1
        while self.stack[-1][1] <= price:
            self.stack.pop()
        lastId = self.stack[-1][0]
        self.stack.append((self.idx, price))
        return self.idx - lastId

if __name__ == '__main__':
    spanner = StockSpanner()
    re = spanner.next(100)
    re = spanner.next(80)
    re = spanner.next(60)
    re = spanner.next(70)
    re = spanner.next(60)
    re = spanner.next(75)
    re = spanner.next(85)