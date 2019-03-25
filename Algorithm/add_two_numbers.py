"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_nums(l1: ListNode, l2: ListNode) -> ListNode:
    """两数相加"""
    n1 = list_node_to_nums(l1)
    n2 = list_node_to_nums(l2)
    result = n1 + n2
    r = nums_to_list_node(result)
    return r


def list_node_to_nums(list_node: ListNode) -> int:
    num_list = []
    temp_node = list_node
    while True:

        if temp_node.next is None:
            num_list.append(temp_node.val)
            break
        else:
            num_list.append(temp_node.val)
            temp_node = temp_node.next
    nums = int("".join(num_list[::-1]))
    return nums


def nums_to_list_node(nums: int) -> ListNode:
    nums_list = list(str(nums))
    # print(nums_list)
    last = True
    temp_node = None
    for i in nums_list:
        # print(i)
        if last is True:
            new_node = ListNode(i)
            last = False
            temp_node = new_node
        else:
            new_node = ListNode(i)
            new_node.next = temp_node
            temp_node = new_node

    return new_node


if __name__ == '__main__':
    a = 243
    b = 564
    l1 = nums_to_list_node(a)
    l2 = nums_to_list_node(b)
    r = add_two_nums(l1, l2)
    print(list_node_to_nums(r))
