#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#
# https://leetcode.com/problems/shortest-bridge/description/
#
# algorithms
# Medium (43.71%)
# Total Accepted:    6.8K
# Total Submissions: 15.6K
# Testcase Example:  '[[0,1],[1,0]]'
#
# In a given 2D binary array A, there are two islands.  (An island is a
# 4-directionally connected group of 1s not connected to any other 1s.)
# 
# Now, we may change 0s to 1s so as to connect the two islands together to form
# 1 island.
# 
# Return the smallest number of 0s that must be flipped.  (It is guaranteed
# that the answer is at least 1.)
# 
# 
# 
# Example 1:
# 
# 
# Input: [[0,1],[1,0]]
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# 
# 
# 
# Example 3:
# 
# 
# Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length = A[0].length <= 100
# A[i][j] == 0 or A[i][j] == 1
# 
# 
# 
# 
# 
# 
# 
#
from collections import deque

class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        have_find = False
        first_island = deque()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    self.dfs(grid=A, x=i, y=j, first_island=first_island)
                    have_find = True
                    break
            if have_find:
                break
        distance = 2
        ans = len(A) * len(A[0])
        while first_island:
            l = len(first_island)
            for i in range(l):
                x, y = first_island.popleft()
                for dir_x, dir_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    n_x, n_y = x + dir_x, y + dir_y
                    if self.judge(n_x, n_y, A):
                        if A[n_x][n_y] == 1:
                            ans = min(ans, abs(A[x][y]) - 1)
                        elif A[n_x][n_y] != 0:
                            A[n_x][n_y] = -1 * abs(A[n_x][n_y])
                        else:
                            A[n_x][n_y] = distance
                            if (n_x, n_y) not in first_island:
                                first_island.append((n_x, n_y))
            distance += 1
        return ans

    def dfs(self, grid, x, y, first_island):
        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
            if grid[x][y] == 1:
                grid[x][y] = -1
                first_island.append((x, y))
                self.dfs(grid, x - 1, y, first_island)
                self.dfs(grid, x + 1, y, first_island)
                self.dfs(grid, x, y - 1, first_island)
                self.dfs(grid, x, y + 1, first_island)
    
    def judge(self, x, y, grid):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])


if __name__ == '__main__':
    s = Solution()
    A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    print(s.shortestBridge(A=A))
    
