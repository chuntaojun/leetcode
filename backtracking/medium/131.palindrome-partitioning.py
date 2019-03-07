#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (39.65%)
# Total Accepted:    152.8K
# Total Submissions: 385.3K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.ans = []
        if s is None or len(s) == 0:
            return []
        self.dfs(s=s, t=[], l=0)
        return self.ans
    
    def dfs(self, s, t, l):
        if l == len(s):
            self.ans.append(t.copy())
        else:
            for i in range(l, len(s)):
                if self.isPalindrome(s=s, l=l, r=i):
                    t.append(s[l:i + 1])
                    self.dfs(s, t, i + 1)
                    t.pop(len(t) - 1)
    
    def isPalindrome(self, s, l, r):
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1
        return l >= r


if __name__ == '__main__':
    s = Solution()
    t = "aab"
    print(s.partition(s=t))
    
