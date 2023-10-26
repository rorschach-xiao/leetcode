from typing import Optional

from utils.LinkedList import ListNode
# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         new_head = ListNode(-1)
#         pre = new_head
#         pre.next = head
#         cur = head
#         if cur is None or cur.next is None:
#             return cur
#         while(cur and cur.next):
#             while(cur.next and cur.val == cur.next.val):
#                 cur = cur.next
#             if pre.next != cur:
#                 pre.next = cur.next
#             else:
#                 pre = cur
#             cur = cur.next
#         return new_head.next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        pre_head = ListNode(-1, head)
        pre = pre_head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                p = cur.next
                while p and p.val == cur.val:
                    p = p.next
                cur = p
                continue
            pre.next = cur
            pre = pre.next
            if cur is not None:
                cur = cur.next
        pre.next = cur
        return pre_head.next

if __name__ == '__main__':
    head = ListNode.list_to_linkedlist([1,1,2,3,3,4,5,6,7,8,8])
    solution = Solution()
    new_head = solution.deleteDuplicates(head)
    print(ListNode.linkedlist_to_list(new_head))