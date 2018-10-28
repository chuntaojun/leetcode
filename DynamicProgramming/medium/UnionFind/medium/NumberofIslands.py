"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and grid[i][j] != '-1':
                    self.DFS(grid, grid, i, j)
                    res += 1
        return res

    def DFS(self, grid, visited, x, y):
        if x < 0 or x >= len(grid):
            return
        if y < 0 or y >= len(grid[0]):
            return
        if grid[x][y] != '1' or visited[x][y] == '-1':
            return
        visited[x][y] = -1
        self.DFS(grid=grid, visited=visited, x=x - 1, y=y)
        self.DFS(grid=grid, visited=visited, x=x + 1, y=y)
        self.DFS(grid=grid, visited=visited, x=x, y=y - 1)
        self.DFS(grid=grid, visited=visited, x=x, y=y + 1)


if __name__ == '__main__':
    s = Solution()
    s.numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
