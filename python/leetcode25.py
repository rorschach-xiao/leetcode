# Definition for singly-linked list.
from typing import Optional

from utils.LinkedList import ListNode

# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         result_head = None
#         pre_tail = None
#         cur = head
#         pre = None
#         final_head = None
#         is_reverse = True
#         while(cur):
#             group_head = cur
#             for i in range(k):
#                 pre = cur
#                 cur = cur.next
#                 if cur is None and i != k-1:
#                     final_head = group_head
#                     is_reverse = False
#                     break
#             if is_reverse == True:
#                 pre.next = None
#                 rev_head,rev_tail = self.reverse(group_head)
#                 if result_head is None: result_head = rev_head
#                 if pre_tail is not None:
#                     pre_tail.next = rev_head
#                 pre_tail = rev_tail
#
#         if final_head is not None:
#             if pre_tail is None:
#                 return head
#             else:
#                 pre_tail.next = final_head
#         return result_head
#
#     def reverse(self,head):
#         tail = head
#         pre = None
#         cur = head
#         while(cur):
#             tmp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = tmp
#         return [pre,tail]

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if k == 1:
            return head

        pre_head = ListNode(-1, head)
        pre_left, right_next = pre_head, None
        left_node, right_node = head, None
        idx = 1
        cur = head
        # initialize left and right
        left = 1
        right = left + k - 1
        while cur:
            if idx == left:
                left_node = cur
            if idx == right:
                right_node = cur
                right_next = cur.next
            # reverse nodes between left and right
            if right_node is not None:
                p = left_node
                pre = right_next
                while p != right_next:
                    temp = p.next
                    p.next = pre
                    pre = p
                    p = temp
                pre_left.next = right_node

                # update left and right
                left = right + 1
                right = left + k - 1

                # update pre_left and right_next
                cur = left_node
                pre_left = cur
                # update rigth_node
                right_node = None

            cur = cur.next
            idx += 1

        return pre_head.next

if __name__ == '__main__':
    l = [1,2,3,4,5]
    k = 2
    head = ListNode.list_to_linkedlist(l)
    solution = Solution()
    print(ListNode.linkedlist_to_list(solution.reverseKGroup(head,k)))

