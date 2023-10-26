from typing import Optional

from utils.LinkedList import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        if p1 is None:
            return p2
        if p2 is None:
            return p1

        head = ListNode(-1)
        p3 = head
        while p1 and p2:
            if p1.val < p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next
        if p1:
            p3.next = p1
        if p2:
            p3.next = p2

        return head.next
