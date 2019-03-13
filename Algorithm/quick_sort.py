"""
快速排序法
"""


def quick_sort(array):
    """快速排序法"""
    return q_sort(array, 0, len(array) - 1)


def q_sort(array, left, right):
    if left < right:
        pivot = partition(array, left, right)
        # 左右分治
        q_sort(array, left, pivot-1)
        q_sort(array, pivot+1, right)
    return array


def partition(array, left, right):
    """
    分割函数
    :param array: 数组
    :param left: 左边的起始索引
    :param right: 右边的结束索引
    :return: 分割位置的索引
    """
    pivot_key = array[left]  # 将数组的第一个值设置为参考值

    while left < right:
        while left < right and array[right] >= pivot_key:
            right -= 1
        # 从右边开始找，找到比参考值小的数的时候，将右边的值赋值给左边
        array[left] = array[right]
        while left < right and array[left] <= pivot_key:
            left += 1
        # 继续从左边开始找，找到比参考值大的数的时候，将左边的值复制给右边
        array[right] = array[left]
    # 上面的步骤在赋值过程中，参考值被替换，数组中参考值没有了，将参考值赋值给左边最后的索引
    array[left] = pivot_key
    return left


if __name__ == '__main__':
    a = [5, 9, 1, 11, 6, 7, 2, 4, 8]
    b = quick_sort(a)
    print(b)
