# 冒泡排序

冒泡排序是一种比较简单的排序方法。通过比较两个相邻的元素，如果他们的顺序有误，就把他们交换顺序。

比如要将一个列表进行排序，就是对该列表进行遍历，将每次拿到的元素与其他元素进行比较交换位置，每一次遍历只排好一个数字。

下面看看图示：

一次遍历：

![loop](https://i.loli.net/2019/06/26/5d1328e72991010400.png)

后续的遍历也只是循环这样的操作，就不再用图解释了。

看看python实现的[代码](bubble_sort.py):

```python
def bubble_sort(array: list) -> list:
    """
    冒泡排序
    冒泡排序要排序n个数，由于每遍历一趟只排好一个数字，
    则需要遍历n-1趟，所以最外层循环是要循环n-1次，
    而每次趟遍历中需要比较每归位的数字，
    则要在n-1次比较中减去已排好的i位数字，
    则第二层循环要遍历是n-1-i次
    """
    array_len = len(array)
    for i in range(array_len - 1):
        for j in range(array_len - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)
    return array
```

> 建议自己画图或者Debug调试看看排序过程中元素的变化，更好去理解。
