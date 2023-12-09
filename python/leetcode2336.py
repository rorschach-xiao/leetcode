class SmallestInfiniteSet:

    def __init__(self):
        self.curSmallest = 1
        self.minHeap = []
        self.heapSet = set()
        self.heapsize = 0

    def popSmallest(self) -> int:
        if self.heapsize == 0:
            smallest = self.curSmallest
            self.curSmallest += 1
        else:
            smallest = self.minHeap[0]
            self.minHeap[0], self.minHeap[-1] = self.minHeap[-1], self.minHeap[0]
            self.minHeap.pop()
            self.heapsize -= 1
            self.heapifyDown(self.heapsize, 0)
            self.heapSet.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.curSmallest and num not in self.heapSet:
            self.minHeap.append(num)
            self.heapsize += 1
            self.heapifyUp(self.heapsize - 1)
            self.heapSet.add(num)

    def heapifyUp(self, i):
        parent = (i - 1) // 2
        cur = i
        if parent >= 0 and self.minHeap[parent] > self.minHeap[cur]:
            cur = parent
        if cur != i:
            self.minHeap[i], self.minHeap[cur] = self.minHeap[cur], self.minHeap[i]
            self.heapifyUp(cur)

    def heapifyDown(self, n, i):
        smallest = i
        left = i * 2 + 1
        right = i * 2 + 2

        if left < n and self.minHeap[left] < self.minHeap[smallest]:
            smallest = left
        if right < n and self.minHeap[right] < self.minHeap[smallest]:
            smallest = right


        if smallest != i:
            self.minHeap[smallest], self.minHeap[i] = self.minHeap[i], self.minHeap[smallest]
            self.heapifyDown(n, smallest)

if __name__ == '__main__':
    solution = SmallestInfiniteSet()
    for i in range(10):
        print(solution.popSmallest())

    solution.addBack(5)
    solution.addBack(5)
    solution.addBack(5)
    solution.addBack(5)
    solution.addBack(20)
    solution.addBack(1)
    solution.addBack(1)
    solution.addBack(1)
    solution.addBack(5)
    for i in range(10):
        print(solution.popSmallest())

