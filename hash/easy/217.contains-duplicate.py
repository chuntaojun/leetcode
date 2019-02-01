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
        self.qSort(nums=nums, start=0, end=len(nums) - 1)
        print(nums)
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False
    
    def qSort(self, nums, start, end):
        if start < end:
            i = start; j = end
            key = nums[int((i + j) / 2)]
            while i <= j:
                while nums[i] < key:
                    i += 1
                while nums[j] > key:
                    j -=1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            self.qSort(nums=nums, start=start, end=j)
            self.qSort(nums=nums, start=i, end=end)


if __name__ == '__main__':
    s = Solution()
    n = [1,2,3,1]
    print(s.containsDuplicate(nums=n))
    
