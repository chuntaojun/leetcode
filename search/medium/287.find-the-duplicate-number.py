#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (46.93%)
# Total Accepted:    147.1K
# Total Submissions: 313.4K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# 
# Example 1:
# 
# 
# Input: [1,3,4,2,2]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,1,3,4,2]
# Output: 3
# 
# Note:
# 
# 
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
# 
# 
#
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 1
        end = len(nums) - 1
        while start <= end:
            mid = start + int((end - start) / 2)
            c = self.count(nums=nums, start=start, end=mid)
            if start == end:
                if c > 1:
                    return start
                else:
                    break
            if c > (mid - start + 1):
                end = mid
            else:
                start = mid + 1
        return -1
    
    def count(self, nums, start, end):
        n = 0
        for i in range(len(nums)):
            if nums[i] >= start and nums[i] <= end:
                n += 1
        return n


if __name__ == '__main__':
    s = Solution()
    t = [1,3,4,2,2]
    print(s.findDuplicate(nums=t))
