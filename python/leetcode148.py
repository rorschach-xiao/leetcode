# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def sortList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         heads = self.cut(head)
#         if len(heads) == 1:
#             return heads[0]
#         else:
#             left, right = heads
#             sorted_left = self.sortList(left)
#             sorted_right = self.sortList(right)
#             new_head = self.merge(sorted_left, sorted_right)
#             return new_head
#
#     def cut(self, head):
#         slow = head
#         fast = head
#         pre = None
#         while (fast and fast.next):
#             fast = fast.next.next
#             pre = slow
#             slow = slow.next
#         if pre is None:
#             return [head]
#         else:
#             pre.next = None
#             return [head, slow]
#
#     def merge(self, head1, head2):
#         new_head = ListNode(-1)
#         cur1 = head1
#         cur2 = head2
#         cur = new_head
#         new_head.next = cur1 if cur1.val < cur2.val else cur2
#         while (cur1 and cur2):
#             if cur1.val < cur2.val:
#                 cur.next = cur1
#                 cur1 = cur1.next
#                 cur = cur.next
#             else:
#                 cur.next = cur2
#                 cur2 = cur2.next
#                 cur = cur.next
#
#         cur.next = cur2 if cur2 else cur1
#         return new_head.next
from typing import Optional

from utils.LinkedList import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow, fast = head, head
        while (fast and fast.next):
            fast = fast.next.next
            if fast: slow = slow.next
        head2 = slow.next
        slow.next = None
        head1 = self.sortList(head)
        head2 = self.sortList(head2)
        head = self.merge(head1, head2)
        return head

    def merge(self, head1, head2):
        p1 = head1
        p2 = head2
        pre_head = ListNode(-1)
        p3 = pre_head

        while (p1 and p2):
            if p1.val < p2.val:
                p3.next = p1
                p1 = p1.next
                p3 = p3.next
            else:
                p3.next = p2
                p2 = p2.next
                p3 = p3.next
        while (p1):
            p3.next = p1
            p1 = p1.next
            p3 = p3.next
        while (p2):
            p3.next = p2
            p2 = p2.next
            p3 = p3.next

        return pre_head.next

if __name__ == '__main__':
    val_list = [3, 4, 1]
    head = ListNode.list_to_linkedlist(val_list)
    solution = Solution()
    new_head = solution.sortList(head)
    print(ListNode.linkedlist_to_list(new_head))