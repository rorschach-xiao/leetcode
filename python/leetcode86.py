from typing import Optional

from utils.LinkedList import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None

        less_head = ListNode(-1, head)
        large_head = ListNode(-1, head)
        less, large = less_head, large_head
        cur = head
        while cur:
            if cur.val < x:
                less.next = cur
                less = less.next
            else:
                large.next = cur
                large = large.next
            cur = cur.next
        large.next = None
        less.next = large_head.next
        return less_head.next