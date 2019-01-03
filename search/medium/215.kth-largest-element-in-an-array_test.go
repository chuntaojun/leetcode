/*
 * @lc app=leetcode id=215 lang=golang
 *
 * [215] Kth Largest Element in an Array
 *
 * https://leetcode.com/problems/kth-largest-element-in-an-array/description/
 *
 * algorithms
 * Medium (44.36%)
 * Total Accepted:    290.1K
 * Total Submissions: 653.8K
 * Testcase Example:  '[3,2,1,5,6,4]\n2'
 *
 * Find the kth largest element in an unsorted array. Note that it is the kth
 * largest element in the sorted order, not the kth distinct element.
 *
 * Example 1:
 *
 *
 * Input: [3,2,1,5,6,4] and k = 2
 * Output: 5
 *
 *
 * Example 2:
 *
 *
 * Input: [3,2,3,1,2,4,5,5,6] and k = 4
 * Output: 4
 *
 * Note:
 * You may assume k is always valid, 1 ≤ k ≤ array's length.
 *
 */

package medium

import (
	"fmt"
	"testing"
)

// 二分查找解法版本
func findKthLargest2(nums []int, k int) int {
	t := nums[0]
	all := true
	for i := 1; i < len(nums); i ++ {
		if t != nums[i] {
			all = false
			break
		}
	}
	if all {
		return t
	}
	right := 65535
	left := -65535
	for left < right {
		mid := (left + right) / 2
		kth, sames, ok := minTh(nums, mid)
		if kth <= k && k <= kth + sames && ok {
			return mid
		}
		if kth > k {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return left
}

func minTh(nums []int, target int) (int, int, bool) {
	a := 0
	b := 0
	k := false
	for i := 0; i < len(nums); i ++ {
		if nums[i] > target {
			a ++
		}
		if nums[i] == target {
			b ++
			k = true
		}
	}
	if b != 0 {
		b --
	}
	return a + 1, b, k
}

func TestFunc(t *testing.T) {
	arr := []int{3, 2, 3, 1, 2, 4, 5, 5, 6}
	fmt.Printf("%d", findKthLargest2(arr, 4))
}
