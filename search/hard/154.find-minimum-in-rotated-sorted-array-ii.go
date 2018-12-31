/*
 * @lc app=leetcode id=154 lang=golang
 *
 * [154] Find Minimum in Rotated Sorted Array II
 *
 * https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
 *
 * algorithms
 * Hard (38.70%)
 * Total Accepted:    115.6K
 * Total Submissions: 298.7K
 * Testcase Example:  '[1,3,5]'
 *
 * Suppose an array sorted in ascending order is rotated at some pivot unknown
 * to you beforehand.
 * 
 * (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
 * 
 * Find the minimum element.
 * 
 * The array may contain duplicates.
 * 
 * Example 1:
 * 
 * 
 * Input: [1,3,5]
 * Output: 1
 * 
 * Example 2:
 * 
 * 
 * Input: [2,2,2,0,1]
 * Output: 0
 * 
 * Note:
 * 
 * 
 * This is a follow up problem to Find Minimum in Rotated Sorted Array.
 * Would allow duplicates affect the run-time complexity? How and why?
 * 
 * 
 */
package hard

func findMin(nums []int) int {
	right := 65535
	left := -65535
	k := len(nums)
	t := nums[0]
	all := true
	for i := 1; i < k; i ++ {
		if t != nums[i] {
			all = false
			break
		}
	}
	if all {
		return t
	}
	for left < right {
		mid := (left + right) / 2
		kth, ok := minTh(nums, mid)
		if kth == k && ok {
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

func minTh(nums []int, target int) (int, bool) {
	a := 0
	k := false
	for i := 0; i < len(nums); i++ {
		if nums[i] > target {
			a++
		} else if nums[i] == target {
			k = true
		}
	}
	return a + 1, k
}