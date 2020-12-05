# [有效的括号](https://leetcode.com/problems/valid-parentheses/)

题目的中文地址：[有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

题目：

```python
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。 
#  有效字符串需满足： 
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  注意空字符串可被认为是有效字符串。 
#  示例 1: 
#  输入: "()"
# 输出: true
#  示例 2: 
#  输入: "()[]{}"
# 输出: true
#  示例 3: 
#  输入: "(]"
# 输出: false
#  示例 4: 
#  输入: "([)]"
# 输出: false
#  示例 5: 
#  输入: "{[]}"
# 输出: true 
```

题解：

比较典型的一个堆栈问题，重点思路就是当遇到闭合的括号的时候，上一个括号必须是它的反括号，使用栈的方式来实现的话，
遇到闭合括号，则从堆栈中弹出上一个括号，看是否是它的反括号。还是看下面的逻辑部分吧，更清晰一点，逻辑部分来自LeetCode。

逻辑：

1. 初始化栈 S。

2. 一次处理表达式的每个括号。

3. 如果遇到开括号，我们只需将其推到栈上即可。这意味着我们将稍后处理它，让我们简单地转到前面的 子表达式。

4. 如果我们遇到一个闭括号，那么我们检查栈顶的元素。如果栈顶的元素是一个 相同类型的 左括号，那么我们将它从栈中弹出并继续处理。否则，这意味着表达式无效。

5. 如果到最后我们剩下的栈中仍然有元素，那么这意味着表达式无效。

直接上代码了：

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        res_list = []
        for i in s:
            if i in check_map:
                tmp = res_list.pop() if res_list else "#"
                if check_map[i] != tmp:
                    return False
            else:
                res_list.append(i)
        if not res_list:
            return True
        return False
```
