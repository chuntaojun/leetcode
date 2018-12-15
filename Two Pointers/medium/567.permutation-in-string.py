#
# @lc app=leetcode id=567 lang=python
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (36.87%)
# Total Accepted:    34.5K
# Total Submissions: 93.7K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, write a function to return true if s2 contains
# the permutation of s1. In other words, one of the first string's permutations
# is the substring of the second string.
# 
# Example 1:
# 
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# 
# Example 2:
# 
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# 
# 
# 
# Note:
# 
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
# 
# 
#
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len_s1 = len(s1)
        s_1 = [0 for i in range(26)]
        s_2 = [0 for i in range(26)]
        for i in range(len(s1)):
            s_1[ord(s1[i]) - ord('a')] += 1
        l = 0
        r = l
        while l <= len(s2) - len_s1:
            if r == len(s2):
                break
            if r >= len_s1:
                l += 1
                s_2[ord(s2[l - 1]) - ord('a')] -= 1
            s_2[ord(s2[r]) - ord('a')] += 1
            r += 1
            if s_2 == s_1:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    s1 = "adc"
    s2 = "dcda"
    print(s.checkInclusion(s1=s1, s2=s2))
    
