/*
 * @lc app=leetcode id=658 lang=golang
 *
 * [658] Find K Closest Elements
 *
 * https://leetcode.com/problems/find-k-closest-elements/description/
 *
 * algorithms
 * Medium (36.18%)
 * Total Accepted:    38.6K
 * Total Submissions: 106.6K
 * Testcase Example:  '[1,2,3,4,5]\n4\n3'
 *
 * 
 * Given a sorted array, two integers k and x, find the k closest elements to x
 * in the array.  The result should also be sorted in ascending order.
 * If there is a tie,  the smaller elements are always preferred.
 * 
 * 
 * Example 1:
 * 
 * Input: [1,2,3,4,5], k=4, x=3
 * Output: [1,2,3,4]
 * 
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: [1,2,3,4,5], k=4, x=-1
 * Output: [1,2,3,4]
 * 
 * 
 * 
 * Note:
 * 
 * The value k is positive and will always be smaller than the length of the
 * sorted array.
 * ⁠Length of the given array is positive and will not exceed 104
 * ⁠Absolute value of elements in the array and x will not exceed 104
 * 
 * 
 * 
 * 
 * 
 * 
 * UPDATE (2017/9/19):
 * The arr parameter had been changed to an array of integers (instead of a
 * list of integers). Please reload the code definition to get the latest
 * changes.
 * 
 */
package medium

import (
	"math"
)

func findClosestElements(arr []int, k int, x int) []int {
	xLoc, ok := find(arr, x)
	if xLoc == -1 && ok {
		if x < arr[0] {
			return arr[:k]
		} else if x > arr[len(arr) - 1] {
			return arr[len(arr) - k:]
		}
	}
	left := 0
	if xLoc - k + 1 > 0 && ok {
		left = xLoc - k + 1
	}
	right := len(arr) - 1
	if xLoc + k - 1 < right && ok {
		right = xLoc + k - 1
	}
	for right - left + 1 > k {
		if math.Abs(float64(arr[left] - x)) > math.Abs(float64(arr[right] - x)) {
			left ++
		} else if math.Abs(float64(arr[left] - x)) < math.Abs(float64(arr[right] - x)) {
			right --
		} else {
			right --
		}
	}
	return arr[left: right + 1]
}

func find(arr []int , x int) (int, bool) {
	loc := -1
	find := false
	for i := 0; i < len(arr); i ++ {
		if arr[i] == x {
			loc = i
			find = true
		}
	}
	return loc, find
}