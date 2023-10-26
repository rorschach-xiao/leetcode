from typing import Optional

from utils.LinkedList import ListNode
# class Solution(object):
#     def reverseBetween(self, head, left, right):
#         """
#         :type head: ListNode
#         :type left: int
#         :type right: int
#         :rtype: ListNode
#         """
#         self.reverse_len=right-left
#         if self.reverse_len==0:
#             return head
#         cur = head
#         pre = None
#
#         for _ in range(left-1):
#             pre = cur
#             cur = cur.next
#         left_node = tail = cur
#         right_node = None
#         for _ in range(self.reverse_len+1):
#             right_node = tail
#             tail = tail.next
#         if pre:
#             pre.next = None
#         right_node.next = None
#         new_left,new_right = self.reverse(left_node)
#         if pre:
#             pre.next = new_left
#         new_right.next = tail
#         if pre:
#             return head
#         else:
#             return new_left
#
#     def reverse(self,head):
#         cur = head
#         tail = head
#         pre = None
#         while(cur):
#             tmp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = tmp
#         return pre,tail
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return None
        pre_head = ListNode(-1, head)
        pre_left, right_next = pre_head, None
        left_node, right_node = head, head
        idx = 1
        cur = head
        # find the start and end nodes
        while cur:
            if idx + 1 == left:
                pre_left = cur
            if cur.next and idx == right:
                right_next = cur.next
            if idx == left:
                left_node = cur
            if idx == right:
                right_node = cur
            cur = cur.next
            idx += 1

        # reverse nodes between left and right
        cur = left_node
        pre = right_next
        while cur != right_next:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        pre_left.next = right_node

        return pre_head.next

if __name__ =='__main__':
    solution=Solution()
    head = ListNode.list_to_linkedlist([1,2,3,4,5])
    left = 2
    right = 4
    head = solution.reverseBetween(head,left,right)
    print(ListNode.linkedlist_to_list(head))