"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


def two_sum(nums, target):
    """

    :param nums: list[int]
    :param target: int
    :return: List[int]
    """
    hash_map = {}
    for index, num in enumerate(nums):
        another_number = target - num
        if another_number in hash_map:
            return [hash_map[another_number], index]
        hash_map[num] = index

    return False


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    # nums = [3, 3]
    target = 9
    # target = 6
    print(two_sum(nums, target))
