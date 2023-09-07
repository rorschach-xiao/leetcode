class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        pre = None

        for i in range(n):
            p2 = p2.next
        while(p2):
            pre=p1
            p1=p1.next
            p2=p2.next
        if pre:
            pre.next = p1.next
        else:
            head = head.next
        return head
if __name__=='__main__':
    head = ListNode(1)
    cur = head
    for i in range(2,5):
        node = ListNode(i)
        cur.next = node
        cur = cur.next
    solution = Solution()
    new_head = solution.removeNthFromEnd(head,2)
    cur = new_head
    while(cur):
        print(cur.val)
        cur=cur.next