# [整数反转](https://leetcode.com/problems/reverse-integer/)

题目的中文地址：[整数反转](https://leetcode.com/problems/reverse-integer/)

比较简单的题目，我的实现思路是先将数字转为字符串，然后倒序，再次转为数字，再根据原始数字判断结果的正负即可。

在实现过程中，比较取巧的Python内置的取绝对值的函数。思路没什么可写的，毕竟题目比较简单，直接看代码吧。

```python
class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        tmp = str(abs(x))
        sorted_str = tmp[::-1]
        result = int(sorted_str)
        if result > 2**31:
            return 0
        if x < 0:
            return 0 - result
        return result
```