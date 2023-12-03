from typing import Optional

from utils.LinkedList import ListNode


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        slow, fast = head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        rev_head = self.reverse(slow)
        cur, cur_rev = head, rev_head
        maxTwinSum = 0
        while cur and cur_rev:
            maxTwinSum = max(maxTwinSum, cur.val + cur_rev.val)
            cur = cur.next
            cur_rev = cur_rev.next
        return maxTwinSum

    def reverse(self, head):
        if not head:
            return None
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre