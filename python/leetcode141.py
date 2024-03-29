from typing import Optional
from utils.LinkedList import ListNode


# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if head is None:
#             return False
#         hashset = set()
#         cur = head
#         while cur not in hashset and cur is not None:
#             hashset.add(cur)
#             cur = cur.next
#         return cur is not None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        return fast == slow

if __name__ == '__main__':
    solution = Solution()
    root = ListNode.list_to_linkedlist_with_cycle([3,2,0,-4], -1)
    print(solution.hasCycle(root))
