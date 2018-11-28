#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (34.97%)
# Total Accepted:    442.4K
# Total Submissions: 1.3M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        t = [s[0]]
        top_c = s[0]
        for i in range(1, len(s)):
            if top_c == '' and len(t) != 0:
                top_c = t[-1]
            t.append(s[i])
            if top_c == '' and len(t) == 1:
                top_c = t[-1]
            if top_c == '{' and t[-1] == '}':
                t.pop()
                if t[-1] ==  top_c:
                    t.pop()
                top_c = ''
            elif top_c == '[' and t[-1] == ']':
                t.pop()
                if t[-1] ==  top_c:
                    t.pop()
                top_c = ''
            elif top_c == '(' and t[-1] == ')':
                t.pop()
                if t[-1] ==  top_c:
                    t.pop()
                top_c = ''
            else:
                top_c = t[-1]
        return len(t) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValid(s="{[]}()[]{}"))
