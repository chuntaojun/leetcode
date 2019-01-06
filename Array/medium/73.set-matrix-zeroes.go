/*
 * @lc app=leetcode id=73 lang=golang
 *
 * [73] Set Matrix Zeroes
 *
 * https://leetcode.com/problems/set-matrix-zeroes/description/
 *
 * algorithms
 * Medium (38.43%)
 * Total Accepted:    179.1K
 * Total Submissions: 466K
 * Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
 *
 * Given a m x n matrix, if an element is 0, set its entire row and column to
 * 0. Do it in-place.
 * 
 * Example 1:
 * 
 * 
 * Input: 
 * [
 * [1,1,1],
 * [1,0,1],
 * [1,1,1]
 * ]
 * Output: 
 * [
 * [1,0,1],
 * [0,0,0],
 * [1,0,1]
 * ]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 
 * [
 * [0,1,2,0],
 * [3,4,5,2],
 * [1,3,1,5]
 * ]
 * Output: 
 * [
 * [0,0,0,0],
 * [0,4,5,0],
 * [0,3,1,0]
 * ]
 * 
 * 
 * Follow up:
 * 
 * 
 * A straight forward solution using O(mn) space is probably a bad idea.
 * A simple improvement uses O(m + n) space, but still not the best
 * solution.
 * Could you devise a constant space solution?
 * 
 * 
 */
package medium

func setZeroes(matrix [][]int)  {
    for i := 0; i < len(matrix); i ++ {
		for j := 0; j < len(matrix[0]); j ++ {
			if matrix[i][j] == 0 {
				matrix[i][j] = 65535
				row(&matrix, i, len(matrix[0]))
				line(&matrix, j, len(matrix))
			}
		}
	}
	for i := 0; i < len(matrix); i ++ {
		for j := 0; j < len(matrix[0]); j ++ {
			if matrix[i][j] == 65535 {
				matrix[i][j] = 0
			}
		}
	}
}

func row(matrix *[][]int, row, w int) {
	for i := 0; i < len((*matrix)[0]); i ++ {
		if (*matrix)[row][i] != 0 {
			(*matrix)[row][i] = 65535
		}
	}
}

func line(matrix *[][]int, line, h int) {
	for i := 0; i < len(*matrix); i ++ {
		if (*matrix)[i][line] != 0 {
			(*matrix)[i][line] = 65535
		}
	}
}
