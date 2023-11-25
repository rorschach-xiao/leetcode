import heapq
class MedianFinder:

    def __init__(self):
        self.minpq = [] # max heap
        self.maxpq = [] # min heap

    def addNum(self, num: int) -> None:
        if len(self.minpq) == 0:
            heapq.heappush(self.minpq, -num)
        else:
            if -self.minpq[0] >= num:
                heapq.heappush(self.minpq, -num)
                if len(self.minpq) > len(self.maxpq) + 1:
                    heapq.heappush(self.maxpq, -heapq.heappop(self.minpq))
            else:
                heapq.heappush(self.maxpq, num)
                if len(self.maxpq) > len(self.minpq):
                    heapq.heappush(self.minpq, -heapq.heappop(self.maxpq))

    def findMedian(self) -> float:
        if len(self.minpq) == len(self.maxpq):
            return (-self.minpq[0] + self.maxpq[0]) / 2
        else:
            return -self.minpq[0]

if __name__ == '__main__':
    solution = MedianFinder()
    solution.addNum(-1)
    print(solution.findMedian())
    solution.addNum(-2)
    print(solution.findMedian())
    solution.addNum(-3)
    print(solution.findMedian())
    solution.addNum(-4)
    print(solution.findMedian())