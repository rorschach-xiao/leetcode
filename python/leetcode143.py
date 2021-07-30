# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head
        if fast.next is None:
            return 
        # find middle node
        while(fast is not None and fast.next is not None):
            pre = slow
            slow = slow.next
            fast = fast.next.next
        mid = slow
        new_head = self.reverse(mid)
        pre.next = None
        self.merge(head,new_head)

    def reverse(self,head):
        pre = None
        cur = head
        while(cur):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def merge(self,head1,head2):
        cur1 = head1
        cur2 = head2
        while(cur1 and cur2):
            pre1 = cur1
            pre2 = cur2
            tmp1 = cur1.next
            cur1.next = cur2
            tmp2 = cur2.next
            cur2.next = tmp1
            cur2 = tmp2
            cur1 = tmp1
        if cur1:
            pre1.next=cur1
        else:
            pre2.next=cur2

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
