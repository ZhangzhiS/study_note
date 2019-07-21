# 插入排序

插入排序是一种简单直观的排序方法。就是将元素插入到有序序列中，在有序序列中从后向前扫描，找到相应位置并插入。

在列表排序的过程中，可以将第一个元素看作是一个有序的序列，遍历后面的元素进行插入。

如下图所示，如果j大于i，则j插入到i后面，反之i和j更换位置，i所指的位置前移一位。

![insert](https://i.loli.net/2019/07/08/5d22af80db4d462231.png)

看看代码如何实现的

```python
def insert_sort(array: list) -> list:
    """
    插入排序
    :param array:
    :return:
    """
    # 第一个元素默认可以认为他是有序的
    # 从列表中第二个元素开始遍历
    for loop_index in range(1, len(array)):
        insertion_index = loop_index
        # 当插入位置的索引大于0，且小于前一位数的时候
        while insertion_index > 0 and (array[insertion_index - 1] > array[insertion_index]):
            # 交换两个元素的位置            
            array[insertion_index], array[insertion_index - 1] = array[
                insertion_index-1], array[insertion_index]
            insertion_index -= 1
    return array
```
