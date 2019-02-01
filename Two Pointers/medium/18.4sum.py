#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (29.26%)
# Total Accepted:    202.7K
# Total Submissions: 692.8K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        length = len(nums)
        nums.sort()
        ans = []
        for l_1 in range(length - 3):
            t_target = target - nums[l_1]
            for l_2 in range(l_1 + 1, length - 2):
                r = length - 1
                mid = l_2 + 1
                while mid < r:
                    sum_val = nums[l_2] + nums[mid] + nums[r]
                    diff = t_target - sum_val
                    if diff == 0:
                        t = [nums[l_1], nums[l_2], nums[mid], nums[r]]
                        if t not in ans:
                            ans.append(t)
                        mid += 1
                        r -= 1
                    elif diff > 0:
                        mid += 1
                    else:
                        r -= 1
        return ans
        
