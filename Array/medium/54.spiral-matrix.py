#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (28.94%)
# Total Accepted:    192.3K
# Total Submissions: 664.6K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.ans = []
        self.h = len(matrix)
        if self.h == 0:
            return []
        self.w = len(matrix[0])
        x = y = 0
        while self.h > 0 and self.w > 0:
            if self.w == 1:
                for _ in range(self.h):
                    self.ans.append(matrix[x][y])
                    x += 1
                break
            if self.h == 1:
                for _ in range(self.w):
                    self.ans.append(matrix[x][y])
                    y += 1
                break
            for _ in range(self.w - 1):
                self.ans.append(matrix[x][y])
                y += 1
            for _ in range(self.h - 1):
                self.ans.append(matrix[x][y])
                x += 1
            for _ in range(self.w - 1):
                self.ans.append(matrix[x][y])
                y -= 1
            for _ in range(self.h - 1):
                self.ans.append(matrix[x][y])
                x -= 1
            self.w -= 2
            self.h -= 2
            x += 1
            y += 1
        return self.ans


if __name__ == '__main__':
    s = Solution()
    m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(s.spiralOrder(matrix=m))
