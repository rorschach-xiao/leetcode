from typing import Optional

from utils.LinkedList import ListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        i = 0
        slow, fast = head, head
        pre_head = ListNode(-1, head)
        while i < k and fast:
            fast = fast.next
            i += 1
        if not fast:
            k = k % i
            i = 0
            fast = head
            while i < k and fast:
                fast = fast.next
                i += 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = head
        pre_head.next = slow.next
        slow.next = None
        return pre_head.next

if __name__ == '__main__':
    solution = Solution()
    head = ListNode.list_to_linkedlist([1,2,3,4,5])
    new_head = solution.rotateRight(head, 4)
    print(ListNode.linkedlist_to_list(new_head))