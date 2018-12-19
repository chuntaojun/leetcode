#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (32.36%)
# Total Accepted:    337.5K
# Total Submissions: 1M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.target = target
        return self.two_search(arr=nums, left=0, right=len(nums) - 1)
    
    def two_search(self, arr, left, right):
        if left > right:
            return -1
        mid = int((left + right) / 2)
        if arr[mid] == self.target:
            return mid
        if arr[mid] < arr[right]:
            if self.target > arr[mid] and self.target <= arr[right]:
                return self.two_search(arr=arr, left=mid + 1, right=right)
            else:
                return self.two_search(arr=arr, left=left, right=mid - 1)
        else:
            if self.target >= arr[left] and self.target < arr[mid]:
                return self.two_search(arr=arr, left=left, right=mid - 1)
            else:
                return self.two_search(arr=arr, left=mid + 1, right=right)



if __name__ == '__main__':
    s = Solution()
    t_1 = [1,3]
    t_2 = 0
    print(s.search(nums=t_1, target=t_2))
    
