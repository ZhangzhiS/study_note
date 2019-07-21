#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-


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
            # 交换两个数字的位置            
            array[insertion_index], array[insertion_index - 1] = array[
                insertion_index-1], array[insertion_index]
            insertion_index -= 1
    return array


if __name__ == '__main__':
    array_list = [1, 2, 45, 5, 7, 313, 43, 6, 25, 9]
    print(insert_sort(array_list))
