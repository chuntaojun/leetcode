#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#
# https://leetcode.com/problems/number-complement/description/
#
# algorithms
# Easy (61.79%)
# Total Accepted:    96.6K
# Total Submissions: 156.4K
# Testcase Example:  '5'
#
# Given a positive integer, output its complement number. The complement
# strategy is to flip the bits of its binary representation.
# 
# Note:
# 
# The given integer is guaranteed to fit within the range of a 32-bit signed
# integer.
# You could assume no leading zero bit in the integer’s binary
# representation.
# 
# 
# 
# Example 1:
# 
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.
# 
# 
# 
# Example 2:
# 
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and
# its complement is 0. So you need to output 0.
# 
# 
#
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = list(bin(num)[2:])
        t = 0
        for i in range(len(n)):
            if 1^int(n.pop()):
                t += pow(2, i)
        return t


if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(num=5))
