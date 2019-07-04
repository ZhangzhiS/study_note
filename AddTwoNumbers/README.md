# [两数相加](https://leetcode.com/problems/add-two-numbers/)

题目的中文地址：[两数相加](https://leetcode-cn.com/problems/add-two-numbers/)

```python
# 给出两个*非空*的链表用来表示两个*非负*的整数。其中，它们各自的位数是按照**逆序**的方式存储的，并且它们的每个节点只能存储一位数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
```

## 我的思路

- Runtime: *84 ms*, faster than 47.11% of Python3 online submissions for Add Two
 Numbers.
- Memory Usage: *13.3 MB*, less than 33.94% of Python3 online submissions for 
Add Two Numbers.

方法比较傻分了三步，代码就不贴在这来，有兴趣可以看看[add_two_numbers.py](add_two_numbers.py)

1. 将两个链表转为整数

2. 两数相加

3. 将结果转为链表

提交的代码虽然执行完成了，但是占用的空间以及使用的时间比较长，属于leetcode提交结果中排名末尾的。

## 别人家的思路

执行时间：**sample 48 ms submission**

用时*48ms*，虽然和我的84有点像😯。

看看代码

```python
# Definition for singly-linked list.
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
            node.next =  ListNode(1)
        return root

```

将两个链表对应的节点的值相加，每次都将相加的结果保存，在计算下个节点的时候，判断是否满10进1。

在程序中，root在内存地址中是等于l1的，所以其实是在链表l1上进行原地操作，会减少程序占用的空间。

用例子中的`(2 -> 4 -> 3) + (5 -> 6 -> 4)`来看看怎么执行的。

**注意**：在图片中的l1和l2是表示在函数执行过程中节点指向的变化，不是直真实的传入参数l1、l2两个参数的变化，这里需要了解Python里面深复制，浅复制，可变与不可变对象的区别。

初始状态

![start](https://i.loli.net/2019/06/20/5d0b19276a61455852.png)

第一次循环

![1](https://i.loli.net/2019/06/20/5d0b197fd26f094779.png)

第二次循环

![2](https://i.loli.net/2019/06/20/5d0b19ac7db1e73686.png)

第三次循环

![3](https://i.loli.net/2019/06/20/5d0b19dbb15c552165.png)

然后返回root，这里的root指向的其实是原来的l1。这个例子没有用到temp>10
的判断，这个是为了在最后一个节点，最大位数进行相加结果大于十，需要进1的时候准备的，比如：

3->6->6+3->6->6，如果没有最后的大于10进1，最后结果足足少了1000💰，不是个小数目。

可以自己进行调试，看看执行的过程。