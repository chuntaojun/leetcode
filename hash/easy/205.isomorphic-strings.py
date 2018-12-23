#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (36.14%)
# Total Accepted:    175K
# Total Submissions: 484.1K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# Example 1:
# 
# 
# Input: s = "egg", t = "add"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "foo", t = "bar"
# Output: false
# 
# Example 3:
# 
# 
# Input: s = "paper", t = "title"
# Output: true
# 
# Note:
# You may assume both s and t have the same length.
# 
#
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_map = {}
        is_map = {}
        for i in range(len(s)):
            if char_map.__contains__(s[i]):
                if char_map[s[i]] != t[i]:
                    return False
            else:
                if is_map.__contains__(t[i]):
                    return False
                is_map[t[i]] = True
                char_map[s[i]] = t[i]
        return True


if __name__ == '__main__':
    s = Solution()
    t1 = "ab"
    t2 = "aa"
    print(s.isIsomorphic(s=t1, t=t2))
