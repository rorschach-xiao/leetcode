class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(-1)
        pre = new_head
        pre.next = head
        cur = head
        if cur is None or cur.next is None:
            return cur
        while(cur and cur.next):
            while(cur.next and cur.val == cur.next.val):
                cur = cur.next
            if pre.next != cur:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return new_head.next

if __name__ == '__main__':
    val_list = [1,1,2,3,3,4,5,6,7,8,8]
    head = ListNode(val_list[0])
    cur = head

    for val in val_list[1:]:
        node = ListNode(val)
        cur.next = node
        cur = cur.next

    solution = Solution()
    new_head = solution.deleteDuplicates(head)
    cur = new_head
    result_val_list = []
    while(cur):
        result_val_list.append(cur.val)
        cur = cur.next
    print(result_val_list)