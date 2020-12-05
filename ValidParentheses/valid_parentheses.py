#!/usr/bin/env python3.8


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
