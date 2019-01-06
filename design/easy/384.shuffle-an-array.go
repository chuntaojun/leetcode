/*
 * @lc app=leetcode id=384 lang=golang
 *
 * [384] Shuffle an Array
 *
 * https://leetcode.com/problems/shuffle-an-array/description/
 *
 * algorithms
 * Medium (48.99%)
 * Total Accepted:    63.1K
 * Total Submissions: 128.7K
 * Testcase Example:  '["Solution","shuffle","reset","shuffle"]\n[[[1,2,3]],[],[],[]]'
 *
 * Shuffle a set of numbers without duplicates.
 * 
 * 
 * Example:
 * 
 * // Init an array with set 1, 2, and 3.
 * int[] nums = {1,2,3};
 * Solution solution = new Solution(nums);
 * 
 * // Shuffle the array [1,2,3] and return its result. Any permutation of
 * [1,2,3] must equally likely to be returned.
 * solution.shuffle();
 * 
 * // Resets the array back to its original configuration [1,2,3].
 * solution.reset();
 * 
 * // Returns the random shuffling of array [1,2,3].
 * solution.shuffle();
 * 
 * 
 */
 type Solution struct {
	Origin	[]int
	Kth	[]int
	Len	int
}


func Constructor(nums []int) Solution {
	s := &Solution{}
	s.Origin = nums
	s.Kth = make([]int, len(nums) + 1, len(nums) + 1)
	s.Kth[0] = 1
	s.Len = len(nums)
	for i := 1; i <= len(nums); i ++ {
		s.Kth[i] = s.Kth[i - 1] * i
	}
	return *s
}


/** Resets the array to its original configuration and return it. */
func (this *Solution) Reset() []int {
	return this.Origin
}


/** Returns a random shuffling of the array. */
func (this *Solution) Shuffle() []int {
	k := int(rand.Float64() * float64(this.Len))
	tmp := make([]int, this.Len)
	copy(tmp, this.Origin)
	t := make([]int, this.Len)
	for i := 0; i < this.Len; i ++ {
		digit := (k - 1) / this.Kth[this.Len - i - 1]
		t[i] = tmp[digit]
		tmp = append(tmp[:digit], tmp[digit + 1:]...)
		k = (k - 1) % this.Kth[this.Len - i - 1] + 1
	}
	return t
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.Reset();
 * param_2 := obj.Shuffle();
 */
