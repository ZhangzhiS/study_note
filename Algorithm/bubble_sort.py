"""
冒泡排序
比较相邻的两个元素,如果顺序有误则把他们交换位置.
"""


def bubble_sort(array):
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


if __name__ == '__main__':
    seq = [1, 2, 45, 5, 7, 313, 43, 6, 25, 9]
    bubble_sort(seq)
