#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (52.89%)
# Total Accepted:    381.4K
# Total Submissions: 721.1K
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_n = len(nums)
        a = 0; b = 1
        while a < len_n and b < len_n:
            if nums[a] == 0 and nums[b] != 0:
                nums[a], nums[b] = (nums[b], nums[a])
                a += 1
                b += 1
            elif nums[a] == 0 and nums[b] == 0:
                b += 1
            elif nums[a] != 0 and nums[b] == 0:
                a += 1
                b += 1
            elif nums[a] != 0 and nums[b] != 0:
                a = b
                b += 1
        print(nums)
