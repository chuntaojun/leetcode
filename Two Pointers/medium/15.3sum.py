#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (22.53%)
# Total Accepted:    431K
# Total Submissions: 1.9M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = {}
        for i in range(len(nums)):
            if ans.__contains__(nums[i]):
                ans[nums[i]] += 1
            else:
                ans[nums[i]] = 0
        key_list = ans.keys()
        for i in range(len(key_List)):
            pass
