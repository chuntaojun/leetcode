/*
 * @lc app=leetcode id=240 lang=golang
 *
 * [240] Search a 2D Matrix II
 *
 * https://leetcode.com/problems/search-a-2d-matrix-ii/description/
 *
 * algorithms
 * Medium (40.26%)
 * Total Accepted:    162.2K
 * Total Submissions: 402.7K
 * Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
 *
 * Write an efficient algorithm that searches for a value in an m x n matrix.
 * This matrix has the following properties:
 * 
 * 
 * Integers in each row are sorted in ascending from left to right.
 * Integers in each column are sorted in ascending from top to bottom.
 * 
 * 
 * Example:
 * 
 * Consider the following matrix:
 * 
 * 
 * [
 * ⁠ [1,   4,  7, 11, 15],
 * ⁠ [2,   5,  8, 12, 19],
 * ⁠ [3,   6,  9, 16, 22],
 * ⁠ [10, 13, 14, 17, 24],
 * ⁠ [18, 21, 23, 26, 30]
 * ]
 * 
 * 
 * Given target = 5, return true.
 * 
 * Given target = 20, return false.
 * 
 */
package medium

func searchMatrix(matrix [][]int, target int) bool {
	row := len(matrix)
    if row == 0 {
        return false
    }
	col := len(matrix[0])
     if col == 0 {
        return false
    }
	i := 0
	j := col - 1
	value := matrix[i][j]
	for {
		if value == target {
			return true
		} else if value < target && i < row - 1 {
			i ++
			value = matrix[i][j]
		} else if value > target && j > 0 {
			j --
			value = matrix[i][j]
		} else {
			return false
		}
	}
}


