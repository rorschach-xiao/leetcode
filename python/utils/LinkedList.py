class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

    @classmethod
    def list_to_linkedlist(cls, l):
        root = cls(l[0])
        cur = root
        n = len(l)
        for i in range(1, n):
            node = cls(l[i])
            cur.next = node
            cur = node
        return root

    @classmethod
    def list_to_linkedlist_with_cycle(cls, l, pos):
        root = cls(l[0])
        cur = root
        node_list = [cur]
        n = len(l)
        for i in range(1, n):
            node = cls(l[i])
            node_list.append(node)
            cur.next = node
            cur = node
        if pos != -1:
            cur.next = node_list[pos]
        return root

    @classmethod
    def linkedlist_to_list(cls, head):
        re = []
        cur = head
        while cur:
            re.append(cur.val)
            cur = cur.next
        return re



