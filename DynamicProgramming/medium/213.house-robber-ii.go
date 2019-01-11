/*
 * @lc app=leetcode id=213 lang=golang
 *
 * [213] House Robber II
 *
 * https://leetcode.com/problems/house-robber-ii/description/
 *
 * algorithms
 * Medium (34.91%)
 * Total Accepted:    100.6K
 * Total Submissions: 288.2K
 * Testcase Example:  '[2,3,2]'
 *
 * You are a professional robber planning to rob houses along a street. Each
 * house has a certain amount of money stashed. All houses at this place are
 * arranged in a circle. That means the first house is the neighbor of the last
 * one. Meanwhile, adjacent houses have security system connected and it will
 * automatically contact the police if two adjacent houses were broken into on
 * the same night.
 * 
 * Given a list of non-negative integers representing the amount of money of
 * each house, determine the maximum amount of money you can rob tonight
 * without alerting the police.
 * 
 * Example 1:
 * 
 * 
 * Input: [2,3,2]
 * Output: 3
 * Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money
 * = 2),
 * because they are adjacent houses.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [1,2,3,1]
 * Output: 4
 * Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
 * 3).
 * Total amount you can rob = 1 + 3 = 4.
 * 
 */
package medium

func rob(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) <= 2 {
		return int(math.Max(float64(nums[0]), float64(nums[len(nums) - 1])))
	}
	a := solution(nums[1: len(nums) - 1])
	b := solution(nums[2:])
	return int(math.Max(float64(a), float64(b)))
}

func solution(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	if len(nums) <= 2 {
		return int(math.Max(float64(nums[0]), float64(nums[len(nums) - 1])))
	}
	dp := make([]int, len(nums), len(nums))
	dp[0] = nums[0]
	dp[1] = int(math.Max(float64(nums[0]), float64(nums[1])))
	for i := 2; i < len(nums); i ++ {
		a := dp[i - 2] + nums[i]
		b := dp[i - 1]
		dp[i] = int(math.Max(float64(a), float64(b)))
	}
	return dp[len(nums) - 1]
}
