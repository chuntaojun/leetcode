#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (30.07%)
# Total Accepted:    304.4K
# Total Submissions: 1M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 1
        r = x
        while l <= r:
            mid = int((l + r) / 2)
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1
            elif mid * mid > x:
                r = mid - 1
        if l * l > x:
            return l - 1
        return l


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(x=12))
    