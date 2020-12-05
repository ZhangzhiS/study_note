#!/usr/bin/env python3.8
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
            if len(set(i)) == 1:
                r += i[0]
            else:
                break
        return r
