/*
 * @lc app=leetcode id=204 lang=golang
 *
 * [204] Count Primes
 *
 * https://leetcode.com/problems/count-primes/description/
 *
 * algorithms
 * Easy (27.67%)
 * Total Accepted:    200K
 * Total Submissions: 722.8K
 * Testcase Example:  '10'
 *
 * Count the number of prime numbers less than a non-negative number, n.
 * 
 * Example:
 * 
 * 
 * Input: 10
 * Output: 4
 * Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
 * 
 */
package easy

func countPrimes(n int) int {
    if n <= 2 {
        return 0
    }
	dp := make([]int, n + 2)
	for i := 2; i <= n; i ++ {
		for j := 2 * i; j <= n; j += i {
			dp[j] = 1
		}
	}
	t := n - 1
	for i := 0; i < n; i ++ {
		t -= dp[i]
	}
	return t - 1
}