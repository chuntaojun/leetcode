#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (40.13%)
# Total Accepted:    177.5K
# Total Submissions: 442.4K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        nums.sort()
        a = 0; b = 1
        max_len = 0
        tmp_a = a
        sign = 0
        while a < len(nums) and b < len(nums):
            if nums[b] - nums[tmp_a] == 1:
                tmp_a += 1
                b += 1
            elif nums[b] - nums[tmp_a] == 0:
                sign += 1
                tmp_a += 1
                b += 1
            else:
                max_len = max(max_len, b - a - sign)
                a = b
                tmp_a = a
                b += 1
                sign = 0
        max_len = max(max_len, b - a - sign)
        return max_len
