#
# @lc app=leetcode id=374 lang=python
#
# [374] Guess Number Higher or Lower
#
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (38.18%)
# Total Accepted:    93.7K
# Total Submissions: 245.4K
# Testcase Example:  '10\n6'
#
# We are playing the Guess Game. The game is as follows:
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I'll tell you whether the number is higher or
# lower.
# 
# You call a pre-defined API guess(int num) which returns 3 possible results
# (-1, 1, or 0):
# 
# 
# -1 : My number is lower
# ⁠1 : My number is higher
# ⁠0 : Congrats! You got it!
# 
# 
# Example :
# 
# 
# 
# Input: n = 10, pick = 6
# Output: 6
# 
# 
# 
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l <= n:
            mid = int((l + r) / 2)
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans == 1:
                r = mid - 1
            else:
                l = mid + 1
