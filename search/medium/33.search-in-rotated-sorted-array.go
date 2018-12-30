/*
 * @lc app=leetcode id=33 lang=golang
 *
 * [33] Search in Rotated Sorted Array
 *
 * https://leetcode.com/problems/search-in-rotated-sorted-array/description/
 *
 * algorithms
 * Medium (32.36%)
 * Total Accepted:    337.5K
 * Total Submissions: 1M
 * Testcase Example:  '[4,5,6,7,0,1,2]\n0'
 *
 * Suppose an array sorted in ascending order is rotated at some pivot unknown
 * to you beforehand.
 * 
 * (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
 * 
 * You are given a target value to search. If found in the array return its
 * index, otherwise return -1.
 * 
 * You may assume no duplicate exists in the array.
 * 
 * Your algorithm's runtime complexity must be in the order of O(log n).
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [4,5,6,7,0,1,2], target = 0
 * Output: 4
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [4,5,6,7,0,1,2], target = 3
 * Output: -1
 * 
 */

package medium

func search(nums []int, target int) int {
    return twoSearch(nums, 0, len(nums) - 1, target)
}

func twoSearch(nums []int, left, right, target int) int {
	if left > right {
		return -1
	}
	mid := (left + right) / 2
	if nums[mid] == target {
		return mid
	}
	if nums[mid] < nums[right] {
		if target > nums[mid] && target <= nums[right] {
			return twoSearch(nums, mid + 1, right, target)
		}
		return twoSearch(nums, left, mid - 1, target)
	} else {
		if target < nums[mid] && target >= nums[left] {
			return twoSearch(nums, left, mid - 1, target)
		}
		return twoSearch(nums, mid + 1, right, target)
	}
}
