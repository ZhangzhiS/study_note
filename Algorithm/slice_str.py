class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        temp = 0
        node = l1
        root = node
        while l1 or l2:
            if not l1:
                temp = l2.val + temp // 10
                l2 = l2.next
            elif not l2:
                temp = l1.val + temp // 10
                l1 = l1.next
            else:
                temp = l1.val + l2.val + temp // 10
                l1 = l1.next
                l2 = l2.next
            if not node.next and l2:
                node.next = ListNode(0)
            node.val = temp % 10
            if node.next:
                node = node.next
        if temp >= 10:
            node.next = ListNode(1)
        return root


if __name__ == '__main__':
    l = ListNode(2)
    l.next = ListNode(4)
    l.next.next = ListNode(3)
    ll = ListNode(5)
    ll.next = ListNode(6)
    ll.next.next = ListNode(4)
    r = Solution().addTwoNumbers(l, ll)
    print(r)

