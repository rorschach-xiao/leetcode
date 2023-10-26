# class ListNode(object):
#     def __init__(self, key, value):
#         self.value = value
#         self.key = key
#         self.left = None
#         self.right = None
#
#
# class LRUCache(object):
#
#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.capacity = capacity
#         self.dict = {}
#         self.head = ListNode(-1, -1)
#         self.tail = ListNode(-1, -1)
#         self.head.right = self.tail
#         self.tail.left = self.head
#
#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key in self.dict:
#             self.dict[key].left.right = self.dict[key].right
#             self.dict[key].right.left = self.dict[key].left
#             self.dict[key].left = self.tail.left
#             self.dict[key].right = self.tail
#             self.dict[key].left.right = self.dict[key]
#             self.tail.left = self.dict[key]
#             return self.dict[key].value
#         else:
#             return -1
#
#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         if key in self.dict:
#             self.dict[key].value = value
#             self.dict[key].key = key
#             self.dict[key].left.right = self.dict[key].right
#             self.dict[key].right.left = self.dict[key].left
#         else:
#             new_node = ListNode(key, value)
#             self.dict[key] = new_node
#             if len(self.dict) > self.capacity:
#                 old_key = self.head.right.key
#                 self.head.right.right.left = self.head
#                 self.head.right = self.head.right.right
#                 self.dict.pop(old_key)
#
#         self.dict[key].left = self.tail.left
#         self.dict[key].right = self.tail
#         self.dict[key].left.right = self.dict[key]
#         self.tail.left = self.dict[key]

class ListNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.left = None
        self.right = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        # initialize a double linkedlist
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.right = self.tail
        self.tail.left = self.head

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        else:
            # move the key to the tail of the dll
            node = self.data[key]
            node.left.right = node.right
            node.right.left = node.left
            node.left = self.tail.left
            node.right = self.tail
            self.tail.left = node
            node.left.right = node
            return self.data[key].value

    def put(self, key: int, value: int) -> None:
        if key not in self.data:
            if len(self.data) == self.capacity:
                # remove the node at the head of dll
                lru_node = self.head.right
                lru_key = lru_node.key
                lru_node.left.right = lru_node.right
                lru_node.right.left = lru_node.left
                lru_node.left = None
                lru_node.right = None
                self.data.pop(lru_key)
            # insert the new node to the tail of dll
            node = ListNode(key, value)
            self.data[key] = node
            node.left = self.tail.left
            node.right = self.tail
            self.tail.left = node
            node.left.right = node
        else:
            self.data[key].value = value
            node = self.data[key]
            node.left.right = node.right
            node.right.left = node.left
            node.left = self.tail.left
            node.right = self.tail
            self.tail.left = node
            node.left.right = node

if __name__ == '__main__':
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1); # 缓存是{1 = 1}
    lRUCache.put(2, 2); # 缓存是{1 = 1, 2 = 2}
    lRUCache.get(1); # 返回1
    lRUCache.put(3, 3); # 该操作会使得关键字2作废，缓存是{1 = 1, 3 = 3}
    lRUCache.get(2); # 返回 - 1(未找到)
    lRUCache.put(4, 4); # 该操作会使得关键字1作废，缓存是{4 = 4, 3 = 3}
    lRUCache.get(1); # 返回 - 1(未找到)
    lRUCache.get(3); # 返回3
    lRUCache.get(4); # 返回4
