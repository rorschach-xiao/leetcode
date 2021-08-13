# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        heads = self.cut(head)
        if len(heads) == 1:
            return heads[0]
        else:
            left, right = heads
            sorted_left = self.sortList(left)
            sorted_right = self.sortList(right)
            new_head = self.merge(sorted_left, sorted_right)
            return new_head

    def cut(self, head):
        slow = head
        fast = head
        pre = None
        while (fast and fast.next):
            fast = fast.next.next
            pre = slow
            slow = slow.next
        if pre is None:
            return [head]
        else:
            pre.next = None
            return [head, slow]

    def merge(self, head1, head2):
        new_head = ListNode(-1)
        cur1 = head1
        cur2 = head2
        cur = new_head
        new_head.next = cur1 if cur1.val < cur2.val else cur2
        while (cur1 and cur2):
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
                cur = cur.next
            else:
                cur.next = cur2
                cur2 = cur2.next
                cur = cur.next

        cur.next = cur2 if cur2 else cur1
        return new_head.next

if __name__ == '__main__':
    val_list = [-1,5,3,4,0]
    head = ListNode(val_list[0])
    cur = head
    for val in val_list[1:]:
        node = ListNode(val)
        cur.next = node
        cur = cur.next
    solution = Solution()
    new_head = solution.sortList(head)
    cur = new_head
    new_val_list = []
    while(cur):
        new_val_list.append(cur.val)
        cur=cur.next
    print(new_val_list)