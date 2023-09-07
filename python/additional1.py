class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def Sort(self,head):
        head_odd,head_even = self.split(head)
        head_even = self.reverse(head_even)
        new_head = self.merge(head_odd,head_even)
        return new_head

    def split(self,head):
        head_odd = head
        head_even = head.next
        p_odd = head
        p_even = head.next
        while(p_even and p_even.next):
            p_odd.next = p_odd.next.next
            p_even.next = p_even.next.next
            p_odd = p_odd.next
            p_even = p_even.next
        p_odd.next = None
        return head_odd,head_even


    def merge(self,head1,head2):
        cur1 = head1
        cur2 = head2
        init_flag = 0
        while(cur1 and cur2):
            if init_flag==0:
                if cur1.val > cur2.val:
                    new_head = head2
                    cur2 = cur2.next
                else:
                    new_head = head1
                    cur1 = cur1.next
                cur3 = new_head
                init_flag=1
                continue
            if cur1.val > cur2.val:
                cur3.next = cur2
                cur2 = cur2.next
            else:
                cur3.next = cur1
                cur1 = cur1.next
            cur3 = cur3.next
        if cur1:
            cur3.next = cur1
        elif cur2:
            cur3.next = cur2
        return new_head

    def reverse(self,head):
        pre = None
        cur = head
        while(cur):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

if __name__ == '__main__':
    a = [1,8,3,6,5,4,7,2]
    head = ListNode(a[0])
    cur = head
    for n in a[1:]:
        new_node = ListNode(n)
        cur.next = new_node
        cur = cur.next

    solution = Solution()
    new_head = solution.Sort(head)
    cur = new_head
    while(cur):
        print(cur.val)
        cur = cur.next


