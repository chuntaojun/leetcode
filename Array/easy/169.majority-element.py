#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (50.69%)
# Total Accepted:    329.5K
# Total Submissions: 649.4K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = nums[0]
        nTimes = 1
        for i in range(1, len(nums)):
            if nTimes == 0:
                candidate = nums[i]
                nTimes = 1
            else:
                if candidate == nums[i]:
                    nTimes += 1
                else:
                    nTimes -= 1
        return candidate


if __name__ == '__main__':
    s = Solution()
    t = [10,9,9,9,10]
    print(s.majorityElement(nums=t))
    