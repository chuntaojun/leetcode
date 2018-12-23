#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (39.54%)
# Total Accepted:    1.3M
# Total Submissions: 3.2M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
# 
# 
#
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {}
        for i in range(len(nums)):
            if s.__contains__(nums[i]):
                s[nums[i]].append(i)
            else:
                s[nums[i]] = [i]
        keys = list(s.keys())
        for i in range(len(keys)):
            tmp = target - keys[i]
            if tmp == keys[i] and len(s[tmp]) == 1:
                continue
            if tmp == keys[i] and len(s[tmp]) != 1:
                return s[tmp][0:2]
            if s.__contains__(tmp):
                return [s[tmp][0], s[keys[i]][0]]
        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    t = [3,2,3]
    target = 6
    print(s.twoSum(nums=t, target=target))
    
