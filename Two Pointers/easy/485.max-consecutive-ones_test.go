/*
 * @lc app=leetcode id=485 lang=golang
 *
 * [485] Max Consecutive Ones
 *
 * https://leetcode.com/problems/max-consecutive-ones/description/
 *
 * algorithms
 * Easy (54.09%)
 * Total Accepted:    114.8K
 * Total Submissions: 212.2K
 * Testcase Example:  '[1,0,1,1,0,1]'
 *
 * Given a binary array, find the maximum number of consecutive 1s in this
 * array.
 * 
 * Example 1:
 * 
 * Input: [1,1,0,1,1,1]
 * Output: 3
 * Explanation: The first two digits or the last three digits are consecutive
 * 1s.
 * ⁠   The maximum number of consecutive 1s is 3.
 * 
 * 
 * 
 * Note:
 * 
 * The input array will only contain 0 and 1.
 * The length of input array is a positive integer and will not exceed 10,000
 * 
 * 
 */
package easy

func findMaxConsecutiveOnes(nums []int) int {
	length := len(nums)
	a := 0
	b := 0
	ans := 0
	for b < length {
		if nums[b] == 1 {
			b ++
		} else {
			ans = Max(ans, b - a)
			a = b + 1
			b = a
		}
	}
	ans = Max(ans, b - a)
	return ans
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}