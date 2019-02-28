/*
 * @lc app=leetcode id=120 lang=golang
 *
 * [120] Triangle
 *
 * https://leetcode.com/problems/triangle/description/
 *
 * algorithms
 * Medium (37.56%)
 * Total Accepted:    161.3K
 * Total Submissions: 428.9K
 * Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
 *
 * Given a triangle, find the minimum path sum from top to bottom. Each step
 * you may move to adjacent numbers on the row below.
 * 
 * For example, given the following triangle
 * 
 * 
 * [
 * ⁠    [2],
 * ⁠   [3,4],
 * ⁠  [6,5,7],
 * ⁠ [4,1,8,3]
 * ]
 * 
 * 
 * The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
 * 
 * Note:
 * 
 * Bonus point if you are able to do this using only O(n) extra space, where n
 * is the total number of rows in the triangle.
 * 
 */
package medium

import (
	"math"
)

func minimumTotal(triangle [][]int) int {
    for i := len(triangle) - 2; i >= 0; i -- {
		for j := 0; j < len(triangle[i]); j ++ {
			triangle[i][j] += int(math.Min(float64(triangle[i + 1][j]), float64(triangle[i + 1][j + 1])))
		}
	}
	return triangle[0][0]
}
