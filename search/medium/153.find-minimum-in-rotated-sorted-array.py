#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (42.10%)
# Total Accepted:    244.4K
# Total Submissions: 580.6K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# 
# Input: [3,4,5,1,2] 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,5,6,7,0,1,2]
# Output: 0
# 
# 
#
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] < nums[-1]:
            return nums[0]
        return self.twoSearch(arr=nums, left=0, right=len(nums) - 1)
    
    def twoSearch(self, arr, left, right):
        if left == right:
            return arr[left]
        mid = int((left + right) / 2)
        if arr[mid] < arr[right]:
            return self.twoSearch(arr, left=left, right=mid)
        else:
            return self.twoSearch(arr, left=mid + 1, right=right)
        

if __name__ == '__main__':
    s = Solution()
    t = [3,4,5,1,2]
    print(s.findMin(nums=t))
    