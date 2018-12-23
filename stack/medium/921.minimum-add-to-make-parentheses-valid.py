#
# @lc app=leetcode id=921 lang=python
#
# [921] Minimum Add to Make Parentheses Valid
#
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
#
# algorithms
# Medium (68.95%)
# Total Accepted:    11.6K
# Total Submissions: 16.8K
# Testcase Example:  '"())"'
#
# Given a string S of '(' and ')' parentheses, we add the minimum number of
# parentheses ( '(' or ')', and in any positions ) so that the resulting
# parentheses string is valid.
# 
# Formally, a parentheses string is valid if and only if:
# 
# 
# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are valid
# strings, or
# It can be written as (A), where A is a valid string.
# 
# 
# Given a parentheses string, return the minimum number of parentheses we must
# add to make the resulting string valid.
# 
# 
# 
# Example 1:
# 
# 
# Input: "())"
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: "((("
# Output: 3
# 
# 
# 
# Example 3:
# 
# 
# Input: "()"
# Output: 0
# 
# 
# 
# Example 4:
# 
# 
# Input: "()))(("
# Output: 4
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 1000
# S only consists of '(' and ')' characters.
# 
# 
# 
# 
# 
# 
# 
# 
# 
#
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        if len(S) == 0:
            return 0
        self.stack = [S[0]]
        for i in range(1, len(S)):
            if len(self.stack) == 0:
                self.stack.append(S[i])
            elif self.stack[-1] == '(' and S[i] == ')':
                self.stack.pop()
            else:
                self.stack.append(S[i])
        return len(self.stack)


if __name__ == '__main__':
    s = Solution()
    t = "()))(("
    print(s.minAddToMakeValid(S=t))
