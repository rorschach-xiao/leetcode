# Definition for singly-linked list.
from typing import Optional

from utils.LinkedList import ListNode
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         carrying=0
#         cur1=l1
#         cur2=l2
#         pre1=None
#         while(cur1 and cur2):
#             cur_digit = cur1.val+cur2.val+carrying
#             if cur_digit>=10:
#                 carrying=1
#                 cur1.val = cur_digit%10
#             else:
#                 carrying=0
#                 cur1.val = cur_digit
#             pre1 = cur1
#             cur1 = cur1.next
#             cur2 = cur2.next
#         if pre1 is None:
#             return cur2
#         else:
#             if cur2:
#                 pre1.next = cur2
#                 pre2 = pre1
#                 while(carrying==1 and cur2):
#                     cur_digit = cur2.val+carrying
#                     if cur_digit>=10:
#                         cur2.val = cur_digit%10
#                         carrying=1
#                     else:
#                         cur2.val = cur_digit
#                         carrying=0
#                     pre2 = cur2
#                     cur2 = cur2.next
#                 if carrying==1 :
#                     new_node = ListNode(1)
#                     pre2.next = new_node
#             elif cur1:
#                 while(carrying==1 and cur1):
#                     cur_digit = cur1.val+carrying
#                     if cur_digit>=10:
#                         cur1.val = cur_digit%10
#                         carrying=1
#                     else:
#                         cur1.val = cur_digit
#                         carrying=0
#                     pre1 = cur1
#                     cur1 = cur1.next
#                 if carrying==1 :
#                     new_node = ListNode(1)
#                     pre1.next = new_node
#             else:
#                 if carrying==1 :
#                     new_node = ListNode(1)
#                     pre1.next = new_node
#             return l1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        p1 = l1
        p2 = l2
        sum_head = None
        carry = 0
        while p1 and p2:
            s = p1.val + p2.val + carry
            carry = s // 10
            digit = s % 10
            if sum_head is None:
                sum_head = ListNode(digit)
                p3 = sum_head
            else:
                new_node = ListNode(digit)
                p3.next = new_node
                p3 = p3.next
            p1 = p1.next
            p2 = p2.next

        while (p1):
            s = p1.val + carry
            carry = s // 10
            digit = s % 10
            p3.next = ListNode(digit)
            p3 = p3.next
            p1 = p1.next

        while (p2):
            s = p2.val + carry
            carry = s // 10
            digit = s % 10
            p3.next = ListNode(digit)
            p3 = p3.next
            p2 = p2.next

        if carry != 0:
            p3.next = ListNode(carry)

        return sum_head



if __name__=='__main__':
    solution=Solution()
    l1 = [9,9,9,9]
    l2 = [9,9,9,9,9,9]
    head1 = ListNode.list_to_linkedlist(l1)
    head2 = ListNode.list_to_linkedlist(l2)
    head3 = solution.addTwoNumbers(head1, head2)
    print(ListNode.linkedlist_to_list(head3))