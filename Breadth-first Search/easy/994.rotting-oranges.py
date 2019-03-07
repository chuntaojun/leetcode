#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Easy (46.54%)
# Total Accepted:    5.7K
# Total Submissions: 12.3K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# In a given grid, each cell can have one of three values:
# 
# 
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# 
# Example 3:
# 
# 
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the
# answer is just 0.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
# 
# 
# 
# 
# 
#
from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.minutes = 0
        origins = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    origins += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q and origins > 0:
            l = len(q)
            self.minutes += 1
            for i in range(l):
                x, y = q.popleft()
                for delate_x, delate_y in direction:
                    next_x, next_y = x + delate_x, y + delate_y
                    if not self.judge(next_x, next_y, grid):
                        continue
                    grid[next_x][next_y] = 2
                    origins -= 1
                    if (next_x, next_y) not in q:
                        q.append((next_x, next_y))
        return self.minutes if origins == 0 else -1
    
    def judge(self, x, y, grid):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == 1


if __name__ == '__main__':
    s = Solution()
    grid = [[0,2]]
    print(s.orangesRotting(grid=grid))
    
