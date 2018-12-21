package medium

import (
	"math"
)


func maxAreaOfIsland(grid [][]int) int {
	maxArea := 0
	width := len(grid[0])
	height := len(grid)
	for i := 0; i < width; i ++ {
		for j := 0; j < height; j ++ {
			if grid[j][i] == 1 {
				maxArea = int(math.Max(float64(maxArea), float64(DFS(&grid, i, j, width, height))))
			}
		}
	}
	return maxArea
}

func DFS(grid *[][]int, x, y, width, height int) int {
	maxArea := 0
	if x < 0 || x >= width {
		return maxArea
	}
	if y < 0 || y >= height {
		return maxArea
	}
	if (*grid)[y][x] == -1 {
		return maxArea
	}
    (*grid)[y][x] = -1
	maxArea += 1
	maxArea += DFS(grid, x + 1, y, width, height)
	maxArea += DFS(grid, x - 1, y, width, height)
	maxArea += DFS(grid, x, y + 1, width, height)
	return maxArea + DFS(grid, x, y - 1, width, height)
}