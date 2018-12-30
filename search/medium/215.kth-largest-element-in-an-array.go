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

// 快速选择解法版本
func findKthLargest(nums []int, k int) int {
	QuickChoose(&nums, 0, len(nums) - 1, k - 1)
	return nums[k - 1]
}

func QuickChoose(nums *[]int, start, end, k int) {
	if start < end {
		i, j := start, end
		mid := (*nums)[(i + j) / 2]
		for i <= j {
			for (*nums)[i] > mid {
				i ++
			}
			for (*nums)[j] < mid {
				j --
			}
			if i <= j {
				(*nums)[i], (*nums)[j] = (*nums)[j], (*nums)[i]
				i++
				j--
			}
		}
		if k <= j {
			QuickChoose(nums, start, j, k)
		} else if k >= i {
			QuickChoose(nums, i, end, k)
		}
	}
}