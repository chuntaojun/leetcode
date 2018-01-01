"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
"""

import sys

sys.setrecursionlimit(1000000)


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        wight, length = len(grid), len(grid[0])
        for i in range(wight):
            for j in range(length):
                if grid[i][j] == 1 and grid[i][j] != -1:
                    max_area = max(max_area, self.DFS(grid, grid, i, j, length, wight))
        return max_area

    def DFS(self, grid, visited, i, j, length, wight):
        max_area = 0
        if i < 0 or i >= wight:
            return max_area
        if j < 0 or j >= length:
            return max_area
        if grid[i][j] != 1 or visited[i][j] == -1:
            return max_area
        visited[i][j] = -1
        max_area += 1
        max_area += self.DFS(grid, visited, i, j + 1, length, wight)
        max_area += self.DFS(grid, visited, i, j - 1, length, wight)
        max_area += self.DFS(grid, visited, i + 1, j, length, wight)
        max_area += self.DFS(grid, visited, i - 1, j, length, wight)
        return max_area


if __name__ == '__main__':
    s = Solution()
    test = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print s.maxAreaOfIsland(test)
