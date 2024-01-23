from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_cnt = {}
        for word in words:
            if word not in word_cnt:
                word_cnt[word] = 1
            else:
                word_cnt[word] += 1
        heap = MinHeap()
        for key, value in word_cnt.items():
            heap.heappush((key, value))
            if len(heap) > k:
                heap.heappop()
        ans = []
        for i in range(k):
            ans.insert(0, heap.heappop()[0])
        return ans


class MinHeap:
    def __init__(self):
        self.minheap = []
        self.heapsize = 0

    def __len__(self):
        return self.heapsize

    def getdata(self):
        return [self.minheap[i][0] for i in range(self.heapsize - 1, -1, -1)]

    def heappop(self):
        if self.heapsize == 0:
            return None
        self.minheap[0], self.minheap[-1] = self.minheap[-1], self.minheap[0]
        p = self.minheap.pop(-1)
        self.heapsize -= 1
        self.__heapifyDown(self.heapsize, 0)
        return p

    def heappush(self, w):
        self.minheap.append(w)
        self.heapsize += 1
        self.__heapifyUp(self.heapsize - 1)

    def __comp(self, p1, p2):
        if p1[1] == p2[1]:
            return p1[0] < p2[0]
        else:
            return p1[1] > p2[1]

    def __heapifyUp(self, i):
        largest = i
        parent = (i - 1) // 2
        if parent >= 0 and self.__comp(self.minheap[parent], self.minheap[i]):
            largest = parent
        if largest != i:
            self.minheap[largest], self.minheap[i] = self.minheap[i], self.minheap[largest]
            self.__heapifyUp(largest)

    def __heapifyDown(self, n, i):
        smallest = i
        left, right = i * 2 + 1, i * 2 + 2
        if left < n and self.__comp(self.minheap[smallest], self.minheap[left]):
            smallest = left
        if right < n and self.__comp(self.minheap[smallest], self.minheap[right]):
            smallest = right

        if smallest != i:
            self.minheap[smallest], self.minheap[i] = self.minheap[i], self.minheap[smallest]
            self.__heapifyDown(n, smallest)