import random
class RandomizedSet(object):

    def __init__(self):
        self.arr = []
        self.dict = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        self.arr.append(val)
        self.dict[val] = len(self.arr) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            pos = self.dict[val]
            self.swap(pos, len(self.arr)-1)
            self.dict[self.arr[pos]] = pos
            self.arr.pop(-1)
            self.dict.pop(val)
            return True
        return False

    def getRandom(self):
        """
        :rtype: int
        """
        rand = random.randint(0, len(self.arr) - 1)
        return self.arr[rand]

    def swap(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp

if __name__ == '__main__':
    obj = RandomizedSet()
    obj.remove(0)
    obj.remove(0)
    obj.insert(0)
    obj.getRandom()
    obj.remove(0)
    obj.insert(0)
    print(obj.getRandom())

