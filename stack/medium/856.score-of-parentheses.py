#
# [886] Score of Parentheses
#
# https://leetcode.com/problems/score-of-parentheses/description/
#
# algorithms
# Medium (53.97%)
# Total Accepted:    11.3K
# Total Submissions: 20.9K
# Testcase Example:  '"()"'
#
# Given a balanced parentheses string S, compute the score of the string based
# on the following rule:
# 
# 
# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "()"
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: "(())"
# Output: 2
# 
# 
# 
# Example 3:
# 
# 
# Input: "()()"
# Output: 2
# 
# 
# 
# Example 4:
# 
# 
# Input: "(()(()))"
# Output: 6
# 
# 
# 
# 
# Note:
# 
# 
# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50
# 
# 
# 
# 
# 
# 
#
from functools import reduce
import math


class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        pre_get_score = False
        tmp = []
        score = []
        deep = 0
        tmp.insert(0, (S[-1], deep))
        deep += 1
        max_deep = 0
        for i in range(len(S) - 2, -1, -1):
            if S[i] == "(" and tmp[0][0] == ")":
                if pre_get_score:
                    deep -= 1
                    continue
                deep -= 1
                score.append(tmp.pop(0))
                pre_get_score = True
            else:
                pre_get_score = False
                tmp.insert(0, (S[i], deep))
                deep += 1
                max_deep = max(max_deep, deep)
        max_deep -= 1
        print(score)
        sums = 0
        for i in score:
            sums += math.pow(2, i[1])
        return int(sums)
