#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (40.97%)
# Total Accepted:    173.4K
# Total Submissions: 423.3K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the kth index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return []
        ans = [[1]]
        for i in range(2, rowIndex + 2):
            tmp = [1]
            _t = ans[-1]
            for j in range(len(_t) - 1):
                tmp.append(_t[j] + _t[j + 1])
            tmp.append(1)
            ans.append(tmp)
        return ans[rowIndex]


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(rowIndex=3))
