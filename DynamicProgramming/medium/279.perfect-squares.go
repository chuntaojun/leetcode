/*
 * @lc app=leetcode id=279 lang=golang
 *
 * [279] Perfect Squares
 *
 * https://leetcode.com/problems/perfect-squares/description/
 *
 * algorithms
 * Medium (39.59%)
 * Total Accepted:    148.9K
 * Total Submissions: 375.9K
 * Testcase Example:  '12'
 *
 * Given a positive integer n, find the least number of perfect square numbers
 * (for example, 1, 4, 9, 16, ...) which sum to n.
 * 
 * Example 1:
 * 
 * 
 * Input: n = 12
 * Output: 3 
 * Explanation: 12 = 4 + 4 + 4.
 * 
 * Example 2:
 * 
 * 
 * Input: n = 13
 * Output: 2
 * Explanation: 13 = 4 + 9.
 */
package medium

import (
	"math"
)

func numSquares(n int) int {
    dp := make([]int, n + 1, n + 1)
	for i := 0; i <= n; i ++ {
		dp[i] = i
	}
	for i:= 0; i <= n; i ++ {
		for j := 1; i + j * j <=n; j ++ {
			dp[i + j * j] = int(math.Min(float64(dp[i + j * j]), float64(dp[i] + 1)))
		}
	}
	return dp[n]
}
