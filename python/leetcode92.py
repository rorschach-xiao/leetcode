# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        self.reverse_len=right-left
        if self.reverse_len==0:
            return head
        cur = head
        pre = None

        for _ in range(left-1):
            pre = cur
            cur = cur.next
        left_node = tail = cur
        right_node = None
        for _ in range(self.reverse_len+1):
            right_node = tail
            tail = tail.next
        if pre:
            pre.next = None
        right_node.next = None
        new_left,new_right = self.reverse(left_node)
        if pre:
            pre.next = new_left
        new_right.next = tail
        if pre:
            return head
        else:
            return new_left

    def reverse(self,head):
        cur = head
        tail = head
        pre = None
        while(cur):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre,tail

if __name__ =='__main__':
    solution=Solution()
    head = ListNode(1)
    cur = head
    for i in range(2,6):
        new_node = ListNode(i)
        cur.next = new_node
        cur = cur.next
    left = 2
    right = 4
    head = solution.reverseBetween(head,left,right)
    cur = head
    while(cur):
        print(cur.val)
        cur=cur.next