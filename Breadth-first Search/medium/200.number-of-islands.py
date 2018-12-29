#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (39.17%)
# Total Accepted:    265.5K
# Total Submissions: 677.7K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#
from collections import deque

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        self.h = len(grid)
        self.w = len(grid[0])
        res = 0
        for i in range(self.h):
            for j in range(self.w):
                if grid[i][j] == '1':
                    self.bfs(x=i, y=j, grid=grid)
                    res += 1
        return res
    
    def bfs(self, x, y, grid):
        queue = deque([(x, y)])
        grid[x][y] = '0'
        while queue:
            x, y = queue.popleft()
            for delate_x, delate_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_x = x + delate_x
                next_y = y + delate_y
                if not self.judge(x=next_x, y=next_y, grid=grid):
                    continue
                grid[next_x][next_y] = '0'
                if (next_x, next_y) not in queue:
                    queue.append((next_x, next_y))
    
    def judge(self, x, y, grid):
        return (x >= 0 and x < self.h) and (y >=0 and y < self.w) and grid[x][y] == '1'
