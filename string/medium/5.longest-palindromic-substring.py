#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (25.94%)
# Total Accepted:    435.5K
# Total Submissions: 1.7M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(list(s)) + '#'
        p = [0 for i in range(len(s))]
        mx = 0
        _id = 0
        for i in range(1, len(s)):
            p[i] = min(p[2 * _id - i], mx - i) if mx > i else 1
            while i + p[i] < len(s) and s[i + p[i]] == s[i - p[i]]:
                p[i] += 1
            if i + p[i] > mx:
                mx = i + p[i]
                _id = i
        ans = 0
        loc = 0
        for i in range(len(p)):
            if p[i] - 1 > ans:
                ans = p[i] - 1
                loc = i
        return s[loc - ans: loc + ans + 1].replace('#', '')


if __name__ == '__main__':
    s = Solution()
    t = "babad"
    s.longestPalindrome(s=t)
    
