#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (33.66%)
# Total Accepted:    150.8K
# Total Submissions: 448K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        min_len = len(nums) + 1
        l = 0; r = 0
        tmp = 0
        while l < len(nums):
            if r < len(nums) and tmp < s:
                tmp += nums[r]
                r += 1
            else:
                tmp -= nums[l]
                l += 1
            if tmp >= s:
                min_len = min(min_len, r - l + 1)
        return min_len if min_len != len(nums) + 1 else 0
