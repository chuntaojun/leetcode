#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (40.13%)
# Total Accepted:    177.5K
# Total Submissions: 442.4K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_nums = {}
        maxAns = 0
        for i in range(len(nums)):
            if not hash_nums.__contains__(nums[i]):
                left = hash_nums.get(nums[i] - 1, 0)
                right = hash_nums.get(nums[i] + 1, 0)
                cur = left + right + 1
                maxAns = max(maxAns, cur)
                hash_nums[nums[i]] = cur
                hash_nums[nums[i] - left] = cur
                hash_nums[nums[i] + right] = cur
        return maxAns


if __name__ == '__main__':
    s = Solution()
    t = [100,4,200,1,3,2]
    print(s.longestConsecutive(nums=t))
