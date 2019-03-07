#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (40.46%)
# Total Accepted:    350.5K
# Total Submissions: 866.1K
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# 
# Example:
# 
# 
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# Note:
# 
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#
# import sys
# sys.setrecursionlimit(1000000)

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.n = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.result = []
        if digits is None or len(digits) == 0:
            return []
        self.dfs(s=digits, t="", l=0)
        return self.result
    
    def dfs(self, s, t, l):
        if l == len(s):
            self.result.append(t)
        else:
            c = s[l]
            if c <= '9' and c >= '0' and c != '1':
                letter = self.n[ord(c) - ord('0')]
                for i in range(len(letter)):
                    self.dfs(s=s, t=t + letter[i], l=l + 1)


if __name__ == '__main__':
    s = Solution()
    t = '23'
    print(s.letterCombinations(digits=t))
    


