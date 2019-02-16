#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (25.14%)
# Total Accepted:    119K
# Total Submissions: 473.6K
# Testcase Example:  '[10,2]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
# 
# Example 1:
# 
# 
# Input: [10,2]
# Output: "210"
# 
# Example 2:
# 
# 
# Input: [3,30,34,5,9]
# Output: "9534330"
# 
# 
# Note: The result may be very large, so you need to return a string instead of
# an integer.
# 
#
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        import functools
        nums = [str(i) for i in sorted(nums, key=functools.cmp_to_key(self.myCompare))]
        print(nums)
        if nums[0] == nums[-1] and nums[len(nums) // 2] == '0':
            return "0"
        return ''.join(nums)
    
    def myCompare(self, x, y):
        a = str(x) + str(y)
        b = str(y) + str(x)
        for i in range(len(a)):
            if a[i] != b[i]:
                return ord(b[i]) - ord(a[i])
        return 0


if __name__ == '__main__':
    s = Solution()
    n = [323,32]
    print(s.myCompare(x=883,y=8))
    # print(s.largestNumber(nums=n))
    
        