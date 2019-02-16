#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#
# https://leetcode.com/problems/maximum-gap/description/
#
# algorithms
# Hard (31.71%)
# Total Accepted:    65.5K
# Total Submissions: 206.7K
# Testcase Example:  '[3,6,9,1]'
#
# Given an unsorted array, find the maximum difference between the successive
# elements in its sorted form.
# 
# Return 0 if the array contains less than 2 elements.
# 
# Example 1:
# 
# 
# Input: [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either
# (3,6) or (6,9) has the maximum difference 3.
# 
# Example 2:
# 
# 
# Input: [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
# 
# Note:
# 
# 
# You may assume all elements in the array are non-negative integers and fit in
# the 32-bit signed integer range.
# Try to solve it in linear time/space.
# 
# 
#
class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        if len(nums) == 2:
            return abs(nums[0] - nums[1])
        return self.getMaxGap(arr=nums, n=len(nums))
    
    def getMaxGap(self, arr, n):
        maxN, minN = self.get_max_min(arr=arr)
        count = [0 for i in range(n + 1)]
        low = [maxN for i in range(n + 1)]
        heigh = [minN for i in range(n + 1)]
        for i in range(1, n + 1):
            bucket = int((n - 1) * (arr[i - 1] - minN) / (maxN - minN)) + 1
            if bucket == n:
                bucket -= 1
            count[bucket] += 1
            low[bucket] = min(low[bucket], arr[i - 1])
            heigh[bucket] = max(heigh[bucket], arr[i - 1])
        maxGap = 0; l = heigh[1]
        for i in range(2, n):
            if count[i]:
                maxGap = max(maxGap, low[i] - l)
                l = heigh[i]
        return maxGap


    def get_max_min(self, arr):
        a = -1; b = 2 ** 32
        for i in range(len(arr)):
            a = max(a, arr[i])
            b = min(b, arr[i])
        return a, b


if __name__ == '__main__':
    s = Solution()
    n = [3,6,9,1]
    print(s.maximumGap(nums=n))
