#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#
# https://leetcode.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (26.09%)
# Total Accepted:    52.7K
# Total Submissions: 202.1K
# Testcase Example:  '"1432219"\n3'
#
# Given a non-negative integer num represented as a string, remove k digits
# from the number so that the new number is the smallest possible.
# 
# 
# Note:
# 
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# 
# 
# 
# 
# Example 1:
# 
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
# which is the smallest.
# 
# 
# 
# Example 2:
# 
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output
# must not contain leading zeroes.
# 
# 
# 
# Example 3:
# 
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with
# nothing which is 0.
# 
# 
#
class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):
            return '0'
        new_nums =[]
        for i in range(len(num)):
            while new_nums and num[i] < new_nums[-1] and k > 0:
                new_nums.pop()
                k -= 1
            new_nums.append(str(num[i]))
        if k > 0:
            new_nums = new_nums[:-k]
        while new_nums and new_nums[0] == '0':
            new_nums.pop(0)
        if not new_nums:
            return '0'
        return ''.join(new_nums)
        
