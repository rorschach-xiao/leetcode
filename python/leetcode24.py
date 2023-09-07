# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linklist(l):
    head_node = None
    pre = None
    for n in l:
        cur_node = ListNode(n)
        if pre is not None: pre.next = cur_node
        if head_node is None:
            head_node = cur_node
        pre = cur_node
    return head_node

def print_linklist(head):
    cur = head
    while (cur):
        print(cur.val)
        cur = cur.next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        cur_pointer = head
        pre = ListNode(-1)
        new_head = pre
        while (cur_pointer is not None and cur_pointer.next is not None):
            next_pointer = cur_pointer.next
            cur_pointer.next = next_pointer.next
            next_pointer.next = cur_pointer
            pre.next = next_pointer
            pre = cur_pointer
            cur_pointer = cur_pointer.next

        return new_head.next

if __name__ == '__main__':
    solution = Solution()
    l = [1,2,3,4,5,6]
    head = create_linklist(l)
    new_head = solution.swapPairs(head)
    print_linklist(new_head)

