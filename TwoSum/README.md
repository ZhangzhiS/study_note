# [两数之和](https://leetcode.com/problems/two-sum/)

题目的中文地址：[两数之和](https://leetcode-cn.com/problems/two-sum/)

```python
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# 示例:
#   给定 nums = [2, 7, 11, 15], target = 9
#   因为 nums[0] + nums[1] = 2 + 7 = 9
#   所以返回 [0, 1]
```

一道简单的题，比较直接的方法就是对列表进行循环遍历了，但是时间复杂度会比较高，这里就不进行介绍了，说说使用字典模拟哈希的方法。

```python
def two_sum(nums: list, target: int) -> list or bool:
    """
    两数之和
    :param nums:
    :param target:
    :return:
    """
    hash_map = {}
    for index, num in enumerate(nums):
        another_num = target - num
        # 找到与当前数字对应的另一个数字
        if another_num in hash_map:
            # 如果要找的另外一个数字在字典中了，那就输出两个数字的索引
            return [hash_map[another_num], index]
        hash_map[num] = index
    return False
```
