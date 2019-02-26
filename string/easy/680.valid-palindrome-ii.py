#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (33.73%)
# Total Accepted:    62.2K
# Total Submissions: 184.5K
# Testcase Example:  '"aba"'
#
# 
# Given a non-empty string s, you may delete at most one character.  Judge
# whether you can make it a palindrome.
# 
# 
# Example 1:
# 
# Input: "aba"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# 
# 
# 
# Note:
# 
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
# 
# 
#
class Solution(object):
    def __init__(self):
        self.diff = 0

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        if r < 0:
            return True
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                break
        print(l, r)
        if l == r or l - 1 == r:
            return True
        else:
            self.diff += 1
            if self.diff > 1:
                return False
            if s[l] == s[r - 1] or s[l + 1] == s[r]:
                return self.validPalindrome(s=s[l + 1: r - 1]) or self.validPalindrome(s=s[l + 2: r])
            else:
                return False


if __name__ == '__main__':
    s = Solution()
    t = "abca"
    print(s.validPalindrome(s=t))
    
