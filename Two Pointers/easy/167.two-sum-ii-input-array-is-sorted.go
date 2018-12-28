/*
 * @lc app=leetcode id=167 lang=golang
 *
 * [167] Two Sum II - Input array is sorted
 *
 * https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
 *
 * algorithms
 * Easy (48.29%)
 * Total Accepted:    191.5K
 * Total Submissions: 396.6K
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * Given an array of integers that is already sorted in ascending order, find
 * two numbers such that they add up to a specific target number.
 * 
 * The function twoSum should return indices of the two numbers such that they
 * add up to the target, where index1 must be less than index2.
 * 
 * Note:
 * 
 * 
 * Your returned answers (both index1 and index2) are not zero-based.
 * You may assume that each input would have exactly one solution and you may
 * not use the same element twice.
 * 
 * 
 * Example:
 * 
 * 
 * Input: numbers = [2,7,11,15], target = 9
 * Output: [1,2]
 * Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
 * 
 */
package easy

func twoSum(numbers []int, target int) []int {
	length := len(numbers)
	a := 0
	b := length - 1
	for a < b {
		t := numbers[a] + numbers[b]
		if t == target {
			return []int{a + 1, b + 1}
		} else if t > target {
			b -= 1
		} else if t < target {
			a += 1
		}
	}
	return []int{-1, -1}
}
