from typing import List


class MaxHeap():
    def __init__(self):
        self.heap = []

    def heappush(self, v):
        self.heap.append(v)
        self.__heapifyUp(len(self.heap) - 1)

    def heappop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        maxValue = self.heap.pop()
        self.__heapifyDown(0)
        return maxValue

    def __heapifyUp(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if parent != index and self.heap[index] > self.heap[parent]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break

    def __heapifyDown(self, index):
        n = len(self.heap)
        while index * 2 + 1 < n:
            largest = index
            left = index * 2 + 1
            right = index * 2 + 2

            if self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break
    def __len__(self):
        return len(self.heap)

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w > max(capital):
            return w + sum(sorted(profits)[-k:])
        arr = sorted(zip(capital, profits))
        priority_queue = MaxHeap()
        i, n = 0, len(arr)
        for _ in range(k):
            while i < n and arr[i][0] <= w:
                priority_queue.heappush(arr[i][1])
                i += 1
            if len(priority_queue) > 0:
                w += priority_queue.heappop()
            else:
                break
        return w
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    solution = Solution()
    k, w, profits, capital = 2, 0, [1,2,3], [0, 1, 1]
    print(solution.findMaximizedCapital(k, w, profits, capital))