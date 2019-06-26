# 二分查找法

二分查找也称折半查找（Binary Search），它是一种效率较高的查找方法。
但是，折半查找要求线性表必须采用顺序存储结构，而且表中元素按关键字有序排列

**注意**：必须是从有序列表中找。

看看下面的例子，从列表[1, 2, 3, 4, 5, 6, 7, 8, 9]中找到数字"2"所在的位置。

使用二分查找法找到数字"2"的过程图解

![二分查找](https://i.loli.net/2019/06/26/5d12e34ab9cc871563.png)

通过与列表中间的数做比较，判断需要寻找的数在列表的哪一部分，直到找到该元素的位置，或者该数字不存在于列表中。

循环条件就是两个边界位置的索引，小的**小于等于**大的。看看有哪些跳出循环的条件：

1. 要寻找的数大于最大值或者小于最小值。

2. 找到需要查找的数

3. 循环结束

下面看看代码是怎么实现的吧：

```python
def binary_search(target: list, num: int) -> int or None:
    """
    二分查找
    :param target: 有序数组
    :param num: 要查找的数字
    :return: 要查找的数字所在的位置或者None
    """
    low = 0  # 要查找的列表的左边边界索引位置
    high = len(target) - 1  # 要查找的列表的右边边界索引位置
    while low <= high:
        if num < target[low] or num > target[high]:
            # 如果要查找的数的小于最小值或者大于最大值，则结束
            return None
        # 找到位于列表中间的元素的索引位置
        mid = int((low + high) / 2)
        # 该元素的值
        guess = target[mid]
        if guess == num:
            return mid
        elif guess > num:
            high = mid - 1
        else:
            low = mid + 1
    return None
```

> 建议自己画图或者但不调试看看查找过程。
