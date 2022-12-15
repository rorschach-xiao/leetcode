class Allocator:

    def __init__(self, n: int):
        self.mem = [None for _ in range(n)]
        self.mid2mem = {-1: [[0, n - 1]]}

    def insert_interval(self, intervals, new_interval):
        n = len(intervals)
        if n == 0:
            intervals.append(new_interval)
        for i in range(n):
            if intervals[i][0] - 1 == new_interval[1]:
                intervals[i][0] = new_interval[0]
                break
            elif intervals[i][1] + 1 == new_interval[0]:
                intervals[i][1] = new_interval[1]
                break
            elif intervals[i][1] + 1 < new_interval[0]:
                intervals.insert(i + 1, new_interval.copy())
                break
            elif intervals[i][0] - 1 > new_interval[1]:
                intervals.insert(i , new_interval.copy())
                break

    def merge_interval(self, intervals):
        i = 0
        intervals = sorted(intervals)
        while i < len(intervals) - 1:
            if intervals[i][1] + 1 == intervals[i+1][0]:
                intervals[i][1] = intervals[i+1][1]
                intervals.pop(i + 1)
            i += 1

    def allocate(self, size: int, mID: int) -> int:
        # find available memory
        index = -1
        for i, interval in enumerate(self.mid2mem[-1]):
            if (interval[1] - interval[0] + 1) > size:
                index = interval[0]
                self.mid2mem[-1][i][0] += size
                if mID not in self.mid2mem:
                    self.mid2mem[mID] = [[index, index + size - 1]]
                else:
                    self.insert_interval(self.mid2mem[mID], [index, index + size - 1])
                    self.merge_interval(self.mid2mem[mID])
                for i in range(size):
                    self.mem[index + i] = mID
                break
            elif (interval[1] - interval[0] + 1) == size:
                index = interval[0]
                self.mid2mem[-1].pop(i)
                if mID not in self.mid2mem:
                    self.mid2mem[mID] = [[index, index + size - 1]]
                else:
                    self.insert_interval(self.mid2mem[mID], [index, index + size - 1])
                    self.merge_interval(self.mid2mem[mID])
                for i in range(size):
                    self.mem[index + i] = mID
                break
        return index

    def free(self, mID: int) -> int:
        # recover memory
        if mID not in self.mid2mem:
            return 0
        mem_intervals = self.mid2mem.pop(mID)
        mem_size = 0
        for mem_interval in mem_intervals:
            self.insert_interval(self.mid2mem[-1], mem_interval)
            self.merge_interval(self.mid2mem[-1])
            mem_size += mem_interval[1] - mem_interval[0] + 1

            for i in range(mem_interval[0], mem_interval[1] + 1):
                self.mem[i] = None
        return mem_size

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)

if __name__ == '__main__':

    operation =  ["Allocator", "free", "free", "allocate", "free", "free", "free", "free", "free", "free", "free", "allocate",
     "free", "allocate", "allocate", "allocate", "allocate", "allocate", "allocate", "allocate", "free", "allocate",
     "allocate", "free", "allocate", "free", "allocate", "allocate", "free", "free", "free", "allocate", "allocate",
     "free", "free", "free", "allocate", "allocate", "allocate", "free", "free", "allocate", "free", "free", "allocate",
     "free", "free", "free", "free", "allocate", "free", "free", "allocate", "allocate", "allocate", "allocate", "free",
     "allocate", "allocate", "free", "allocate", "allocate", "allocate", "allocate", "free", "free", "allocate",
     "allocate", "allocate", "allocate", "free", "free", "free", "free", "free", "free", "allocate", "free", "free",
     "allocate", "allocate", "allocate", "free", "free", "free", "allocate", "free", "free", "allocate", "free",
     "allocate", "free", "allocate", "allocate", "allocate", "allocate", "allocate", "free", "allocate", "allocate",
     "allocate", "allocate", "free", "allocate", "free", "free", "free", "free", "allocate", "free", "free", "free",
     "free", "free", "free", "free", "free", "free", "free", "allocate", "free", "free", "free", "allocate", "free",
     "allocate", "free", "allocate", "free", "free", "free", "free", "free", "free", "free", "allocate", "allocate",
     "allocate", "allocate", "allocate", "allocate", "allocate", "free", "allocate", "free", "free", "free", "allocate",
     "free", "allocate", "allocate", "free", "free", "free", "allocate", "allocate", "free", "free", "free", "free",
     "allocate", "free", "allocate", "free", "free", "free", "free", "free", "free", "allocate", "free"]
    params = [[176], [97], [42], [82, 76], [62], [62], [76], [62], [62], [62], [76], [7, 19], [19], [18, 146], [52, 73],
     [191, 42], [186, 83], [49, 120], [68, 187], [98, 13], [73], [62, 37], [158, 92], [42], [123, 100], [92], [81, 101],
     [5, 77], [116], [183], [116], [80, 179], [151, 186], [120], [191], [100], [183, 113], [55, 69], [130, 136], [113],
     [42], [113, 23], [83], [1], [59, 60], [94], [151], [1], [62], [68, 167], [157], [110], [69, 94], [196, 176],
     [70, 103], [64, 59], [191], [70, 141], [189, 2], [62], [49, 200], [104, 138], [113, 105], [134, 74], [167], [96],
     [13, 58], [112, 197], [39, 45], [48, 157], [39], [68], [186], [95], [173], [25], [59, 168], [120], [95],
     [170, 160], [78, 141], [170, 101], [197], [200], [96], [34, 21], [160], [101], [2, 183], [107], [145, 140], [19],
     [96, 74], [163, 102], [54, 36], [130, 137], [46, 74], [83], [143, 86], [161, 182], [186, 149], [102, 165], [45],
     [83, 97], [137], [81], [1], [149], [117, 141], [179], [168], [101], [94], [81], [149], [160], [117], [69], [1],
     [9, 165], [4], [141], [76], [57, 137], [43], [162, 54], [157], [112, 81], [63], [183], [74], [157], [1], [167],
     [4], [34, 152], [150, 37], [149, 30], [111, 87], [29, 81], [78, 34], [119, 18], [81], [10, 3], [160], [73], [94],
     [72, 36], [117], [154, 139], [11, 154], [60], [137], [151], [114, 76], [188, 160], [186], [165], [58], [71],
     [169, 183], [19], [91, 110], [60], [3], [11], [117], [132], [110], [27, 123], [2]]
    result = []
    for op, param in zip(operation, params):
        if op == 'Allocator':
            obj = Allocator(param[0])
        elif op == 'allocate':
            result.append(obj.allocate(param[0], param[1]))
        else:
            result.append(obj.free(param[0]))
    print(result)


