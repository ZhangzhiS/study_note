"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""


def find_median_sorted_arrays(nums1: list, nums2: list) -> float:
    nums = nums1+nums2
    nums = sorted(nums)
    print(nums)
    length = len(nums)
    if length == 1:
        return float(nums[0])
    elif length % 2:
        return float(nums[length // 2 ])
    else:
        mid = length // 2
        return (nums[mid]+nums[mid-1]) / 2


if __name__ == '__main__':
    a = [1, 3]
    b = [2]
    print(find_median_sorted_arrays(a, b))
