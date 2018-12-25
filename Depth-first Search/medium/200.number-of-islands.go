/*
 * @lc app=leetcode id=200 lang=golang
 *
 * [200] Number of Islands
 *
 * https://leetcode.com/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (39.17%)
 * Total Accepted:    265.5K
 * Total Submissions: 677.7K
 * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
 *
 * Given a 2d grid map of '1's (land) and '0's (water), count the number of
 * islands. An island is surrounded by water and is formed by connecting
 * adjacent lands horizontally or vertically. You may assume all four edges of
 * the grid are all surrounded by water.
 * 
 * Example 1:
 * 
 * 
 * Input:
 * 11110
 * 11010
 * 11000
 * 00000
 * 
 * Output: 1
 * 
 * 
 * Example 2:
 * 
 * 
 * Input:
 * 11000
 * 11000
 * 00100
 * 00011
 * 
 * Output: 3
 * 
 */
package medium

func numIslands(grid [][]byte) int {
	res := 0
	height := len(grid)
	width := len(grid[0])
	for i := 0; i < height; i ++ {
		for j := 0; j < width; j ++ {
			if grid[i][j] == byte('1') {
				res += 1
				DFS(&grid, j, i, height, width)
			}
		}
	}
	return res
}

func DFS(grid *[][]byte, x, y, height, width int) {
	if x < 0 || x >= width {
		return
	}
	if y < 0 || y >= height {
		return
	}
	if (*grid)[y][x] == byte('2') || (*grid)[y][x] == byte('0') {
		return
	}
	(*grid)[y][x] = 2
	DFS(grid, x - 1, y, height, width)
	DFS(grid, x + 1, y, height, width)
	DFS(grid, x, y - 1, height, width)
	DFS(grid, x, y + 1, height, width)
}
