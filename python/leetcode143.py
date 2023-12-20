# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def reorderList(self, head):
#         """
#         :type head: ListNode
#         :rtype: None Do not return anything, modify head in-place instead.
#         """
#
#         slow = head
#         fast = head
#         if fast.next is None:
#             return
#         # find middle node
#         while(fast is not None and fast.next is not None):
#             pre = slow
#             slow = slow.next
#             fast = fast.next.next
#         mid = slow
#         new_head = self.reverse(mid)
#         pre.next = None
#         self.merge(head,new_head)
#
#     def reverse(self,head):
#         pre = None
#         cur = head
#         while(cur):
#             tmp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = tmp
#         return pre
#
#     def merge(self,head1,head2):
#         cur1 = head1
#         cur2 = head2
#         while(cur1 and cur2):
#             pre1 = cur1
#             pre2 = cur2
#             tmp1 = cur1.next
#             cur1.next = cur2
#             tmp2 = cur2.next
#             cur2.next = tmp1
#             cur2 = tmp2
#             cur1 = tmp1
#         if cur1:
#             pre1.next=cur1
#         else:
#             pre2.next=cur2
from typing import Optional

from utils.LinkedList import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow, fast = head, head
        # find the mid of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        pre = None
        # reverse back part of the list
        while mid:
            temp = mid.next
            mid.next = pre
            pre = mid
            mid = temp

        p1, p2 = head, pre
        preHead = ListNode(-1)
        p3 = preHead
        # merge
        while p1 or p2:
            if p1:
                p3.next = p1
                p1 = p1.next
                p3 = p3.next
            if p2:
                p3.next = p2
                p2 = p2.next
                p3 = p3.next
            else:
                break
        return preHead.next

if __name__ == '__main__':
    head = ListNode(1)
    cur = head
    for i in range(2,6):
        new_node = ListNode(i)
        cur.next = new_node
        cur = cur.next
    solution = Solution()
    solution.reorderList(head)
    cur = head
    while(cur):
        print(cur.val)
        cur=cur.next
