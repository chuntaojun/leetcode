#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (49.91%)
# Total Accepted:    281.3K
# Total Submissions: 563.7K
# Testcase Example:  '[1,2,3,1]'
#
# Given an array of integers, find if the array contains any duplicates.
# 
# Your function should return true if any value appears at least twice in the
# array, and it should return false if every element is distinct.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: true
# 
# Example 2:
# 
# 
# Input: [1,2,3,4]
# Output: false
# 
# Example 3:
# 
# 
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
# 
#
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.hash_set = [[] for i in range(1001)]
        for i in range(len(nums)):
            loc = self.hash_func(key=nums[i])
            if nums[i] in self.hash_set[loc]:
                return True
            else:
                self.hash_set[loc].append(nums[i])
        return False

    
    def hash_func(self, key):
        return int(key % 1000)
        
        