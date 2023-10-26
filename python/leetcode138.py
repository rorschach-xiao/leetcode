from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None
        p_origin = head
        new_head = None
        origin_node_map = {}
        new_node_list = []
        i = 0
        # copy next pointers and create the index mapping
        while (p_origin):
            if new_head is None:
                new_head = Node(p_origin.val)
                p_new = new_head
            else:
                node_copy = Node(p_origin.val)
                p_new.next = node_copy
                p_new = p_new.next

            origin_node_map[p_origin] = i
            new_node_list.append(p_new)
            p_origin = p_origin.next
            i += 1

        p_origin = head
        p_new = new_head
        # copy random pointers
        while p_origin:
            if p_origin.random is None:
                p_new.random = None
            else:
                p_new.random = new_node_list[origin_node_map[p_origin.random]]
            p_origin = p_origin.next
            p_new = p_new.next

        return new_head