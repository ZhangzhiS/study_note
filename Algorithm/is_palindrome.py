"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""
import re


def is_palindrome(s: str) -> bool:
    s = re.findall(r"[a-zA-Z0-9]", s)
    s = "".join(s)
    print(s)
    # s = s.replace(" ", "")
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    a = "A man, a plan, a canal: Panama"
    print(is_palindrome(a))
