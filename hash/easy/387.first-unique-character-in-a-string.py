#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (48.20%)
# Total Accepted:    199.6K
# Total Submissions: 414.1K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        c = [[0, 0] for i in range(26)]
        for i in range(len(s)):
            c[ord(s[i]) - ord('a')][0] = i
            c[ord(s[i]) - ord('a')][1] += 1
        minIndex = len(s) + 1
        for i in range(len(c)):
            if c[i][1] == 1:
                if c[i][0] < minIndex:
                    minIndex = c[i][0]
        return minIndex if minIndex != len(s) + 1 else -1