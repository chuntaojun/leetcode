#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
# https://leetcode.com/problems/find-peak-element/description/
#
# algorithms
# Medium (40.29%)
# Total Accepted:    202K
# Total Submissions: 501.3K
# Testcase Example:  '[1,2,3,1]'
#
# A peak element is an element that is greater than its neighbors.
# 
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and
# return its index.
# 
# The array may contain multiple peaks, in that case return the index to any
# one of the peaks is fine.
# 
# You may imagine that nums[-1] = nums[n] = -∞.
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
# 
# Example 2:
# 
# 
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5 
# Explanation: Your function can return either index number 1 where the peak
# element is 2, 
# or index number 5 where the peak element is 6.
# 
# 
# Note:
# 
# Your solution should be in logarithmic complexity.
# 
#
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            if right - left == 1:
                return left if nums[left] > nums[right] else right
            mid = int((left + right) / 2)
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid - 1] < nums[mid] and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    s = Solution()
    t = [1,2,3,4,5,6]
    print(s.findPeakElement(nums=t))
