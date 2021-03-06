/*
 * @lc app=leetcode id=220 lang=golang
 *
 * [220] Contains Duplicate III
 *
 * https://leetcode.com/problems/contains-duplicate-iii/description/
 *
 * algorithms
 * Medium (19.11%)
 * Total Accepted:    81.6K
 * Total Submissions: 427.2K
 * Testcase Example:  '[1,2,3,1]\n3\n0'
 *
 * Given an array of integers, find out whether there are two distinct indices
 * i and j in the array such that the absolute difference between nums[i] and
 * nums[j] is at most t and the absolute difference between i and j is at most
 * k.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,2,3,1], k = 3, t = 0
 * Output: true
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [1,0,1,1], k = 1, t = 2
 * Output: true
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [1,5,9,1,5,9], k = 2, t = 3
 * Output: false
 * 
 * 
 * 
 * 
 * 
 */
package medum

import (
	"math"
)

func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
    start := 0
    end := start + 1
    for start < len(nums) - 1 {
        if start != end && int(math.Abs(float64(nums[start]) - float64(nums[end]))) <= t {
            return true
        }
        if end - start >= k || len(nums) - 1 == end {
            start ++
            if t != 0 {
                end = start + 1
            }
        } else {
            end ++
        }
    }
    return false
}



