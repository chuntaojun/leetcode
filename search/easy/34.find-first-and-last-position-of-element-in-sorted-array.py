#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (32.53%)
# Total Accepted:    247.8K
# Total Submissions: 761.5K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == target and nums[right] == target:
                return [left, right]
            if nums[left] != target:
                left += 1
            if nums[right] != target:
                right -= 1
        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    print(s.searchRange(nums=nums, target=target))
    