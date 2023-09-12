class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        ptr = head
        meet_flag = 0
        start_flag = 0
        while (fast and fast.next):
            if fast == slow and meet_flag == 0 and start_flag!=0:
                meet_flag = 1
            if meet_flag == 1:
                if ptr == slow:
                    return ptr
                else:
                    ptr = ptr.next
            fast = fast.next.next
            slow = slow.next
            start_flag = 1
        return None

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break
        if fast is None or fast.next is None: return None
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
if __name__ == '__main__':
    head = ListNode(0)
    head.next = node_1 = ListNode(1)
    node_1.next = node_2 = ListNode(2)
    node_2.next = node_3 = ListNode(3)
    node_3.next = head
    solution = Solution()
    node = solution.detectCycle(head)
    if node:
        print(f'tail connect to node {node.val}')
    else:
        print(f'no ring exists!')
