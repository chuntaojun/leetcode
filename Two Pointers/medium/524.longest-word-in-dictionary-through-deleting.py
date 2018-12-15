#
# @lc app=leetcode id=524 lang=python
#
# [524] Longest Word in Dictionary through Deleting
#
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (44.19%)
# Total Accepted:    33.3K
# Total Submissions: 75.4K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
# 
# Given a string and a string dictionary, find the longest string in the
# dictionary that can be formed by deleting some characters of the given
# string. If there are more than one possible results, return the longest word
# with the smallest lexicographical order. If there is no possible result,
# return the empty string.
# 
# Example 1:
# 
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# 
# Output: 
# "apple"
# 
# 
# 
# 
# Example 2:
# 
# Input:
# s = "abpcplea", d = ["a","b","c"]
# 
# Output: 
# "a"
# 
# 
# 
# Note:
# 
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
# 
# 
#
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key=lambda x:(-len(x), x))
        for i in range(len(d)):
            tmp = list(s)
            a = 0; b = 0
            while a < len(tmp) and b < len(d[i]):
                if tmp[a] == d[i][b]:
                    a += 1
                    b += 1
                else:
                    a += 1
                if b == len(d[i]):
                    return d[i]
        return ""


if __name__ == '__main__':
    s = Solution()
    t_1 = "aewfafwafjlwajflwajflwafj"
    t_2 = ["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]
    print(s.findLongestWord(s=t_1, d=t_2))
