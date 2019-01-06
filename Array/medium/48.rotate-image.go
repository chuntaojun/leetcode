/*
 * @lc app=leetcode id=48 lang=golang
 *
 * [48] Rotate Image
 *
 * https://leetcode.com/problems/rotate-image/description/
 *
 * algorithms
 * Medium (45.64%)
 * Total Accepted:    209.9K
 * Total Submissions: 459.9K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * You are given an n x n 2D matrix representing an image.
 *
 * Rotate the image by 90 degrees (clockwise).
 *
 * Note:
 *
 * You have to rotate the image in-place, which means you have to modify the
 * input 2D matrix directly. DO NOT allocate another 2D matrix and do the
 * rotation.
 *
 * Example 1:
 *
 *
 * Given input matrix =
 * [
 * ⁠ [1,2,3],
 * ⁠ [4,5,6],
 * ⁠ [7,8,9]
 * ],
 *
 * rotate the input matrix in-place such that it becomes:
 * [
 * ⁠ [7,4,1],
 * ⁠ [8,5,2],
 * ⁠ [9,6,3]
 * ]
 *
 *
 * Example 2:
 *
 *
 * Given input matrix =
 * [
 * ⁠ [ 5, 1, 9,11],
 * ⁠ [ 2, 4, 8,10],
 * ⁠ [13, 3, 6, 7],
 * ⁠ [15,14,12,16]
 * ],
 *
 * rotate the input matrix in-place such that it becomes:
 * [
 * ⁠ [15,13, 2, 5],
 * ⁠ [14, 3, 4, 1],
 * ⁠ [12, 6, 8, 9],
 * ⁠ [16, 7,10,11]
 * ]
 *
 *
 */
package medium

import "fmt"

func rotate(matrix [][]int) {
	n := len(matrix)
	if n < 2 {
		return
	}
	var visit [][]bool
	for i := 0; i < n; i++ {
		temp := make([]bool, n)
		visit = append(visit, temp)
	}
	fmt.Printf("%#v", visit)
	for i := 0; i < len(matrix) / 2; i++ {
		for j := i; j < len(matrix) - i; j++ {
			if !visit[i][j] && !visit[j][n-1-i] && !visit[n-1-i][n-1-j] && !visit[n-1-j][i] {
				matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]
				visit[i][j] = true
				visit[j][n-1-i] = true
				visit[n-1-i][n-1-j] = true
				visit[n-1-j][i] = true
			}
		}
	}
}
