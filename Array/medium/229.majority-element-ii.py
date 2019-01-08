#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (30.88%)
# Total Accepted:    88.6K
# Total Submissions: 286.7K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# Note: The algorithm should run in linear time and in O(1) space.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: [3]
# 
# Example 2:
# 
# 
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# 
#
class Solution(object):
    def majorityElement(self, nums):        
        num1 = num2 = 1e9
        cnt1 = cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = num
                cnt1 += 1
            elif cnt2 == 0:
                num2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1 = nums.count(num1)
        cnt2 = nums.count(num2)
        res = []
        if cnt1 > int(len(nums)/3):
            res.append(num1)
        if cnt2 > int(len(nums)/3):
            res.append(num2)
        return res

if __name__ == '__main__':
    s = Solution()
    t = [0,3,4,0]
    print(s.majorityElement(nums=t))
    