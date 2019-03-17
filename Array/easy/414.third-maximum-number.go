/*
 * @lc app=leetcode id=414 lang=golang
 *
 * [414] Third Maximum Number
 *
 * https://leetcode.com/problems/third-maximum-number/description/
 *
 * algorithms
 * Easy (28.67%)
 * Total Accepted:    85K
 * Total Submissions: 296.4K
 * Testcase Example:  '[3,2,1]'
 *
 * Given a non-empty array of integers, return the third maximum number in this
 * array. If it does not exist, return the maximum number. The time complexity
 * must be in O(n).
 * 
 * Example 1:
 * 
 * Input: [3, 2, 1]
 * 
 * Output: 1
 * 
 * Explanation: The third maximum is 1.
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: [1, 2]
 * 
 * Output: 2
 * 
 * Explanation: The third maximum does not exist, so the maximum (2) is
 * returned instead.
 * 
 * 
 * 
 * Example 3:
 * 
 * Input: [2, 2, 3, 1]
 * 
 * Output: 1
 * 
 * Explanation: Note that the third maximum here means the third maximum
 * distinct number.
 * Both numbers with value 2 are both considered as second maximum.
 * 
 * 
 */
package easy

func thirdMax(nums []int) int {
	n := -99999999999
	first := n
	second := n
	third := n
	for i := 0; i < len(nums); i ++ {
		if nums[i] >= first {
			if nums[i] == first {
				continue
			}
			t_f := first
			t_s := second
			first = nums[i]
			second = t_f
			third = t_s
		} else if nums[i] >= second {
			if nums[i] == second {
				continue
			}
			t_s := second
			second = nums[i]
			third = t_s
		} else if nums[i] >= third {
			if nums[i] == third {
				continue
			}
			third = nums[i]
		}
	}
	if third == n {
		return first
	}
	return third
}

