from typing import Optional

from utils.LinkedList import ListNode


class Solution:
    # recursive solution
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     rev_head, _ = self.helper(head)
    #     return rev_head
    #
    # def helper(self, head):
    #     if not head or not head.next:
    #         return head, head
    #     cur = head
    #     new_head, new_tail = self.helper(cur.next)
    #     new_tail.next = cur
    #     cur.next = None
    #     return new_head, cur

    # iterative solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

