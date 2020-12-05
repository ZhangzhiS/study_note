# [两数之和](https://leetcode.com/problems/two-sum/)

题目的中文地址：[两数之和](https://leetcode-cn.com/problems/two-sum/)

```python
# 编写一个函数来查找字符串数组中的最长公共前缀。 
#  如果不存在公共前缀，返回空字符串 ""。 
#  示例 1: 
#  输入: ["flower","flow","flight"]
# 输出: "fl"
#  示例 2: 
#  输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#  说明: 
#  所有输入只包含小写字母 a-z 。 
#  Related Topics 字符串
```


逻辑：

使用Python的zip函数，将列表中的每个字符串当做迭代对象，对迭代出来的字符去重，如果是同一个字符，则代表大家都一样，将该字符添加到结果中，否则跳出循环。返回已有的结果。上代码：


```python
class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        r = ""
        for i in zip(*strs):
            # 等于1，表示迭代的字符相同 
            if len(set(i)) == 1:
                r += i[0]
            # 否则跳出 
            else:
                break
        return r
```
