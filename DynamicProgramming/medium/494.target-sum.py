#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (44.45%)
# Total Accepted:    77K
# Total Submissions: 173.3K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 
# You are given a list of non-negative integers, a1, a2, ..., an, and a target,
# S. Now you have 2 symbols + and -. For each integer, you should choose one
# from + and - as its new symbol.
# ⁠
# 
# Find out how many ways to assign symbols to make sum of integers equal to
# target S.  
# 
# 
# Example 1:
# 
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# 
# 
# 
# Note:
# 
# The length of the given array is positive and will not exceed 20. 
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
# 
# 
#
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.ans = 0
        self.find(index=0, nums=nums, t_sum=0, S=S)
        return self.ans
    
    def find(self, index, nums, t_sum, S):
        if index >= len(nums):
            if t_sum == S:
                self.ans += 1
        else:
            self.find(index=index + 1, nums=nums, t_sum=t_sum + nums[index], S=S)
            self.find(index=index + 1, nums=nums, t_sum=t_sum - nums[index], S=S)


if __name__ == '__main__':
    s = Solution()
    nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    S = 0
    print(s.findTargetSumWays(nums=nums, S=S))
