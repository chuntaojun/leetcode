#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (43.37%)
# Total Accepted:    212K
# Total Submissions: 488.8K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(2, numRows + 1):
            tmp = [1]
            _t = ans[-1]
            for j in range(len(_t) - 1):
                tmp.append(_t[j] + _t[j + 1])
            tmp.append(1)
            ans.append(tmp)
        return ans

if __name__ == '__main__':
    s = Solution()
    s.generate(numRows=1)
    
