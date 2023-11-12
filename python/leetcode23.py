from typing import List, Optional

from utils.LinkedList import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if len(lists) == 0:
            return None
        self.lists = lists
        return self.helper(0, n - 1)

    def helper(self, start, end):
        if start == end:
            return self.lists[start]
        left = self.helper(start, (start + end) // 2)
        right = self.helper((start + end) // 2 + 1, end)
        return self.merge(left, right)

    def merge(self, head1, head2):
        p1 = head1
        p2 = head2
        pre_head = ListNode(-1)
        p3 = pre_head
        while p1 and p2:
            if p1.val < p2.val:
                p3.next = p1
                p1 = p1.next
                p3 = p3.next
            else:
                p3.next = p2
                p2 = p2.next
                p3 = p3.next
        while p1:
            p3.next = p1
            p1 = p1.next
            p3 = p3.next
        while p2:
            p3.next = p2
            p2 = p2.next
            p3 = p3.next
        return pre_head.next

if __name__ == '__main__':
    solution = Solution()
    lists = [
        ListNode.list_to_linkedlist([1, 4, 5]),
        ListNode.list_to_linkedlist([1, 3, 4]),
        ListNode.list_to_linkedlist([2, 6]),
    ]
    solution.mergeKLists(lists)
