#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (43.12%)
# Total Accepted:    269.7K
# Total Submissions: 625.5K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strsMap = {}
        ans = []
        for i in range(len(strs)):
            loc = self.hash_func(s=strs[i])
            if strsMap.__contains__(loc):
                strsMap[loc].append(strs[i])
            else:
                strsMap[loc] = [strs[i]]
        for _, v in strsMap.items():
            ans.append(v)
        return ans

    
    def hash_func(self, s):
        _t = []
        for i in range(len(s)):
            _t.append(ord(s[i]) - 87)
        _t.sort()
        hashValue = 0

        for i in range(len(_t)):
            hashValue = hashValue * 100 + _t[i]
        return hashValue
