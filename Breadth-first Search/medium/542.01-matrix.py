#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (34.05%)
# Total Accepted:    32.9K
# Total Submissions: 96.6K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for
# each cell.
# 
# The distance between two adjacent cells is 1.
# 
# Example 1: 
# Input:
# 
# 0 0 0
# 0 1 0
# 0 0 0
# 
# Output:
# 
# 0 0 0
# 0 1 0
# 0 0 0
# 
# 
# 
# Example 2: 
# Input:
# 
# 0 0 0
# 0 1 0
# 1 1 1
# 
# Output:
# 
# 0 0 0
# 0 1 0
# 1 2 1
# 
# 
# 
# Note:
# 
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
# 
# 
# 
#
from collections import deque


class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        self.h = len(matrix)
        self.w = len(matrix[0])
        queue = deque([])
        for i in range(self.h):
            for j in range(self.w):
                if matrix[i][j] == 1:
                    matrix[i][j] = self.h * self.w
                else:
                    queue.append((i, j))
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            x, y = queue.popleft()
            for delate_x, delate_y in direction:
                next_x = x + delate_x
                next_y = y + delate_y
                if not self.vail(x=next_x, y=next_y) or matrix[next_x][next_y] <= matrix[x][y] + 1:
                    continue
                matrix[next_x][next_y] = matrix[x][y] + 1
                queue.append((next_x, next_y))
        return matrix
        
    
    def vail(self, x, y):
        return (x >= 0 and x < self.h) and (y >=0 and y < self.w)


if __name__ == '__main__':
    s = Solution()
    t = [[0,0,0],[0,1,0],[1,1,1]]
    s.updateMatrix(matrix=t)
