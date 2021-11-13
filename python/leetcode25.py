# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linklist(l):
    head_node = None
    pre = None
    for n in l:
        cur_node = ListNode(n)
        if pre is not None: pre.next = cur_node
        if head_node is None:
            head_node = cur_node
        pre = cur_node
    return head_node

def print_linklist(head):
    cur = head
    while (cur):
        print(cur.val)
        cur = cur.next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        result_head = None
        pre_tail = None
        cur = head
        pre = None
        final_head = None
        is_reverse = True
        while(cur):
            group_head = cur
            for i in range(k):
                pre = cur
                cur = cur.next
                if cur is None and i != k-1:
                    final_head = group_head
                    is_reverse = False
                    break
            if is_reverse == True:
                pre.next = None
                rev_head,rev_tail = self.reverse(group_head)
                if result_head is None: result_head = rev_head
                if pre_tail is not None:
                    pre_tail.next = rev_head
                pre_tail = rev_tail

        if final_head is not None:
            if pre_tail is None:
                return head
            else:
                pre_tail.next = final_head
        return result_head

    def reverse(self,head):
        tail = head
        pre = None
        cur = head
        while(cur):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return [pre,tail]

if __name__ == '__main__':
    l = [1,2,3,4,5]
    k = 3
    head = create_linklist(l)
    solution = Solution()
    print_linklist(solution.reverseKGroup(head,k))

