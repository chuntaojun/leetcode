#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (33.99%)
# Total Accepted:    299.8K
# Total Submissions: 881.9K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
# 
#
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        loc = len(nums1) - 1
        a = m - 1; b = n - 1
        while a > -1 and b > -1:
            if nums1[a] > nums2[b]:
                nums1[loc] = nums1[a]
                a -= 1
            else:
                nums1[loc] = nums2[b]
                b -= 1
            loc -= 1
        while a > -1:
            nums1[loc] = nums1[a]
            a -= 1
            loc -= 1
        while b > -1:
            nums1[loc] = nums2[b]
            b -= 1
            loc -= 1
        print(nums1)
