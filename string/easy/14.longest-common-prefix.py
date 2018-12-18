#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (32.44%)
# Total Accepted:    367.1K
# Total Submissions: 1.1M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        ans = ""
        stand = strs[0]
        pointer = [i for i in range(len(stand))]
        len_s = [len(s) for s in strs]
        len_s.sort()
        for i in range(len_s[0]):
            t = set([strs[s][pointer[i]] for s in range(1, len(strs))])
            if len(t) != 1:
                return ans
            else:
                if t.pop() == stand[i]:
                    ans += stand[i]
                else:
                    return ans
        return ans
