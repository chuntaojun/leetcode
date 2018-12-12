#
# @lc app=leetcode id=150 lang=python
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (30.53%)
# Total Accepted:    139.4K
# Total Submissions: 456.6K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
# 
# Note:
# 
# 
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would
# always evaluate to a result and there won't be any divide by zero
# operation.
# 
# 
# Example 1:
# 
# 
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# 
# Example 2:
# 
# 
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# 
# Example 3:
# 
# 
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
#
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def add(a, b):
            return a + b
        
        def sub(a, b):
            return b - a
        
        def mul(a, b):
            return a * b
        
        def div(a, b):
            return int(b / a)

        cul = {'+': add, '-': sub, '*': mul, '/': div}
        tmp = []
        for i in range(len(tokens)):
            if tokens[i] in cul:
                a = tmp.pop()
                b = tmp.pop()
                tmp.append(cul.get(tokens[i])(int(a), int(b)))
            else:
                tmp.append(int(tokens[i]))
        print(tmp)
        return tmp[0]


if __name__ == '__main__':
    s = Solution()
    t = ["4", "13", "5", "/", "+"]
    s.evalRPN(tokens=t)
