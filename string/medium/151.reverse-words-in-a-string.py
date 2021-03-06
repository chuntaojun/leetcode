#
# @lc app=leetcode id=151 lang=python
#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (15.78%)
# Total Accepted:    241K
# Total Submissions: 1.5M
# Testcase Example:  '"the sky is blue"'
#
# Given an input string, reverse the string word by word.
# 
# Example:  
# 
# 
# Input: "the sky is blue",
# Output: "blue is sky the".
# 
# 
# Note:
# 
# 
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed
# string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the
# reversed string.
# 
# 
# Follow up: For C programmers, try to solve it in-place in O(1) space.
# 
#
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        tmp = []
        for i in range(len(s)):
            if s[i] == " ":
                if len(tmp) != 0:
                    ans.insert(0, ''.join(tmp))
                    tmp = []
                continue
            else:
                tmp.append(s[i])
        if len(tmp) != 0:
            ans.insert(0, ''.join(tmp))
        return ' '.join(ans)


if __name__ == '__main__':
    s = Solution()
    s.reverseWords(s="the sky is blue")
    
