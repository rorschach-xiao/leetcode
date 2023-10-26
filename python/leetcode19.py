from typing import Optional

from utils.LinkedList import ListNode
# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         p1 = head
#         p2 = head
#         pre = None
#
#         for i in range(n):
#             p2 = p2.next
#         while(p2):
#             pre=p1
#             p1=p1.next
#             p2=p2.next
#         if pre:
#             pre.next = p1.next
#         else:
#             head = head.next
#         return head
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        slow, fast = head, head
        i = 0
        while i < n and fast:
            fast = fast.next
            i += 1
        if i != n:
            return head
        pre_head = ListNode(-1, head)
        pre = pre_head
        while(fast):
            pre = slow
            slow = slow.next
            fast = fast.next
        pre.next = slow.next

        return pre_head.next
if __name__=='__main__':
    head = ListNode.list_to_linkedlist([1,2,3,4,5])
    solution = Solution()
    new_head = solution.removeNthFromEnd(head,2)
    print(ListNode.linkedlist_to_list(new_head))