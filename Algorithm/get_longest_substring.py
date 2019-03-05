"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


def length_of_longest_substring(s):
    s_length = len(s)
    if s_length == 1:
        return 1
    i = 0
    j = 1
    max_len = 0
    max_index = s_length-1
    while j <= max_index:
        if s[j] not in s[i: j]:
            temp_max_len = (j - i) + 1
            if temp_max_len > max_len:
                max_len = temp_max_len
            j += 1
        else:
            i += 1
            # j += 1
    return max_len


if __name__ == '__main__':
    # s = "abcabcbb"
    # s = "bbbbbbbb"
    s = "pwwkew"
    s = "aedgdterguiiktmjynfh"
    print(length_of_longest_substring(s))

