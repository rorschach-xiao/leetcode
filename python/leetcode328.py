from typing import Optional

from utils.LinkedList import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd_head = head
        even_head = head.next
        cur_odd, cur_even = odd_head, even_head
        while cur_odd and cur_even:
            pre_odd = cur_odd
            cur_odd.next = cur_even.next
            cur_odd = cur_odd.next
            if cur_odd:
                cur_even.next = cur_odd.next
            else:
                cur_even.next = None
            cur_even = cur_even.next
        if cur_odd:
            cur_odd.next = even_head
        else:
            pre_odd.next = even_head
        return odd_head