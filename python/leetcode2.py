# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carrying=0
        cur1=l1
        cur2=l2
        pre1=None
        while(cur1 and cur2):
            cur_digit = cur1.val+cur2.val+carrying
            if cur_digit>=10:
                carrying=1
                cur1.val = cur_digit%10
            else:
                carrying=0
                cur1.val = cur_digit
            pre1 = cur1
            cur1 = cur1.next
            cur2 = cur2.next
        if pre1 is None:
            return cur2
        else:
            if cur2:
                pre1.next = cur2
                pre2 = pre1
                while(carrying==1 and cur2):
                    cur_digit = cur2.val+carrying
                    if cur_digit>=10:
                        cur2.val = cur_digit%10
                        carrying=1
                    else:
                        cur2.val = cur_digit
                        carrying=0
                    pre2 = cur2
                    cur2 = cur2.next
                if carrying==1 :
                    new_node = ListNode(1)
                    pre2.next = new_node
            elif cur1:
                while(carrying==1 and cur1):
                    cur_digit = cur1.val+carrying
                    if cur_digit>=10:
                        cur1.val = cur_digit%10
                        carrying=1
                    else:
                        cur1.val = cur_digit
                        carrying=0
                    pre1 = cur1
                    cur1 = cur1.next
                if carrying==1 :
                    new_node = ListNode(1)
                    pre1.next = new_node
            else:
                if carrying==1 :
                    new_node = ListNode(1)
                    pre1.next = new_node
            return l1
if __name__=='__main__':
    solution=Solution()
    l1 = [9,9,9,9]
    l2 = [9,9,9,9,9,9]
    head1 = ListNode(l1[0])
    head2 = ListNode(l2[0])
    cur1 = head1
    cur2 = head2

    for n in l1[1:]:
        node = ListNode(n)
        cur1.next = node
        cur1 = cur1.next
    for n in l2[1:]:
        node = ListNode(n)
        cur2.next = node
        cur2 = cur2.next
    l3 = solution.addTwoNumbers(head1,head2)
    cur3 = l3
    result = []
    while(cur3):
        result.append(cur3.val)
        cur3=cur3.next
    print(result)